#!/usr/bin/env python
#
# Copyright 2015 The Android Open Source Project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Subset the Noto Sans Japanese font."""

from nototools import subset

CHARSET = [
    0x22EF, # MIDLINE HORIZONTAL ELLIPSIS
    0x3031, # VERTICAL KANA REPEAT MARK
    0x3032, # VERTICAL KANA REPEAT WITH VOICED SOUND MARK
    0x3033, # VERTICAL KANA REPEAT MARK UPPER HALF
    0x3034, # VERTICAL KANA REPEAT WITH VOICED SOUND MARK UPPER HALF
    0x3035, # VERTICAL KANA REPEAT MARK LOWER HALF
    0x303B, # VERTICAL IDEOGRAPHIC ITERATION MARK
    0x3094, # HIRAGANA LETTER VU
    0x3095, # HIRAGANA LETTER SMALL KA
    0x3096, # HIRAGANA LETTER SMALL KE
    0x3099, # COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK
    0x309A, # COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK
    0x309F, # HIRAGANA DIGRAPH YORI
    0x30F7, # KATAKANA LETTER VA
    0x30F8, # KATAKANA LETTER VI
    0x30F9, # KATAKANA LETTER VE
    0x30FA, # KATAKANA LETTER VO
    0x30FF, # KATAKANA DIGRAPH KOTO
    0x31F0, # KATAKANA LETTER SMALL KU
    0x31F1, # KATAKANA LETTER SMALL SI
    0x31F2, # KATAKANA LETTER SMALL SU
    0x31F3, # KATAKANA LETTER SMALL TO
    0x31F4, # KATAKANA LETTER SMALL NU
    0x31F5, # KATAKANA LETTER SMALL HA
    0x31F6, # KATAKANA LETTER SMALL HI
    0x31F7, # KATAKANA LETTER SMALL HU
    0x31F8, # KATAKANA LETTER SMALL HE
    0x31F9, # KATAKANA LETTER SMALL HO
    0x31FA, # KATAKANA LETTER SMALL MU
    0x31FB, # KATAKANA LETTER SMALL RA
    0x31FC, # KATAKANA LETTER SMALL RI
    0x31FD, # KATAKANA LETTER SMALL RU
    0x31FE, # KATAKANA LETTER SMALL RE
    0x31FF, # KATAKANA LETTER SMALL RO
    0x32D0, # CIRCLED KATAKANA A
    0x32D1, # CIRCLED KATAKANA I
    0x32D2, # CIRCLED KATAKANA U
    0x32D3, # CIRCLED KATAKANA E
    0x32D4, # CIRCLED KATAKANA O
    0x32D5, # CIRCLED KATAKANA KA
    0x32D6, # CIRCLED KATAKANA KI
    0x32D7, # CIRCLED KATAKANA KU
    0x32D8, # CIRCLED KATAKANA KE
    0x32D9, # CIRCLED KATAKANA KO
    0x32DA, # CIRCLED KATAKANA SA
    0x32DB, # CIRCLED KATAKANA SI
    0x32DC, # CIRCLED KATAKANA SU
    0x32DD, # CIRCLED KATAKANA SE
    0x32DE, # CIRCLED KATAKANA SO
    0x32DF, # CIRCLED KATAKANA TA
    0x32E0, # CIRCLED KATAKANA TI
    0x32E1, # CIRCLED KATAKANA TU
    0x32E2, # CIRCLED KATAKANA TE
    0x32E3, # CIRCLED KATAKANA TO
    0x32E4, # CIRCLED KATAKANA NA
    0x32E5, # CIRCLED KATAKANA NI
    0x32E6, # CIRCLED KATAKANA NU
    0x32E7, # CIRCLED KATAKANA NE
    0x32E8, # CIRCLED KATAKANA NO
    0x32E9, # CIRCLED KATAKANA HA
    0x32EA, # CIRCLED KATAKANA HI
    0x32EB, # CIRCLED KATAKANA HU
    0x32EC, # CIRCLED KATAKANA HE
    0x32ED, # CIRCLED KATAKANA HO
    0x32EE, # CIRCLED KATAKANA MA
    0x32EF, # CIRCLED KATAKANA MI
    0x32F0, # CIRCLED KATAKANA MU
    0x32F1, # CIRCLED KATAKANA ME
    0x32F2, # CIRCLED KATAKANA MO
    0x32F3, # CIRCLED KATAKANA YA
    0x32F4, # CIRCLED KATAKANA YU
    0x32F5, # CIRCLED KATAKANA YO
    0x32F6, # CIRCLED KATAKANA RA
    0x32F7, # CIRCLED KATAKANA RI
    0x32F8, # CIRCLED KATAKANA RU
    0x32F9, # CIRCLED KATAKANA RE
    0x32FA, # CIRCLED KATAKANA RO
    0x32FB, # CIRCLED KATAKANA WA
    0x32FC, # CIRCLED KATAKANA WI
    0x32FD, # CIRCLED KATAKANA WE
    0x32FE, # CIRCLED KATAKANA WO
    0x3300, # SQUARE APAATO
    0x3301, # SQUARE ARUHUA
    0x3302, # SQUARE ANPEA
    0x3304, # SQUARE ININGU
    0x3305, # SQUARE INTI
    0x3306, # SQUARE UON
    0x3307, # SQUARE ESUKUUDO
    0x3308, # SQUARE EEKAA
    0x3309, # SQUARE ONSU
    0x330A, # SQUARE OOMU
    0x330B, # SQUARE KAIRI
    0x330C, # SQUARE KARATTO
    0x330E, # SQUARE GARON
    0x330F, # SQUARE GANMA
    0x3310, # SQUARE GIGA
    0x3311, # SQUARE GINII
    0x3312, # SQUARE KYURII
    0x3313, # SQUARE GIRUDAA
    0x3315, # SQUARE KIROGURAMU
    0x3316, # SQUARE KIROMEETORU
    0x3317, # SQUARE KIROWATTO
    0x3319, # SQUARE GURAMUTON
    0x331A, # SQUARE KURUZEIRO
    0x331B, # SQUARE KUROONE
    0x331C, # SQUARE KEESU
    0x331D, # SQUARE KORUNA
    0x331E, # SQUARE KOOPO
    0x331F, # SQUARE SAIKURU
    0x3320, # SQUARE SANTIIMU
    0x3321, # SQUARE SIRINGU
    0x3324, # SQUARE DAASU
    0x3325, # SQUARE DESI
    0x3328, # SQUARE NANO
    0x3329, # SQUARE NOTTO
    0x332A, # SQUARE HAITU
    0x332D, # SQUARE BAARERU
    0x332E, # SQUARE PIASUTORU
    0x332F, # SQUARE PIKURU
    0x3330, # SQUARE PIKO
    0x3331, # SQUARE BIRU
    0x3332, # SQUARE HUARADDO
    0x3333, # SQUARE HUIITO
    0x3334, # SQUARE BUSSYERU
    0x3335, # SQUARE HURAN
    0x3337, # SQUARE PESO
    0x3338, # SQUARE PENIHI
    0x3339, # SQUARE HERUTU
    0x333A, # SQUARE PENSU
    0x333C, # SQUARE BEETA
    0x333D, # SQUARE POINTO
    0x333E, # SQUARE BORUTO
    0x333F, # SQUARE HON
    0x3340, # SQUARE PONDO
    0x3341, # SQUARE HOORU
    0x3342, # SQUARE HOON
    0x3343, # SQUARE MAIKURO
    0x3344, # SQUARE MAIRU
    0x3345, # SQUARE MAHHA
    0x3346, # SQUARE MARUKU
    0x3347, # SQUARE MANSYON
    0x3348, # SQUARE MIKURON
    0x334B, # SQUARE MEGA
    0x334C, # SQUARE MEGATON
    0x334E, # SQUARE YAADO
    0x334F, # SQUARE YAARU
    0x3350, # SQUARE YUAN
    0x3352, # SQUARE RIRA
    0x3353, # SQUARE RUPII
    0x3354, # SQUARE RUUBURU
    0x3355, # SQUARE REMU
    0x3356, # SQUARE RENTOGEN
    0x2000B, # CJK UNIFIED IDEOGRAPH-2000B
    0x200A2, # CJK UNIFIED IDEOGRAPH-200A2
    0x200A4, # CJK UNIFIED IDEOGRAPH-200A4
    0x200B0, # CJK UNIFIED IDEOGRAPH-200B0
    0x200F5, # CJK UNIFIED IDEOGRAPH-200F5
    0x20158, # CJK UNIFIED IDEOGRAPH-20158
    0x201A2, # CJK UNIFIED IDEOGRAPH-201A2
    0x20213, # CJK UNIFIED IDEOGRAPH-20213
    0x2032B, # CJK UNIFIED IDEOGRAPH-2032B
    0x20371, # CJK UNIFIED IDEOGRAPH-20371
    0x20381, # CJK UNIFIED IDEOGRAPH-20381
    0x203F9, # CJK UNIFIED IDEOGRAPH-203F9
    0x2044A, # CJK UNIFIED IDEOGRAPH-2044A
    0x20509, # CJK UNIFIED IDEOGRAPH-20509
    0x2053F, # CJK UNIFIED IDEOGRAPH-2053F
    0x205B1, # CJK UNIFIED IDEOGRAPH-205B1
    0x205D6, # CJK UNIFIED IDEOGRAPH-205D6
    0x206EC, # CJK UNIFIED IDEOGRAPH-206EC
    0x2074F, # CJK UNIFIED IDEOGRAPH-2074F
    0x207C8, # CJK UNIFIED IDEOGRAPH-207C8
    0x20807, # CJK UNIFIED IDEOGRAPH-20807
    0x2083A, # CJK UNIFIED IDEOGRAPH-2083A
    0x208B9, # CJK UNIFIED IDEOGRAPH-208B9
    0x2090E, # CJK UNIFIED IDEOGRAPH-2090E
    0x2097C, # CJK UNIFIED IDEOGRAPH-2097C
    0x20984, # CJK UNIFIED IDEOGRAPH-20984
    0x2099D, # CJK UNIFIED IDEOGRAPH-2099D
    0x20A64, # CJK UNIFIED IDEOGRAPH-20A64
    0x20AD3, # CJK UNIFIED IDEOGRAPH-20AD3
    0x20B1D, # CJK UNIFIED IDEOGRAPH-20B1D
    0x20BB7, # CJK UNIFIED IDEOGRAPH-20BB7
    0x20D45, # CJK UNIFIED IDEOGRAPH-20D45
    0x20D58, # CJK UNIFIED IDEOGRAPH-20D58
    0x20DE1, # CJK UNIFIED IDEOGRAPH-20DE1
    0x20E64, # CJK UNIFIED IDEOGRAPH-20E64
    0x20E95, # CJK UNIFIED IDEOGRAPH-20E95
    0x20F5F, # CJK UNIFIED IDEOGRAPH-20F5F
    0x21201, # CJK UNIFIED IDEOGRAPH-21201
    0x2123D, # CJK UNIFIED IDEOGRAPH-2123D
    0x21255, # CJK UNIFIED IDEOGRAPH-21255
    0x21274, # CJK UNIFIED IDEOGRAPH-21274
    0x2127B, # CJK UNIFIED IDEOGRAPH-2127B
    0x212D7, # CJK UNIFIED IDEOGRAPH-212D7
    0x212E4, # CJK UNIFIED IDEOGRAPH-212E4
    0x212FD, # CJK UNIFIED IDEOGRAPH-212FD
    0x2131B, # CJK UNIFIED IDEOGRAPH-2131B
    0x21344, # CJK UNIFIED IDEOGRAPH-21344
    0x213C4, # CJK UNIFIED IDEOGRAPH-213C4
    0x2146D, # CJK UNIFIED IDEOGRAPH-2146D
    0x2146E, # CJK UNIFIED IDEOGRAPH-2146E
    0x21647, # CJK UNIFIED IDEOGRAPH-21647
    0x216B4, # CJK UNIFIED IDEOGRAPH-216B4
    0x21706, # CJK UNIFIED IDEOGRAPH-21706
    0x21742, # CJK UNIFIED IDEOGRAPH-21742
    0x218BD, # CJK UNIFIED IDEOGRAPH-218BD
    0x219C3, # CJK UNIFIED IDEOGRAPH-219C3
    0x21A1A, # CJK UNIFIED IDEOGRAPH-21A1A
    0x21C56, # CJK UNIFIED IDEOGRAPH-21C56
    0x21D2D, # CJK UNIFIED IDEOGRAPH-21D2D
    0x21D45, # CJK UNIFIED IDEOGRAPH-21D45
    0x21D62, # CJK UNIFIED IDEOGRAPH-21D62
    0x21D78, # CJK UNIFIED IDEOGRAPH-21D78
    0x21D92, # CJK UNIFIED IDEOGRAPH-21D92
    0x21D9C, # CJK UNIFIED IDEOGRAPH-21D9C
    0x21DA1, # CJK UNIFIED IDEOGRAPH-21DA1
    0x21DB7, # CJK UNIFIED IDEOGRAPH-21DB7
    0x21DE0, # CJK UNIFIED IDEOGRAPH-21DE0
    0x21E33, # CJK UNIFIED IDEOGRAPH-21E33
    0x21E34, # CJK UNIFIED IDEOGRAPH-21E34
    0x21F1E, # CJK UNIFIED IDEOGRAPH-21F1E
    0x21F76, # CJK UNIFIED IDEOGRAPH-21F76
    0x21FFA, # CJK UNIFIED IDEOGRAPH-21FFA
    0x2217B, # CJK UNIFIED IDEOGRAPH-2217B
    0x22218, # CJK UNIFIED IDEOGRAPH-22218
    0x2231E, # CJK UNIFIED IDEOGRAPH-2231E
    0x223AD, # CJK UNIFIED IDEOGRAPH-223AD
    0x22609, # CJK UNIFIED IDEOGRAPH-22609
    0x226F3, # CJK UNIFIED IDEOGRAPH-226F3
    0x2285B, # CJK UNIFIED IDEOGRAPH-2285B
    0x228AB, # CJK UNIFIED IDEOGRAPH-228AB
    0x22AB8, # CJK UNIFIED IDEOGRAPH-22AB8
    0x22B46, # CJK UNIFIED IDEOGRAPH-22B46
    0x22B4F, # CJK UNIFIED IDEOGRAPH-22B4F
    0x22B50, # CJK UNIFIED IDEOGRAPH-22B50
    0x22BA6, # CJK UNIFIED IDEOGRAPH-22BA6
    0x22C1D, # CJK UNIFIED IDEOGRAPH-22C1D
    0x22C24, # CJK UNIFIED IDEOGRAPH-22C24
    0x22DE1, # CJK UNIFIED IDEOGRAPH-22DE1
    0x22FEB, # CJK UNIFIED IDEOGRAPH-22FEB
    0x231B6, # CJK UNIFIED IDEOGRAPH-231B6
    0x231C3, # CJK UNIFIED IDEOGRAPH-231C3
    0x231C4, # CJK UNIFIED IDEOGRAPH-231C4
    0x231F5, # CJK UNIFIED IDEOGRAPH-231F5
    0x23372, # CJK UNIFIED IDEOGRAPH-23372
    0x233D0, # CJK UNIFIED IDEOGRAPH-233D0
    0x233D2, # CJK UNIFIED IDEOGRAPH-233D2
    0x233D3, # CJK UNIFIED IDEOGRAPH-233D3
    0x233D5, # CJK UNIFIED IDEOGRAPH-233D5
    0x233DA, # CJK UNIFIED IDEOGRAPH-233DA
    0x233DF, # CJK UNIFIED IDEOGRAPH-233DF
    0x233E4, # CJK UNIFIED IDEOGRAPH-233E4
    0x2344A, # CJK UNIFIED IDEOGRAPH-2344A
    0x2344B, # CJK UNIFIED IDEOGRAPH-2344B
    0x23451, # CJK UNIFIED IDEOGRAPH-23451
    0x23465, # CJK UNIFIED IDEOGRAPH-23465
    0x234E4, # CJK UNIFIED IDEOGRAPH-234E4
    0x23594, # CJK UNIFIED IDEOGRAPH-23594
    0x235C4, # CJK UNIFIED IDEOGRAPH-235C4
    0x23638, # CJK UNIFIED IDEOGRAPH-23638
    0x23639, # CJK UNIFIED IDEOGRAPH-23639
    0x2363A, # CJK UNIFIED IDEOGRAPH-2363A
    0x23647, # CJK UNIFIED IDEOGRAPH-23647
    0x2370C, # CJK UNIFIED IDEOGRAPH-2370C
    0x2371C, # CJK UNIFIED IDEOGRAPH-2371C
    0x23763, # CJK UNIFIED IDEOGRAPH-23763
    0x23764, # CJK UNIFIED IDEOGRAPH-23764
    0x237E7, # CJK UNIFIED IDEOGRAPH-237E7
    0x237F1, # CJK UNIFIED IDEOGRAPH-237F1
    0x237FF, # CJK UNIFIED IDEOGRAPH-237FF
    0x23824, # CJK UNIFIED IDEOGRAPH-23824
    0x2383D, # CJK UNIFIED IDEOGRAPH-2383D
    0x23A98, # CJK UNIFIED IDEOGRAPH-23A98
    0x23C7F, # CJK UNIFIED IDEOGRAPH-23C7F
    0x23CBE, # CJK UNIFIED IDEOGRAPH-23CBE
    0x23D00, # CJK UNIFIED IDEOGRAPH-23D00
    0x23D0E, # CJK UNIFIED IDEOGRAPH-23D0E
    0x23DD3, # CJK UNIFIED IDEOGRAPH-23DD3
    0x23DF9, # CJK UNIFIED IDEOGRAPH-23DF9
    0x23DFA, # CJK UNIFIED IDEOGRAPH-23DFA
    0x23F7E, # CJK UNIFIED IDEOGRAPH-23F7E
    0x2404B, # CJK UNIFIED IDEOGRAPH-2404B
    0x24096, # CJK UNIFIED IDEOGRAPH-24096
    0x24103, # CJK UNIFIED IDEOGRAPH-24103
    0x241C6, # CJK UNIFIED IDEOGRAPH-241C6
    0x243BC, # CJK UNIFIED IDEOGRAPH-243BC
    0x243D0, # CJK UNIFIED IDEOGRAPH-243D0
    0x24629, # CJK UNIFIED IDEOGRAPH-24629
    0x246A5, # CJK UNIFIED IDEOGRAPH-246A5
    0x247F1, # CJK UNIFIED IDEOGRAPH-247F1
    0x24896, # CJK UNIFIED IDEOGRAPH-24896
    0x24A4D, # CJK UNIFIED IDEOGRAPH-24A4D
    0x24B56, # CJK UNIFIED IDEOGRAPH-24B56
    0x24B6F, # CJK UNIFIED IDEOGRAPH-24B6F
    0x24C16, # CJK UNIFIED IDEOGRAPH-24C16
    0x24D14, # CJK UNIFIED IDEOGRAPH-24D14
    0x24E04, # CJK UNIFIED IDEOGRAPH-24E04
    0x24E0E, # CJK UNIFIED IDEOGRAPH-24E0E
    0x24E37, # CJK UNIFIED IDEOGRAPH-24E37
    0x24E6A, # CJK UNIFIED IDEOGRAPH-24E6A
    0x24E8B, # CJK UNIFIED IDEOGRAPH-24E8B
    0x24FF2, # CJK UNIFIED IDEOGRAPH-24FF2
    0x2504A, # CJK UNIFIED IDEOGRAPH-2504A
    0x25055, # CJK UNIFIED IDEOGRAPH-25055
    0x25122, # CJK UNIFIED IDEOGRAPH-25122
    0x251A9, # CJK UNIFIED IDEOGRAPH-251A9
    0x251E5, # CJK UNIFIED IDEOGRAPH-251E5
    0x2521E, # CJK UNIFIED IDEOGRAPH-2521E
    0x2524C, # CJK UNIFIED IDEOGRAPH-2524C
    0x2542E, # CJK UNIFIED IDEOGRAPH-2542E
    0x2548E, # CJK UNIFIED IDEOGRAPH-2548E
    0x254D9, # CJK UNIFIED IDEOGRAPH-254D9
    0x2550E, # CJK UNIFIED IDEOGRAPH-2550E
    0x255A7, # CJK UNIFIED IDEOGRAPH-255A7
    0x2567F, # CJK UNIFIED IDEOGRAPH-2567F
    0x25771, # CJK UNIFIED IDEOGRAPH-25771
    0x257A9, # CJK UNIFIED IDEOGRAPH-257A9
    0x257B4, # CJK UNIFIED IDEOGRAPH-257B4
    0x25874, # CJK UNIFIED IDEOGRAPH-25874
    0x259C4, # CJK UNIFIED IDEOGRAPH-259C4
    0x259D4, # CJK UNIFIED IDEOGRAPH-259D4
    0x25AE3, # CJK UNIFIED IDEOGRAPH-25AE3
    0x25AE4, # CJK UNIFIED IDEOGRAPH-25AE4
    0x25AF1, # CJK UNIFIED IDEOGRAPH-25AF1
    0x25BB2, # CJK UNIFIED IDEOGRAPH-25BB2
    0x25C4B, # CJK UNIFIED IDEOGRAPH-25C4B
    0x25C64, # CJK UNIFIED IDEOGRAPH-25C64
    0x25DA1, # CJK UNIFIED IDEOGRAPH-25DA1
    0x25E2E, # CJK UNIFIED IDEOGRAPH-25E2E
    0x25E56, # CJK UNIFIED IDEOGRAPH-25E56
    0x25E62, # CJK UNIFIED IDEOGRAPH-25E62
    0x25E65, # CJK UNIFIED IDEOGRAPH-25E65
    0x25EC2, # CJK UNIFIED IDEOGRAPH-25EC2
    0x25EE8, # CJK UNIFIED IDEOGRAPH-25EE8
    0x25F23, # CJK UNIFIED IDEOGRAPH-25F23
    0x25F5C, # CJK UNIFIED IDEOGRAPH-25F5C
    0x25FD4, # CJK UNIFIED IDEOGRAPH-25FD4
    0x25FE0, # CJK UNIFIED IDEOGRAPH-25FE0
    0x25FFB, # CJK UNIFIED IDEOGRAPH-25FFB
    0x2600C, # CJK UNIFIED IDEOGRAPH-2600C
    0x26017, # CJK UNIFIED IDEOGRAPH-26017
    0x26060, # CJK UNIFIED IDEOGRAPH-26060
    0x260ED, # CJK UNIFIED IDEOGRAPH-260ED
    0x26222, # CJK UNIFIED IDEOGRAPH-26222
    0x26270, # CJK UNIFIED IDEOGRAPH-26270
    0x26286, # CJK UNIFIED IDEOGRAPH-26286
    0x2667E, # CJK UNIFIED IDEOGRAPH-2667E
    0x266B0, # CJK UNIFIED IDEOGRAPH-266B0
    0x2671D, # CJK UNIFIED IDEOGRAPH-2671D
    0x268DD, # CJK UNIFIED IDEOGRAPH-268DD
    0x268EA, # CJK UNIFIED IDEOGRAPH-268EA
    0x2696F, # CJK UNIFIED IDEOGRAPH-2696F
    0x26999, # CJK UNIFIED IDEOGRAPH-26999
    0x269DD, # CJK UNIFIED IDEOGRAPH-269DD
    0x26A1E, # CJK UNIFIED IDEOGRAPH-26A1E
    0x26A58, # CJK UNIFIED IDEOGRAPH-26A58
    0x26A8C, # CJK UNIFIED IDEOGRAPH-26A8C
    0x26AB7, # CJK UNIFIED IDEOGRAPH-26AB7
    0x26AFF, # CJK UNIFIED IDEOGRAPH-26AFF
    0x26C29, # CJK UNIFIED IDEOGRAPH-26C29
    0x26C73, # CJK UNIFIED IDEOGRAPH-26C73
    0x26C9E, # CJK UNIFIED IDEOGRAPH-26C9E
    0x26CDD, # CJK UNIFIED IDEOGRAPH-26CDD
    0x26E40, # CJK UNIFIED IDEOGRAPH-26E40
    0x26E65, # CJK UNIFIED IDEOGRAPH-26E65
    0x26F94, # CJK UNIFIED IDEOGRAPH-26F94
    0x26FF6, # CJK UNIFIED IDEOGRAPH-26FF6
    0x26FF7, # CJK UNIFIED IDEOGRAPH-26FF7
    0x26FF8, # CJK UNIFIED IDEOGRAPH-26FF8
    0x270F4, # CJK UNIFIED IDEOGRAPH-270F4
    0x27139, # CJK UNIFIED IDEOGRAPH-27139
    0x273DA, # CJK UNIFIED IDEOGRAPH-273DA
    0x273DB, # CJK UNIFIED IDEOGRAPH-273DB
    0x273FE, # CJK UNIFIED IDEOGRAPH-273FE
    0x27410, # CJK UNIFIED IDEOGRAPH-27410
    0x27449, # CJK UNIFIED IDEOGRAPH-27449
    0x27614, # CJK UNIFIED IDEOGRAPH-27614
    0x27615, # CJK UNIFIED IDEOGRAPH-27615
    0x27631, # CJK UNIFIED IDEOGRAPH-27631
    0x27684, # CJK UNIFIED IDEOGRAPH-27684
    0x27693, # CJK UNIFIED IDEOGRAPH-27693
    0x2770E, # CJK UNIFIED IDEOGRAPH-2770E
    0x27723, # CJK UNIFIED IDEOGRAPH-27723
    0x27752, # CJK UNIFIED IDEOGRAPH-27752
    0x27985, # CJK UNIFIED IDEOGRAPH-27985
    0x279B4, # CJK UNIFIED IDEOGRAPH-279B4
    0x27BB3, # CJK UNIFIED IDEOGRAPH-27BB3
    0x27BBE, # CJK UNIFIED IDEOGRAPH-27BBE
    0x27BC7, # CJK UNIFIED IDEOGRAPH-27BC7
    0x27C3C, # CJK UNIFIED IDEOGRAPH-27C3C
    0x27CB8, # CJK UNIFIED IDEOGRAPH-27CB8
    0x27DA0, # CJK UNIFIED IDEOGRAPH-27DA0
    0x27E10, # CJK UNIFIED IDEOGRAPH-27E10
    0x2808A, # CJK UNIFIED IDEOGRAPH-2808A
    0x280BB, # CJK UNIFIED IDEOGRAPH-280BB
    0x28277, # CJK UNIFIED IDEOGRAPH-28277
    0x28282, # CJK UNIFIED IDEOGRAPH-28282
    0x282F3, # CJK UNIFIED IDEOGRAPH-282F3
    0x283CD, # CJK UNIFIED IDEOGRAPH-283CD
    0x2840C, # CJK UNIFIED IDEOGRAPH-2840C
    0x28455, # CJK UNIFIED IDEOGRAPH-28455
    0x2856B, # CJK UNIFIED IDEOGRAPH-2856B
    0x285C8, # CJK UNIFIED IDEOGRAPH-285C8
    0x285C9, # CJK UNIFIED IDEOGRAPH-285C9
    0x286D7, # CJK UNIFIED IDEOGRAPH-286D7
    0x286FA, # CJK UNIFIED IDEOGRAPH-286FA
    0x28946, # CJK UNIFIED IDEOGRAPH-28946
    0x2896B, # CJK UNIFIED IDEOGRAPH-2896B
    0x28987, # CJK UNIFIED IDEOGRAPH-28987
    0x28988, # CJK UNIFIED IDEOGRAPH-28988
    0x289BA, # CJK UNIFIED IDEOGRAPH-289BA
    0x289BB, # CJK UNIFIED IDEOGRAPH-289BB
    0x28A1E, # CJK UNIFIED IDEOGRAPH-28A1E
    0x28A43, # CJK UNIFIED IDEOGRAPH-28A43
    0x28A71, # CJK UNIFIED IDEOGRAPH-28A71
    0x28A99, # CJK UNIFIED IDEOGRAPH-28A99
    0x28ACD, # CJK UNIFIED IDEOGRAPH-28ACD
    0x28ADD, # CJK UNIFIED IDEOGRAPH-28ADD
    0x28AE4, # CJK UNIFIED IDEOGRAPH-28AE4
    0x28BC1, # CJK UNIFIED IDEOGRAPH-28BC1
    0x28BEF, # CJK UNIFIED IDEOGRAPH-28BEF
    0x28CDD, # CJK UNIFIED IDEOGRAPH-28CDD
    0x28D10, # CJK UNIFIED IDEOGRAPH-28D10
    0x28D71, # CJK UNIFIED IDEOGRAPH-28D71
    0x28DFB, # CJK UNIFIED IDEOGRAPH-28DFB
    0x28E17, # CJK UNIFIED IDEOGRAPH-28E17
    0x28E1F, # CJK UNIFIED IDEOGRAPH-28E1F
    0x28E89, # CJK UNIFIED IDEOGRAPH-28E89
    0x28EEB, # CJK UNIFIED IDEOGRAPH-28EEB
    0x28EF6, # CJK UNIFIED IDEOGRAPH-28EF6
    0x28F32, # CJK UNIFIED IDEOGRAPH-28F32
    0x28FF8, # CJK UNIFIED IDEOGRAPH-28FF8
    0x292A0, # CJK UNIFIED IDEOGRAPH-292A0
    0x292B1, # CJK UNIFIED IDEOGRAPH-292B1
    0x29490, # CJK UNIFIED IDEOGRAPH-29490
    0x295CF, # CJK UNIFIED IDEOGRAPH-295CF
    0x296F0, # CJK UNIFIED IDEOGRAPH-296F0
    0x29719, # CJK UNIFIED IDEOGRAPH-29719
    0x29750, # CJK UNIFIED IDEOGRAPH-29750
    0x298C6, # CJK UNIFIED IDEOGRAPH-298C6
    0x29A72, # CJK UNIFIED IDEOGRAPH-29A72
    0x29D4B, # CJK UNIFIED IDEOGRAPH-29D4B
    0x29DDB, # CJK UNIFIED IDEOGRAPH-29DDB
    0x29E15, # CJK UNIFIED IDEOGRAPH-29E15
    0x29E3D, # CJK UNIFIED IDEOGRAPH-29E3D
    0x29E49, # CJK UNIFIED IDEOGRAPH-29E49
    0x29E8A, # CJK UNIFIED IDEOGRAPH-29E8A
    0x29EC4, # CJK UNIFIED IDEOGRAPH-29EC4
    0x29EDB, # CJK UNIFIED IDEOGRAPH-29EDB
    0x29EE9, # CJK UNIFIED IDEOGRAPH-29EE9
    0x29FCE, # CJK UNIFIED IDEOGRAPH-29FCE
    0x29FD7, # CJK UNIFIED IDEOGRAPH-29FD7
    0x2A01A, # CJK UNIFIED IDEOGRAPH-2A01A
    0x2A02F, # CJK UNIFIED IDEOGRAPH-2A02F
    0x2A082, # CJK UNIFIED IDEOGRAPH-2A082
    0x2A0F9, # CJK UNIFIED IDEOGRAPH-2A0F9
    0x2A190, # CJK UNIFIED IDEOGRAPH-2A190
    0x2A38C, # CJK UNIFIED IDEOGRAPH-2A38C
    0x2A437, # CJK UNIFIED IDEOGRAPH-2A437
    0x2A5F1, # CJK UNIFIED IDEOGRAPH-2A5F1
    0x2A602, # CJK UNIFIED IDEOGRAPH-2A602
    0x2A61A, # CJK UNIFIED IDEOGRAPH-2A61A
    0x2A6B2, # CJK UNIFIED IDEOGRAPH-2A6B2
    0x2A9E6, # CJK UNIFIED IDEOGRAPH-2A9E6
    0x2B746, # CJK UNIFIED IDEOGRAPH-2B746
    0x2B751, # CJK UNIFIED IDEOGRAPH-2B751
    0x2B753, # CJK UNIFIED IDEOGRAPH-2B753
    0x2B75A, # CJK UNIFIED IDEOGRAPH-2B75A
    0x2B75C, # CJK UNIFIED IDEOGRAPH-2B75C
    0x2B765, # CJK UNIFIED IDEOGRAPH-2B765
    0x2B776, # CJK UNIFIED IDEOGRAPH-2B776
    0x2B777, # CJK UNIFIED IDEOGRAPH-2B777
    0x2B77C, # CJK UNIFIED IDEOGRAPH-2B77C
    0x2B782, # CJK UNIFIED IDEOGRAPH-2B782
    0x2B789, # CJK UNIFIED IDEOGRAPH-2B789
    0x2B78B, # CJK UNIFIED IDEOGRAPH-2B78B
    0x2B78E, # CJK UNIFIED IDEOGRAPH-2B78E
    0x2B794, # CJK UNIFIED IDEOGRAPH-2B794
    0x2B7AC, # CJK UNIFIED IDEOGRAPH-2B7AC
    0x2B7AF, # CJK UNIFIED IDEOGRAPH-2B7AF
    0x2B7BD, # CJK UNIFIED IDEOGRAPH-2B7BD
    0x2B7C9, # CJK UNIFIED IDEOGRAPH-2B7C9
    0x2B7CF, # CJK UNIFIED IDEOGRAPH-2B7CF
    0x2B7D2, # CJK UNIFIED IDEOGRAPH-2B7D2
    0x2B7D8, # CJK UNIFIED IDEOGRAPH-2B7D8
    0x2B7F0, # CJK UNIFIED IDEOGRAPH-2B7F0
    0x2B80D, # CJK UNIFIED IDEOGRAPH-2B80D
    0x2B817, # CJK UNIFIED IDEOGRAPH-2B817
    0x2B81A, # CJK UNIFIED IDEOGRAPH-2B81A
]

subset.subset_font('NotoSansJP-Regular.otf',
                   'NotoSansJP-Regular-Subsetted.otf',
                   include=CHARSET)
