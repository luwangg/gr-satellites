# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    satellites_kiss_to_pdu.xml
    satellites_pdu_to_kiss.xml
    satellites_hdlc_framer.xml
    satellites_nrzi_encode.xml
    satellites_nrzi_decode.xml
    satellites_hdlc_deframer.xml
    satellites_check_address.xml
    satellites_fixedlen_tagger.xml
    satellites_print_header.xml
    satellites_check_crc.xml
    satellites_swap_crc.xml
    satellites_swap_header.xml
    satellites_submit.xml
    satellites_print_timestamp.xml
    satellites_sat3cat2_telemetry_parser.xml
    satellites_ao40_syncframe.xml
    satellites_ao40_deinterleaver.xml
    satellites_ao40_rs_decoder.xml
    satellites_funcube_telemetry_parser.xml
    satellites_gomx3_beacon_parser.xml
    satellites_adsb_kml.xml
    satellites_ax100_decode.xml
    satellites_u482c_decode.xml
    satellites_gomx1_beacon_parser.xml
    satellites_ks1q_header_remover.xml
    satellites_decode_rs.xml
    satellites_encode_rs.xml
    satellites_lilacsat1_demux.xml
    satellites_by701_image_decoder.xml
    satellites_by701_telemetry_parser.xml
    satellites_by701_camera_telemetry_parser.xml
    satellites_kr01_telemetry_parser.xml
    satellites_check_ao40_uncoded_crc.xml
    satellites_lilacsat1_gps_kml.xml
    satellites_au03_telemetry_parser.xml
    satellites_check_tt64_crc.xml
    satellites_varlen_packet_tagger.xml
    satellites_varlen_packet_framer.xml
    satellites_append_crc32c.xml
    satellites_dsat_image_decoder.xml
    satellites_nusat_decoder.xml
    satellites_rscode_decoder.xml
    satellites_strip_ax25_header.xml
    satellites_picsat_telemetry_parser.xml
    DESTINATION share/gnuradio/grc/blocks
)
