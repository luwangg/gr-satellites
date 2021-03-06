#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 Daniel Estevez <daniel@destevez.net>
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from construct import *

import datetime

from ccsds_telemetry import *

class TimeAdapter(Adapter):
    def _encode(self, obj, context):
        d = obj - datetime.datetime(2000, 1, 1)
        return Container(days = d.days, milliseconds = d.seconds * 1000 + d.microseconds / 1000)
    def _decode(self, obj, context):
        return datetime.datetime(2000, 1, 1) + datetime.timedelta(days=obj.days, seconds=obj.milliseconds/1000, microseconds=(obj.milliseconds%1000)*1000)

SecondaryHeaderTM = TimeAdapter(Struct('days' / Int16ub, 'milliseconds' / Int32ub))

SecondaryHeaderTC = BitStruct('req_ack_reception' / Flag,
                              'req_fmt_reception' / Flag,
                              'req_exe_reception' / Flag,
                              'telecommand_id' / BitsInteger(10),
                              'emitter_id' / BitsInteger(3),
                              'signature' / String(16))

AntStatus = Struct(
    'undeployed' / Flag,
    'timeout' / Flag,
    'deploying' / Flag)

BeaconA = BitStruct(
    Padding(1),
    'solar_panel_error_flags' / Flag[5],
    'i_adcs_get_attitude_error' / Flag,
    'i_adcs_get_status_register_error' / Flag,
    Padding(1),
    'fram_enable_error_flag' / Flag,
    'ants_error_flag' / Flag[2],
    'trxvu_tx_error_flag' / Flag,
    'trxvu_rx_error_flag' / Flag,
    'obc_supervisor_error_flag' / Flag,
    'gom_eps_error_flag' / Flag,
    'ant1_status_b' / AntStatus,
    Padding(1),
    'ant2_status_b' / AntStatus,
    'ignore_flag_ants_b_status' / Flag,
    'ant3_status_b' / AntStatus,
    Padding(1),
    'ant4_status_b' / AntStatus,
    'armed_ants_b_status' / Flag,
    'ant1_status_a' / AntStatus,
    Padding(1),
    'ant2_status_a' / AntStatus,
    'ignore_flag_ants_a_status' / Flag,
    'ant3_status_a' / AntStatus,
    Padding(1),
    'ant4_status_a' / AntStatus,
    'armed_ants_a_status' / Flag)
    
BeaconB = Struct(
    'solar_panel_temps' / Int16ub[5],
    'ants_temperature' / Int16ub[2],
    'tx_trxvu_hk_current' / Int16ub,
    'tx_trxvu_hk_forwardpower' / Int16ub,
    'tx_trxvu_tx_reflectedpower' / Int16ub,
    'tx_trxvu_hk_pa_temp' / Int16ub,
    'rx_trxvu_hk_pa_temp' / Int16ub,
    'rx_trxvu_hk_board_temp' / Int16ub,
    'eps_hk_temp_batts' / Int16sb,
    'eps_hk_batt_mode' / Int8ub,
    'eps_h_kv_batt' / Int8ub,
    'eps_hk_boot_cause' / Int32ub,
    'n_reboots_eps' / Int32ub,
    'n_reboots_obc' / Int32ub,
    'quaternions' / Float32b[4],
    'angular_rates' / Float32b[3])

BeaconC = BitStruct(
    Padding(12),
    'adcs_stat_flag_hl_op_tgt_cap' / Flag,
    'adcs_stat_flag_hl_op_tgt_track_fix_wgs84' / Flag,
    'adcs_stat_flag_hl_op_tgt_track_nadir' / Flag,
    'adcs_stat_flag_hl_op_tgt_track' / Flag,
    'adcs_stat_flag_hl_op_tgt_track_const_v' / Flag,
    'adcs_stat_flag_hl_op_spin' / Flag,
    Padding(1),
    'adcs_stat_flag_hl_op_sunp' / Flag,
    'adcs_stat_flag_hl_op_detumbling' / Flag,
    'adcs_stat_flag_hl_op_measure' / Flag,
    Padding(5),
    'adcs_stat_flag_datetime_valid' / Flag,
    Padding(1),
    'adcs_stat_flag_hl_op_safe' / Flag,
    'adcs_stat_flag_hl_op_idle' / Flag,
    Padding(1))

BeaconD = Struct(
    'up_time' / Int32ub,
    'last_fram_log_fun_err_code' / Int16sb,
    'last_fram_log_line_code' / Int16ub,
    'last_fram_log_file_crc_code' / Int32ub,
    'last_fram_log_counter' / Int16ub,
    'average_photon_count' / Int16ub,
    'sat_mode' / Int8ub,
    'tc_sequence_count' / Int16ub)

Beacon = Struct(Padding(3), Embedded(BeaconA), Embedded(BeaconB), Embedded(BeaconC), Embedded(BeaconD))

Packet = Struct(
    'primary_header' / PrimaryHeader,
    'secondary_header' / SecondaryHeaderTM, # TODO choose between TM and TC
    'beacon' / If(lambda c: c.primary_header.payload_flag == 0 and c.primary_header.packet_category == 1, Beacon))
