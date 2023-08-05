#!/usr/bin/env python3

from irrd.rpsl.rpsl_objects import rpsl_object_from_text

AS3257 = """aut-num:        AS3257
as-name:        GTT-BACKBONE
descr:          GTT
org:            ORG-GCI2-RIPE
import:         from AS12 accept AS12
import:         from AS14 accept AS14
import:         from AS21 accept AS21
import:         from AS57 accept AS-NLG-TO-TRANSIT
import:         from AS62 accept AS-C1
import:         from AS97 accept AS97
import:         from AS109 accept AS109
import:         from AS260 accept AS-XCONNECT24
import:         from AS286 accept AS286
import:         from AS288 accept AS288
import:         from AS376 accept AS376:AS-CLIENTS
import:         from AS517 accept AS517
import:         from AS559 accept AS559
import:         from AS572 accept AS572
import:         from AS577 accept AS577:AS-CUSTOMERS
import:         from AS600 accept AS600
import:         from AS612 accept AS612
import:         from AS714 accept AS714
import:         from AS766 accept AS766
import:         from AS792 accept AS792
import:         from AS812 accept AS-ROGERS:AS-CUSTOMERS
import:         from AS852 accept AS-TELUS
import:         from AS855 accept AS855
import:         from AS979 accept AS979
import:         from AS1017 accept AS1017
import:         from AS1065 accept AS1065
import:         from AS1100 accept AS-NUDAY
import:         from AS1103 accept AS-SURFNET
import:         from AS1213 accept AS-HEANET
import:         from AS1215 accept AS1215
import:         from AS1216 accept AS1216
import:         from AS1219 accept AS1219
import:         from AS1257 accept AS1257
import:         from AS1258 accept AS1258
import:         from AS1261 accept AS1261
import:         from AS1267 accept AS1267
import:         from AS1311 accept AS1311
import:         from AS1341 accept AS1341
import:         from AS1445 accept AS1445
import:         from AS1449 accept AS1449
import:         from AS1605 accept AS1605
import:         from AS1610 accept AS1610
import:         from AS1612 accept AS1612
import:         from AS1678 accept AS1678
import:         from AS1680 accept AS1680
import:         from AS1764 accept AS-NEXTLAYER
import:         from AS1803 accept AS1803
import:         from AS1820 accept AS-WTUC
import:         from AS1828 accept AS-UNITAS
import:         from AS1968 accept AS1968
import:         from AS2121 accept AS2121
import:         from AS2147 accept AS2147
import:         from AS2200 accept AS-RENATER
import:         from AS2381 accept AS-WISCNET
import:         from AS2484 accept AS2484
import:         from AS2495 accept AS2495
import:         from AS2516 accept AS2516
import:         from AS2572 accept AS2572
import:         from AS2609 accept AS2609
import:         from AS2611 accept AS-BELNET
import:         from AS2698 accept AS2698
import:         from AS2721 accept AS2721
import:         from AS2728 accept AS2728
import:         from AS2734 accept AS-CORESITE
import:         from AS3165 accept AS3165
import:         from AS3170 accept AS-VELOXSERV
import:         from AS3206 accept AS3206
import:         from AS3212 accept AS3212
import:         from AS3214 accept AS-XTOM
import:         from AS3215 accept AS3215
import:         from AS3252 accept AS-FBRX
import:         from AS3255 accept AS3255
import:         from AS3264 accept AS3264
import:         from AS3291 accept AS3291
import:         from AS3292 accept AS3292
import:         from AS3302 accept AS-TIPNETIT
import:         from AS3352 accept AS3352
import:         from AS3367 accept AS-F6
import:         from AS3399 accept AS-OBE
import:         from AS3573 accept AS3573
import:         from AS3584 accept AS3584
import:         from AS3676 accept AS-UIOWA
import:         from AS3722 accept AS3722
import:         from AS3728 accept AS3728
import:         from AS3737 accept AS-PTD
import:         from AS3842 accept AS-RN1
import:         from AS3908 accept AS3908
import:         from AS3925 accept AS3925
import:         from AS3943 accept AS3943
import:         from AS4058 accept AS4058
import:         from AS4150 accept AS4150
import:         from AS4181 accept AS-TDS-TRANSIT
import:         from AS4229 accept AS4229
import:         from AS4230 accept AS-EMBRATELNET
import:         from AS4250 accept AS4250
import:         from AS4385 accept AS4385
import:         from AS4436 accept AS4436
import:         from AS4540 accept AS4540
import:         from AS4556 accept AS-PACKETFABRIC
import:         from AS4565 accept AS4565
import:         from AS4589 accept AS4589
import:         from AS4648 accept AS-4648-CUSTOMERS
import:         from AS4788 accept AS-TMNET-CUSTOMERS
import:         from AS4826 accept AS4826:AS-VOCUS
import:         from AS4867 accept AS4867
import:         from AS4882 accept AS4882
import:         from AS4889 accept AS4889
import:         from AS4893 accept AS4893
import:         from AS5008 accept AS5008
import:         from AS5009 accept AS5009
import:         from AS5078 accept AS-ONENETOK
import:         from AS5091 accept AS5091
import:         from AS5394 accept AS-UNIDATACUST
import:         from AS5396 accept AS-MCLINK
import:         from AS5398 accept AS5398
import:         from AS5409 accept AS5409
import:         from AS5459 accept AS5459
import:         from AS5463 accept AS5463
import:         from AS5486 accept AS5486
import:         from AS5524 accept AS5524
import:         from AS5580 accept AS5580
import:         from AS5582 accept AS5582
import:         from AS5602 accept AS-KQIT
import:         from AS5606 accept AS-GTSRO
import:         from AS5607 accept AS5607
import:         from AS5645 accept AS5645:AS-CUSTOMERS
import:         from AS5669 accept AS5669
import:         from AS5670 accept AS-VAPOR
import:         from AS5697 accept AS5697
import:         from AS5715 accept AS-NTAJC
import:         from AS5738 accept AS5738:AS-CUSTOMERS
import:         from AS5742 accept AS-CCI
import:         from AS5760 accept AS5760
import:         from AS5769 accept AS5769
import:         from AS5777 accept AS5777
import:         from AS5784 accept AS5784
import:         from AS6059 accept AS6059
import:         from AS6067 accept AS6067
import:         from AS6071 accept AS6071
import:         from AS6072 accept AS6072
import:         from AS6079 accept AS6079
import:         from AS6095 accept AS6095
import:         from AS6142 accept AS6142
import:         from AS6169 accept AS-KENTIK
import:         from AS6181 accept AS-FUSE
import:         from AS6199 accept AS6199
import:         from AS6220 accept AS6220
import:         from AS6267 accept AS6267
import:         from AS6325 accept AS6325
import:         from AS6327 accept AS-BIGPIPE
import:         from AS6391 accept AS-URBAN
import:         from AS6407 accept AS6407
import:         from AS6459 accept AS6459
import:         from AS6462 accept AS6462
import:         from AS6471 accept AS6471
import:         from AS6493 accept AS6493
import:         from AS6498 accept AS-INTRADO-INTERNAL
import:         from AS6507 accept AS6507
import:         from AS6508 accept AS6508
import:         from AS6517 accept AS6517
import:         from AS6566 accept AS6566
import:         from AS6597 accept AS6597
import:         from AS6621 accept AS6621
import:         from AS6643 accept AS6643
import:         from AS6659 accept AS6659
import:         from AS6663 accept AS-STARNETSRO
import:         from AS6667 accept AS6667
import:         from AS6696 accept AS6696
import:         from AS6713 accept AS6713
import:         from AS6717 accept AS6717
import:         from AS6723 accept AS6723
import:         from AS6738 accept AS6738
import:         from AS6747 accept AS-LATTELEKOM
import:         from AS6752 accept AS6752
import:         from AS6768 accept AS-EUROTELE
import:         from AS6770 accept AS6770
import:         from AS6774 accept AS6774:AS-BICS-TRANSIT
import:         from AS6779 accept AS6779
import:         from AS6805 accept AS6805
import:         from AS6812 accept AS-VIRTUSTREAM-EU
import:         from AS6830 accept AS6830
import:         from AS6848 accept AS6848
import:         from AS6866 accept AS-CYTANET
import:         from AS6894 accept AS-KDDIEU
import:         from AS6898 accept AS-INTERNETONE_CH
import:         from AS6907 accept AS6907
import:         from AS6951 accept AS6951
import:         from AS7012 accept AS7012
import:         from AS7014 accept AS7014
import:         from AS7029 accept AS-WINDSTREAM
import:         from AS7148 accept AS7148
import:         from AS7153 accept AS7153
import:         from AS7155 accept AS7155
import:         from AS7158 accept AS7158
import:         from AS7160 accept AS7160
import:         from AS7203 accept AS-Leaseweb-US
import:         from AS7219 accept AS7219
import:         from AS7270 accept AS7270
import:         from AS7296 accept AS7296
import:         from AS7303 accept AS7303
import:         from AS7311 accept AS7311
import:         from AS7334 accept AS7334
import:         from AS7384 accept AS7384
import:         from AS7459 accept AS7459
import:         from AS7473 accept AS7473
import:         from AS7500 accept AS7500
import:         from AS7713 accept AS7713:AS-TELKOM-TRANSIT
import:         from AS7738 accept AS-OINETBR
import:         from AS7752 accept AS-THRESHINC
import:         from AS7754 accept AS7754
import:         from AS7768 accept AS7768
import:         from AS7784 accept AS-AOI
import:         from AS7786 accept AS7786
import:         from AS7795 accept AS7795
import:         from AS7843 accept AS-ROADRUNNER
import:         from AS7859 accept AS7859
import:         from AS7896 accept AS7896
import:         from AS7944 accept AS7944
import:         from AS7992 accept AS7992
import:         from AS8001 accept AS-NETACCESS
import:         from AS8018 accept AS8018
import:         from AS8038 accept AS8038
import:         from AS8057 accept AS8057:AS-CUSTOMERS
import:         from AS8069 accept AS8069
import:         from AS8075 accept AS-MICROSOFT
import:         from AS8084 accept AS8084
import:         from AS8092 accept AS8092
import:         from AS8100 accept AS-SET-QUADRANET-MIAMI
import:         from AS8111 accept AS8111
import:         from AS8131 accept AS8131
import:         from AS8151 accept AS-8151
import:         from AS8190 accept AS8190
import:         from AS8201 accept AS-EVONET
import:         from AS8245 accept AS8245
import:         from AS8247 accept AS8247
import:         from AS8262 accept AS-EVOLINK
import:         from AS8301 accept AS8301
import:         from AS8304 accept AS8304
import:         from AS8308 accept AS-NASK:AS-Customers
import:         from AS8315 accept AS8315:AS-SENTIA
import:         from AS8318 accept AS8318
import:         from AS8323 accept AS8323
import:         from AS8328 accept AS8328
import:         from AS8368 accept AS-BENESOL
import:         from AS8399 accept AS-SEWAN
import:         from AS8400 accept AS-TELEKOM
import:         from AS8426 accept AS8426
import:         from AS8452 accept AS-TEDATA
import:         from AS8453 accept AS8453
import:         from AS8468 accept AS-ENTANET
import:         from AS8476 accept AS8476
import:         from AS8487 accept AS8487
import:         from AS8495 accept AS8495
import:         from AS8513 accept AS-SKYVISION
import:         from AS8523 accept AS8523
import:         from AS8551 accept AS-BEZEQINT
import:         from AS8554 accept AS8554
import:         from AS8560 accept AS-1AND1
import:         from AS8587 accept AS8587
import:         from AS8607 accept AS-TIMICO
import:         from AS8612 accept AS8612
import:         from AS8648 accept AS8648
import:         from AS8657 accept AS-CPRM
import:         from AS8751 accept AS-MEDIASAT
import:         from AS8757 accept AS-NSFOCUS
import:         from AS8781 accept AS8781
import:         from AS8784 accept AS8784:AS-ODIGO
import:         from AS8793 accept AS8793
import:         from AS8816 accept AS8816
import:         from AS8822 accept AS8822
import:         from AS8849 accept AS-MELBICOM
import:         from AS8851 accept AS8851
import:         from AS8859 accept AS8859
import:         from AS8895 accept AS8895:AS-KACST
import:         from AS8902 accept AS8902
import:         from AS8903 accept AS8903
import:         from AS8918 accept AS8918
import:         from AS8922 accept AS8922
import:         from AS8928 accept AS-INTEROUTE
import:         from AS8954 accept AS8954
import:         from AS8966 accept AS-EMIX
import:         from AS8978 accept AS8978
import:         from AS8990 accept AS8990
import:         from AS9002 accept AS-RETN
import:         from AS9009 accept AS-GBXS
import:         from AS9031 accept AS9031
import:         from AS9038 accept AS-9038
import:         from AS9050 accept AS-RTD
import:         from AS9070 accept AS-ITDOUT
import:         from AS9116 accept AS9116
import:         from AS9137 accept AS9137
import:         from AS9142 accept AS9142
import:         from AS9186 accept AS9186
import:         from AS9192 accept AS9192
import:         from AS9211 accept AS9211
import:         from AS9269 accept AS-HKBN
import:         from AS9304 accept AS9304
import:         from AS9381 accept AS9381
import:         from AS9498 accept AS9498:AS-BHARTI-IN
import:         from AS9658 accept AS9658
import:         from AS9744 accept AS9744
import:         from AS9821 accept AS9821
import:         from AS9829 accept AS9829
import:         from AS10030 accept AS10030
import:         from AS10098 accept AS10098
import:         from AS10099 accept AS-10099NTT
import:         from AS10122 accept AS10122
import:         from AS10325 accept AS10325
import:         from AS10361 accept AS10361
import:         from AS10397 accept AS10397
import:         from AS10461 accept AS10461
import:         from AS10490 accept AS-SOX-TRANSIT
import:         from AS10561 accept AS10561
import:         from AS10625 accept AS10625
import:         from AS10661 accept AS10661
import:         from AS10674 accept AS10674
import:         from AS10700 accept AS10700
import:         from AS10747 accept AS10747
import:         from AS10780 accept AS10780
import:         from AS10835 accept AS-10835
import:         from AS10886 accept AS10886:AS-ISP-PART
import:         from AS10905 accept AS10905
import:         from AS10910 accept AS10910
import:         from AS10982 accept AS10982
import:         from AS10996 accept AS10996
import:         from AS11013 accept AS-11013
import:         from AS11019 accept AS-HAPNET
import:         from AS11036 accept AS11036
import:         from AS11049 accept AS11049
import:         from AS11071 accept AS11071
import:         from AS11074 accept AS11074
import:         from AS11082 accept AS11082
import:         from AS11158 accept AS11158
import:         from AS11174 accept AS11174
import:         from AS11208 accept AS11208
import:         from AS11215 accept AS11215
import:         from AS11232 accept AS-MIDCO
import:         from AS11251 accept AS11251
import:         from AS11260 accept AS-EASTLINK
import:         from AS11262 accept AS11262
import:         from AS11267 accept AS11267
import:         from AS11290 accept AS11290
import:         from AS11320 accept AS-ALL
import:         from AS11323 accept AS11323
import:         from AS11403 accept AS-NYI
import:         from AS11404 accept AS-VOBIZ
import:         from AS11468 accept AS11468
import:         from AS11478 accept AS-OPENFACE
import:         from AS11522 accept AS11522
import:         from AS11528 accept AS11528
import:         from AS11618 accept AS11618
import:         from AS11641 accept AS11641
import:         from AS11647 accept AS11647
import:         from AS11653 accept AS11653
import:         from AS11682 accept AS11682
import:         from AS11696 accept AS-FUSION
import:         from AS11711 accept AS11711
import:         from AS11731 accept AS11731
import:         from AS11747 accept AS11747
import:         from AS11807 accept AS11807
import:         from AS11849 accept AS11849
import:         from AS11852 accept AS11852
import:         from AS11856 accept AS11856
import:         from AS11866 accept AS11866
import:         from AS11876 accept AS11876
import:         from AS11878 accept AS-TZULO
import:         from AS11889 accept AS11889
import:         from AS11924 accept AS11924
import:         from AS11931 accept AS11931
import:         from AS11954 accept AS11954
import:         from AS11966 accept AS11966
import:         from AS12008 accept AS12008
import:         from AS12041 accept AS-AFILIAS-FULLMONTY
import:         from AS12042 accept AS12042
import:         from AS12059 accept AS12059
import:         from AS12083 accept AS-WOW
import:         from AS12085 accept AS-EQUINIX
import:         from AS12096 accept AS12096
import:         from AS12105 accept AS12105
import:         from AS12129 accept AS12129
import:         from AS12132 accept AS12132
import:         from AS12133 accept AS12133
import:         from AS12168 accept AS12168
import:         from AS12175 accept AS12175
import:         from AS12189 accept AS-PHOENIXNAP
import:         from AS12200 accept AS12200
import:         from AS12252 accept AS-TMX-PERU-TRANSIT
import:         from AS12287 accept AS-AFILIAS-FULLMONTY
import:         from AS12301 accept AS12301:AS-ROUTES
import:         from AS12312 accept AS12312
import:         from AS12333 accept AS12333
import:         from AS12348 accept AS12348
import:         from AS12355 accept AS12355
import:         from AS12360 accept AS-KTK-V4
import:         from AS12362 accept AS12362
import:         from AS12372 accept AS12372
import:         from AS12387 accept AS-TON
import:         from AS12389 accept AS-ROSTELECOM
import:         from AS12409 accept AS12409
import:         from AS12414 accept AS12414
import:         from AS12470 accept AS12470
import:         from AS12474 accept AS12474
import:         from AS12480 accept AS12480
import:         from AS12488 accept AS-KRYSTAL
import:         from AS12498 accept AS12498
import:         from AS12533 accept AS12533
import:         from AS12541 accept AS-BTIGS
import:         from AS12546 accept AS12546
import:         from AS12570 accept AS-NEJCZ-TRANSIT
import:         from AS12578 accept AS-LATTELEKOM
import:         from AS12580 accept AS12580
import:         from AS12581 accept AS12581
import:         from AS12586 accept AS-GHOSTNET
import:         from AS12601 accept AS12601
import:         from AS12615 accept AS12615
import:         from AS12625 accept AS-DBG
import:         from AS12655 accept AS12655
import:         from AS12676 accept AS12676
import:         from AS12678 accept AS-BADOO
import:         from AS12684 accept AS12684
import:         from AS12693 accept AS12693
import:         from AS12703 accept AS-PULSANT
import:         from AS12731 accept AS12731
import:         from AS12732 accept AS12732
import:         from AS12741 accept AS-NETIA
import:         from AS12754 accept AS12754
import:         from AS12775 accept AS12775
import:         from AS12779 accept AS12779:AS-CUSTOMERS
import:         from AS12786 accept AS12786
import:         from AS12787 accept AS12787
import:         from AS12801 accept AS12801
import:         from AS12831 accept AS5550:AS-TASK
import:         from AS12843 accept AS12843
import:         from AS12859 accept AS12859
import:         from AS12883 accept AS-UCOMLINE
import:         from AS12884 accept AS12884
import:         from AS12897 accept AS-MEDIANET
import:         from AS12905 accept AS12905
import:         from AS12906 accept AS12906
import:         from AS12945 accept AS12945
import:         from AS12963 accept AS12963
import:         from AS12968 accept AS-CDP
import:         from AS12989 accept AS-HWNG
import:         from AS12993 accept AS-DEAC
import:         from AS13000 accept AS13000
import:         from AS13006 accept AS13006
import:         from AS13039 accept AS13039
import:         from AS13046 accept AS13046
import:         from AS13101 accept AS13101
import:         from AS13105 accept AS13105
import:         from AS13119 accept AS13119:AS-Szczecin-COM
import:         from AS13126 accept AS13126
import:         from AS13132 accept AS13132
import:         from AS13150 accept AS13150
import:         from AS13194 accept AS13194
import:         from AS13213 accept AS-UK2NET
import:         from AS13237 accept AS-LAMBDANET
import:         from AS13250 accept AS13250
import:         from AS13280 accept AS13280
import:         from AS13285 accept AS-OPAL
import:         from AS13287 accept AS13287
import:         from AS13331 accept AS-METAPEER
import:         from AS13333 accept AS13333
import:         from AS13335 accept AS-CLOUDFLARE
import:         from AS13360 accept AS13360
import:         from AS13414 accept AS-TWITTER
import:         from AS13428 accept AS13428
import:         from AS13431 accept AS13431
import:         from AS13443 accept AS13443
import:         from AS13446 accept AS13446
import:         from AS13448 accept AS13448
import:         from AS13464 accept AS13464
import:         from AS13471 accept AS13471
import:         from AS13480 accept AS13480
import:         from AS13490 accept AS13490
import:         from AS13491 accept AS13491
import:         from AS13511 accept AS13511
import:         from AS13517 accept AS13517
import:         from AS13524 accept AS13524
import:         from AS13537 accept AS13537
import:         from AS13556 accept AS13556
import:         from AS13557 accept AS13557
import:         from AS13628 accept AS13628
import:         from AS13631 accept AS13631
import:         from AS13649 accept AS-FLEXENTIAL
import:         from AS13658 accept AS13658
import:         from AS13739 accept AS13739
import:         from AS13760 accept AS-UNITI
import:         from AS13768 accept AS13768:AS-CUSTOMERS
import:         from AS13778 accept AS13778
import:         from AS13789 accept AS13789
import:         from AS13798 accept AS13798
import:         from AS13821 accept AS13821
import:         from AS13860 accept AS13860
import:         from AS13876 accept AS13876
import:         from AS13887 accept AS13887
import:         from AS13909 accept AS13909
import:         from AS13938 accept AS13938
import:         from AS13971 accept AS13971
import:         from AS13981 accept AS13981
import:         from AS13984 accept AS13984
import:         from AS13988 accept AS13988
import:         from AS14010 accept AS14010
import:         from AS14014 accept AS14014
import:         from AS14016 accept AS14016
import:         from AS14037 accept AS-DZEU
import:         from AS14049 accept AS14049
import:         from AS14074 accept AS14074
import:         from AS14080 accept AS14080
import:         from AS14086 accept AS14086
import:         from AS14108 accept AS14108
import:         from AS14135 accept AS14135
import:         from AS14148 accept AS14148
import:         from AS14157 accept AS14157
import:         from AS14170 accept AS14170
import:         from AS14201 accept AS14201
import:         from AS14210 accept AS14210
import:         from AS14237 accept AS14237
import:         from AS14253 accept AS14253
import:         from AS14332 accept AS14332
import:         from AS14335 accept AS14335
import:         from AS14343 accept AS14343
import:         from AS14361 accept AS14361
import:         from AS14365 accept AS14365
import:         from AS14371 accept AS14371
import:         from AS14395 accept AS14395
import:         from AS14398 accept AS14398
import:         from AS14409 accept AS14409
import:         from AS14492 accept AS14492
import:         from AS14500 accept AS14500
import:         from AS14525 accept AS14525
import:         from AS14544 accept AS14544
import:         from AS14585 accept AS14585
import:         from AS14589 accept AS-DWNI
import:         from AS14593 accept AS14593:AS-SX-STARLINK
import:         from AS14601 accept AS14601
import:         from AS14616 accept AS14616
import:         from AS14630 accept AS-IVZ
import:         from AS14643 accept AS14643
import:         from AS14665 accept AS14665
import:         from AS14689 accept AS14689
import:         from AS14707 accept AS14707
import:         from AS14717 accept AS14717
import:         from AS14743 accept AS14743
import:         from AS14745 accept AS14745
import:         from AS14746 accept AS14746
import:         from AS14753 accept AS14753
import:         from AS14754 accept AS14754
import:         from AS14762 accept AS14762
import:         from AS14817 accept AS14817
import:         from AS14821 accept AS14821
import:         from AS14862 accept AS14862
import:         from AS14879 accept AS14879
import:         from AS14928 accept AS-ADAMS
import:         from AS14973 accept AS14973
import:         from AS14986 accept AS14986
import:         from AS14987 accept AS14987
import:         from AS15003 accept AS-NOBIS
import:         from AS15042 accept AS15042
import:         from AS15092 accept AS15092
import:         from AS15093 accept AS15093
import:         from AS15128 accept AS-COMWAVE
import:         from AS15133 accept AS-EDGECAST
import:         from AS15146 accept AS-CBL-TRANSIT
import:         from AS15206 accept AS15206
import:         from AS15211 accept AS-SQUARE
import:         from AS15220 accept AS15220
import:         from AS15225 accept AS15225
import:         from AS15238 accept AS15238
import:         from AS15247 accept AS15247
import:         from AS15277 accept AS15277
import:         from AS15317 accept AS15317
import:         from AS15324 accept AS15324
import:         from AS15346 accept AS15346
import:         from AS15421 accept AS15421
import:         from AS15435 accept AS15435
import:         from AS15447 accept AS15447
import:         from AS15557 accept AS15557
import:         from AS15562 accept AS15562
import:         from AS15570 accept AS15570
import:         from AS15576 accept AS15576
import:         from AS15587 accept AS15587:AS-FOREIGN
import:         from AS15605 accept AS15605
import:         from AS15694 accept AS15694
import:         from AS15695 accept AS-EXPEREO
import:         from AS15703 accept AS-TRUE
import:         from AS15735 accept AS-GOM-GTT
import:         from AS15782 accept AS15782
import:         from AS15806 accept AS15806
import:         from AS15830 accept AS-EQUINIX-EMEA
import:         from AS15879 accept AS15879
import:         from AS15919 accept AS15919
import:         from AS15923 accept AS15923
import:         from AS15924 accept AS15924
import:         from AS15943 accept AS-WTNET
import:         from AS15953 accept AS15953
import:         from AS15954 accept AS-Tecnocratica
import:         from AS15966 accept AS15966
import:         from AS15967 accept AS-NAZWAPL
import:         from AS15989 accept AS15989
import:         from AS15994 accept AS15994
import:         from AS16080 accept AS16080
import:         from AS16097 accept AS16097
import:         from AS16110 accept AS16110
import:         from AS16131 accept AS16131
import:         from AS16147 accept AS16147
import:         from AS16162 accept AS16162
import:         from AS16168 accept AS16168
import:         from AS16189 accept AS-SET-KLEEGROUP-IP4
import:         from AS16236 accept AS16236
import:         from AS16238 accept AS16238
import:         from AS16297 accept AS16297
import:         from AS16360 accept AS16360
import:         from AS16364 accept AS16364
import:         from AS16406 accept AS16406
import:         from AS16501 accept AS16501
import:         from AS16504 accept AS16504
import:         from AS16509 accept AS-AMAZON
import:         from AS16524 accept AS-16524
import:         from AS16551 accept AS16551
import:         from AS16552 accept AS-TIGGEE
import:         from AS16570 accept AS16570
import:         from AS16573 accept AS16573
import:         from AS16591 accept AS-GOOGLE-FIBER
import:         from AS16625 accept AS16625
import:         from AS16633 accept AS16633
import:         from AS16647 accept AS16647
import:         from AS16668 accept AS16668
import:         from AS16676 accept AS16676
import:         from AS16733 accept AS16733
import:         from AS16750 accept AS16750
import:         from AS16761 accept AS16761
import:         from AS16815 accept AS16815
import:         from AS16820 accept AS16820
import:         from AS16823 accept AS16823
import:         from AS16832 accept AS16832
import:         from AS16839 accept AS16839
import:         from AS16851 accept AS16851
import:         from AS16863 accept AS-CONE
import:         from AS16876 accept AS16876
import:         from AS16940 accept AS16940
import:         from AS17012 accept AS-PAYPAL
import:         from AS17035 accept AS17035
import:         from AS17045 accept AS17045
import:         from AS17088 accept AS17088
import:         from AS17130 accept AS17130
import:         from AS17139 accept AS-CORPCOLO
import:         from AS17149 accept AS17149
import:         from AS17151 accept AS17151
import:         from AS17184 accept AS-FUSION
import:         from AS17204 accept AS17204
import:         from AS17240 accept AS17240
import:         from AS17316 accept AS17316
import:         from AS17330 accept AS17330
import:         from AS17352 accept AS17352
import:         from AS17378 accept AS-TIERPOINT
import:         from AS17466 accept AS17466
import:         from AS17666 accept AS17666
import:         from AS17814 accept AS17814
import:         from AS18119 accept AS18119
import:         from AS18214 accept AS18214
import:         from AS18434 accept AS18434
import:         from AS18450 accept AS-WEBNX
import:         from AS18451 accept AS18451
import:         from AS18456 accept AS18456
import:         from AS18465 accept AS18465
import:         from AS18474 accept AS18474
import:         from AS18485 accept AS-NTTGN-US
import:         from AS18518 accept AS18518
import:         from AS18540 accept AS18540
import:         from AS18549 accept AS18549
import:         from AS18566 accept AS18566
import:         from AS18588 accept AS18588
import:         from AS18608 accept AS18608
import:         from AS18619 accept AS18619
import:         from AS18622 accept AS18622
import:         from AS18670 accept AS18670
import:         from AS18712 accept AS-CCI
import:         from AS18717 accept AS18717
import:         from AS18723 accept AS18723
import:         from AS18734 accept AS-BESTEL-NET
import:         from AS18747 accept AS18747
import:         from AS18777 accept AS18777
import:         from AS18779 accept AS-EnergyGroupNetworks
import:         from AS18854 accept AS18854
import:         from AS18880 accept AS18880
import:         from AS18882 accept AS18882
import:         from AS18919 accept AS18919
import:         from AS18929 accept AS18929
import:         from AS18966 accept AS18966
import:         from AS18978 accept AS18978
import:         from AS18990 accept AS18990
import:         from AS18994 accept AS18994
import:         from AS19001 accept AS19001
import:         from AS19006 accept AS19006
import:         from AS19037 accept AS19037
import:         from AS19108 accept AS-SUDDENLINK-TRANSIT
import:         from AS19137 accept AS19137
import:         from AS19165 accept AS-WEBPASS
import:         from AS19186 accept AS-GMCHosting
import:         from AS19193 accept AS19193
import:         from AS19208 accept AS19208
import:         from AS19214 accept AS19214
import:         from AS19222 accept AS19222
import:         from AS19231 accept AS19231
import:         from AS19237 accept AS19237
import:         from AS19305 accept AS19305
import:         from AS19318 accept AS19318
import:         from AS19324 accept AS-AS19324-CUSTAS
import:         from AS19380 accept AS19380
import:         from AS19397 accept AS-ACN
import:         from AS19398 accept AS19398
import:         from AS19416 accept AS19416
import:         from AS19448 accept AS19448
import:         from AS19457 accept AS19457
import:         from AS19460 accept AS19460
import:         from AS19515 accept AS19515:AS-CUSTOMERS
import:         from AS19531 accept AS19531
import:         from AS19551 accept AS-INCAPSULA
import:         from AS19602 accept AS19602
import:         from AS19637 accept AS19637
import:         from AS19679 accept AS-DROPBOX
import:         from AS19683 accept AS19683
import:         from AS19710 accept AS19710
import:         from AS19740 accept AS19740
import:         from AS19750 accept AS19750
import:         from AS19752 accept AS19752
import:         from AS19773 accept AS19773
import:         from AS19803 accept AS19803
import:         from AS19806 accept AS19806
import:         from AS19808 accept AS19808
import:         from AS19811 accept AS19811
import:         from AS19868 accept AS19868
import:         from AS19894 accept AS19894
import:         from AS19905 accept AS-UDOS
import:         from AS19911 accept AS19911
import:         from AS19920 accept AS19920
import:         from AS19936 accept AS19936
import:         from AS19950 accept AS19950
import:         from AS19966 accept AS19966
import:         from AS19969 accept AS19969
import:         from AS19982 accept AS19982
import:         from AS19993 accept AS19993
import:         from AS20054 accept AS20054
import:         from AS20055 accept AS20055
import:         from AS20070 accept AS20070
import:         from AS20077 accept AS20077
import:         from AS20115 accept AS-CHTR-BB
import:         from AS20135 accept AS20135
import:         from AS20144 accept AS20144
import:         from AS20205 accept AS-AMPLEX
import:         from AS20216 accept AS20216
import:         from AS20220 accept AS20220
import:         from AS20223 accept AS20223
import:         from AS20249 accept AS20249
import:         from AS20278 accept AS-NEXEON
import:         from AS20284 accept AS20284
import:         from AS20285 accept AS20285
import:         from AS20326 accept AS-TERASWITCH
import:         from AS20331 accept AS20331
import:         from AS20340 accept AS20340
import:         from AS20355 accept AS20355
import:         from AS20384 accept AS20384
import:         from AS20385 accept AS20385
import:         from AS20429 accept AS20429
import:         from AS20462 accept AS20462
import:         from AS20473 accept AS-CHOOPA
import:         from AS20565 accept AS20565
import:         from AS20621 accept AS20621
import:         from AS20640 accept AS20640
import:         from AS20645 accept AS20645
import:         from AS20650 accept AS20650
import:         from AS20676 accept AS20676
import:         from AS20681 accept AS20681
import:         from AS20694 accept AS20694
import:         from AS20776 accept AS20776
import:         from AS20847 accept AS20847
import:         from AS20853 accept AS-ETOP
import:         from AS20857 accept AS20857
import:         from AS20878 accept AS20878
import:         from AS20896 accept AS20896
import:         from AS20912 accept AS-PANSERVICE
import:         from AS20914 accept AS20914
import:         from AS20917 accept AS20917
import:         from AS20924 accept AS20924
import:         from AS20928 accept AS-NOOR
import:         from AS20940 accept AS-AKAMAI
import:         from AS20953 accept AS20953
import:         from AS20976 accept AS20976
import:         from AS21013 accept AS-ITANDTEL
import:         from AS21034 accept AS21034
import:         from AS21056 accept AS-WELCOMEITALIA
import:         from AS21057 accept AS21057
import:         from AS21069 accept AS21069
import:         from AS21094 accept AS21094
import:         from AS21188 accept AS21188
import:         from AS21221 accept AS21221
import:         from AS21235 accept AS21235
import:         from AS21254 accept AS21254
import:         from AS21267 accept AS21267
import:         from AS21277 accept AS-NT
import:         from AS21321 accept AS21321
import:         from AS21345 accept AS-MESSAGELABSEUROPE
import:         from AS21357 accept AS21357
import:         from AS21371 accept AS-EQUINIX-EU
import:         from AS21409 accept AS21409
import:         from AS21433 accept AS21433
import:         from AS21459 accept AS21459
import:         from AS21488 accept AS21488
import:         from AS21497 accept AS-UMC-CUSTOMERS
import:         from AS21509 accept AS21509
import:         from AS21513 accept AS21513
import:         from AS21534 accept AS-WxC
import:         from AS21537 accept AS21537
import:         from AS21559 accept AS21559:AS-OSNPR
import:         from AS21570 accept AS21570
import:         from AS21589 accept AS21589
import:         from AS21636 accept AS21636
import:         from AS21646 accept AS21646
import:         from AS21655 accept AS21655
import:         from AS21693 accept AS21693
import:         from AS21700 accept AS-NEPTUNE-NETWORKS
import:         from AS21723 accept AS-CONE
import:         from AS21724 accept AS21724
import:         from AS21743 accept AS21743
import:         from AS21755 accept AS21755
import:         from AS21777 accept AS21777
import:         from AS21802 accept AS21802
import:         from AS21804 accept AS-ACCESS_TRANSIT
import:         from AS21859 accept AS-ZENLAYER
import:         from AS21886 accept AS21886
import:         from AS21947 accept AS21947
import:         from AS21983 accept AS21983
import:         from AS22075 accept AS22075
import:         from AS22124 accept AS22124
import:         from AS22191 accept AS22191
import:         from AS22208 accept AS22208
import:         from AS22298 accept AS22298
import:         from AS22317 accept AS22317
import:         from AS22332 accept AS22332
import:         from AS22356 accept AS-DURAND1
import:         from AS22363 accept AS22363
import:         from AS22393 accept AS22393
import:         from AS22404 accept AS22404
import:         from AS22413 accept AS22413
import:         from AS22418 accept AS22418
import:         from AS22512 accept AS22512
import:         from AS22537 accept AS22537
import:         from AS22541 accept AS22541:AS-ALL
import:         from AS22549 accept AS22549
import:         from AS22557 accept AS22557
import:         from AS22611 accept AS22611
import:         from AS22612 accept AS22612
import:         from AS22616 accept AS22616
import:         from AS22620 accept AS22620
import:         from AS22645 accept AS-LEARN-COMM
import:         from AS22646 accept AS22646
import:         from AS22652 accept AS22652
import:         from AS22653 accept AS22653
import:         from AS22683 accept AS22683
import:         from AS22741 accept AS22741
import:         from AS22742 accept AS22742
import:         from AS22768 accept AS22768
import:         from AS22769 accept AS22769
import:         from AS22773 accept AS22773:AS-CONE
import:         from AS22792 accept AS22792
import:         from AS22803 accept AS-NOV
import:         from AS22822 accept AS-LLNW
import:         from AS22838 accept AS22838
import:         from AS22911 accept AS-AS22911
import:         from AS22915 accept AS22915
import:         from AS22925 accept AS-ALLIED_TELECOM
import:         from AS22957 accept AS22957
import:         from AS22964 accept AS22964
import:         from AS22973 accept AS22973
import:         from AS22987 accept AS22987
import:         from AS22995 accept AS-BXI
import:         from AS23010 accept AS23010
import:         from AS23028 accept AS23028
import:         from AS23029 accept AS23029
import:         from AS23081 accept AS23081
import:         from AS23108 accept AS23108
import:         from AS23114 accept AS23114
import:         from AS23132 accept AS23132
import:         from AS23136 accept AS23136
import:         from AS23148 accept AS23148
import:         from AS23161 accept AS23161
import:         from AS23232 accept AS23232
import:         from AS23241 accept AS23241
import:         from AS23247 accept AS23247
import:         from AS23262 accept AS23262
import:         from AS23312 accept AS23312
import:         from AS23314 accept AS-Summit
import:         from AS23316 accept AS23316
import:         from AS23342 accept AS23342
import:         from AS23352 accept AS-SERVERCENTRAL
import:         from AS23367 accept AS-ADAPTIVEDATA
import:         from AS23393 accept AS-NUCDN
import:         from AS23420 accept AS-DAVENPRO
import:         from AS23442 accept AS23442
import:         from AS23470 accept AS23470:AS-ALL
import:         from AS23487 accept AS23487
import:         from AS23498 accept AS23498:AS-CUSTOMERS2
import:         from AS23507 accept AS23507
import:         from AS23528 accept AS23528
import:         from AS23533 accept AS23533
import:         from AS23547 accept AS23547
import:         from AS23576 accept AS-NBP
import:         from AS23655 accept AS-23655-ALL
import:         from AS23764 accept AS23764
import:         from AS23947 accept AS23947:AS-MORATEL
import:         from AS24232 accept AS24232
import:         from AS24331 accept AS24331
import:         from AS24413 accept AS24413
import:         from AS24514 accept AS24514
import:         from AS24637 accept AS-WEBDISCOUNT
import:         from AS24724 accept AS24724
import:         from AS24730 accept AS-NETHOLDING
import:         from AS24750 accept AS24750
import:         from AS24753 accept AS24753
import:         from AS24776 accept AS24776
import:         from AS24778 accept AS24778
import:         from AS24817 accept AS24817
import:         from AS24835 accept AS24835
import:         from AS24875 accept AS24875
import:         from AS24940 accept AS24940
import:         from AS24953 accept AS-24953
import:         from AS24958 accept AS-TBSH-ALL
import:         from AS24989 accept AS-EQUINIX-EU
import:         from AS24990 accept AS-EQUINIX-EU
import:         from AS24993 accept AS24993
import:         from AS25003 accept AS25003
import:         from AS25030 accept AS25030
import:         from AS25038 accept AS25038
import:         from AS25056 accept AS25056
import:         from AS25089 accept AS25089
import:         from AS25091 accept AS-IP-MAX
import:         from AS25148 accept AS-BASEFARM
import:         from AS25182 accept AS25182
import:         from AS25194 accept AS25194
import:         from AS25198 accept AS25198
import:         from AS25220 accept AS25220
import:         from AS25268 accept AS25268
import:         from AS25286 accept AS25286
import:         from AS25369 accept AS-BANDWIDTH
import:         from AS25376 accept AS-NETNORTH
import:         from AS25407 accept AS25407
import:         from AS25421 accept AS25421
import:         from AS25433 accept AS25433
import:         from AS25441 accept AS-IBIS
import:         from AS25459 accept AS25459
import:         from AS25465 accept AS25465
import:         from AS25472 accept AS-WIND-HELLAS
import:         from AS25542 accept AS25542
import:         from AS25562 accept AS25562
import:         from AS25575 accept AS25575
import:         from AS25577 accept AS25577
import:         from AS25593 accept AS25593
import:         from AS25596 accept AS25596
import:         from AS25605 accept AS25605
import:         from AS25614 accept AS25614
import:         from AS25653 accept AS25653
import:         from AS25657 accept AS25657
import:         from AS25697 accept AS-UPCLOUD
import:         from AS25717 accept AS25717
import:         from AS25738 accept AS25738
import:         from AS25773 accept AS25773
import:         from AS25818 accept AS25818
import:         from AS25841 accept AS25841
import:         from AS25844 accept AS25844
import:         from AS25864 accept AS25864
import:         from AS25875 accept AS-FFN
import:         from AS25882 accept AS25882
import:         from AS25894 accept AS25894
import:         from AS25896 accept AS25896
import:         from AS25898 accept AS25898
import:         from AS25934 accept AS25934
import:         from AS25940 accept AS25940
import:         from AS25956 accept AS25956
import:         from AS25973 accept AS25973
import:         from AS25981 accept AS25981
import:         from AS26001 accept AS26001
import:         from AS26008 accept AS26008
import:         from AS26063 accept AS26063
import:         from AS26097 accept AS26097
import:         from AS26120 accept AS26120
import:         from AS26156 accept AS26156
import:         from AS26167 accept AS26167
import:         from AS26237 accept AS26237
import:         from AS26245 accept AS26245
import:         from AS26258 accept AS26258
import:         from AS26265 accept AS26265
import:         from AS26278 accept AS26278
import:         from AS26282 accept AS-SYMC
import:         from AS26342 accept AS26342
import:         from AS26362 accept AS26362
import:         from AS26378 accept AS26378
import:         from AS26380 accept AS26380
import:         from AS26462 accept AS26462
import:         from AS26476 accept AS26476
import:         from AS26512 accept AS26512
import:         from AS26523 accept AS26523
import:         from AS26546 accept AS26546
import:         from AS26554 accept AS26554:AS-Customers
import:         from AS26558 accept AS26558
import:         from AS26577 accept AS26577
import:         from AS26582 accept AS26582
import:         from AS26637 accept AS26637
import:         from AS26642 accept AS26642
import:         from AS26649 accept AS26649
import:         from AS26667 accept AS26667
import:         from AS26669 accept AS26669
import:         from AS26673 accept AS26673
import:         from AS26688 accept AS26688
import:         from AS26744 accept AS-PRTC-TRANSIT
import:         from AS26757 accept AS26757
import:         from AS26759 accept AS26759
import:         from AS26769 accept AS-HWNG
import:         from AS26804 accept AS-SET26804
import:         from AS26848 accept AS26848
import:         from AS26863 accept AS-GSK
import:         from AS26878 accept AS26878
import:         from AS26914 accept AS26914
import:         from AS26931 accept AS26931
import:         from AS26962 accept AS26962
import:         from AS26967 accept AS26967
import:         from AS26972 accept AS-SIRIUS
import:         from AS27177 accept AS27177
import:         from AS27263 accept AS27263
import:         from AS27299 accept AS27299
import:         from AS27301 accept AS27301
import:         from AS27311 accept AS27311
import:         from AS27364 accept AS27364:AS-ALL
import:         from AS27381 accept AS27381
import:         from AS27385 accept AS27385
import:         from AS27393 accept AS27393
import:         from AS27401 accept AS27401
import:         from AS27405 accept AS27405
import:         from AS27439 accept AS27439
import:         from AS27458 accept AS-PROXYPIPE
import:         from AS27471 accept AS-SYMC
import:         from AS27506 accept AS27506
import:         from AS27508 accept AS27508
import:         from AS27536 accept AS27536
import:         from AS27566 accept AS-EQUINIX
import:         from AS27592 accept AS27592
import:         from AS27596 accept AS27596
import:         from AS27612 accept AS27612
import:         from AS27621 accept AS27621
import:         from AS27646 accept AS27646
import:         from AS27647 accept AS27647
import:         from AS27768 accept AS27768
import:         from AS27908 accept AS27908
import:         from AS27978 accept AS27978
import:         from AS28007 accept AS28007
import:         from AS28398 accept AS-GBIC
import:         from AS28458 accept AS-IENTC-MX
import:         from AS28513 accept AS-28513
import:         from AS28663 accept AS-FLYS
import:         from AS28677 accept AS28677
import:         from AS28685 accept AS28685
import:         from AS28707 accept AS28707
import:         from AS28729 accept AS28729
import:         from AS28753 accept AS28753
import:         from AS28757 accept AS28757
import:         from AS28760 accept AS28760
import:         from AS28776 accept AS28776
import:         from AS28780 accept AS28780
import:         from AS28786 accept AS28786
import:         from AS28792 accept AS-PUBLICINET
import:         from AS28806 accept AS28806
import:         from AS28817 accept AS28817
import:         from AS28858 accept AS28858
import:         from AS28889 accept AS-LINZNET
import:         from AS28909 accept AS28909
import:         from AS28917 accept AS-FIORD
import:         from AS28920 accept AS28920
import:         from AS28928 accept AS28928
import:         from AS28929 accept AS28929
import:         from AS28959 accept AS28959
import:         from AS28971 accept AS28971
import:         from AS29006 accept AS-POBOX
import:         from AS29019 accept AS29019
import:         from AS29045 accept AS29045
import:         from AS29049 accept AS29049
import:         from AS29056 accept AS29056
import:         from AS29066 accept AS-VELIANET
import:         from AS29081 accept AS-WVNETAT
import:         from AS29097 accept AS-HOSTPOINT
import:         from AS29107 accept AS29107
import:         from AS29119 accept AS29119
import:         from AS29120 accept AS29120
import:         from AS29140 accept AS29140
import:         from AS29152 accept AS-29152
import:         from AS29169 accept AS29169
import:         from AS29177 accept AS29177
import:         from AS29208 accept AS-DIALTELECOM
import:         from AS29259 accept AS29259
import:         from AS29269 accept AS29269
import:         from AS29278 accept AS29278
import:         from AS29286 accept AS29286
import:         from AS29297 accept AS29297
import:         from AS29314 accept AS29314
import:         from AS29386 accept AS29386
import:         from AS29396 accept AS-UNET
import:         from AS29405 accept AS29405
import:         from AS29419 accept AS29419
import:         from AS29430 accept AS29430
import:         from AS29435 accept AS29435
import:         from AS29446 accept AS29446
import:         from AS29449 accept AS29449
import:         from AS29457 accept AS29457
import:         from AS29467 accept AS29467
import:         from AS29518 accept AS29518:AS-BREDBAND2
import:         from AS29535 accept AS29535
import:         from AS29550 accept AS-AS29550
import:         from AS29551 accept AS29551
import:         from AS29591 accept AS29591
import:         from AS29617 accept AS29617
import:         from AS29636 accept AS29636
import:         from AS29644 accept AS-AIRSPEED
import:         from AS29646 accept AS29646
import:         from AS29655 accept AS29655:AS-TRANSIT
import:         from AS29680 accept AS29680
import:         from AS29697 accept AS29697
import:         from AS29732 accept AS29732
import:         from AS29748 accept AS-CARPATHIA
import:         from AS29757 accept AS29757
import:         from AS29761 accept AS29761
import:         from AS29770 accept AS29770
import:         from AS29802 accept AS-29802
import:         from AS29838 accept AS-AMC
import:         from AS29866 accept AS29866
import:         from AS29884 accept AS-EQUINIX
import:         from AS29907 accept AS29907
import:         from AS29909 accept AS29909:AS-METROOPTIC
import:         from AS29960 accept AS29960
import:         from AS29967 accept AS29967
import:         from AS29976 accept AS29976
import:         from AS30012 accept AS30012
import:         from AS30029 accept AS30029
import:         from AS30036 accept AS-MEDIACOM-TRANSIT
import:         from AS30041 accept AS30041
import:         from AS30056 accept AS30056
import:         from AS30071 accept AS30071
import:         from AS30079 accept AS30079
import:         from AS30081 accept AS-CACHENETWORKS
import:         from AS30094 accept AS30094
import:         from AS30103 accept AS30103
import:         from AS30114 accept AS30114
import:         from AS30146 accept AS30146
import:         from AS30148 accept AS30148
import:         from AS30188 accept AS30188
import:         from AS30197 accept AS30197
import:         from AS30215 accept AS30215
import:         from AS30231 accept AS30231
import:         from AS30238 accept AS30238
import:         from AS30286 accept AS30286
import:         from AS30303 accept AS30303
import:         from AS30366 accept AS30366
import:         from AS30367 accept AS30367
import:         from AS30394 accept AS30394
import:         from AS30403 accept AS30403
import:         from AS30404 accept AS30404
import:         from AS30456 accept AS-COSMIC-GLOBAL
import:         from AS30475 accept AS30475
import:         from AS30524 accept AS30524
import:         from AS30588 accept AS30588
import:         from AS30600 accept AS-CMN
import:         from AS30607 accept AS-OPENDNS
import:         from AS30616 accept AS30616
import:         from AS30633 accept AS-LEASEWEB-US
import:         from AS30643 accept AS30643
import:         from AS30742 accept AS30742
import:         from AS30762 accept AS30762
import:         from AS30818 accept AS30818
import:         from AS30827 accept AS30827
import:         from AS30838 accept AS30838
import:         from AS30848 accept AS30848
import:         from AS30891 accept AS30891
import:         from AS30925 accept AS30925
import:         from AS30931 accept AS-IG
import:         from AS30937 accept AS30937
import:         from AS30961 accept AS30961
import:         from AS30967 accept AS30967
import:         from AS31029 accept AS31029
import:         from AS31042 accept AS-SBB
import:         from AS31050 accept AS31050
import:         from AS31059 accept AS31059
import:         from AS31078 accept AS31078
import:         from AS31080 accept AS-GWP-O2
import:         from AS31083 accept AS-31083
import:         from AS31084 accept AS31084
import:         from AS31108 accept AS31108
import:         from AS31115 accept AS31115
import:         from AS31116 accept AS31116
import:         from AS31122 accept AS-DIGIWEB
import:         from AS31131 accept AS31131
import:         from AS31147 accept AS31147
import:         from AS31154 accept AS31154
import:         from AS31221 accept AS31221
import:         from AS31235 accept AS31235
import:         from AS31241 accept AS31241
import:         from AS31242 accept AS31242
import:         from AS31250 accept AS-ODOUT
import:         from AS31263 accept AS31263
import:         from AS31270 accept AS31270
import:         from AS31287 accept AS31287
import:         from AS31293 accept AS31293
import:         from AS31298 accept AS31298
import:         from AS31317 accept AS31317
import:         from AS31400 accept AS31400
import:         from AS31402 accept AS31402
import:         from AS31404 accept AS31404
import:         from AS31424 accept AS31424
import:         from AS31428 accept AS31428
import:         from AS31445 accept AS31445
import:         from AS31463 accept AS31463
import:         from AS31474 accept AS31474
import:         from AS31479 accept AS31479
import:         from AS31529 accept AS-DENIC-ANY
import:         from AS31570 accept AS31570
import:         from AS31595 accept AS-AWELL
import:         from AS31612 accept AS31612
import:         from AS31631 accept AS31631
import:         from AS31641 accept AS31641
import:         from AS31651 accept AS31651
import:         from AS31654 accept AS31654
import:         from AS31655 accept AS31655
import:         from AS31669 accept AS31669
import:         from AS31672 accept AS31672
import:         from AS31688 accept AS31688
import:         from AS31708 accept AS-COREIX
import:         from AS31712 accept AS31712
import:         from AS31727 accept AS31727
import:         from AS31743 accept AS31743
import:         from AS31760 accept AS31760
import:         from AS31798 accept AS31798
import:         from AS31858 accept AS31858
import:         from AS31898 accept AS31898
import:         from AS31917 accept AS31917
import:         from AS31936 accept AS31936
import:         from AS31980 accept AS31980
import:         from AS31983 accept AS31983
import:         from AS32030 accept AS-VOIPSTER
import:         from AS32035 accept AS-NETFORTRIS
import:         from AS32059 accept AS32059
import:         from AS32098 accept AS-32098
import:         from AS32133 accept AS32133
import:         from AS32155 accept AS32155
import:         from AS32181 accept AS-CQ-GIGENET
import:         from AS32201 accept AS32201
import:         from AS32211 accept AS32211
import:         from AS32212 accept AS32212
import:         from AS32217 accept AS-GPIEX
import:         from AS32222 accept AS32222
import:         from AS32256 accept AS32256
import:         from AS32261 accept AS32261
import:         from AS32281 accept AS32281
import:         from AS32286 accept AS32286
import:         from AS32323 accept AS-EC-TR
import:         from AS32354 accept AS32354
import:         from AS32385 accept AS32385
import:         from AS32389 accept AS32389
import:         from AS32425 accept AS32425
import:         from AS32432 accept AS32432
import:         from AS32440 accept AS32440
import:         from AS32444 accept AS32444
import:         from AS32475 accept AS32475
import:         from AS32478 accept AS32478
import:         from AS32484 accept AS32484
import:         from AS32489 accept AS-AS32489
import:         from AS32578 accept AS32578
import:         from AS32596 accept AS32596
import:         from AS32613 accept AS-LEASEWEB-CA
import:         from AS32624 accept AS32624
import:         from AS32648 accept AS32648
import:         from AS32662 accept AS32662
import:         from AS32669 accept AS32669
import:         from AS32671 accept AS32671
import:         from AS32710 accept AS32710
import:         from AS32780 accept AS32780
import:         from AS32798 accept RS-HIGHLINE-TX
import:         from AS32805 accept AS32805
import:         from AS32806 accept AS32806
import:         from AS32880 accept AS32880
import:         from AS32881 accept AS-CFC
import:         from AS32886 accept AS32886
import:         from AS32899 accept AS32899
import:         from AS32934 accept AS-FACEBOOK
import:         from AS32943 accept AS32943
import:         from AS32987 accept AS32987
import:         from AS33007 accept AS33007
import:         from AS33016 accept AS33016
import:         from AS33040 accept AS33040
import:         from AS33047 accept AS33047
import:         from AS33058 accept AS33058
import:         from AS33071 accept AS33071
import:         from AS33132 accept AS-FN
import:         from AS33154 accept AS-DQECUST
import:         from AS33164 accept AS33164
import:         from AS33185 accept AS33185
import:         from AS33189 accept AS33189
import:         from AS33247 accept AS33247
import:         from AS33257 accept AS33257
import:         from AS33280 accept AS33280
import:         from AS33288 accept AS33288
import:         from AS33361 accept AS33361
import:         from AS33368 accept AS33368
import:         from AS33371 accept AS33371
import:         from AS33404 accept AS33404
import:         from AS33419 accept AS33419
import:         from AS33438 accept AS-HIGHWINDS
import:         from AS33445 accept AS-YELP
import:         from AS33459 accept AS33459
import:         from AS33494 accept AS-IHNETWORKS
import:         from AS33529 accept AS-PEAKWEB
import:         from AS33532 accept AS33532
import:         from AS33536 accept AS33536
import:         from AS33549 accept AS33549
import:         from AS33576 accept AS-IMPORTED
import:         from AS33597 accept AS-INFORELAY
import:         from AS33619 accept AS33619
import:         from AS33633 accept AS33633
import:         from AS33675 accept AS33675
import:         from AS33694 accept AS33694
import:         from AS33724 accept AS33724
import:         from AS33802 accept AS33802
import:         from AS33831 accept AS33831
import:         from AS33835 accept AS33835
import:         from AS33874 accept AS33874
import:         from AS33891 accept AS33891
import:         from AS33923 accept AS-ART-COM
import:         from AS33941 accept AS33941
import:         from AS33968 accept AS33968
import:         from AS33986 accept AS33986
import:         from AS34002 accept AS34002
import:         from AS34006 accept AS34006
import:         from AS34074 accept AS34074
import:         from AS34080 accept AS34080
import:         from AS34164 accept AS34164
import:         from AS34178 accept AS34178
import:         from AS34191 accept AS34191
import:         from AS34197 accept AS-SHRD
import:         from AS34209 accept AS-PLIXDC-MIX
import:         from AS34224 accept AS-NETERRA-INT
import:         from AS34245 accept AS34245
import:         from AS34279 accept AS34279
import:         from AS34290 accept AS34290
import:         from AS34305 accept AS34305
import:         from AS34308 accept AS-RIEDEL
import:         from AS34309 accept AS34309
import:         from AS34386 accept AS34386
import:         from AS34393 accept AS34393
import:         from AS34409 accept AS34409
import:         from AS34428 accept AS-GLPR
import:         from AS34442 accept AS34442
import:         from AS34510 accept AS34510
import:         from AS34523 accept AS34523
import:         from AS34525 accept AS34525
import:         from AS34549 accept AS-MEER
import:         from AS34569 accept AS-NETWORXBG
import:         from AS34589 accept AS34589
import:         from AS34697 accept AS34697
import:         from AS34715 accept AS34715
import:         from AS34737 accept AS34737
import:         from AS34762 accept AS34762
import:         from AS34764 accept AS34764
import:         from AS34788 accept AS34788
import:         from AS34814 accept AS34814
import:         from AS34854 accept AS-MERKEL
import:         from AS34863 accept AS34863
import:         from AS34895 accept AS34895
import:         from AS34922 accept AS-NETNAMES
import:         from AS34927 accept AS-iFog
import:         from AS34966 accept AS34966
import:         from AS34967 accept AS34967
import:         from AS34968 accept AS34968
import:         from AS34973 accept AS34973
import:         from AS34979 accept AS34979
import:         from AS34984 accept AS34984:AS-TELLCOM
import:         from AS35030 accept AS35030
import:         from AS35056 accept AS35056
import:         from AS35066 accept AS35066
import:         from AS35070 accept AS35070
import:         from AS35176 accept AS35176
import:         from AS35180 accept AS35180
import:         from AS35228 accept AS35228
import:         from AS35259 accept AS35259
import:         from AS35266 accept AS-EXN
import:         from AS35289 accept AS35289
import:         from AS35311 accept AS35311
import:         from AS35313 accept AS35313
import:         from AS35315 accept AS35315
import:         from AS35327 accept AS35327
import:         from AS35370 accept AS35370
import:         from AS35421 accept AS35421
import:         from AS35426 accept AS35426
import:         from AS35444 accept AS35444
import:         from AS35461 accept AS35461
import:         from AS35491 accept AS-TPNETS
import:         from AS35522 accept AS35522
import:         from AS35548 accept AS35548
import:         from AS35574 accept AS-LOTTOMATICA
import:         from AS35593 accept AS35593
import:         from AS35643 accept AS35643
import:         from AS35679 accept AS35679
import:         from AS35695 accept AS35695
import:         from AS35699 accept AS35699
import:         from AS35745 accept AS-PROVECTOR
import:         from AS35760 accept AS35760
import:         from AS35787 accept AS35787
import:         from AS35825 accept AS35825
import:         from AS35834 accept AS35834
import:         from AS35838 accept AS35838
import:         from AS35872 accept AS35872
import:         from AS35890 accept AS35890
import:         from AS35906 accept AS35906
import:         from AS35908 accept AS35908
import:         from AS35928 accept AS35928
import:         from AS35953 accept AS35953
import:         from AS35974 accept AS-CARPATHIA
import:         from AS35975 accept AS35975
import:         from AS35985 accept AS-ONERINGNETWORKS
import:         from AS35993 accept AS35993
import:         from AS35994 accept AS-AKAMAI
import:         from AS36007 accept AS-Cloudwm
import:         from AS36040 accept AS36040
import:         from AS36062 accept AS36062
import:         from AS36073 accept AS36073
import:         from AS36077 accept AS36077
import:         from AS36086 accept AS-TELX
import:         from AS36103 accept AS36103
import:         from AS36184 accept AS36184
import:         from AS36187 accept AS36187
import:         from AS36224 accept AS36224
import:         from AS36236 accept AS-NETACTUATE
import:         from AS36243 accept AS36243
import:         from AS36306 accept AS36306
import:         from AS36352 accept AS-COLOCROSSING
import:         from AS36385 accept AS36385
import:         from AS36399 accept AS36399
import:         from AS36408 accept AS-PANTHER
import:         from AS36444 accept AS36444
import:         from AS36459 accept AS36459
import:         from AS36473 accept AS36473
import:         from AS36483 accept AS36483
import:         from AS36493 accept AS36493
import:         from AS36589 accept AS36589
import:         from AS36613 accept AS36613
import:         from AS36614 accept AS36614
import:         from AS36657 accept AS36657
import:         from AS36671 accept AS36671
import:         from AS36692 accept AS-OPENDNS
import:         from AS36734 accept AS-PAXIO
import:         from AS36776 accept AS36776
import:         from AS36853 accept AS36853
import:         from AS36884 accept AS36884
import:         from AS37100 accept AS-SET-SEACOM
import:         from AS37271 accept AS-WOLCOMM
import:         from AS37468 accept AS-ANGOLACABLES
import:         from AS37518 accept AS37518
import:         from AS37721 accept AS37721
import:         from AS37958 accept AS37958
import:         from AS38082 accept AS-TIG-GROUP
import:         from AS38880 accept AS-M21
import:         from AS38915 accept AS38915
import:         from AS38930 accept AS38930
import:         from AS38949 accept AS38949
import:         from AS38963 accept AS38963
import:         from AS38966 accept AS38966
import:         from AS38983 accept AS-COPACOCLOUD
import:         from AS39063 accept AS39063
import:         from AS39090 accept AS39090
import:         from AS39116 accept AS39116
import:         from AS39120 accept AS-CONVERGENZE
import:         from AS39175 accept AS-TOUCHTEC
import:         from AS39179 accept AS-NASSTAR
import:         from AS39180 accept AS-LASOTEL
import:         from AS39233 accept AS39233
import:         from AS39234 accept AS39234
import:         from AS39251 accept AS-NETGUARDBG
import:         from AS39271 accept AS39271
import:         from AS39343 accept AS39343
import:         from AS39372 accept AS39372
import:         from AS39392 accept AS-SUPERNETWORK
import:         from AS39447 accept AS39447
import:         from AS39449 accept AS39449
import:         from AS39474 accept AS39474
import:         from AS39477 accept AS39477
import:         from AS39498 accept AS39498
import:         from AS39505 accept AS39505
import:         from AS39506 accept AS39506
import:         from AS39512 accept AS39512
import:         from AS39526 accept AS39526
import:         from AS39545 accept AS-FLUIDATA
import:         from AS39560 accept AS-KT-NET
import:         from AS39572 accept AS39572
import:         from AS39584 accept AS39584
import:         from AS39591 accept AS39591
import:         from AS39636 accept AS39636
import:         from AS39637 accept AS39637
import:         from AS39648 accept AS39648
import:         from AS39686 accept AS-EUROFIBER
import:         from AS39704 accept AS-CJ2
import:         from AS39729 accept AS39729
import:         from AS39766 accept AS39766
import:         from AS39781 accept AS39781
import:         from AS39816 accept AS39816
import:         from AS39822 accept AS39822
import:         from AS39829 accept AS39829
import:         from AS39832 accept AS-OPERA
import:         from AS39852 accept AS39852
import:         from AS39855 accept AS-MOD
import:         from AS39878 accept AS-RAUTER
import:         from AS39884 accept AS39884
import:         from AS39892 accept AS39892
import:         from AS39912 accept AS39912
import:         from AS39923 accept AS-UNIXSOLUTIONS
import:         from AS39964 accept AS39964
import:         from AS40028 accept AS40028:AS-ALL
import:         from AS40029 accept AS40029
import:         from AS40065 accept AS-CNSERVERS
import:         from AS40089 accept AS40089
import:         from AS40123 accept AS40123
import:         from AS40136 accept AS40136
import:         from AS40160 accept AS40160
import:         from AS40165 accept AS40165
import:         from AS40167 accept AS40167
import:         from AS40193 accept AS-TRIT
import:         from AS40224 accept AS40224
import:         from AS40317 accept AS40317
import:         from AS40350 accept AS40350
import:         from AS40401 accept AS40401
import:         from AS40402 accept AS40402
import:         from AS40418 accept AS40418
import:         from AS40430 accept AS40430
import:         from AS40446 accept AS40446
import:         from AS40467 accept AS40467
import:         from AS40490 accept AS40490
import:         from AS40491 accept AS40491
import:         from AS40521 accept AS40521
import:         from AS40523 accept AS40523
import:         from AS40528 accept AS40528
import:         from AS40578 accept AS40578
import:         from AS40581 accept AS40581
import:         from AS40584 accept AS40584
import:         from AS40624 accept AS40624
import:         from AS40657 accept AS40657
import:         from AS40669 accept AS40669
import:         from AS40676 accept AS-40676
import:         from AS40729 accept AS40729
import:         from AS40731 accept AS40731
import:         from AS40739 accept AS40739
import:         from AS40763 accept AS40763
import:         from AS40769 accept AS40769
import:         from AS40788 accept AS40788
import:         from AS40841 accept AS40841
import:         from AS40844 accept AS40844
import:         from AS40858 accept AS40858
import:         from AS40885 accept AS40885
import:         from AS40889 accept AS40889
import:         from AS40922 accept AS40922
import:         from AS40926 accept AS40926
import:         from AS40934 accept AS40934
import:         from AS40988 accept AS40988
import:         from AS41041 accept AS41041
import:         from AS41057 accept AS41057
import:         from AS41073 accept AS-RTE
import:         from AS41135 accept AS41135
import:         from AS41146 accept AS41146
import:         from AS41157 accept AS-OXYMIUM
import:         from AS41160 accept AS41160
import:         from AS41204 accept AS-HC49
import:         from AS41230 accept AS41230
import:         from AS41265 accept AS41265
import:         from AS41291 accept AS41291
import:         from AS41313 accept AS41313
import:         from AS41319 accept AS-SOFTPRO2
import:         from AS41327 accept AS41327:AS-CUSTOMERS
import:         from AS41354 accept AS41354
import:         from AS41357 accept AS41357
import:         from AS41364 accept AS41364:AS-PDIMEMBERS
import:         from AS41410 accept AS41410
import:         from AS41415 accept AS41415
import:         from AS41435 accept AS41435
import:         from AS41436 accept AS41436
import:         from AS41477 accept AS41477
import:         from AS41488 accept AS41488
import:         from AS41495 accept AS-FAELIX
import:         from AS41497 accept AS41497
import:         from AS41508 accept AS-IWACOM
import:         from AS41511 accept AS41511
import:         from AS41538 accept AS41538
import:         from AS41549 accept AS41549
import:         from AS41564 accept as-px9
import:         from AS41653 accept AS41653
import:         from AS41764 accept AS41764
import:         from AS41765 accept AS41765
import:         from AS41803 accept AS41803
import:         from AS41883 accept AS41883
import:         from AS41887 accept AS41887
import:         from AS41931 accept AS41931
import:         from AS41935 accept AS41935
import:         from AS41945 accept AS41945
import:         from AS41960 accept AS41960
import:         from AS41966 accept AS-SKYNET1
import:         from AS42004 accept AS42004
import:         from AS42005 accept AS42005
import:         from AS42013 accept AS42013
import:         from AS42040 accept AS42040
import:         from AS42044 accept AS-CNIC
import:         from AS42128 accept AS42128
import:         from AS42172 accept AS42172
import:         from AS42176 accept AS42176
import:         from AS42177 accept AS42177
import:         from AS42184 accept AS-TKRZ
import:         from AS42211 accept AS42211
import:         from AS42213 accept AS42213
import:         from AS42229 accept AS42229
import:         from AS42266 accept AS42266
import:         from AS42293 accept AS42293
import:         from AS42344 accept AS42344
import:         from AS42366 accept AS42366
import:         from AS42385 accept AS42385
import:         from AS42392 accept AS42392
import:         from AS42401 accept AS42401
import:         from AS42416 accept AS42416
import:         from AS42459 accept AS-FOBUL
import:         from AS42463 accept AS42463
import:         from AS42466 accept AS42466
import:         from AS42467 accept AS42467
import:         from AS42475 accept AS42475
import:         from AS42479 accept AS42479
import:         from AS42555 accept AS-OC-ASSET
import:         from AS42607 accept AS42607
import:         from AS42612 accept AS42612
import:         from AS42624 accept AS42624
import:         from AS42633 accept AS42633
import:         from AS42643 accept AS42643
import:         from AS42673 accept AS42673
import:         from AS42689 accept AS-INUK
import:         from AS42804 accept AS42804
import:         from AS42808 accept AS42808
import:         from AS42816 accept AS42816
import:         from AS42830 accept AS-TVSAT364
import:         from AS42831 accept AS-UKSERVERS
import:         from AS42836 accept AS42836
import:         from AS42845 accept AS42845
import:         from AS42880 accept AS42880
import:         from AS42912 accept AS42912
import:         from AS42927 accept AS-SZARANET
import:         from AS42944 accept AS42944
import:         from AS42989 accept AS42989
import:         from AS43074 accept AS43074
import:         from AS43142 accept AS-ADELINOVIUS
import:         from AS43187 accept AS43187
import:         from AS43205 accept AS43205
import:         from AS43251 accept AS43251
import:         from AS43266 accept AS-ABSET
import:         from AS43289 accept AS43289:AS-EXPORT
import:         from AS43311 accept AS43311
import:         from AS43338 accept AS43338
import:         from AS43372 accept AS43372
import:         from AS43406 accept AS43406
import:         from AS43437 accept AS43437
import:         from AS43438 accept AS43438
import:         from AS43440 accept AS43440
import:         from AS43494 accept AS43494
import:         from AS43515 accept AS-GOOGLE
import:         from AS43519 accept AS-NOMINET-NS
import:         from AS43520 accept AS43520
import:         from AS43534 accept AS43534
import:         from AS43545 accept AS-TELEDATAUK
import:         from AS43578 accept AS43578
import:         from AS43599 accept AS43599
import:         from AS43639 accept AS43639
import:         from AS43641 accept AS43641
import:         from AS43829 accept AS43829
import:         from AS43843 accept AS43843
import:         from AS43848 accept AS43848
import:         from AS43872 accept AS43872
import:         from AS43885 accept AS43885
import:         from AS43894 accept AS43894
import:         from AS43898 accept AS43898
import:         from AS43915 accept AS43915
import:         from AS43935 accept AS43935
import:         from AS43984 accept AS43984
import:         from AS44062 accept AS44062
import:         from AS44066 accept AS-FIRSTCOLO
import:         from AS44086 accept AS44086
import:         from AS44124 accept AS44124
import:         from AS44134 accept AS44134
import:         from AS44150 accept AS44150
import:         from AS44166 accept AS44166
import:         from AS44212 accept AS44212
import:         from AS44217 accept AS44217
import:         from AS44226 accept AS44226
import:         from AS44227 accept AS44227
import:         from AS44356 accept AS44356
import:         from AS44384 accept AS44384
import:         from AS44411 accept AS44411
import:         from AS44426 accept AS44426
import:         from AS44431 accept AS44431
import:         from AS44444 accept AS44444
import:         from AS44451 accept AS44451
import:         from AS44454 accept AS44454
import:         from AS44473 accept AS44473
import:         from AS44521 accept AS-JAGEX
import:         from AS44600 accept AS44600
import:         from AS44608 accept AS44608
import:         from AS44765 accept AS44765
import:         from AS44776 accept AS44776
import:         from AS44784 accept AS44784
import:         from AS44786 accept AS44786
import:         from AS44788 accept AS44788
import:         from AS44806 accept AS44806
import:         from AS44814 accept AS-FOBUL
import:         from AS44815 accept AS44815
import:         from AS44829 accept AS44829
import:         from AS44898 accept AS44898
import:         from AS44901 accept AS-BELCLOUD
import:         from AS44926 accept AS44926
import:         from AS44942 accept AS44942
import:         from AS44946 accept AS44946
import:         from AS44965 accept AS44965
import:         from AS44976 accept AS44976
import:         from AS45187 accept AS45187
import:         from AS45217 accept AS45217
import:         from AS45474 accept AS45474
import:         from AS45499 accept AS45499
import:         from AS45530 accept AS45530
import:         from AS45629 accept AS-45629
import:         from AS45630 accept AS45630
import:         from AS45758 accept AS45758
import:         from AS45896 accept AS45896
import:         from AS45899 accept AS45899
import:         from AS46130 accept AS46130
import:         from AS46160 accept AS46160
import:         from AS46168 accept AS46168
import:         from AS46199 accept AS46199
import:         from AS46261 accept AS-QP
import:         from AS46272 accept AS46272
import:         from AS46281 accept AS46281
import:         from AS46340 accept AS46340
import:         from AS46363 accept AS46363
import:         from AS46371 accept AS46371
import:         from AS46375 accept AS46375
import:         from AS46379 accept AS46379
import:         from AS46395 accept AS46395
import:         from AS46401 accept AS46401
import:         from AS46454 accept AS46454
import:         from AS46455 accept AS46455
import:         from AS46475 accept AS46475
import:         from AS46489 accept AS-TWITCH
import:         from AS46556 accept AS46556
import:         from AS46558 accept AS46558
import:         from AS46559 accept AS46559
import:         from AS46562 accept AS-COLOAT
import:         from AS46573 accept AS46573
import:         from AS46609 accept as-HostingLogistic
import:         from AS46621 accept AS46621
import:         from AS46632 accept AS46632
import:         from AS46635 accept AS46635
import:         from AS46664 accept AS46664
import:         from AS46687 accept AS46687
import:         from AS46711 accept AS46711
import:         from AS46762 accept AS46762
import:         from AS46805 accept AS-CACHEN1
import:         from AS46844 accept AS-46844
import:         from AS46847 accept AS46847
import:         from AS46852 accept AS46852
import:         from AS46865 accept AS46865
import:         from AS46887 accept AS-CCF
import:         from AS46889 accept AS46889
import:         from AS46922 accept AS46922
import:         from AS46931 accept AS46931
import:         from AS46956 accept AS46956
import:         from AS46994 accept AS46994
import:         from AS47099 accept AS47099
import:         from AS47167 accept AS47167
import:         from AS47169 accept AS47169
import:         from AS47195 accept AS47195
import:         from AS47232 accept AS47232
import:         from AS47242 accept AS47242:AS-CUSTOMERS
import:         from AS47292 accept AS-SENTIADK
import:         from AS47381 accept AS47381
import:         from AS47443 accept AS47443
import:         from AS47494 accept AS47494
import:         from AS47532 accept AS47532
import:         from AS47544 accept AS-IQPL
import:         from AS47572 accept AS47572
import:         from AS47674 accept AS-DOTSI
import:         from AS47680 accept AS47680
import:         from AS47720 accept AS47720:AS-CIX
import:         from AS47754 accept AS47754
import:         from AS47762 accept AS47762
import:         from AS47771 accept AS47771
import:         from AS47787 accept AS-EDGOO
import:         from AS47793 accept AS47793
import:         from AS47836 accept AS47836
import:         from AS47850 accept AS-TAU
import:         from AS47866 accept AS47866
import:         from AS47872 accept AS-SOFIA-CONNECT
import:         from AS47874 accept AS47874
import:         from AS47886 accept AS-EQUINIX-EU
import:         from AS47887 accept AS-SET-NTT
import:         from AS47892 accept AS47892
import:         from AS47927 accept AS47927
import:         from AS47946 accept AS47946
import:         from AS47950 accept AS-LNK
import:         from AS47956 accept AS47956
import:         from AS47961 accept AS47961
import:         from AS47969 accept AS47969
import:         from AS47973 accept AS-DRT
import:         from AS48006 accept AS48006
import:         from AS48083 accept AS48083
import:         from AS48119 accept AS48119
import:         from AS48134 accept AS48134
import:         from AS48135 accept AS48135
import:         from AS48137 accept AS48137
import:         from AS48152 accept AS-DLR
import:         from AS48237 accept AS48237
import:         from AS48305 accept AS-XPNTI
import:         from AS48339 accept AS48339
import:         from AS48345 accept AS48345
import:         from AS48348 accept AS-INTERDOMINIOS
import:         from AS48374 accept AS48374
import:         from AS48426 accept AS48426
import:         from AS48447 accept AS48447
import:         from AS48452 accept AS-TRAFFICNET
import:         from AS48468 accept AS48468
import:         from AS48493 accept AS48493
import:         from AS48505 accept AS48505
import:         from AS48544 accept AS-TECNOADSL
import:         from AS48545 accept AS48545
import:         from AS48559 accept AS48559
import:         from AS48582 accept AS-SET-NGENA
import:         from AS48635 accept AS-ASTRALUS
import:         from AS48638 accept AS-CRONOS
import:         from AS48659 accept AS48659
import:         from AS48804 accept AS48804
import:         from AS48809 accept AS48809
import:         from AS48832 accept as-ZAIN-JO-ALL
import:         from AS48846 accept AS48846
import:         from AS48849 accept AS48849
import:         from AS48850 accept AS48850
import:         from AS48851 accept AS48851
import:         from AS48896 accept AS48896
import:         from AS48910 accept AS48910
import:         from AS48918 accept AS-GLOBALWAYS
import:         from AS48950 accept as-px9
import:         from AS48957 accept AS48957
import:         from AS48961 accept AS48961
import:         from AS48967 accept AS48967
import:         from AS48968 accept AS48968
import:         from AS49088 accept AS49088
import:         from AS49102 accept AS-CONNECTED
import:         from AS49158 accept AS49158
import:         from AS49216 accept AS49216
import:         from AS49220 accept AS-AIRIT
import:         from AS49229 accept AS49229
import:         from AS49233 accept AS49233
import:         from AS49289 accept AS-IPROUTE-SET
import:         from AS49296 accept AS49296
import:         from AS49375 accept AS49375
import:         from AS49405 accept AS49405
import:         from AS49415 accept AS49415
import:         from AS49425 accept AS-DLR
import:         from AS49434 accept AS-HHOSTING
import:         from AS49493 accept AS49493
import:         from AS49515 accept AS-NSC
import:         from AS49524 accept AS49524
import:         from AS49567 accept AS49567
import:         from AS49600 accept AS-NEARIP
import:         from AS49605 accept AS49605
import:         from AS49607 accept AS49607
import:         from AS49650 accept AS49650
import:         from AS49677 accept AS49677
import:         from AS49683 accept AS49683
import:         from AS49699 accept AS49699
import:         from AS49709 accept AS49709
import:         from AS49744 accept AS49744
import:         from AS49761 accept AS49761
import:         from AS49765 accept AS49765
import:         from AS49785 accept AS49785
import:         from AS49823 accept AS49823
import:         from AS49838 accept AS49838
import:         from AS49849 accept AS49849
import:         from AS49870 accept AS-49870
import:         from AS49915 accept AS49915
import:         from AS49958 accept AS49958
import:         from AS50020 accept AS50020
import:         from AS50121 accept AS50121
import:         from AS50153 accept AS50153
import:         from AS50173 accept AS50173
import:         from AS50183 accept AS50183
import:         from AS50185 accept AS50185
import:         from AS50188 accept AS-KOLNET
import:         from AS50202 accept AS50202
import:         from AS50226 accept AS50226
import:         from AS50245 accept AS-SERVEREL
import:         from AS50287 accept AS50287
import:         from AS50292 accept AS50292
import:         from AS50300 accept AS50300
import:         from AS50314 accept AS50314
import:         from AS50326 accept AS50326
import:         from AS50331 accept AS50331
import:         from AS50343 accept AS50343
import:         from AS50360 accept AS-TAMATIYA
import:         from AS50411 accept AS50411
import:         from AS50429 accept AS50429
import:         from AS50463 accept AS50463
import:         from AS50469 accept AS50469
import:         from AS50550 accept AS50550
import:         from AS50581 accept AS50581
import:         from AS50584 accept AS50584
import:         from AS50597 accept AS50597
import:         from AS50607 accept AS-EPIX-TRANSIT
import:         from AS50625 accept AS50625
import:         from AS50835 accept AS50835
import:         from AS50877 accept AS-AIRBEAM
import:         from AS50889 accept AS50889
import:         from AS50965 accept AS50965
import:         from AS50974 accept AS50974
import:         from AS50994 accept AS50994
import:         from AS51043 accept AS-ASPIRE
import:         from AS51060 accept AS51060
import:         from AS51068 accept AS51068
import:         from AS51088 accept AS-A2B
import:         from AS51269 accept AS-HEXATOM
import:         from AS51270 accept AS51270
import:         from AS51294 accept AS51294
import:         from AS51303 accept AS51303
import:         from AS51310 accept AS-MATRONIX
import:         from AS51337 accept AS51337
import:         from AS51390 accept AS51390
import:         from AS51394 accept AS51394
import:         from AS51395 accept AS-SOFTPLUS
import:         from AS51399 accept AS51399
import:         from AS51406 accept AS51406
import:         from AS51407 accept AS-MadaSET
import:         from AS51483 accept AS51483
import:         from AS51510 accept AS51510
import:         from AS51553 accept AS-UTILITY
import:         from AS51580 accept AS51580
import:         from AS51582 accept AS51582
import:         from AS51606 accept AS51606
import:         from AS51616 accept AS51616
import:         from AS51664 accept AS51664
import:         from AS51677 accept AS51677
import:         from AS51752 accept AS51752
import:         from AS51761 accept AS51761
import:         from AS51796 accept AS51796
import:         from AS51809 accept AS-BRSK
import:         from AS51820 accept AS51820
import:         from AS51823 accept AS51823
import:         from AS51852 accept AS51852
import:         from AS51857 accept AS51857
import:         from AS51863 accept AS51863
import:         from AS51871 accept AS51871
import:         from AS51890 accept AS51890
import:         from AS51934 accept AS51934
import:         from AS51944 accept AS-PROMEDIA
import:         from AS51960 accept AS51960:AS-PARTNERS
import:         from AS51984 accept AS51984
import:         from AS52030 accept AS52030
import:         from AS52101 accept AS52101
import:         from AS52106 accept AS-GALATEA
import:         from AS52183 accept AS52183
import:         from AS52320 accept AS-GNT
import:         from AS52347 accept AS52347
import:         from AS52393 accept AS52393
import:         from AS52438 accept AS52438
import:         from AS52580 accept AS52580
import:         from AS52873 accept AS52873
import:         from AS53258 accept AS53258
import:         from AS53264 accept AS-CDC
import:         from AS53292 accept AS53292
import:         from AS53316 accept AS53316
import:         from AS53321 accept AS53321
import:         from AS53340 accept AS-FIBERHUB
import:         from AS53342 accept AS53342
import:         from AS53345 accept AS53345
import:         from AS53346 accept AS53346
import:         from AS53362 accept AS53362
import:         from AS53369 accept AS53369
import:         from AS53388 accept AS53388
import:         from AS53398 accept AS53398
import:         from AS53400 accept AS53400
import:         from AS53428 accept AS53428
import:         from AS53440 accept AS53440
import:         from AS53464 accept AS53464
import:         from AS53483 accept AS53483
import:         from AS53487 accept AS53487
import:         from AS53502 accept AS53502
import:         from AS53521 accept AS53521
import:         from AS53560 accept AS53560
import:         from AS53582 accept AS53582
import:         from AS53620 accept AS53620
import:         from AS53639 accept AS53639
import:         from AS53640 accept AS53640
import:         from AS53667 accept AS-FRANTECH
import:         from AS53699 accept AS53699
import:         from AS53722 accept AS53722
import:         from AS53723 accept AS53723
import:         from AS53726 accept AS53726
import:         from AS53764 accept AS53764
import:         from AS53766 accept AS53766
import:         from AS53813 accept AS53813
import:         from AS53828 accept AS-53828-CUSTOMERS
import:         from AS53831 accept AS53831
import:         from AS53845 accept AS53845
import:         from AS53850 accept AS-GORILLASERVERS
import:         from AS53856 accept AS-NJIX
import:         from AS53889 accept AS-MICFO
import:         from AS53902 accept AS53902
import:         from AS53913 accept AS53913
import:         from AS53914 accept AS53914
import:         from AS53939 accept AS53939
import:         from AS53973 accept AS53973
import:         from AS54036 accept AS54036
import:         from AS54040 accept AS54040
import:         from AS54092 accept AS54092
import:         from AS54103 accept AS-MOD
import:         from AS54107 accept AS54107
import:         from AS54119 accept AS54119
import:         from AS54125 accept AS54125
import:         from AS54128 accept AS54128
import:         from AS54197 accept AS54197
import:         from AS54201 accept AS54201
import:         from AS54235 accept AS54235
import:         from AS54247 accept AS54247
import:         from AS54293 accept AS54293
import:         from AS54301 accept AS54301
import:         from AS54303 accept AS54303
import:         from AS54312 accept AS54312
import:         from AS54329 accept AS54329
import:         from AS54359 accept AS54359
import:         from AS54455 accept AS54455
import:         from AS54460 accept AS54460
import:         from AS54483 accept AS54483
import:         from AS54489 accept AS54489
import:         from AS54498 accept AS54498
import:         from AS54509 accept AS54509
import:         from AS54527 accept AS54527:AS-GLOBAL
import:         from AS54531 accept AS54531
import:         from AS54535 accept AS54535
import:         from AS54588 accept AS-EQUINIX
import:         from AS54593 accept AS54593
import:         from AS54600 accept AS-PEGTECHCUSTOMERS
import:         from AS54618 accept AS54618
import:         from AS54624 accept AS54624
import:         from AS54641 accept AS54641
import:         from AS54652 accept AS54652
import:         from AS54706 accept AS54706
import:         from AS54717 accept AS54717
import:         from AS54778 accept AS54778
import:         from AS54816 accept AS54816
import:         from AS54825 accept AS-EQUINIX-EMEA
import:         from AS54913 accept AS54913
import:         from AS54934 accept AS54934
import:         from AS54957 accept AS54957
import:         from AS54963 accept AS54963
import:         from AS54994 accept AS54994
import:         from AS55002 accept AS55002
import:         from AS55011 accept AS55011
import:         from AS55061 accept AS55061
import:         from AS55081 accept AS-24SHELLS
import:         from AS55129 accept AS55129
import:         from AS55191 accept AS55191
import:         from AS55256 accept AS-NETSKOPE
import:         from AS55259 accept AS55259
import:         from AS55786 accept AS55786
import:         from AS55891 accept AS55891
import:         from AS55943 accept AS55943
import:         from AS56286 accept AS-SET-IXTELECOM
import:         from AS56320 accept AS56320
import:         from AS56381 accept AS56381:AS-ALL
import:         from AS56474 accept AS56474
import:         from AS56478 accept AS56478
import:         from AS56504 accept AS56504
import:         from AS56511 accept AS56511
import:         from AS56515 accept AS56515
import:         from AS56575 accept AS56575
import:         from AS56595 accept AS-FLUENCY
import:         from AS56611 accept AS56611
import:         from AS56630 accept AS-MELBICOM
import:         from AS56647 accept AS56647
import:         from AS56655 accept AS-TERRAHOST
import:         from AS56675 accept AS56675
import:         from AS56683 accept AS56683
import:         from AS56767 accept AS56767
import:         from AS56773 accept AS56773
import:         from AS56778 accept AS56778
import:         from AS56786 accept AS56786
import:         from AS56894 accept AS56894
import:         from AS56953 accept AS56953
import:         from AS56958 accept AS56958
import:         from AS56990 accept AS56990
import:         from AS57111 accept AS57111
import:         from AS57141 accept AS57141
import:         from AS57169 accept AS57169
import:         from AS57263 accept AS57263
import:         from AS57276 accept AS-OPTIMITY
import:         from AS57286 accept AS57286
import:         from AS57332 accept AS57332
import:         from AS57344 accept AS-57344
import:         from AS57476 accept AS57476
import:         from AS57478 accept AS57478
import:         from AS57480 accept AS57480
import:         from AS57546 accept AS57546
import:         from AS57607 accept AS57607
import:         from AS57626 accept AS57626
import:         from AS57704 accept AS-SPEEDCLICKSET
import:         from AS57717 accept AS-FBX
import:         from AS57723 accept AS57723
import:         from AS57750 accept AS57750
import:         from AS57795 accept AS57795
import:         from AS57811 accept AS-ATDS-SERVICES
import:         from AS57846 accept AS57846
import:         from AS57877 accept AS57877
import:         from AS57896 accept AS57896
import:         from AS57976 accept AS-BLIZZARD
import:         from AS57987 accept AS57987
import:         from AS58065 accept as-px9
import:         from AS58082 accept AS58082
import:         from AS58131 accept AS58131
import:         from AS58246 accept AS58246
import:         from AS58307 accept AS-RADIX
import:         from AS58321 accept AS-OXYLION-GLOBAL
import:         from AS58453 accept AS-CMI-ALL
import:         from AS58511 accept AS-CIT
import:         from AS58664 accept AS58664
import:         from AS59028 accept AS59028
import:         from AS59253 accept AS59253
import:         from AS59371 accept AS-59371
import:         from AS59432 accept AS-GINERNET
import:         from AS59455 accept AS59455
import:         from AS59492 accept AS59492
import:         from AS59524 accept AS59524
import:         from AS59545 accept AS59545
import:         from AS59580 accept AS59580
import:         from AS59582 accept AS59582
import:         from AS59605 accept AS-ZAINGP
import:         from AS59611 accept AS59611
import:         from AS59655 accept AS59655
import:         from AS59711 accept AS59711
import:         from AS59816 accept AS-SAFEHOSTS
import:         from AS59827 accept AS59827
import:         from AS59842 accept AS59842
import:         from AS59865 accept AS-IVMOB
import:         from AS59874 accept AS59874
import:         from AS59933 accept AS59933
import:         from AS59950 accept AS59950
import:         from AS60015 accept AS60015
import:         from AS60022 accept AS60022
import:         from AS60038 accept AS60038
import:         from AS60068 accept AS-CDN77
import:         from AS60144 accept AS60144
import:         from AS60191 accept AS60191
import:         from AS60193 accept AS60193
import:         from AS60219 accept AS60219
import:         from AS60277 accept AS60277
import:         from AS60339 accept AS-H3GUK
import:         from AS60362 accept AS60362
import:         from AS60384 accept AS60384
import:         from AS60436 accept AS60436
import:         from AS60447 accept AS-I-NET
import:         from AS60475 accept AS60475
import:         from AS60481 accept AS60481
import:         from AS60486 accept AS60486
import:         from AS60497 accept AS-ictmedia01
import:         from AS60501 accept AS60501
import:         from AS60624 accept AS60624
import:         from AS60636 accept AS60636
import:         from AS60669 accept AS60669
import:         from AS60670 accept AS60670
import:         from AS60706 accept AS60706
import:         from AS60736 accept AS60736
import:         from AS60750 accept AS60750
import:         from AS60752 accept AS60752
import:         from AS60758 accept AS60758
import:         from AS60781 accept AS-LEASEWEB-NL
import:         from AS60798 accept AS-SERVEREASY1
import:         from AS60800 accept AS-NETWISE
import:         from AS60822 accept AS60822
import:         from AS60893 accept AS60893
import:         from AS60923 accept AS60923
import:         from AS60940 accept AS60940
import:         from AS61003 accept AS-GTHOST
import:         from AS61018 accept AS61018
import:         from AS61046 accept AS-HZ-HOSTING-LTD
import:         from AS61049 accept AS61049
import:         from AS61149 accept AS61149
import:         from AS61154 accept AS61154
import:         from AS61181 accept AS61181
import:         from AS61215 accept AS61215
import:         from AS61234 accept AS61234
import:         from AS61244 accept AS61244
import:         from AS61266 accept AS61266
import:         from AS61273 accept AS61273
import:         from AS61315 accept AS-SEDMULTITEL
import:         from AS61317 accept AS61317
import:         from AS61323 accept AS-UKFAST
import:         from AS61349 accept AS-MAXITEL
import:         from AS61373 accept AS61373
import:         from AS61429 accept AS61429
import:         from AS61430 accept AS61430
import:         from AS61461 accept AS61461
import:         from AS61573 accept AS61573:AS-CUSTOMERS
import:         from AS62001 accept AS62001
import:         from AS62021 accept AS62021
import:         from AS62044 accept AS62044
import:         from AS62068 accept AS62068
import:         from AS62081 accept AS-EPIX-TRANSIT
import:         from AS62087 accept AS62087
import:         from AS62112 accept AS62112
import:         from AS62129 accept AS62129
import:         from AS62134 accept AS62134
import:         from AS62167 accept AS62167
import:         from AS62168 accept AS62168
import:         from AS62184 accept AS62184
import:         from AS62190 accept AS62190
import:         from AS62234 accept AS62234
import:         from AS62240 accept AS-CLOUVIDER
import:         from AS62244 accept AS62244
import:         from AS62363 accept AS-EGW-IPv4
import:         from AS62488 accept AS62488
import:         from AS62490 accept AS62490
import:         from AS62519 accept AS62519
import:         from AS62523 accept AS62523
import:         from AS62542 accept AS62542
import:         from AS62563 accept AS-GTHOST
import:         from AS62594 accept AS62594
import:         from AS62597 accept AS-NSONE
import:         from AS62638 accept AS62638
import:         from AS62646 accept AS62646
import:         from AS62648 accept AS62648
import:         from AS62664 accept AS62664
import:         from AS62665 accept AS62665
import:         from AS62668 accept AS62668
import:         from AS62698 accept AS62698
import:         from AS62703 accept AS62703
import:         from AS62710 accept AS62710
import:         from AS62713 accept AS62713
import:         from AS62728 accept AS62728
import:         from AS62738 accept AS-ATB
import:         from AS62746 accept AS62746
import:         from AS62769 accept AS62769
import:         from AS62780 accept AS62780
import:         from AS62784 accept AS62784
import:         from AS62798 accept AS62798
import:         from AS62799 accept AS62799
import:         from AS62804 accept AS62804
import:         from AS62833 accept AS-62833-ny4
import:         from AS62834 accept AS62834
import:         from AS62874 accept AS62874:AS-ALL
import:         from AS62887 accept AS62887
import:         from AS62905 accept AS62905
import:         from AS62918 accept AS62918
import:         from AS62955 accept AS-EBAYMTBB
import:         from AS62982 accept AS-US-CHI-TRANSIT
import:         from AS63008 accept AS63008
import:         from AS63023 accept AS-GTHOST
import:         from AS63086 accept AS63086
import:         from AS63103 accept AS63103
import:         from AS63110 accept AS63110
import:         from AS63120 accept AS63120
import:         from AS63140 accept AS63140
import:         from AS63157 accept AS63157
import:         from AS63199 accept AS63199
import:         from AS63213 accept AS63213:AS-GLOBAL
import:         from AS63226 accept AS63226
import:         from AS63267 accept AS63267
import:         from AS63287 accept AS63287
import:         from AS63300 accept AS63300
import:         from AS63311 accept AS-20C
import:         from AS63351 accept AS63351
import:         from AS63365 accept AS63365
import:         from AS63382 accept AS63382
import:         from AS63383 accept AS63383
import:         from AS63395 accept AS63395
import:         from AS63399 accept AS-SWITCHCO
import:         from AS63402 accept AS63402
import:         from AS63428 accept AS63428
import:         from AS63452 accept AS63452
import:         from AS63454 accept AS63454
import:         from AS63471 accept AS63471
import:         from AS63476 accept AS63476
import:         from AS63916 accept AS63916
import:         from AS63949 accept AS63949
import:         from AS64000 accept AS64000
import:         from AS64022 accept AS-Cloudwm
import:         from AS64096 accept AS64096
import:         from AS64122 accept AS64122
import:         from AS64240 accept AS64240
import:         from AS64266 accept AS64266
import:         from AS64275 accept AS64275
import:         from AS64277 accept AS64277
import:         from AS64294 accept AS64294
import:         from AS64304 accept AS64304
import:         from AS64426 accept AS64426
import:         from AS64485 accept AS64485
import:         from AS65538 accept AS65538
import:         from AS65540 accept AS65540
import:         from AS65542 accept AS65542
import:         from AS131189 accept AS131189
import:         from AS131274 accept AS131274
import:         from AS131314 accept AS131314
import:         from AS132057 accept AS132057
import:         from AS132168 accept AS132168
import:         from AS133012 accept AS133012
import:         from AS133335 accept AS133335
import:         from AS133486 accept AS133486
import:         from AS133752 accept AS133752
import:         from AS133936 accept AS133936
import:         from AS133942 accept AS133942
import:         from AS134345 accept AS134345
import:         from AS134351 accept AS134351
import:         from AS134406 accept AS134406
import:         from AS135354 accept AS135354
import:         from AS135356 accept AS135356
import:         from AS135391 accept AS135391
import:         from AS135530 accept AS135530
import:         from AS135607 accept AS-INFINIVAN
import:         from AS136455 accept AS136455
import:         from AS136897 accept AS136897
import:         from AS137753 accept AS137753
import:         from AS137816 accept AS137816
import:         from AS137819 accept AS137819
import:         from AS137912 accept AS137912
import:         from AS138005 accept AS138005
import:         from AS138576 accept AS138576
import:         from AS138611 accept AS138611
import:         from AS139062 accept AS139062
import:         from AS141039 accept AS141039
import:         from AS141235 accept AS141235
import:         from AS142111 accept AS142111
import:         from AS142268 accept AS-QUANTUMCA
import:         from AS142578 accept AS-ELARGE
import:         from AS147049 accept AS147049
import:         from AS196640 accept AS196640
import:         from AS196670 accept AS196670
import:         from AS196681 accept AS196681
import:         from AS196729 accept AS-CZARNET
import:         from AS196755 accept AS196755
import:         from AS196933 accept AS196933
import:         from AS196956 accept AS196956
import:         from AS196975 accept AS196975
import:         from AS196983 accept AS196983
import:         from AS196987 accept AS196987
import:         from AS196998 accept AS196998
import:         from AS197009 accept AS197009
import:         from AS197036 accept AS-IPLINE
import:         from AS197071 accept AS197071
import:         from AS197075 accept AS197075
import:         from AS197106 accept AS197106
import:         from AS197116 accept AS197116
import:         from AS197156 accept AS197156
import:         from AS197181 accept AS197181
import:         from AS197206 accept AS197206
import:         from AS197226 accept AS-SPRINT-SDC
import:         from AS197262 accept AS197262
import:         from AS197264 accept AS197264
import:         from AS197308 accept AS197308
import:         from AS197355 accept AS197355
import:         from AS197429 accept AS197429
import:         from AS197437 accept AS197437
import:         from AS197447 accept AS197447
import:         from AS197479 accept AS197479
import:         from AS197518 accept AS197518
import:         from AS197549 accept AS197549
import:         from AS197572 accept AS197572
import:         from AS197573 accept AS197573
import:         from AS197592 accept AS197592
import:         from AS197610 accept AS197610
import:         from AS197651 accept AS197651
import:         from AS197664 accept AS197664
import:         from AS197667 accept AS197667
import:         from AS197669 accept AS197669
import:         from AS197690 accept AS197690
import:         from AS197711 accept AS197711
import:         from AS197712 accept AS197712
import:         from AS197727 accept AS197727
import:         from AS197809 accept AS197809
import:         from AS197880 accept AS197880
import:         from AS197883 accept AS197883
import:         from AS197902 accept AS197902
import:         from AS197985 accept AS197985
import:         from AS198040 accept AS198040
import:         from AS198045 accept AS198045
import:         from AS198085 accept AS198085
import:         from AS198187 accept AS198187
import:         from AS198193 accept AS198193
import:         from AS198203 accept AS198203
import:         from AS198211 accept AS198211
import:         from AS198216 accept AS198216
import:         from AS198260 accept AS198260
import:         from AS198279 accept AS-ATU-SET
import:         from AS198301 accept AS198301
import:         from AS198330 accept AS198330
import:         from AS198334 accept AS198334
import:         from AS198374 accept AS198374
import:         from AS198386 accept AS198386
import:         from AS198440 accept AS-M12
import:         from AS198452 accept AS198452
import:         from AS198471 accept AS198471
import:         from AS198651 accept AS198651
import:         from AS198726 accept AS198726
import:         from AS198760 accept AS198760
import:         from AS198761 accept AS198761
import:         from AS198847 accept AS198847
import:         from AS198858 accept AS198858
import:         from AS198890 accept AS198890
import:         from AS198935 accept AS198935
import:         from AS198939 accept AS198939
import:         from AS198948 accept AS198948
import:         from AS198949 accept AS198949:AS-SD
import:         from AS199047 accept AS199047
import:         from AS199064 accept AS199064
import:         from AS199081 accept AS199081
import:         from AS199095 accept AS199095
import:         from AS199113 accept AS199113
import:         from AS199114 accept AS199114
import:         from AS199156 accept AS199156
import:         from AS199163 accept AS199163
import:         from AS199190 accept AS199190
import:         from AS199237 accept AS199237
import:         from AS199250 accept AS199250
import:         from AS199283 accept AS199283
import:         from AS199338 accept AS199338
import:         from AS199358 accept AS199358
import:         from AS199403 accept AS199403
import:         from AS199410 accept AS199410
import:         from AS199483 accept AS199483
import:         from AS199496 accept AS199496
import:         from AS199503 accept AS199503
import:         from AS199509 accept AS199509
import:         from AS199524 accept AS-GCORE
import:         from AS199559 accept AS199559
import:         from AS199569 accept AS199569
import:         from AS199617 accept AS199617
import:         from AS199649 accept AS199649
import:         from AS199710 accept AS199710
import:         from AS199713 accept AS199713
import:         from AS199759 accept AS199759
import:         from AS199775 accept AS199775
import:         from AS199790 accept AS-IPTELECOMBG
import:         from AS199799 accept AS199799
import:         from AS199880 accept AS199880
import:         from AS199892 accept AS199892
import:         from AS200031 accept AS200031
import:         from AS200032 accept AS200032
import:         from AS200052 accept AS-FERAL
import:         from AS200089 accept AS-AMSSYSTEM
import:         from AS200099 accept AS200099
import:         from AS200125 accept AS200125
import:         from AS200147 accept AS-HTL
import:         from AS200187 accept AS200187
import:         from AS200271 accept AS200271
import:         from AS200410 accept AS200410
import:         from AS200416 accept AS200416
import:         from AS200425 accept AS200425
import:         from AS200462 accept AS-ETH
import:         from AS200552 accept AS-WHOLESAIL
import:         from AS200562 accept AS200562
import:         from AS200573 accept AS200573
import:         from AS200585 accept AS200585
import:         from AS200587 accept AS200587
import:         from AS200596 accept AS200596
import:         from AS200604 accept AS200604
import:         from AS200612 accept AS-SETGBI
import:         from AS200653 accept AS200653
import:         from AS200692 accept AS200692
import:         from AS200705 accept AS200705
import:         from AS200713 accept AS200713
import:         from AS200738 accept AS200738
import:         from AS200758 accept AS200758
import:         from AS200780 accept AS-APPLIWAVE
import:         from AS200845 accept AS-AVATEL-TRANSIT
import:         from AS200861 accept AS200861
import:         from AS200884 accept AS200884
import:         from AS200899 accept AS200899
import:         from AS200904 accept AS200904
import:         from AS200961 accept AS200961
import:         from AS200994 accept AS200994
import:         from AS200998 accept AS200998
import:         from AS201053 accept AS-EPIX-TRANSIT
import:         from AS201067 accept AS201067
import:         from AS201099 accept AS201099
import:         from AS201101 accept AS201101
import:         from AS201126 accept AS201126
import:         from AS201133 accept AS201133
import:         from AS201188 accept AS201188
import:         from AS201196 accept AS201196
import:         from AS201213 accept AS201213
import:         from AS201222 accept AS201222
import:         from AS201246 accept AS201246
import:         from AS201324 accept AS201324
import:         from AS201333 accept AS201333
import:         from AS201338 accept AS201338
import:         from AS201352 accept AS201352
import:         from AS201375 accept AS201375
import:         from AS201408 accept AS201408
import:         from AS201474 accept AS201474
import:         from AS201478 accept AS201478
import:         from AS201525 accept AS201525
import:         from AS201542 accept AS201542
import:         from AS201565 accept AS201565
import:         from AS201602 accept AS201602
import:         from AS201637 accept AS201637
import:         from AS201710 accept AS201710
import:         from AS201731 accept AS201731
import:         from AS201747 accept AS201747
import:         from AS201789 accept AS-NETOPS
import:         from AS201887 accept AS201887
import:         from AS201895 accept AS201895
import:         from AS201942 accept AS-SOLTIA
import:         from AS201947 accept AS201947
import:         from AS201958 accept AS201958
import:         from AS201971 accept AS-CREEPERHOSTLTD
import:         from AS201990 accept AS201990
import:         from AS201991 accept AS201991
import:         from AS202010 accept AS202010
import:         from AS202032 accept AS202032
import:         from AS202063 accept AS202063
import:         from AS202075 accept AS202075
import:         from AS202149 accept AS202149
import:         from AS202166 accept AS202166
import:         from AS202219 accept AS202219
import:         from AS202321 accept AS202321
import:         from AS202596 accept AS202596
import:         from AS202623 accept AS202623
import:         from AS202688 accept AS202688
import:         from AS202713 accept AS202713
import:         from AS202766 accept AS202766
import:         from AS202885 accept AS202885
import:         from AS202964 accept AS202964
import:         from AS203050 accept AS203050
import:         from AS203055 accept AS203055
import:         from AS203096 accept AS203096
import:         from AS203182 accept AS203182
import:         from AS203184 accept AS203184
import:         from AS203222 accept AS203222
import:         from AS203223 accept AS203223
import:         from AS203256 accept AS203256
import:         from AS203316 accept AS203316
import:         from AS203327 accept AS203327
import:         from AS203346 accept AS-232web
import:         from AS203351 accept AS203351
import:         from AS203380 accept AS203380
import:         from AS203400 accept AS203400
import:         from AS203410 accept AS203410
import:         from AS203585 accept AS203585
import:         from AS203591 accept AS203591
import:         from AS203608 accept AS203608
import:         from AS203639 accept AS203639
import:         from AS203649 accept AS-GOINTERNETUK
import:         from AS203682 accept AS203682
import:         from AS203689 accept AS203689
import:         from AS203724 accept AS203724
import:         from AS203955 accept AS203955
import:         from AS204121 accept AS204121
import:         from AS204126 accept AS204126
import:         from AS204188 accept AS204188
import:         from AS204258 accept AS204258
import:         from AS204260 accept AS-DOTSI
import:         from AS204264 accept AS204264
import:         from AS204353 accept AS-HC49
import:         from AS204419 accept AS204419
import:         from AS204453 accept AS204453
import:         from AS204476 accept AS204476
import:         from AS204536 accept AS204536
import:         from AS204548 accept AS204548
import:         from AS204563 accept AS204563
import:         from AS204577 accept AS-LINZNET
import:         from AS204597 accept AS204597
import:         from AS204622 accept AS204622
import:         from AS204641 accept AS204641
import:         from AS204777 accept AS204777
import:         from AS204801 accept AS204801
import:         from AS204807 accept AS204807
import:         from AS204890 accept AS204890
import:         from AS204959 accept AS204959
import:         from AS204981 accept AS-204981
import:         from AS205016 accept AS-OPERA
import:         from AS205025 accept AS205025
import:         from AS205039 accept AS205039
import:         from AS205041 accept AS205041
import:         from AS205142 accept AS205142
import:         from AS205185 accept AS205185
import:         from AS205263 accept AS205263
import:         from AS205394 accept AS205394
import:         from AS205476 accept AS205476
import:         from AS205544 accept AS205544
import:         from AS205615 accept AS205615
import:         from AS205668 accept AS205668
import:         from AS205697 accept AS205697
import:         from AS205736 accept AS205736
import:         from AS205809 accept AS205809
import:         from AS205817 accept AS205817
import:         from AS205842 accept AS205842
import:         from AS205855 accept AS205855
import:         from AS205860 accept AS205860
import:         from AS205882 accept AS205882
import:         from AS205943 accept AS205943
import:         from AS206067 accept AS-H3GUK
import:         from AS206082 accept AS206082
import:         from AS206121 accept AS206121
import:         from AS206168 accept AS206168
import:         from AS206264 accept AS206264
import:         from AS206370 accept AS206370
import:         from AS206372 accept AS206372
import:         from AS206383 accept AS206383
import:         from AS206399 accept AS206399
import:         from AS206459 accept AS206459
import:         from AS206537 accept AS206537
import:         from AS206539 accept AS206539
import:         from AS206567 accept AS206567
import:         from AS206576 accept AS-ADEPT
import:         from AS206600 accept AS206600
import:         from AS206614 accept AS206614
import:         from AS206662 accept AS206662
import:         from AS206701 accept AS206701
import:         from AS206720 accept AS206720
import:         from AS206741 accept AS206741
import:         from AS206747 accept AS-NCSC-DNS
import:         from AS206776 accept AS206776
import:         from AS206793 accept AS206793
import:         from AS206870 accept AS206870
import:         from AS206892 accept AS206892
import:         from AS206958 accept AS206958
import:         from AS206983 accept AS206983
import:         from AS206984 accept AS206984
import:         from AS207044 accept AS-AIRSPEED
import:         from AS207045 accept AS207045
import:         from AS207063 accept AS207063
import:         from AS207087 accept AS207087
import:         from AS207127 accept AS207127
import:         from AS207137 accept AS-SET-207137
import:         from AS207176 accept AS207176
import:         from AS207367 accept AS207367
import:         from AS207543 accept AS207543
import:         from AS207685 accept AS207685
import:         from AS207686 accept AS207686
import:         from AS207747 accept AS207747
import:         from AS207784 accept AS207784
import:         from AS207856 accept AS207856
import:         from AS207937 accept AS207937
import:         from AS207995 accept AS207995
import:         from AS208098 accept AS208098
import:         from AS208180 accept AS208180
import:         from AS208270 accept AS208270
import:         from AS208350 accept AS208350
import:         from AS208374 accept AS-LU-CIX-2
import:         from AS208416 accept AS208416
import:         from AS208586 accept AS208586
import:         from AS208625 accept AS208625
import:         from AS208693 accept AS208693
import:         from AS208781 accept AS208781
import:         from AS208877 accept AS208877
import:         from AS209181 accept AS209181
import:         from AS209282 accept AS209282
import:         from AS209311 accept AS-VTNKS
import:         from AS209324 accept AS209324
import:         from AS209549 accept AS-Provide
import:         from AS209704 accept AS209704
import:         from AS209765 accept AS209765
import:         from AS209811 accept AS209811
import:         from AS209875 accept AS209875
import:         from AS210040 accept AS210040
import:         from AS210043 accept AS210043
import:         from AS210136 accept AS210136
import:         from AS210211 accept AS210211
import:         from AS210253 accept AS210253
import:         from AS210269 accept AS210269:AS-ALL
import:         from AS210321 accept AS-OPERADORS
import:         from AS210329 accept AS210329
import:         from AS210657 accept AS210657
import:         from AS211029 accept AS211029
import:         from AS211152 accept AS211152
import:         from AS211156 accept AS211156
import:         from AS211526 accept AS211526
import:         from AS211597 accept AS-LITFIBRE
import:         from AS211826 accept AS211826
import:         from AS212045 accept AS212045
import:         from AS212055 accept AS212055
import:         from AS212097 accept AS-VIMTEL
import:         from AS212175 accept AS-ICONIC
import:         from AS212195 accept AS212195
import:         from AS212646 accept AS212646
import:         from AS212708 accept AS212708
import:         from AS212882 accept as-dnxnetwork-set
import:         from AS213035 accept AS213035
import:         from AS213039 accept AS213039
import:         from AS213094 accept AS-FULLFIBRE
import:         from AS213101 accept AS213101
import:         from AS213130 accept AS213130
import:         from AS213202 accept AS-CSG
import:         from AS213205 accept AS213205
import:         from AS213287 accept AS213287
import:         from AS213308 accept AS213308
import:         from AS213373 accept AS213373
import:         from AS262206 accept AS262206:AS-GLOBAL
import:         from AS262287 accept AS262287
import:         from AS262589 accept AS-ITXBR1
import:         from AS262916 accept AS262916
import:         from AS263179 accept AS263179
import:         from AS263735 accept AS263735
import:         from AS264409 accept AS-HUGENET-CUSTOMERS
import:         from AS264763 accept AS-DOSBUFF
import:         from AS265556 accept AS265556
import:         from AS265680 accept AS-FEZ11
import:         from AS329214 accept AS329214
import:         from AS393226 accept AS393226
import:         from AS393234 accept AS393234
import:         from AS393235 accept AS393235
import:         from AS393241 accept AS393241
import:         from AS393246 accept AS393246
import:         from AS393284 accept AS393284
import:         from AS393303 accept AS393303
import:         from AS393316 accept AS393316
import:         from AS393544 accept AS393544
import:         from AS393606 accept AS393606
import:         from AS393646 accept AS393646
import:         from AS393676 accept AS-ZENEDGE
import:         from AS393681 accept AS393681
import:         from AS393725 accept AS393725
import:         from AS393767 accept AS393767
import:         from AS393791 accept AS393791
import:         from AS393826 accept AS393826
import:         from AS393845 accept AS393845
import:         from AS393848 accept AS393848
import:         from AS393886 accept AS393886
import:         from AS393895 accept AS393895
import:         from AS393900 accept AS393900
import:         from AS393950 accept AS393950
import:         from AS393981 accept AS393981
import:         from AS394015 accept AS394015
import:         from AS394085 accept AS394085
import:         from AS394093 accept AS394093
import:         from AS394102 accept AS394102
import:         from AS394122 accept AS394122
import:         from AS394141 accept AS394141
import:         from AS394146 accept AS394146
import:         from AS394186 accept AS394186
import:         from AS394218 accept AS394218
import:         from AS394232 accept AS394232
import:         from AS394244 accept AS394244
import:         from AS394303 accept AS394303
import:         from AS394308 accept AS394308
import:         from AS394346 accept AS394346
import:         from AS394354 accept AS-394354
import:         from AS394380 accept AS394380
import:         from AS394381 accept AS394381
import:         from AS394409 accept AS394409
import:         from AS394430 accept AS394430
import:         from AS394434 accept AS394434
import:         from AS394479 accept AS394479
import:         from AS394480 accept AS394480
import:         from AS394501 accept AS394501
import:         from AS394562 accept AS394562
import:         from AS394584 accept AS394584
import:         from AS394620 accept AS394620
import:         from AS394625 accept AS394625
import:         from AS394628 accept AS394628
import:         from AS394646 accept AS394646
import:         from AS394663 accept AS394663
import:         from AS394687 accept AS394687
import:         from AS394814 accept AS-ISPLI
import:         from AS394851 accept AS394851
import:         from AS394855 accept AS394855
import:         from AS394933 accept AS394933
import:         from AS394935 accept AS394935
import:         from AS394973 accept AS394973
import:         from AS394977 accept AS394977
import:         from AS395052 accept AS395052
import:         from AS395119 accept AS395119
import:         from AS395186 accept AS395186
import:         from AS395247 accept AS395247
import:         from AS395276 accept AS395276
import:         from AS395308 accept AS395308
import:         from AS395309 accept AS395309
import:         from AS395354 accept AS395354
import:         from AS395363 accept AS395363
import:         from AS395369 accept AS395369
import:         from AS395487 accept AS-ACCRETIVE
import:         from AS395505 accept AS395505
import:         from AS395598 accept AS395598
import:         from AS395636 accept AS395636
import:         from AS395654 accept AS395654
import:         from AS395662 accept AS395662
import:         from AS395717 accept AS395717
import:         from AS395743 accept AS395743
import:         from AS395747 accept AS395747
import:         from AS395753 accept AS395753
import:         from AS395849 accept AS395849
import:         from AS395923 accept AS395923
import:         from AS395954 accept AS395954
import:         from AS395978 accept AS395978
import:         from AS396026 accept AS396026
import:         from AS396055 accept AS396055:AS-FIBERXPR
import:         from AS396133 accept AS396133
import:         from AS396158 accept AS396158:AS-ALL
import:         from AS396188 accept AS396188
import:         from AS396190 accept AS396190
import:         from AS396356 accept AS-MAXIHOST
import:         from AS396362 accept AS396362
import:         from AS396417 accept AS396417
import:         from AS396426 accept AS396426
import:         from AS396442 accept AS396442
import:         from AS396472 accept AS396472
import:         from AS396515 accept AS396515
import:         from AS396535 accept AS396535
import:         from AS396871 accept AS396871
import:         from AS396884 accept AS396884
import:         from AS396948 accept AS396948
import:         from AS396949 accept AS396949
import:         from AS396970 accept AS396970
import:         from AS396984 accept AS396984
import:         from AS396986 accept AS396986
import:         from AS396998 accept AS396998:AS-ALL
import:         from AS397025 accept AS397025
import:         from AS397027 accept AS397027
import:         from AS397041 accept AS397041
import:         from AS397048 accept AS397048
import:         from AS397174 accept AS397174
import:         from AS397289 accept AS397289
import:         from AS397301 accept AS397301
import:         from AS397308 accept AS397308
import:         from AS397358 accept AS397358
import:         from AS397369 accept AS397369
import:         from AS397391 accept AS397391
import:         from AS397404 accept AS397404
import:         from AS397418 accept AS397418
import:         from AS397473 accept AS397473
import:         from AS397494 accept AS397494
import:         from AS397505 accept AS397505
import:         from AS397545 accept AS397545
import:         from AS397599 accept AS397599
import:         from AS397601 accept AS397601
import:         from AS397642 accept AS397642
import:         from AS397686 accept AS397686
import:         from AS397689 accept AS397689
import:         from AS397701 accept AS397701
import:         from AS397727 accept AS397727
import:         from AS397751 accept AS397751
import:         from AS397760 accept AS397760
import:         from AS397815 accept AS397815
import:         from AS397912 accept AS397912
import:         from AS397925 accept AS397925
import:         from AS398044 accept AS398044
import:         from AS398107 accept AS398107
import:         from AS398175 accept AS398175
import:         from AS398198 accept AS398198
import:         from AS398240 accept AS398240
import:         from AS398324 accept AS398324
import:         from AS398424 accept AS398424
import:         from AS398427 accept AS398427
import:         from AS398448 accept AS398448
import:         from AS398465 accept AS398465
import:         from AS398698 accept AS-NETASSIST
import:         from AS398712 accept AS-ISPCON
import:         from AS398764 accept AS398764
import:         from AS398765 accept AS398765
import:         from AS398808 accept AS398808
import:         from AS398809 accept AS398809
import:         from AS398814 accept AS398814
import:         from AS398913 accept AS398913
import:         from AS398969 accept AS398969
import:         from AS399024 accept AS399024
import:         from AS399065 accept AS399065
import:         from AS399081 accept AS399081
import:         from AS399143 accept AS399143
import:         from AS399230 accept AS-CFC
import:         from AS399289 accept AS399289
import:         from AS399301 accept AS399301
import:         from AS399424 accept AS399424
import:         from AS399458 accept AS399458
import:         from AS399480 accept AS399480
import:         from AS399515 accept AS399515
import:         from AS399539 accept AS399539
import:         from AS399558 accept AS399558
import:         from AS399587 accept AS399587:AS-ALL
import:         from AS399647 accept AS399647
import:         from AS399678 accept AS399678
import:         from AS399712 accept AS399712
import:         from AS399759 accept AS399759
import:         from AS399808 accept AS399808
import:         from AS399809 accept AS399809
import:         from AS399810 accept AS399810
import:         from AS399814 accept AS399814
import:         from AS399816 accept AS399816
import:         from AS399817 accept AS399817
import:         from AS399818 accept AS399818
import:         from AS399920 accept AS399920
import:         from AS399989 accept AS399989
import:         from AS399998 accept AS399998
import:         from AS400042 accept AS-RIGHTFORGE
import:         from AS400146 accept AS400146
import:         from AS400202 accept AS400202
import:         from AS400282 accept AS400282
import:         from AS400302 accept AS400302
import:         from AS400309 accept AS-GLOBALFRAG
import:         from AS400381 accept AS400381
import:         from AS400444 accept AS400444
import:         from AS400475 accept AS400475
import:         from AS400511 accept AS400511
import:         from AS400541 accept AS400541
import:         from AS400662 accept AS400662
import:         from AS400666 accept AS400666
import:         from AS400687 accept AS400687
import:         from AS400692 accept AS400692
import:         from AS400802 accept AS400802
import:         from AS400852 accept AS400852
mp-import:      afi ipv6.unicast from AS12 accept AS12
mp-import:      afi ipv6.unicast from AS14 accept AS14
mp-import:      afi ipv6.unicast from AS57 accept AS-NLG-TO-TRANSIT
mp-import:      afi ipv6.unicast from AS62 accept AS-C1
mp-import:      afi ipv6.unicast from AS97 accept AS97
mp-import:      afi ipv6.unicast from AS109 accept AS109
mp-import:      afi ipv6.unicast from AS260 accept AS-XCONNECT24
mp-import:      afi ipv6.unicast from AS286 accept AS286
mp-import:      afi ipv6.unicast from AS376 accept AS376
mp-import:      afi ipv6.unicast from AS517 accept AS517
mp-import:      afi ipv6.unicast from AS559 accept AS559
mp-import:      afi ipv6.unicast from AS577 accept AS577:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS600 accept AS600
mp-import:      afi ipv6.unicast from AS766 accept AS766
mp-import:      afi ipv6.unicast from AS792 accept AS792
mp-import:      afi ipv6.unicast from AS812 accept AS-ROGERS:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS852 accept AS-TELUS
mp-import:      afi ipv6.unicast from AS855 accept AS855
mp-import:      afi ipv6.unicast from AS1017 accept AS1017
mp-import:      afi ipv6.unicast from AS1100 accept AS-NUDAY
mp-import:      afi ipv6.unicast from AS1103 accept AS1103
mp-import:      afi ipv6.unicast from AS1213 accept AS-HEANET
mp-import:      afi ipv6.unicast from AS1215 accept AS1215
mp-import:      afi ipv6.unicast from AS1216 accept AS1216
mp-import:      afi ipv6.unicast from AS1219 accept AS1219
mp-import:      afi ipv6.unicast from AS1257 accept AS1257
mp-import:      afi ipv6.unicast from AS1267 accept AS1267
mp-import:      afi ipv6.unicast from AS1341 accept AS1341
mp-import:      afi ipv6.unicast from AS1449 accept AS1449
mp-import:      afi ipv6.unicast from AS1610 accept AS1610
mp-import:      afi ipv6.unicast from AS1612 accept AS1612
mp-import:      afi ipv6.unicast from AS1680 accept AS1680
mp-import:      afi ipv6.unicast from AS1764 accept AS-NEXTLAYER-V6
mp-import:      afi ipv6.unicast from AS1820 accept AS-WTUC
mp-import:      afi ipv6.unicast from AS1828 accept AS-UNITAS
mp-import:      afi ipv6.unicast from AS2121 accept AS2121
mp-import:      afi ipv6.unicast from AS2200 accept AS-RENATER
mp-import:      afi ipv6.unicast from AS2381 accept AS-WISCNET
mp-import:      afi ipv6.unicast from AS2484 accept AS2484
mp-import:      afi ipv6.unicast from AS2516 accept AS2516
mp-import:      afi ipv6.unicast from AS2609 accept AS2609
mp-import:      afi ipv6.unicast from AS2611 accept AS-BELNET
mp-import:      afi ipv6.unicast from AS2698 accept AS2698
mp-import:      afi ipv6.unicast from AS2721 accept AS2721
mp-import:      afi ipv6.unicast from AS2728 accept AS2728
mp-import:      afi ipv6.unicast from AS2734 accept AS-CORESITE
mp-import:      afi ipv6.unicast from AS3170 accept AS-VELOXSERV
mp-import:      afi ipv6.unicast from AS3214 accept AS-XTOM
mp-import:      afi ipv6.unicast from AS3252 accept AS-FBRX
mp-import:      afi ipv6.unicast from AS3255 accept AS3255
mp-import:      afi ipv6.unicast from AS3264 accept AS3264
mp-import:      afi ipv6.unicast from AS3302 accept AS3302
mp-import:      afi ipv6.unicast from AS3367 accept AS3367
mp-import:      afi ipv6.unicast from AS3399 accept AS-OBE
mp-import:      afi ipv6.unicast from AS3584 accept AS3584
mp-import:      afi ipv6.unicast from AS3595 accept AS3595
mp-import:      afi ipv6.unicast from AS3676 accept AS-UIOWA
mp-import:      afi ipv6.unicast from AS3722 accept AS3722
mp-import:      afi ipv6.unicast from AS3728 accept AS3728
mp-import:      afi ipv6.unicast from AS3737 accept AS-PTD
mp-import:      afi ipv6.unicast from AS3842 accept AS-RN1
mp-import:      afi ipv6.unicast from AS3908 accept AS3908
mp-import:      afi ipv6.unicast from AS3943 accept AS3943
mp-import:      afi ipv6.unicast from AS4058 accept AS4058
mp-import:      afi ipv6.unicast from AS4150 accept AS4150
mp-import:      afi ipv6.unicast from AS4181 accept AS-TDS-TRANSIT
mp-import:      afi ipv6.unicast from AS4229 accept AS4229
mp-import:      afi ipv6.unicast from AS4230 accept AS-EMBRATELNET
mp-import:      afi ipv6.unicast from AS4250 accept AS4250
mp-import:      afi ipv6.unicast from AS4385 accept AS4385
mp-import:      afi ipv6.unicast from AS4436 accept AS4436
mp-import:      afi ipv6.unicast from AS4556 accept AS-PACKETFABRIC
mp-import:      afi ipv6.unicast from AS4589 accept AS4589
mp-import:      afi ipv6.unicast from AS4648 accept AS-4648-CUSTOMERS
mp-import:      afi ipv6.unicast from AS4788 accept AS-TMNET-CUSTOMERS
mp-import:      afi ipv6.unicast from AS4826 accept AS4826:AS-VOCUS
mp-import:      afi ipv6.unicast from AS4867 accept AS4867
mp-import:      afi ipv6.unicast from AS4882 accept AS4882
mp-import:      afi ipv6.unicast from AS5008 accept AS5008
mp-import:      afi ipv6.unicast from AS5009 accept AS5009
mp-import:      afi ipv6.unicast from AS5078 accept AS-ONENETOK
mp-import:      afi ipv6.unicast from AS5091 accept AS5091
mp-import:      afi ipv6.unicast from AS5394 accept AS-UNIDATACUST
mp-import:      afi ipv6.unicast from AS5398 accept AS5398
mp-import:      afi ipv6.unicast from AS5409 accept AS5409
mp-import:      afi ipv6.unicast from AS5524 accept AS5524
mp-import:      afi ipv6.unicast from AS5580 accept AS5580
mp-import:      afi ipv6.unicast from AS5582 accept AS5582
mp-import:      afi ipv6.unicast from AS5602 accept AS-KQIT
mp-import:      afi ipv6.unicast from AS5606 accept AS-GTSRO
mp-import:      afi ipv6.unicast from AS5607 accept AS5607
mp-import:      afi ipv6.unicast from AS5645 accept AS5645:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS5669 accept AS5669
mp-import:      afi ipv6.unicast from AS5670 accept AS-VAPOR
mp-import:      afi ipv6.unicast from AS5697 accept AS5697
mp-import:      afi ipv6.unicast from AS5738 accept AS5738:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS5742 accept AS-CCI
mp-import:      afi ipv6.unicast from AS5760 accept AS5760
mp-import:      afi ipv6.unicast from AS5769 accept AS5769
mp-import:      afi ipv6.unicast from AS5777 accept AS5777
mp-import:      afi ipv6.unicast from AS6059 accept AS6059
mp-import:      afi ipv6.unicast from AS6067 accept AS6067
mp-import:      afi ipv6.unicast from AS6071 accept AS6071
mp-import:      afi ipv6.unicast from AS6072 accept AS6072
mp-import:      afi ipv6.unicast from AS6079 accept AS6079
mp-import:      afi ipv6.unicast from AS6142 accept AS6142
mp-import:      afi ipv6.unicast from AS6169 accept AS-KENTIK
mp-import:      afi ipv6.unicast from AS6181 accept AS6181
mp-import:      afi ipv6.unicast from AS6325 accept AS6325
mp-import:      afi ipv6.unicast from AS6327 accept AS-BIGPIPE
mp-import:      afi ipv6.unicast from AS6391 accept AS-URBAN
mp-import:      afi ipv6.unicast from AS6459 accept AS6459
mp-import:      afi ipv6.unicast from AS6498 accept AS-INTRADO-INTERNAL
mp-import:      afi ipv6.unicast from AS6517 accept AS6517
mp-import:      afi ipv6.unicast from AS6566 accept AS6566
mp-import:      afi ipv6.unicast from AS6597 accept AS6597
mp-import:      afi ipv6.unicast from AS6621 accept AS6621
mp-import:      afi ipv6.unicast from AS6643 accept AS6643
mp-import:      afi ipv6.unicast from AS6659 accept AS6659
mp-import:      afi ipv6.unicast from AS6663 accept AS-STARNETSRO
mp-import:      afi ipv6.unicast from AS6667 accept AS6667
mp-import:      afi ipv6.unicast from AS6696 accept AS6696
mp-import:      afi ipv6.unicast from AS6713 accept AS6713
mp-import:      afi ipv6.unicast from AS6717 accept AS6717
mp-import:      afi ipv6.unicast from AS6723 accept AS6723
mp-import:      afi ipv6.unicast from AS6738 accept AS6738
mp-import:      afi ipv6.unicast from AS6752 accept AS6752
mp-import:      afi ipv6.unicast from AS6768 accept AS-EUROTELE
mp-import:      afi ipv6.unicast from AS6770 accept AS6770
mp-import:      afi ipv6.unicast from AS6774 accept AS6774:AS-BICS-TRANSIT
mp-import:      afi ipv6.unicast from AS6779 accept AS6779
mp-import:      afi ipv6.unicast from AS6805 accept AS6805
mp-import:      afi ipv6.unicast from AS6812 accept AS-VIRTUSTREAM-EU
mp-import:      afi ipv6.unicast from AS6848 accept AS6848
mp-import:      afi ipv6.unicast from AS6866 accept AS-CYTANET
mp-import:      afi ipv6.unicast from AS6894 accept AS-KDDIEU
mp-import:      afi ipv6.unicast from AS6898 accept AS-INTERNETONE_CH
mp-import:      afi ipv6.unicast from AS7012 accept AS7012
mp-import:      afi ipv6.unicast from AS7029 accept AS-WINDSTREAM
mp-import:      afi ipv6.unicast from AS7155 accept AS7155
mp-import:      afi ipv6.unicast from AS7160 accept AS7160
mp-import:      afi ipv6.unicast from AS7203 accept AS7203
mp-import:      afi ipv6.unicast from AS7219 accept AS7219
mp-import:      afi ipv6.unicast from AS7226 accept AS7226
mp-import:      afi ipv6.unicast from AS7296 accept AS7296
mp-import:      afi ipv6.unicast from AS7311 accept AS7311
mp-import:      afi ipv6.unicast from AS7459 accept AS7459
mp-import:      afi ipv6.unicast from AS7473 accept AS7473
mp-import:      afi ipv6.unicast from AS7500 accept AS7500
mp-import:      afi ipv6.unicast from AS7713 accept AS7713:AS-TELKOM-TRANSIT
mp-import:      afi ipv6.unicast from AS7738 accept AS-OINETBR
mp-import:      afi ipv6.unicast from AS7752 accept AS-THRESHINC
mp-import:      afi ipv6.unicast from AS7784 accept AS-AOI
mp-import:      afi ipv6.unicast from AS7786 accept AS7786
mp-import:      afi ipv6.unicast from AS7795 accept AS7795
mp-import:      afi ipv6.unicast from AS7843 accept AS-ROADRUNNER
mp-import:      afi ipv6.unicast from AS7859 accept AS7859
mp-import:      afi ipv6.unicast from AS7992 accept AS7992
mp-import:      afi ipv6.unicast from AS8001 accept AS-NETACCESS
mp-import:      afi ipv6.unicast from AS8018 accept AS8018
mp-import:      afi ipv6.unicast from AS8038 accept AS8038
mp-import:      afi ipv6.unicast from AS8057 accept AS8057:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS8069 accept AS8069
mp-import:      afi ipv6.unicast from AS8075 accept AS-MICROSOFT
mp-import:      afi ipv6.unicast from AS8100 accept AS-SET-QUADRANET-MIAMI
mp-import:      afi ipv6.unicast from AS8111 accept AS8111
mp-import:      afi ipv6.unicast from AS8151 accept AS-8151
mp-import:      afi ipv6.unicast from AS8190 accept AS8190
mp-import:      afi ipv6.unicast from AS8245 accept AS8245
mp-import:      afi ipv6.unicast from AS8262 accept AS-EVOLINK6
mp-import:      afi ipv6.unicast from AS8301 accept AS8301
mp-import:      afi ipv6.unicast from AS8304 accept AS8304
mp-import:      afi ipv6.unicast from AS8308 accept AS8308
mp-import:      afi ipv6.unicast from AS8315 accept AS8315:AS-SENTIA
mp-import:      afi ipv6.unicast from AS8328 accept AS8328
mp-import:      afi ipv6.unicast from AS8368 accept AS-BENESOL
mp-import:      afi ipv6.unicast from AS8399 accept AS-SEWAN
mp-import:      afi ipv6.unicast from AS8400 accept AS-TELEKOM
mp-import:      afi ipv6.unicast from AS8426 accept AS8426
mp-import:      afi ipv6.unicast from AS8452 accept AS-TEDATA
mp-import:      afi ipv6.unicast from AS8453 accept AS8453
mp-import:      afi ipv6.unicast from AS8468 accept AS-ENTANET
mp-import:      afi ipv6.unicast from AS8487 accept AS8487
mp-import:      afi ipv6.unicast from AS8495 accept AS8495
mp-import:      afi ipv6.unicast from AS8513 accept AS-SKYVISION
mp-import:      afi ipv6.unicast from AS8523 accept AS8523
mp-import:      afi ipv6.unicast from AS8551 accept AS-BEZEQINT
mp-import:      afi ipv6.unicast from AS8554 accept AS8554
mp-import:      afi ipv6.unicast from AS8560 accept AS-1AND1
mp-import:      afi ipv6.unicast from AS8587 accept AS8587
mp-import:      afi ipv6.unicast from AS8607 accept AS8607
mp-import:      afi ipv6.unicast from AS8612 accept AS8612
mp-import:      afi ipv6.unicast from AS8648 accept AS8648
mp-import:      afi ipv6.unicast from AS8657 accept AS-CPRM
mp-import:      afi ipv6.unicast from AS8751 accept AS-MEDIASAT
mp-import:      afi ipv6.unicast from AS8757 accept AS-NSFOCUS
mp-import:      afi ipv6.unicast from AS8781 accept AS-QTEL-SET
mp-import:      afi ipv6.unicast from AS8784 accept AS8784:AS-ODIGO
mp-import:      afi ipv6.unicast from AS8793 accept AS8793
mp-import:      afi ipv6.unicast from AS8816 accept AS8816
mp-import:      afi ipv6.unicast from AS8822 accept AS8822
mp-import:      afi ipv6.unicast from AS8849 accept AS-MELBICOM
mp-import:      afi ipv6.unicast from AS8851 accept AS8851
mp-import:      afi ipv6.unicast from AS8895 accept AS8895:AS-KACST
mp-import:      afi ipv6.unicast from AS8902 accept AS8902
mp-import:      afi ipv6.unicast from AS8922 accept AS8922
mp-import:      afi ipv6.unicast from AS8928 accept AS-INTEROUTE
mp-import:      afi ipv6.unicast from AS8954 accept AS-INTOUCHPEERS
mp-import:      afi ipv6.unicast from AS8966 accept AS-EMIX
mp-import:      afi ipv6.unicast from AS8978 accept AS8978
mp-import:      afi ipv6.unicast from AS8990 accept AS8990
mp-import:      afi ipv6.unicast from AS9002 accept AS-RETN
mp-import:      afi ipv6.unicast from AS9009 accept AS-GBXS6
mp-import:      afi ipv6.unicast from AS9031 accept AS9031
mp-import:      afi ipv6.unicast from AS9038 accept AS-9038
mp-import:      afi ipv6.unicast from AS9050 accept AS-RTD
mp-import:      afi ipv6.unicast from AS9070 accept AS-ITDOUT
mp-import:      afi ipv6.unicast from AS9116 accept AS9116
mp-import:      afi ipv6.unicast from AS9211 accept AS9211
mp-import:      afi ipv6.unicast from AS9269 accept AS9269
mp-import:      afi ipv6.unicast from AS9304 accept AS9304
mp-import:      afi ipv6.unicast from AS9381 accept AS9381
mp-import:      afi ipv6.unicast from AS9498 accept AS9498:AS-BHARTI-IN
mp-import:      afi ipv6.unicast from AS9658 accept AS9658
mp-import:      afi ipv6.unicast from AS9744 accept AS9744
mp-import:      afi ipv6.unicast from AS9821 accept AS9821
mp-import:      afi ipv6.unicast from AS9829 accept AS9829
mp-import:      afi ipv6.unicast from AS10030 accept AS10030
mp-import:      afi ipv6.unicast from AS10098 accept AS10098
mp-import:      afi ipv6.unicast from AS10099 accept AS-10099
mp-import:      afi ipv6.unicast from AS10122 accept AS10122
mp-import:      afi ipv6.unicast from AS10490 accept AS-SOX-TRANSIT
mp-import:      afi ipv6.unicast from AS10674 accept AS10674
mp-import:      afi ipv6.unicast from AS10700 accept AS10700
mp-import:      afi ipv6.unicast from AS10780 accept AS10780
mp-import:      afi ipv6.unicast from AS10835 accept AS-10835
mp-import:      afi ipv6.unicast from AS10886 accept AS10886
mp-import:      afi ipv6.unicast from AS10910 accept AS10910
mp-import:      afi ipv6.unicast from AS10982 accept AS10982
mp-import:      afi ipv6.unicast from AS10996 accept AS10996
mp-import:      afi ipv6.unicast from AS11013 accept AS11013
mp-import:      afi ipv6.unicast from AS11019 accept AS-HAPNET
mp-import:      afi ipv6.unicast from AS11049 accept AS11049
mp-import:      afi ipv6.unicast from AS11071 accept AS11071
mp-import:      afi ipv6.unicast from AS11074 accept AS11074
mp-import:      afi ipv6.unicast from AS11158 accept AS11158
mp-import:      afi ipv6.unicast from AS11215 accept AS11215
mp-import:      afi ipv6.unicast from AS11232 accept AS-MIDCO
mp-import:      afi ipv6.unicast from AS11251 accept AS11251
mp-import:      afi ipv6.unicast from AS11260 accept AS11260
mp-import:      afi ipv6.unicast from AS11290 accept AS11290
mp-import:      afi ipv6.unicast from AS11320 accept AS-ALL
mp-import:      afi ipv6.unicast from AS11403 accept AS-NYI
mp-import:      afi ipv6.unicast from AS11404 accept AS-VOBIZ
mp-import:      afi ipv6.unicast from AS11468 accept AS11468
mp-import:      afi ipv6.unicast from AS11478 accept AS-OPENFACE
mp-import:      afi ipv6.unicast from AS11522 accept AS11522
mp-import:      afi ipv6.unicast from AS11618 accept AS11618
mp-import:      afi ipv6.unicast from AS11647 accept AS11647
mp-import:      afi ipv6.unicast from AS11682 accept AS11682
mp-import:      afi ipv6.unicast from AS11696 accept AS-FUSION
mp-import:      afi ipv6.unicast from AS11711 accept AS11711
mp-import:      afi ipv6.unicast from AS11807 accept AS11807
mp-import:      afi ipv6.unicast from AS11878 accept AS-TZULO
mp-import:      afi ipv6.unicast from AS11889 accept AS11889
mp-import:      afi ipv6.unicast from AS11924 accept AS11924
mp-import:      afi ipv6.unicast from AS12008 accept AS12008
mp-import:      afi ipv6.unicast from AS12041 accept AS12041
mp-import:      afi ipv6.unicast from AS12042 accept AS12042
mp-import:      afi ipv6.unicast from AS12083 accept AS12083
mp-import:      afi ipv6.unicast from AS12085 accept AS-EQUINIX
mp-import:      afi ipv6.unicast from AS12129 accept AS12129
mp-import:      afi ipv6.unicast from AS12133 accept AS12133
mp-import:      afi ipv6.unicast from AS12189 accept AS-PHOENIXNAP
mp-import:      afi ipv6.unicast from AS12200 accept AS12200
mp-import:      afi ipv6.unicast from AS12252 accept AS-TMX-PERU-TRANSIT
mp-import:      afi ipv6.unicast from AS12287 accept AS12287
mp-import:      afi ipv6.unicast from AS12301 accept AS12301
mp-import:      afi ipv6.unicast from AS12312 accept AS12312
mp-import:      afi ipv6.unicast from AS12348 accept AS12348
mp-import:      afi ipv6.unicast from AS12355 accept AS12355
mp-import:      afi ipv6.unicast from AS12360 accept AS-KTK-V4
mp-import:      afi ipv6.unicast from AS12372 accept AS12372
mp-import:      afi ipv6.unicast from AS12387 accept AS-TON
mp-import:      afi ipv6.unicast from AS12389 accept AS-ROSTELECOM
mp-import:      afi ipv6.unicast from AS12409 accept AS12409
mp-import:      afi ipv6.unicast from AS12414 accept AS12414
mp-import:      afi ipv6.unicast from AS12470 accept AS12470
mp-import:      afi ipv6.unicast from AS12480 accept AS12480
mp-import:      afi ipv6.unicast from AS12488 accept AS-KRYSTAL
mp-import:      afi ipv6.unicast from AS12498 accept AS12498
mp-import:      afi ipv6.unicast from AS12533 accept AS12533
mp-import:      afi ipv6.unicast from AS12541 accept AS-BTIGS6
mp-import:      afi ipv6.unicast from AS12570 accept AS-NEJCZ-TRANSIT
mp-import:      afi ipv6.unicast from AS12578 accept AS-LATTELEKOM
mp-import:      afi ipv6.unicast from AS12581 accept AS12581
mp-import:      afi ipv6.unicast from AS12586 accept AS-GHOSTNET
mp-import:      afi ipv6.unicast from AS12615 accept AS12615
mp-import:      afi ipv6.unicast from AS12625 accept AS-DBG
mp-import:      afi ipv6.unicast from AS12655 accept AS12655
mp-import:      afi ipv6.unicast from AS12676 accept AS12676
mp-import:      afi ipv6.unicast from AS12678 accept AS12678
mp-import:      afi ipv6.unicast from AS12684 accept AS12684
mp-import:      afi ipv6.unicast from AS12693 accept AS12693
mp-import:      afi ipv6.unicast from AS12703 accept AS-PULSANT-V6
mp-import:      afi ipv6.unicast from AS12731 accept AS12731
mp-import:      afi ipv6.unicast from AS12732 accept AS12732
mp-import:      afi ipv6.unicast from AS12741 accept AS-NETIA
mp-import:      afi ipv6.unicast from AS12754 accept AS12754
mp-import:      afi ipv6.unicast from AS12775 accept AS12775
mp-import:      afi ipv6.unicast from AS12779 accept AS12779:AS-CUSTOMERS-V6
mp-import:      afi ipv6.unicast from AS12831 accept AS5550:AS-TASK
mp-import:      afi ipv6.unicast from AS12843 accept AS12843
mp-import:      afi ipv6.unicast from AS12859 accept AS12859
mp-import:      afi ipv6.unicast from AS12883 accept AS12883
mp-import:      afi ipv6.unicast from AS12897 accept AS-MEDIANET
mp-import:      afi ipv6.unicast from AS12905 accept AS12905
mp-import:      afi ipv6.unicast from AS12906 accept AS12906
mp-import:      afi ipv6.unicast from AS12945 accept AS12945
mp-import:      afi ipv6.unicast from AS12963 accept AS12963
mp-import:      afi ipv6.unicast from AS12968 accept AS12968
mp-import:      afi ipv6.unicast from AS12989 accept AS12989
mp-import:      afi ipv6.unicast from AS13000 accept AS13000
mp-import:      afi ipv6.unicast from AS13006 accept AS13006
mp-import:      afi ipv6.unicast from AS13039 accept AS13039
mp-import:      afi ipv6.unicast from AS13101 accept AS13101
mp-import:      afi ipv6.unicast from AS13105 accept AS13105
mp-import:      afi ipv6.unicast from AS13126 accept AS13126
mp-import:      afi ipv6.unicast from AS13132 accept AS13132
mp-import:      afi ipv6.unicast from AS13150 accept AS13150
mp-import:      afi ipv6.unicast from AS13194 accept AS13194
mp-import:      afi ipv6.unicast from AS13213 accept AS-UK2NET
mp-import:      afi ipv6.unicast from AS13237 accept AS-LAMBDANET
mp-import:      afi ipv6.unicast from AS13250 accept AS13250
mp-import:      afi ipv6.unicast from AS13280 accept AS13280
mp-import:      afi ipv6.unicast from AS13285 accept AS-OPAL
mp-import:      afi ipv6.unicast from AS13287 accept AS13287
mp-import:      afi ipv6.unicast from AS13331 accept AS-METAPEER
mp-import:      afi ipv6.unicast from AS13333 accept AS13333
mp-import:      afi ipv6.unicast from AS13335 accept AS-CLOUDFLARE
mp-import:      afi ipv6.unicast from AS13414 accept AS-TWITTER
mp-import:      afi ipv6.unicast from AS13428 accept AS13428
mp-import:      afi ipv6.unicast from AS13431 accept AS13431
mp-import:      afi ipv6.unicast from AS13443 accept AS13443
mp-import:      afi ipv6.unicast from AS13448 accept AS13448
mp-import:      afi ipv6.unicast from AS13464 accept AS13464
mp-import:      afi ipv6.unicast from AS13490 accept AS13490
mp-import:      afi ipv6.unicast from AS13517 accept AS13517
mp-import:      afi ipv6.unicast from AS13524 accept AS13524
mp-import:      afi ipv6.unicast from AS13649 accept AS-FLEXENTIAL
mp-import:      afi ipv6.unicast from AS13658 accept AS13658
mp-import:      afi ipv6.unicast from AS13739 accept AS13739
mp-import:      afi ipv6.unicast from AS13760 accept AS-UNITI
mp-import:      afi ipv6.unicast from AS13768 accept AS13768
mp-import:      afi ipv6.unicast from AS13789 accept AS13789
mp-import:      afi ipv6.unicast from AS13821 accept AS13821
mp-import:      afi ipv6.unicast from AS13860 accept AS13860
mp-import:      afi ipv6.unicast from AS13876 accept AS13876
mp-import:      afi ipv6.unicast from AS13971 accept AS13971
mp-import:      afi ipv6.unicast from AS13984 accept AS13984
mp-import:      afi ipv6.unicast from AS14014 accept AS14014
mp-import:      afi ipv6.unicast from AS14016 accept AS14016
mp-import:      afi ipv6.unicast from AS14037 accept AS-DZEU
mp-import:      afi ipv6.unicast from AS14061 accept AS14061
mp-import:      afi ipv6.unicast from AS14074 accept AS14074
mp-import:      afi ipv6.unicast from AS14080 accept AS14080
mp-import:      afi ipv6.unicast from AS14086 accept AS14086
mp-import:      afi ipv6.unicast from AS14135 accept AS14135
mp-import:      afi ipv6.unicast from AS14148 accept AS14148
mp-import:      afi ipv6.unicast from AS14157 accept AS14157
mp-import:      afi ipv6.unicast from AS14210 accept AS14210
mp-import:      afi ipv6.unicast from AS14237 accept AS14237
mp-import:      afi ipv6.unicast from AS14253 accept AS14253
mp-import:      afi ipv6.unicast from AS14332 accept AS14332
mp-import:      afi ipv6.unicast from AS14335 accept AS14335
mp-import:      afi ipv6.unicast from AS14343 accept AS14343
mp-import:      afi ipv6.unicast from AS14361 accept AS14361
mp-import:      afi ipv6.unicast from AS14365 accept AS14365
mp-import:      afi ipv6.unicast from AS14371 accept AS14371
mp-import:      afi ipv6.unicast from AS14398 accept AS14398
mp-import:      afi ipv6.unicast from AS14525 accept AS14525
mp-import:      afi ipv6.unicast from AS14544 accept AS14544
mp-import:      afi ipv6.unicast from AS14585 accept AS14585
mp-import:      afi ipv6.unicast from AS14589 accept AS14589
mp-import:      afi ipv6.unicast from AS14593 accept AS14593:AS-SX-STARLINK
mp-import:      afi ipv6.unicast from AS14616 accept AS14616
mp-import:      afi ipv6.unicast from AS14630 accept AS-IVZ
mp-import:      afi ipv6.unicast from AS14643 accept AS14643
mp-import:      afi ipv6.unicast from AS14707 accept AS14707
mp-import:      afi ipv6.unicast from AS14717 accept AS14717
mp-import:      afi ipv6.unicast from AS14743 accept AS14743
mp-import:      afi ipv6.unicast from AS14745 accept AS14745
mp-import:      afi ipv6.unicast from AS14746 accept AS14746
mp-import:      afi ipv6.unicast from AS14821 accept AS14821
mp-import:      afi ipv6.unicast from AS14928 accept AS-ADAMS
mp-import:      afi ipv6.unicast from AS14973 accept AS14973
mp-import:      afi ipv6.unicast from AS14987 accept AS14987
mp-import:      afi ipv6.unicast from AS15003 accept AS15003
mp-import:      afi ipv6.unicast from AS15042 accept AS15042
mp-import:      afi ipv6.unicast from AS15092 accept AS15092
mp-import:      afi ipv6.unicast from AS15093 accept AS15093
mp-import:      afi ipv6.unicast from AS15128 accept AS15128
mp-import:      afi ipv6.unicast from AS15133 accept AS-EDGECAST
mp-import:      afi ipv6.unicast from AS15146 accept AS-CBL-TRANSIT
mp-import:      afi ipv6.unicast from AS15206 accept AS15206
mp-import:      afi ipv6.unicast from AS15211 accept AS-SQUARE
mp-import:      afi ipv6.unicast from AS15317 accept AS15317
mp-import:      afi ipv6.unicast from AS15421 accept AS15421
mp-import:      afi ipv6.unicast from AS15435 accept AS15435
mp-import:      afi ipv6.unicast from AS15570 accept AS15570
mp-import:      afi ipv6.unicast from AS15576 accept AS15576
mp-import:      afi ipv6.unicast from AS15587 accept AS15587
mp-import:      afi ipv6.unicast from AS15694 accept AS15694
mp-import:      afi ipv6.unicast from AS15695 accept AS-EXPEREO
mp-import:      afi ipv6.unicast from AS15703 accept AS-TRUE
mp-import:      afi ipv6.unicast from AS15735 accept AS-GOM-GTT
mp-import:      afi ipv6.unicast from AS15782 accept AS15782
mp-import:      afi ipv6.unicast from AS15830 accept AS-EQUINIX-EMEA
mp-import:      afi ipv6.unicast from AS15879 accept AS15879
mp-import:      afi ipv6.unicast from AS15919 accept AS15919
mp-import:      afi ipv6.unicast from AS15924 accept AS15924
mp-import:      afi ipv6.unicast from AS15943 accept AS15943
mp-import:      afi ipv6.unicast from AS15953 accept AS15953
mp-import:      afi ipv6.unicast from AS15954 accept AS-Tecnocratica
mp-import:      afi ipv6.unicast from AS15966 accept AS15966
mp-import:      afi ipv6.unicast from AS15967 accept AS-NAZWAPL
mp-import:      afi ipv6.unicast from AS15989 accept AS15989
mp-import:      afi ipv6.unicast from AS15994 accept AS15994
mp-import:      afi ipv6.unicast from AS16080 accept AS16080
mp-import:      afi ipv6.unicast from AS16097 accept AS16097
mp-import:      afi ipv6.unicast from AS16110 accept AS16110
mp-import:      afi ipv6.unicast from AS16131 accept AS16131
mp-import:      afi ipv6.unicast from AS16147 accept AS16147
mp-import:      afi ipv6.unicast from AS16162 accept AS16162
mp-import:      afi ipv6.unicast from AS16189 accept AS-SET-KLEEGROUP-IP4
mp-import:      afi ipv6.unicast from AS16236 accept AS16236
mp-import:      afi ipv6.unicast from AS16406 accept AS16406
mp-import:      afi ipv6.unicast from AS16504 accept AS16504
mp-import:      afi ipv6.unicast from AS16509 accept AS-AMAZON
mp-import:      afi ipv6.unicast from AS16524 accept AS-16524
mp-import:      afi ipv6.unicast from AS16552 accept AS-TIGGEE
mp-import:      afi ipv6.unicast from AS16570 accept AS16570
mp-import:      afi ipv6.unicast from AS16591 accept AS-GOOGLE-FIBER
mp-import:      afi ipv6.unicast from AS16625 accept AS16625
mp-import:      afi ipv6.unicast from AS16626 accept AS16626
mp-import:      afi ipv6.unicast from AS16633 accept AS16633
mp-import:      afi ipv6.unicast from AS16668 accept AS16668
mp-import:      afi ipv6.unicast from AS16733 accept AS16733
mp-import:      afi ipv6.unicast from AS16750 accept AS16750
mp-import:      afi ipv6.unicast from AS16832 accept AS16832
mp-import:      afi ipv6.unicast from AS16839 accept AS16839
mp-import:      afi ipv6.unicast from AS16851 accept AS16851
mp-import:      afi ipv6.unicast from AS16863 accept AS-CONE
mp-import:      afi ipv6.unicast from AS16876 accept AS16876
mp-import:      afi ipv6.unicast from AS16940 accept AS16940
mp-import:      afi ipv6.unicast from AS17012 accept AS17012
mp-import:      afi ipv6.unicast from AS17035 accept AS17035
mp-import:      afi ipv6.unicast from AS17045 accept AS17045
mp-import:      afi ipv6.unicast from AS17088 accept AS17088
mp-import:      afi ipv6.unicast from AS17139 accept AS-CORPCOLO
mp-import:      afi ipv6.unicast from AS17149 accept AS17149
mp-import:      afi ipv6.unicast from AS17151 accept AS17151
mp-import:      afi ipv6.unicast from AS17184 accept AS-FUSION
mp-import:      afi ipv6.unicast from AS17204 accept AS17204
mp-import:      afi ipv6.unicast from AS17330 accept AS17330
mp-import:      afi ipv6.unicast from AS17378 accept AS-TIERPOINT
mp-import:      afi ipv6.unicast from AS17666 accept AS17666
mp-import:      afi ipv6.unicast from AS18119 accept AS18119
mp-import:      afi ipv6.unicast from AS18450 accept AS-WEBNX
mp-import:      afi ipv6.unicast from AS18451 accept AS18451
mp-import:      afi ipv6.unicast from AS18465 accept AS18465
mp-import:      afi ipv6.unicast from AS18474 accept AS18474
mp-import:      afi ipv6.unicast from AS18485 accept AS-NTTGN-US
mp-import:      afi ipv6.unicast from AS18540 accept AS18540
mp-import:      afi ipv6.unicast from AS18549 accept AS18549
mp-import:      afi ipv6.unicast from AS18588 accept AS18588
mp-import:      afi ipv6.unicast from AS18622 accept AS18622
mp-import:      afi ipv6.unicast from AS18712 accept AS-CCI
mp-import:      afi ipv6.unicast from AS18717 accept AS18717
mp-import:      afi ipv6.unicast from AS18734 accept AS-BESTEL-NET
mp-import:      afi ipv6.unicast from AS18779 accept AS-EnergyGroupNetworks
mp-import:      afi ipv6.unicast from AS18966 accept AS18966
mp-import:      afi ipv6.unicast from AS18978 accept AS18978
mp-import:      afi ipv6.unicast from AS19001 accept AS19001
mp-import:      afi ipv6.unicast from AS19006 accept AS19006
mp-import:      afi ipv6.unicast from AS19037 accept AS19037
mp-import:      afi ipv6.unicast from AS19108 accept AS19108
mp-import:      afi ipv6.unicast from AS19165 accept AS-WEBPASS
mp-import:      afi ipv6.unicast from AS19186 accept AS-GMCHosting
mp-import:      afi ipv6.unicast from AS19214 accept AS19214
mp-import:      afi ipv6.unicast from AS19237 accept AS19237
mp-import:      afi ipv6.unicast from AS19305 accept AS19305
mp-import:      afi ipv6.unicast from AS19318 accept AS19318:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS19324 accept AS-AS19324-CUSTAS
mp-import:      afi ipv6.unicast from AS19397 accept AS19397
mp-import:      afi ipv6.unicast from AS19448 accept AS19448
mp-import:      afi ipv6.unicast from AS19515 accept AS19515
mp-import:      afi ipv6.unicast from AS19531 accept AS19531
mp-import:      afi ipv6.unicast from AS19551 accept AS-INCAPSULA
mp-import:      afi ipv6.unicast from AS19637 accept AS19637
mp-import:      afi ipv6.unicast from AS19679 accept AS-DROPBOX
mp-import:      afi ipv6.unicast from AS19740 accept AS19740
mp-import:      afi ipv6.unicast from AS19750 accept AS19750
mp-import:      afi ipv6.unicast from AS19752 accept AS19752
mp-import:      afi ipv6.unicast from AS19773 accept AS19773
mp-import:      afi ipv6.unicast from AS19803 accept AS19803
mp-import:      afi ipv6.unicast from AS19806 accept AS19806
mp-import:      afi ipv6.unicast from AS19808 accept AS19808
mp-import:      afi ipv6.unicast from AS19868 accept AS19868
mp-import:      afi ipv6.unicast from AS19905 accept AS-UDOS
mp-import:      afi ipv6.unicast from AS19966 accept AS19966
mp-import:      afi ipv6.unicast from AS19969 accept AS19969
mp-import:      afi ipv6.unicast from AS19982 accept AS19982
mp-import:      afi ipv6.unicast from AS20054 accept AS20054
mp-import:      afi ipv6.unicast from AS20055 accept AS20055
mp-import:      afi ipv6.unicast from AS20115 accept AS-CHTR-BB
mp-import:      afi ipv6.unicast from AS20144 accept AS20144
mp-import:      afi ipv6.unicast from AS20205 accept AS-AMPLEX
mp-import:      afi ipv6.unicast from AS20220 accept AS20220
mp-import:      afi ipv6.unicast from AS20249 accept AS20249
mp-import:      afi ipv6.unicast from AS20278 accept AS-NEXEON
mp-import:      afi ipv6.unicast from AS20284 accept AS20284
mp-import:      afi ipv6.unicast from AS20326 accept AS-TERASWITCH
mp-import:      afi ipv6.unicast from AS20355 accept AS20355
mp-import:      afi ipv6.unicast from AS20385 accept AS20385
mp-import:      afi ipv6.unicast from AS20473 accept AS-CHOOPA
mp-import:      afi ipv6.unicast from AS20565 accept AS20565
mp-import:      afi ipv6.unicast from AS20621 accept AS20621
mp-import:      afi ipv6.unicast from AS20640 accept AS20640
mp-import:      afi ipv6.unicast from AS20650 accept AS20650
mp-import:      afi ipv6.unicast from AS20681 accept AS20681
mp-import:      afi ipv6.unicast from AS20694 accept AS20694
mp-import:      afi ipv6.unicast from AS20847 accept AS20847
mp-import:      afi ipv6.unicast from AS20853 accept AS-ETOP
mp-import:      afi ipv6.unicast from AS20857 accept AS20857
mp-import:      afi ipv6.unicast from AS20912 accept AS-PANSERVICE
mp-import:      afi ipv6.unicast from AS20917 accept AS20917
mp-import:      afi ipv6.unicast from AS20924 accept AS20924
mp-import:      afi ipv6.unicast from AS20928 accept AS-NOOR
mp-import:      afi ipv6.unicast from AS20940 accept AS-AKAMAI
mp-import:      afi ipv6.unicast from AS20953 accept AS20953
mp-import:      afi ipv6.unicast from AS21021 accept AS21021
mp-import:      afi ipv6.unicast from AS21034 accept AS21034
mp-import:      afi ipv6.unicast from AS21056 accept AS-WELCOMEITALIA
mp-import:      afi ipv6.unicast from AS21069 accept AS21069
mp-import:      afi ipv6.unicast from AS21221 accept AS21221
mp-import:      afi ipv6.unicast from AS21235 accept AS21235
mp-import:      afi ipv6.unicast from AS21277 accept AS-NT
mp-import:      afi ipv6.unicast from AS21321 accept AS21321
mp-import:      afi ipv6.unicast from AS21345 accept AS-MESSAGELABSEUROPE
mp-import:      afi ipv6.unicast from AS21357 accept AS21357
mp-import:      afi ipv6.unicast from AS21371 accept AS21371
mp-import:      afi ipv6.unicast from AS21409 accept AS21409
mp-import:      afi ipv6.unicast from AS21433 accept AS21433
mp-import:      afi ipv6.unicast from AS21488 accept AS21488
mp-import:      afi ipv6.unicast from AS21497 accept AS-UMC-CUSTOMERS
mp-import:      afi ipv6.unicast from AS21513 accept AS21513
mp-import:      afi ipv6.unicast from AS21534 accept AS-WxC
mp-import:      afi ipv6.unicast from AS21537 accept AS21537
mp-import:      afi ipv6.unicast from AS21559 accept AS21559:AS-OSNPR
mp-import:      afi ipv6.unicast from AS21570 accept AS21570
mp-import:      afi ipv6.unicast from AS21693 accept AS21693
mp-import:      afi ipv6.unicast from AS21700 accept AS-NEPTUNE-NETWORKS
mp-import:      afi ipv6.unicast from AS21723 accept AS-CONE
mp-import:      afi ipv6.unicast from AS21724 accept AS21724
mp-import:      afi ipv6.unicast from AS21743 accept AS21743
mp-import:      afi ipv6.unicast from AS21755 accept AS21755
mp-import:      afi ipv6.unicast from AS21775 accept AS21775
mp-import:      afi ipv6.unicast from AS21777 accept AS21777
mp-import:      afi ipv6.unicast from AS21804 accept AS-ACCESS_TRANSIT
mp-import:      afi ipv6.unicast from AS21859 accept AS-ZENLAYER
mp-import:      afi ipv6.unicast from AS21947 accept AS21947
mp-import:      afi ipv6.unicast from AS22208 accept AS22208
mp-import:      afi ipv6.unicast from AS22298 accept AS22298
mp-import:      afi ipv6.unicast from AS22317 accept AS22317
mp-import:      afi ipv6.unicast from AS22356 accept AS-DURAND1
mp-import:      afi ipv6.unicast from AS22413 accept AS22413
mp-import:      afi ipv6.unicast from AS22418 accept AS22418
mp-import:      afi ipv6.unicast from AS22512 accept AS22512
mp-import:      afi ipv6.unicast from AS22541 accept AS22541:AS-ALL
mp-import:      afi ipv6.unicast from AS22549 accept AS-PBX-CHANGE
mp-import:      afi ipv6.unicast from AS22557 accept AS22557
mp-import:      afi ipv6.unicast from AS22611 accept AS22611
mp-import:      afi ipv6.unicast from AS22612 accept AS22612
mp-import:      afi ipv6.unicast from AS22616 accept AS22616
mp-import:      afi ipv6.unicast from AS22645 accept AS-LEARN-COMM
mp-import:      afi ipv6.unicast from AS22646 accept AS22646
mp-import:      afi ipv6.unicast from AS22652 accept AS22652
mp-import:      afi ipv6.unicast from AS22683 accept AS22683
mp-import:      afi ipv6.unicast from AS22742 accept AS22742
mp-import:      afi ipv6.unicast from AS22768 accept AS22768
mp-import:      afi ipv6.unicast from AS22769 accept AS22769
mp-import:      afi ipv6.unicast from AS22773 accept AS22773:AS-CONE
mp-import:      afi ipv6.unicast from AS22792 accept AS22792
mp-import:      afi ipv6.unicast from AS22822 accept AS-LLNW
mp-import:      afi ipv6.unicast from AS22838 accept AS22838
mp-import:      afi ipv6.unicast from AS22911 accept AS-AS22911
mp-import:      afi ipv6.unicast from AS22915 accept AS22915
mp-import:      afi ipv6.unicast from AS22925 accept AS-ALLIED_TELECOM
mp-import:      afi ipv6.unicast from AS22957 accept AS22957
mp-import:      afi ipv6.unicast from AS22964 accept AS22964
mp-import:      afi ipv6.unicast from AS22987 accept AS22987
mp-import:      afi ipv6.unicast from AS22995 accept AS-BXI
mp-import:      afi ipv6.unicast from AS23028 accept AS23028
mp-import:      afi ipv6.unicast from AS23114 accept AS23114
mp-import:      afi ipv6.unicast from AS23132 accept AS23132
mp-import:      afi ipv6.unicast from AS23148 accept AS23148
mp-import:      afi ipv6.unicast from AS23161 accept AS23161
mp-import:      afi ipv6.unicast from AS23314 accept AS-Summit
mp-import:      afi ipv6.unicast from AS23342 accept AS23342
mp-import:      afi ipv6.unicast from AS23352 accept AS-SERVERCENTRAL
mp-import:      afi ipv6.unicast from AS23367 accept AS-ADAPTIVEDATA
mp-import:      afi ipv6.unicast from AS23393 accept AS-NUCDN
mp-import:      afi ipv6.unicast from AS23420 accept AS-DAVENPRO
mp-import:      afi ipv6.unicast from AS23470 accept AS23470:AS-ALL
mp-import:      afi ipv6.unicast from AS23487 accept AS23487
mp-import:      afi ipv6.unicast from AS23498 accept AS23498:AS-CUSTOMERS2
mp-import:      afi ipv6.unicast from AS23655 accept AS-23655-ALL
mp-import:      afi ipv6.unicast from AS23764 accept AS23764
mp-import:      afi ipv6.unicast from AS23947 accept AS23947:AS-MORATEL
mp-import:      afi ipv6.unicast from AS24232 accept AS24232
mp-import:      afi ipv6.unicast from AS24413 accept AS24413
mp-import:      afi ipv6.unicast from AS24514 accept AS24514
mp-import:      afi ipv6.unicast from AS24637 accept AS-WEBDISCOUNT
mp-import:      afi ipv6.unicast from AS24724 accept AS24724
mp-import:      afi ipv6.unicast from AS24730 accept AS-NETHOLDING
mp-import:      afi ipv6.unicast from AS24776 accept AS24776
mp-import:      afi ipv6.unicast from AS24778 accept AS24778
mp-import:      afi ipv6.unicast from AS24835 accept AS24835
mp-import:      afi ipv6.unicast from AS24875 accept AS24875
mp-import:      afi ipv6.unicast from AS24940 accept AS24940
mp-import:      afi ipv6.unicast from AS24953 accept AS-24953
mp-import:      afi ipv6.unicast from AS24958 accept AS24958
mp-import:      afi ipv6.unicast from AS24989 accept AS-EQUINIX-EU
mp-import:      afi ipv6.unicast from AS24990 accept AS-EQUINIX-EU
mp-import:      afi ipv6.unicast from AS24993 accept AS24993
mp-import:      afi ipv6.unicast from AS25003 accept AS25003
mp-import:      afi ipv6.unicast from AS25091 accept AS-IP-MAX
mp-import:      afi ipv6.unicast from AS25148 accept AS-BASEFARM
mp-import:      afi ipv6.unicast from AS25182 accept AS25182
mp-import:      afi ipv6.unicast from AS25198 accept AS25198
mp-import:      afi ipv6.unicast from AS25220 accept AS25220
mp-import:      afi ipv6.unicast from AS25268 accept AS25268
mp-import:      afi ipv6.unicast from AS25369 accept AS-BANDWIDTH
mp-import:      afi ipv6.unicast from AS25376 accept AS-NETNORTH
mp-import:      afi ipv6.unicast from AS25441 accept AS-IBIS
mp-import:      afi ipv6.unicast from AS25459 accept AS25459
mp-import:      afi ipv6.unicast from AS25472 accept AS-WIND-HELLAS
mp-import:      afi ipv6.unicast from AS25542 accept AS25542
mp-import:      afi ipv6.unicast from AS25562 accept AS25562
mp-import:      afi ipv6.unicast from AS25575 accept AS25575
mp-import:      afi ipv6.unicast from AS25577 accept AS25577
mp-import:      afi ipv6.unicast from AS25593 accept AS25593
mp-import:      afi ipv6.unicast from AS25596 accept AS25596
mp-import:      afi ipv6.unicast from AS25605 accept AS25605
mp-import:      afi ipv6.unicast from AS25653 accept AS25653
mp-import:      afi ipv6.unicast from AS25697 accept AS-UPCLOUD
mp-import:      afi ipv6.unicast from AS25818 accept AS25818
mp-import:      afi ipv6.unicast from AS25864 accept AS25864
mp-import:      afi ipv6.unicast from AS25875 accept AS-FFN
mp-import:      afi ipv6.unicast from AS25934 accept AS25934
mp-import:      afi ipv6.unicast from AS25956 accept AS25956
mp-import:      afi ipv6.unicast from AS25973 accept AS25973
mp-import:      afi ipv6.unicast from AS26008 accept AS26008
mp-import:      afi ipv6.unicast from AS26097 accept AS26097
mp-import:      afi ipv6.unicast from AS26120 accept AS26120
mp-import:      afi ipv6.unicast from AS26156 accept AS26156
mp-import:      afi ipv6.unicast from AS26167 accept AS26167
mp-import:      afi ipv6.unicast from AS26258 accept AS26258
mp-import:      afi ipv6.unicast from AS26265 accept AS26265
mp-import:      afi ipv6.unicast from AS26282 accept AS-SYMC
mp-import:      afi ipv6.unicast from AS26342 accept AS26342
mp-import:      afi ipv6.unicast from AS26380 accept AS26380
mp-import:      afi ipv6.unicast from AS26462 accept AS26462
mp-import:      afi ipv6.unicast from AS26476 accept AS26476
mp-import:      afi ipv6.unicast from AS26512 accept AS26512
mp-import:      afi ipv6.unicast from AS26523 accept AS26523
mp-import:      afi ipv6.unicast from AS26546 accept AS26546
mp-import:      afi ipv6.unicast from AS26554 accept AS26554
mp-import:      afi ipv6.unicast from AS26558 accept AS26558
mp-import:      afi ipv6.unicast from AS26637 accept AS26637
mp-import:      afi ipv6.unicast from AS26667 accept AS26667
mp-import:      afi ipv6.unicast from AS26673 accept AS26673
mp-import:      afi ipv6.unicast from AS26744 accept AS-PRTC-TRANSIT
mp-import:      afi ipv6.unicast from AS26769 accept AS26769
mp-import:      afi ipv6.unicast from AS26848 accept AS26848
mp-import:      afi ipv6.unicast from AS26863 accept AS-GSK
mp-import:      afi ipv6.unicast from AS26878 accept AS26878
mp-import:      afi ipv6.unicast from AS26967 accept AS26967
mp-import:      afi ipv6.unicast from AS27299 accept AS27299
mp-import:      afi ipv6.unicast from AS27311 accept AS27311
mp-import:      afi ipv6.unicast from AS27364 accept AS27364:AS-ALL
mp-import:      afi ipv6.unicast from AS27381 accept AS27381
mp-import:      afi ipv6.unicast from AS27385 accept AS27385
mp-import:      afi ipv6.unicast from AS27393 accept AS27393
mp-import:      afi ipv6.unicast from AS27439 accept AS27439
mp-import:      afi ipv6.unicast from AS27471 accept AS-SYMC
mp-import:      afi ipv6.unicast from AS27506 accept AS27506
mp-import:      afi ipv6.unicast from AS27566 accept AS-EQUINIX
mp-import:      afi ipv6.unicast from AS27647 accept AS27647
mp-import:      afi ipv6.unicast from AS27908 accept AS27908
mp-import:      afi ipv6.unicast from AS27978 accept AS27978
mp-import:      afi ipv6.unicast from AS28007 accept AS28007
mp-import:      afi ipv6.unicast from AS28398 accept AS-GBIC
mp-import:      afi ipv6.unicast from AS28458 accept AS-IENTC-MX
mp-import:      afi ipv6.unicast from AS28513 accept AS28513
mp-import:      afi ipv6.unicast from AS28663 accept AS-FLYS
mp-import:      afi ipv6.unicast from AS28677 accept AS28677
mp-import:      afi ipv6.unicast from AS28685 accept AS28685
mp-import:      afi ipv6.unicast from AS28707 accept AS28707
mp-import:      afi ipv6.unicast from AS28729 accept AS28729
mp-import:      afi ipv6.unicast from AS28753 accept AS28753
mp-import:      afi ipv6.unicast from AS28757 accept AS28757
mp-import:      afi ipv6.unicast from AS28760 accept AS28760
mp-import:      afi ipv6.unicast from AS28776 accept AS28776
mp-import:      afi ipv6.unicast from AS28792 accept AS-PUBLICINET
mp-import:      afi ipv6.unicast from AS28858 accept AS28858
mp-import:      afi ipv6.unicast from AS28889 accept AS-LINZNET
mp-import:      afi ipv6.unicast from AS28909 accept AS28909
mp-import:      afi ipv6.unicast from AS28917 accept AS28917
mp-import:      afi ipv6.unicast from AS28920 accept AS28920
mp-import:      afi ipv6.unicast from AS28929 accept AS28929
mp-import:      afi ipv6.unicast from AS29006 accept AS-POBOX
mp-import:      afi ipv6.unicast from AS29049 accept AS29049
mp-import:      afi ipv6.unicast from AS29056 accept AS29056
mp-import:      afi ipv6.unicast from AS29066 accept AS-VELIANET-V6
mp-import:      afi ipv6.unicast from AS29081 accept AS-WVNETAT
mp-import:      afi ipv6.unicast from AS29097 accept AS-HOSTPOINT
mp-import:      afi ipv6.unicast from AS29107 accept AS29107
mp-import:      afi ipv6.unicast from AS29119 accept AS29119
mp-import:      afi ipv6.unicast from AS29140 accept AS29140
mp-import:      afi ipv6.unicast from AS29152 accept AS-29152
mp-import:      afi ipv6.unicast from AS29169 accept AS29169
mp-import:      afi ipv6.unicast from AS29208 accept AS-DIALTELECOM
mp-import:      afi ipv6.unicast from AS29259 accept AS29259
mp-import:      afi ipv6.unicast from AS29278 accept AS29278
mp-import:      afi ipv6.unicast from AS29286 accept AS29286
mp-import:      afi ipv6.unicast from AS29314 accept AS29314
mp-import:      afi ipv6.unicast from AS29386 accept AS29386
mp-import:      afi ipv6.unicast from AS29396 accept AS-UNET
mp-import:      afi ipv6.unicast from AS29405 accept AS29405
mp-import:      afi ipv6.unicast from AS29449 accept AS29449
mp-import:      afi ipv6.unicast from AS29467 accept AS29467
mp-import:      afi ipv6.unicast from AS29518 accept AS29518:AS-BREDBAND2
mp-import:      afi ipv6.unicast from AS29535 accept AS29535
mp-import:      afi ipv6.unicast from AS29550 accept AS-AS29550
mp-import:      afi ipv6.unicast from AS29551 accept AS29551
mp-import:      afi ipv6.unicast from AS29591 accept AS29591
mp-import:      afi ipv6.unicast from AS29636 accept AS29636
mp-import:      afi ipv6.unicast from AS29644 accept AS-AIRSPEED
mp-import:      afi ipv6.unicast from AS29655 accept AS29655:AS-TRANSIT
mp-import:      afi ipv6.unicast from AS29680 accept AS29680
mp-import:      afi ipv6.unicast from AS29748 accept AS29748
mp-import:      afi ipv6.unicast from AS29757 accept AS29757
mp-import:      afi ipv6.unicast from AS29761 accept AS29761
mp-import:      afi ipv6.unicast from AS29802 accept AS-29802
mp-import:      afi ipv6.unicast from AS29838 accept AS-AMC
mp-import:      afi ipv6.unicast from AS29884 accept AS-EQUINIX
mp-import:      afi ipv6.unicast from AS29907 accept AS29907
mp-import:      afi ipv6.unicast from AS29909 accept AS29909:AS-METROOPTIC
mp-import:      afi ipv6.unicast from AS29976 accept AS29976
mp-import:      afi ipv6.unicast from AS30012 accept AS30012
mp-import:      afi ipv6.unicast from AS30029 accept AS30029
mp-import:      afi ipv6.unicast from AS30036 accept AS-MEDIACOM-TRANSIT
mp-import:      afi ipv6.unicast from AS30041 accept AS30041
mp-import:      afi ipv6.unicast from AS30071 accept AS30071
mp-import:      afi ipv6.unicast from AS30081 accept AS-CACHENETWORKS
mp-import:      afi ipv6.unicast from AS30103 accept AS30103
mp-import:      afi ipv6.unicast from AS30114 accept AS30114
mp-import:      afi ipv6.unicast from AS30146 accept AS30146
mp-import:      afi ipv6.unicast from AS30148 accept AS30148
mp-import:      afi ipv6.unicast from AS30197 accept AS30197
mp-import:      afi ipv6.unicast from AS30215 accept AS30215
mp-import:      afi ipv6.unicast from AS30238 accept AS30238
mp-import:      afi ipv6.unicast from AS30286 accept AS30286
mp-import:      afi ipv6.unicast from AS30404 accept AS30404
mp-import:      afi ipv6.unicast from AS30456 accept AS-COSMIC-GLOBAL
mp-import:      afi ipv6.unicast from AS30475 accept AS30475
mp-import:      afi ipv6.unicast from AS30600 accept AS-CMN-V6
mp-import:      afi ipv6.unicast from AS30607 accept AS-OPENDNS
mp-import:      afi ipv6.unicast from AS30633 accept AS-LEASEWEB-US
mp-import:      afi ipv6.unicast from AS30742 accept AS30742
mp-import:      afi ipv6.unicast from AS30818 accept AS30818
mp-import:      afi ipv6.unicast from AS30827 accept AS30827
mp-import:      afi ipv6.unicast from AS30848 accept AS30848
mp-import:      afi ipv6.unicast from AS30925 accept AS30925
mp-import:      afi ipv6.unicast from AS30931 accept AS-IG
mp-import:      afi ipv6.unicast from AS30937 accept AS30937
mp-import:      afi ipv6.unicast from AS30967 accept AS30967
mp-import:      afi ipv6.unicast from AS31029 accept AS31029
mp-import:      afi ipv6.unicast from AS31042 accept AS31042
mp-import:      afi ipv6.unicast from AS31059 accept AS31059
mp-import:      afi ipv6.unicast from AS31078 accept AS31078
mp-import:      afi ipv6.unicast from AS31080 accept AS-GWP-O2
mp-import:      afi ipv6.unicast from AS31083 accept AS-31083
mp-import:      afi ipv6.unicast from AS31084 accept AS31084
mp-import:      afi ipv6.unicast from AS31108 accept AS31108
mp-import:      afi ipv6.unicast from AS31115 accept AS31115
mp-import:      afi ipv6.unicast from AS31116 accept AS31116
mp-import:      afi ipv6.unicast from AS31122 accept AS31122
mp-import:      afi ipv6.unicast from AS31147 accept AS31147
mp-import:      afi ipv6.unicast from AS31241 accept AS31241
mp-import:      afi ipv6.unicast from AS31242 accept AS31242
mp-import:      afi ipv6.unicast from AS31250 accept AS-ODOUT
mp-import:      afi ipv6.unicast from AS31263 accept AS31263
mp-import:      afi ipv6.unicast from AS31287 accept AS-IPACCT
mp-import:      afi ipv6.unicast from AS31293 accept AS31293
mp-import:      afi ipv6.unicast from AS31400 accept AS31400
mp-import:      afi ipv6.unicast from AS31424 accept AS31424
mp-import:      afi ipv6.unicast from AS31445 accept AS31445
mp-import:      afi ipv6.unicast from AS31463 accept AS31463
mp-import:      afi ipv6.unicast from AS31479 accept AS31479
mp-import:      afi ipv6.unicast from AS31529 accept AS-DENIC-ANY
mp-import:      afi ipv6.unicast from AS31595 accept AS-AWELL
mp-import:      afi ipv6.unicast from AS31612 accept AS31612
mp-import:      afi ipv6.unicast from AS31631 accept AS31631
mp-import:      afi ipv6.unicast from AS31641 accept AS31641
mp-import:      afi ipv6.unicast from AS31655 accept AS31655
mp-import:      afi ipv6.unicast from AS31669 accept AS31669
mp-import:      afi ipv6.unicast from AS31672 accept AS31672
mp-import:      afi ipv6.unicast from AS31688 accept AS31688
mp-import:      afi ipv6.unicast from AS31708 accept AS-COREIX
mp-import:      afi ipv6.unicast from AS31712 accept AS31712
mp-import:      afi ipv6.unicast from AS31727 accept AS31727
mp-import:      afi ipv6.unicast from AS31743 accept AS31743
mp-import:      afi ipv6.unicast from AS31760 accept AS31760
mp-import:      afi ipv6.unicast from AS31898 accept AS31898
mp-import:      afi ipv6.unicast from AS31936 accept AS31936
mp-import:      afi ipv6.unicast from AS32030 accept AS32030
mp-import:      afi ipv6.unicast from AS32035 accept AS-NETFORTRIS
mp-import:      afi ipv6.unicast from AS32098 accept AS-32098
mp-import:      afi ipv6.unicast from AS32133 accept AS32133
mp-import:      afi ipv6.unicast from AS32181 accept AS-CQ-GIGENET
mp-import:      afi ipv6.unicast from AS32217 accept AS-GPIEX
mp-import:      afi ipv6.unicast from AS32222 accept AS32222
mp-import:      afi ipv6.unicast from AS32261 accept AS32261
mp-import:      afi ipv6.unicast from AS32281 accept AS32281
mp-import:      afi ipv6.unicast from AS32323 accept AS-EC-TR
mp-import:      afi ipv6.unicast from AS32354 accept AS32354
mp-import:      afi ipv6.unicast from AS32425 accept AS32425
mp-import:      afi ipv6.unicast from AS32440 accept AS32440
mp-import:      afi ipv6.unicast from AS32475 accept AS32475
mp-import:      afi ipv6.unicast from AS32478 accept AS32478
mp-import:      afi ipv6.unicast from AS32484 accept AS32484
mp-import:      afi ipv6.unicast from AS32489 accept AS-AS32489
mp-import:      afi ipv6.unicast from AS32578 accept AS32578
mp-import:      afi ipv6.unicast from AS32613 accept AS-LEASEWEB-CA
mp-import:      afi ipv6.unicast from AS32624 accept AS32624
mp-import:      afi ipv6.unicast from AS32671 accept AS32671
mp-import:      afi ipv6.unicast from AS32710 accept AS32710
mp-import:      afi ipv6.unicast from AS32780 accept AS32780
mp-import:      afi ipv6.unicast from AS32798 accept RS-HIGHLINE-TX
mp-import:      afi ipv6.unicast from AS32880 accept AS32880
mp-import:      afi ipv6.unicast from AS32881 accept AS-CFC
mp-import:      afi ipv6.unicast from AS32899 accept AS32899
mp-import:      afi ipv6.unicast from AS32934 accept AS-FACEBOOK
mp-import:      afi ipv6.unicast from AS32987 accept AS32987
mp-import:      afi ipv6.unicast from AS33040 accept AS33040
mp-import:      afi ipv6.unicast from AS33047 accept AS33047
mp-import:      afi ipv6.unicast from AS33154 accept AS-DQECUST
mp-import:      afi ipv6.unicast from AS33185 accept AS33185
mp-import:      afi ipv6.unicast from AS33247 accept AS33247
mp-import:      afi ipv6.unicast from AS33280 accept AS33280
mp-import:      afi ipv6.unicast from AS33361 accept AS33361
mp-import:      afi ipv6.unicast from AS33371 accept AS33371
mp-import:      afi ipv6.unicast from AS33419 accept AS33419
mp-import:      afi ipv6.unicast from AS33438 accept AS-HIGHWINDS
mp-import:      afi ipv6.unicast from AS33445 accept AS33445
mp-import:      afi ipv6.unicast from AS33459 accept AS33459
mp-import:      afi ipv6.unicast from AS33494 accept AS33494
mp-import:      afi ipv6.unicast from AS33576 accept AS-IMPORTED
mp-import:      afi ipv6.unicast from AS33597 accept AS-INFORELAY
mp-import:      afi ipv6.unicast from AS33619 accept AS33619
mp-import:      afi ipv6.unicast from AS33694 accept AS33694
mp-import:      afi ipv6.unicast from AS33724 accept AS33724
mp-import:      afi ipv6.unicast from AS33802 accept AS33802
mp-import:      afi ipv6.unicast from AS33835 accept AS33835
mp-import:      afi ipv6.unicast from AS33891 accept AS33891
mp-import:      afi ipv6.unicast from AS33923 accept AS-ART-COM
mp-import:      afi ipv6.unicast from AS33941 accept AS33941
mp-import:      afi ipv6.unicast from AS33986 accept AS33986
mp-import:      afi ipv6.unicast from AS34002 accept AS34002
mp-import:      afi ipv6.unicast from AS34006 accept AS34006
mp-import:      afi ipv6.unicast from AS34080 accept AS34080
mp-import:      afi ipv6.unicast from AS34164 accept AS34164
mp-import:      afi ipv6.unicast from AS34178 accept AS34178
mp-import:      afi ipv6.unicast from AS34191 accept AS34191
mp-import:      afi ipv6.unicast from AS34197 accept AS-SHRD
mp-import:      afi ipv6.unicast from AS34209 accept AS-PLIXDC-MIX
mp-import:      afi ipv6.unicast from AS34224 accept AS-NETERRA-INT
mp-import:      afi ipv6.unicast from AS34245 accept AS34245
mp-import:      afi ipv6.unicast from AS34279 accept AS34279
mp-import:      afi ipv6.unicast from AS34290 accept AS34290
mp-import:      afi ipv6.unicast from AS34305 accept AS34305
mp-import:      afi ipv6.unicast from AS34308 accept AS34308
mp-import:      afi ipv6.unicast from AS34309 accept AS34309
mp-import:      afi ipv6.unicast from AS34409 accept AS34409
mp-import:      afi ipv6.unicast from AS34428 accept AS-GLPR
mp-import:      afi ipv6.unicast from AS34442 accept AS34442
mp-import:      afi ipv6.unicast from AS34510 accept AS34510
mp-import:      afi ipv6.unicast from AS34525 accept AS34525
mp-import:      afi ipv6.unicast from AS34549 accept AS-MEER
mp-import:      afi ipv6.unicast from AS34569 accept AS34569
mp-import:      afi ipv6.unicast from AS34715 accept AS34715
mp-import:      afi ipv6.unicast from AS34737 accept AS34737
mp-import:      afi ipv6.unicast from AS34762 accept AS34762
mp-import:      afi ipv6.unicast from AS34764 accept AS34764
mp-import:      afi ipv6.unicast from AS34814 accept AS34814
mp-import:      afi ipv6.unicast from AS34854 accept AS-MERKEL
mp-import:      afi ipv6.unicast from AS34895 accept AS34895
mp-import:      afi ipv6.unicast from AS34922 accept AS34922
mp-import:      afi ipv6.unicast from AS34927 accept AS-iFog
mp-import:      afi ipv6.unicast from AS34966 accept AS34966
mp-import:      afi ipv6.unicast from AS34967 accept AS34967
mp-import:      afi ipv6.unicast from AS34968 accept AS34968
mp-import:      afi ipv6.unicast from AS34979 accept AS34979
mp-import:      afi ipv6.unicast from AS34984 accept AS34984:AS-TELLCOM-IPV6
mp-import:      afi ipv6.unicast from AS35070 accept AS35070
mp-import:      afi ipv6.unicast from AS35180 accept AS35180
mp-import:      afi ipv6.unicast from AS35266 accept AS-EXN
mp-import:      afi ipv6.unicast from AS35289 accept AS35289
mp-import:      afi ipv6.unicast from AS35311 accept AS35311
mp-import:      afi ipv6.unicast from AS35313 accept AS35313
mp-import:      afi ipv6.unicast from AS35315 accept AS35315
mp-import:      afi ipv6.unicast from AS35370 accept AS-AINET
mp-import:      afi ipv6.unicast from AS35426 accept AS35426
mp-import:      afi ipv6.unicast from AS35444 accept AS35444
mp-import:      afi ipv6.unicast from AS35491 accept AS35491
mp-import:      afi ipv6.unicast from AS35548 accept AS35548
mp-import:      afi ipv6.unicast from AS35574 accept AS35574
mp-import:      afi ipv6.unicast from AS35593 accept AS35593
mp-import:      afi ipv6.unicast from AS35699 accept AS35699
mp-import:      afi ipv6.unicast from AS35745 accept AS35745
mp-import:      afi ipv6.unicast from AS35838 accept AS35838
mp-import:      afi ipv6.unicast from AS35908 accept AS35908
mp-import:      afi ipv6.unicast from AS35953 accept AS35953
mp-import:      afi ipv6.unicast from AS35975 accept AS35975
mp-import:      afi ipv6.unicast from AS35993 accept AS35993
mp-import:      afi ipv6.unicast from AS35994 accept AS-AKAMAI
mp-import:      afi ipv6.unicast from AS36007 accept AS36007
mp-import:      afi ipv6.unicast from AS36040 accept AS36040
mp-import:      afi ipv6.unicast from AS36062 accept AS36062
mp-import:      afi ipv6.unicast from AS36077 accept AS36077
mp-import:      afi ipv6.unicast from AS36086 accept AS-TELX
mp-import:      afi ipv6.unicast from AS36103 accept AS36103
mp-import:      afi ipv6.unicast from AS36236 accept AS-NETACTUATE
mp-import:      afi ipv6.unicast from AS36243 accept AS36243
mp-import:      afi ipv6.unicast from AS36352 accept AS36352
mp-import:      afi ipv6.unicast from AS36385 accept AS36385
mp-import:      afi ipv6.unicast from AS36408 accept AS-PANTHER
mp-import:      afi ipv6.unicast from AS36444 accept AS36444
mp-import:      afi ipv6.unicast from AS36459 accept AS36459
mp-import:      afi ipv6.unicast from AS36473 accept AS36473
mp-import:      afi ipv6.unicast from AS36483 accept AS36483
mp-import:      afi ipv6.unicast from AS36493 accept AS36493
mp-import:      afi ipv6.unicast from AS36692 accept AS-OPENDNS
mp-import:      afi ipv6.unicast from AS36734 accept AS-PAXIO
mp-import:      afi ipv6.unicast from AS36776 accept AS36776
mp-import:      afi ipv6.unicast from AS36884 accept AS36884
mp-import:      afi ipv6.unicast from AS37100 accept AS-SET-SEACOM
mp-import:      afi ipv6.unicast from AS37271 accept AS-WOLCOMM
mp-import:      afi ipv6.unicast from AS37468 accept AS-ANGOLACABLES
mp-import:      afi ipv6.unicast from AS37721 accept AS37721
mp-import:      afi ipv6.unicast from AS38082 accept AS-TIG-GROUP
mp-import:      afi ipv6.unicast from AS38880 accept AS-M21
mp-import:      afi ipv6.unicast from AS38915 accept AS38915
mp-import:      afi ipv6.unicast from AS38930 accept AS38930
mp-import:      afi ipv6.unicast from AS38983 accept AS-COPACOCLOUD
mp-import:      afi ipv6.unicast from AS39063 accept AS39063
mp-import:      afi ipv6.unicast from AS39090 accept AS39090
mp-import:      afi ipv6.unicast from AS39116 accept AS39116
mp-import:      afi ipv6.unicast from AS39120 accept AS-CONVERGENZE
mp-import:      afi ipv6.unicast from AS39175 accept AS-TOUCHTEC
mp-import:      afi ipv6.unicast from AS39179 accept AS-NASSTAR
mp-import:      afi ipv6.unicast from AS39180 accept AS-LASOTEL
mp-import:      afi ipv6.unicast from AS39233 accept AS39233
mp-import:      afi ipv6.unicast from AS39234 accept AS39234
mp-import:      afi ipv6.unicast from AS39372 accept AS39372
mp-import:      afi ipv6.unicast from AS39392 accept AS-SUPERNETWORK
mp-import:      afi ipv6.unicast from AS39447 accept AS39447
mp-import:      afi ipv6.unicast from AS39477 accept AS39477
mp-import:      afi ipv6.unicast from AS39498 accept AS39498
mp-import:      afi ipv6.unicast from AS39505 accept AS39505
mp-import:      afi ipv6.unicast from AS39506 accept AS39506
mp-import:      afi ipv6.unicast from AS39512 accept AS39512
mp-import:      afi ipv6.unicast from AS39526 accept AS39526
mp-import:      afi ipv6.unicast from AS39545 accept AS-FLUIDATA
mp-import:      afi ipv6.unicast from AS39560 accept AS-KT-NET
mp-import:      afi ipv6.unicast from AS39572 accept AS39572
mp-import:      afi ipv6.unicast from AS39591 accept AS39591
mp-import:      afi ipv6.unicast from AS39637 accept AS39637
mp-import:      afi ipv6.unicast from AS39648 accept AS39648
mp-import:      afi ipv6.unicast from AS39686 accept AS-EUROFIBER
mp-import:      afi ipv6.unicast from AS39704 accept AS39704
mp-import:      afi ipv6.unicast from AS39729 accept AS39729
mp-import:      afi ipv6.unicast from AS39766 accept AS39766
mp-import:      afi ipv6.unicast from AS39781 accept AS39781
mp-import:      afi ipv6.unicast from AS39816 accept AS39816
mp-import:      afi ipv6.unicast from AS39822 accept AS39822
mp-import:      afi ipv6.unicast from AS39832 accept AS-OPERA
mp-import:      afi ipv6.unicast from AS39855 accept AS-MOD
mp-import:      afi ipv6.unicast from AS39878 accept AS-RAUTER
mp-import:      afi ipv6.unicast from AS39892 accept AS39892
mp-import:      afi ipv6.unicast from AS39912 accept AS39912
mp-import:      afi ipv6.unicast from AS39923 accept AS-UNIXSOLUTIONS
mp-import:      afi ipv6.unicast from AS39964 accept AS39964
mp-import:      afi ipv6.unicast from AS40028 accept AS40028:AS-ALL
mp-import:      afi ipv6.unicast from AS40029 accept AS40029
mp-import:      afi ipv6.unicast from AS40065 accept AS40065
mp-import:      afi ipv6.unicast from AS40165 accept AS40165
mp-import:      afi ipv6.unicast from AS40193 accept AS-TRIT6
mp-import:      afi ipv6.unicast from AS40224 accept AS40224
mp-import:      afi ipv6.unicast from AS40317 accept AS40317
mp-import:      afi ipv6.unicast from AS40401 accept AS40401
mp-import:      afi ipv6.unicast from AS40402 accept AS40402
mp-import:      afi ipv6.unicast from AS40430 accept AS40430
mp-import:      afi ipv6.unicast from AS40490 accept AS40490
mp-import:      afi ipv6.unicast from AS40523 accept AS40523
mp-import:      afi ipv6.unicast from AS40528 accept AS40528
mp-import:      afi ipv6.unicast from AS40581 accept AS40581
mp-import:      afi ipv6.unicast from AS40676 accept AS-40676
mp-import:      afi ipv6.unicast from AS40729 accept AS40729
mp-import:      afi ipv6.unicast from AS40739 accept AS40739
mp-import:      afi ipv6.unicast from AS40763 accept AS40763
mp-import:      afi ipv6.unicast from AS40769 accept AS40769
mp-import:      afi ipv6.unicast from AS40788 accept AS40788
mp-import:      afi ipv6.unicast from AS40841 accept AS40841
mp-import:      afi ipv6.unicast from AS40885 accept AS40885
mp-import:      afi ipv6.unicast from AS40889 accept AS40889
mp-import:      afi ipv6.unicast from AS40934 accept AS40934
mp-import:      afi ipv6.unicast from AS41041 accept AS41041
mp-import:      afi ipv6.unicast from AS41073 accept AS-RTE
mp-import:      afi ipv6.unicast from AS41135 accept AS41135
mp-import:      afi ipv6.unicast from AS41146 accept AS41146
mp-import:      afi ipv6.unicast from AS41157 accept AS-OXYMIUM
mp-import:      afi ipv6.unicast from AS41160 accept AS41160
mp-import:      afi ipv6.unicast from AS41204 accept AS41204
mp-import:      afi ipv6.unicast from AS41230 accept AS41230
mp-import:      afi ipv6.unicast from AS41313 accept AS41313
mp-import:      afi ipv6.unicast from AS41327 accept AS41327
mp-import:      afi ipv6.unicast from AS41354 accept AS41354
mp-import:      afi ipv6.unicast from AS41357 accept AS41357
mp-import:      afi ipv6.unicast from AS41364 accept AS41364
mp-import:      afi ipv6.unicast from AS41410 accept AS41410
mp-import:      afi ipv6.unicast from AS41415 accept AS41415
mp-import:      afi ipv6.unicast from AS41435 accept AS41435
mp-import:      afi ipv6.unicast from AS41436 accept AS41436
mp-import:      afi ipv6.unicast from AS41495 accept AS-FAELIX
mp-import:      afi ipv6.unicast from AS41497 accept AS41497
mp-import:      afi ipv6.unicast from AS41549 accept AS41549
mp-import:      afi ipv6.unicast from AS41564 accept as-px9
mp-import:      afi ipv6.unicast from AS41653 accept AS41653
mp-import:      afi ipv6.unicast from AS41765 accept AS41765
mp-import:      afi ipv6.unicast from AS41883 accept AS41883
mp-import:      afi ipv6.unicast from AS41887 accept AS41887
mp-import:      afi ipv6.unicast from AS41935 accept AS41935
mp-import:      afi ipv6.unicast from AS41960 accept AS41960
mp-import:      afi ipv6.unicast from AS41966 accept AS41966
mp-import:      afi ipv6.unicast from AS42004 accept AS42004
mp-import:      afi ipv6.unicast from AS42005 accept AS42005
mp-import:      afi ipv6.unicast from AS42013 accept AS42013
mp-import:      afi ipv6.unicast from AS42040 accept AS42040
mp-import:      afi ipv6.unicast from AS42044 accept AS-CNIC
mp-import:      afi ipv6.unicast from AS42177 accept AS42177
mp-import:      afi ipv6.unicast from AS42184 accept AS-TKRZ
mp-import:      afi ipv6.unicast from AS42211 accept AS42211
mp-import:      afi ipv6.unicast from AS42344 accept AS42344
mp-import:      afi ipv6.unicast from AS42366 accept AS42366
mp-import:      afi ipv6.unicast from AS42385 accept AS42385
mp-import:      afi ipv6.unicast from AS42392 accept AS42392
mp-import:      afi ipv6.unicast from AS42416 accept AS42416
mp-import:      afi ipv6.unicast from AS42459 accept AS-FOBUL-V6
mp-import:      afi ipv6.unicast from AS42463 accept AS42463
mp-import:      afi ipv6.unicast from AS42466 accept AS42466
mp-import:      afi ipv6.unicast from AS42607 accept AS42607
mp-import:      afi ipv6.unicast from AS42612 accept AS42612
mp-import:      afi ipv6.unicast from AS42624 accept AS42624
mp-import:      afi ipv6.unicast from AS42633 accept AS42633
mp-import:      afi ipv6.unicast from AS42673 accept AS42673
mp-import:      afi ipv6.unicast from AS42689 accept AS-INUK
mp-import:      afi ipv6.unicast from AS42830 accept AS-TVSAT364
mp-import:      afi ipv6.unicast from AS42831 accept AS-UKSERVERS
mp-import:      afi ipv6.unicast from AS42836 accept AS42836
mp-import:      afi ipv6.unicast from AS42845 accept AS42845
mp-import:      afi ipv6.unicast from AS42912 accept AS42912
mp-import:      afi ipv6.unicast from AS42927 accept AS42927
mp-import:      afi ipv6.unicast from AS42989 accept AS42989
mp-import:      afi ipv6.unicast from AS43074 accept AS43074
mp-import:      afi ipv6.unicast from AS43142 accept AS-ADELINOVIUS
mp-import:      afi ipv6.unicast from AS43205 accept AS43205
mp-import:      afi ipv6.unicast from AS43251 accept AS43251
mp-import:      afi ipv6.unicast from AS43266 accept AS-ABSET
mp-import:      afi ipv6.unicast from AS43289 accept AS43289
mp-import:      afi ipv6.unicast from AS43311 accept AS43311
mp-import:      afi ipv6.unicast from AS43313 accept AS43313
mp-import:      afi ipv6.unicast from AS43372 accept AS43372
mp-import:      afi ipv6.unicast from AS43406 accept AS43406
mp-import:      afi ipv6.unicast from AS43440 accept AS43440
mp-import:      afi ipv6.unicast from AS43494 accept AS43494
mp-import:      afi ipv6.unicast from AS43515 accept AS43515
mp-import:      afi ipv6.unicast from AS43519 accept AS-NOMINET-NS
mp-import:      afi ipv6.unicast from AS43545 accept AS-TELEDATAUK
mp-import:      afi ipv6.unicast from AS43578 accept AS43578
mp-import:      afi ipv6.unicast from AS43599 accept AS43599
mp-import:      afi ipv6.unicast from AS43639 accept AS43639
mp-import:      afi ipv6.unicast from AS43641 accept AS43641
mp-import:      afi ipv6.unicast from AS43848 accept AS43848
mp-import:      afi ipv6.unicast from AS43872 accept AS43872
mp-import:      afi ipv6.unicast from AS43885 accept AS43885
mp-import:      afi ipv6.unicast from AS43894 accept AS43894
mp-import:      afi ipv6.unicast from AS43898 accept AS43898
mp-import:      afi ipv6.unicast from AS43915 accept AS43915
mp-import:      afi ipv6.unicast from AS44066 accept AS-FIRSTCOLO
mp-import:      afi ipv6.unicast from AS44124 accept AS44124
mp-import:      afi ipv6.unicast from AS44134 accept AS44134
mp-import:      afi ipv6.unicast from AS44150 accept AS44150
mp-import:      afi ipv6.unicast from AS44212 accept AS44212
mp-import:      afi ipv6.unicast from AS44217 accept AS44217
mp-import:      afi ipv6.unicast from AS44227 accept AS44227
mp-import:      afi ipv6.unicast from AS44356 accept AS44356
mp-import:      afi ipv6.unicast from AS44384 accept AS44384
mp-import:      afi ipv6.unicast from AS44444 accept AS44444
mp-import:      afi ipv6.unicast from AS44451 accept AS44451
mp-import:      afi ipv6.unicast from AS44454 accept AS44454
mp-import:      afi ipv6.unicast from AS44521 accept AS44521
mp-import:      afi ipv6.unicast from AS44600 accept AS44600
mp-import:      afi ipv6.unicast from AS44608 accept AS44608
mp-import:      afi ipv6.unicast from AS44776 accept AS44776
mp-import:      afi ipv6.unicast from AS44786 accept AS44786
mp-import:      afi ipv6.unicast from AS44788 accept AS44788
mp-import:      afi ipv6.unicast from AS44806 accept AS44806
mp-import:      afi ipv6.unicast from AS44814 accept AS-FOBUL-V6
mp-import:      afi ipv6.unicast from AS44898 accept AS44898
mp-import:      afi ipv6.unicast from AS44901 accept AS44901
mp-import:      afi ipv6.unicast from AS44926 accept AS44926
mp-import:      afi ipv6.unicast from AS44946 accept AS44946
mp-import:      afi ipv6.unicast from AS44965 accept AS44965
mp-import:      afi ipv6.unicast from AS44976 accept AS44976
mp-import:      afi ipv6.unicast from AS45187 accept AS45187
mp-import:      afi ipv6.unicast from AS45474 accept AS45474
mp-import:      afi ipv6.unicast from AS45629 accept AS-45629
mp-import:      afi ipv6.unicast from AS45630 accept AS45630
mp-import:      afi ipv6.unicast from AS45758 accept AS45758
mp-import:      afi ipv6.unicast from AS45896 accept AS45896
mp-import:      afi ipv6.unicast from AS45899 accept AS45899
mp-import:      afi ipv6.unicast from AS46160 accept AS46160
mp-import:      afi ipv6.unicast from AS46261 accept AS-QP
mp-import:      afi ipv6.unicast from AS46371 accept AS46371
mp-import:      afi ipv6.unicast from AS46375 accept AS46375
mp-import:      afi ipv6.unicast from AS46379 accept AS46379
mp-import:      afi ipv6.unicast from AS46455 accept AS46455
mp-import:      afi ipv6.unicast from AS46475 accept AS46475
mp-import:      afi ipv6.unicast from AS46489 accept AS-TWITCH
mp-import:      afi ipv6.unicast from AS46558 accept AS46558
mp-import:      afi ipv6.unicast from AS46562 accept AS-COLOAT
mp-import:      afi ipv6.unicast from AS46573 accept AS46573
mp-import:      afi ipv6.unicast from AS46609 accept as-HostingLogistic
mp-import:      afi ipv6.unicast from AS46632 accept AS46632
mp-import:      afi ipv6.unicast from AS46664 accept AS46664
mp-import:      afi ipv6.unicast from AS46687 accept AS46687
mp-import:      afi ipv6.unicast from AS46844 accept AS-46844
mp-import:      afi ipv6.unicast from AS46887 accept AS-CCF
mp-import:      afi ipv6.unicast from AS46994 accept AS46994
mp-import:      afi ipv6.unicast from AS47167 accept AS47167
mp-import:      afi ipv6.unicast from AS47169 accept AS47169
mp-import:      afi ipv6.unicast from AS47195 accept AS47195
mp-import:      afi ipv6.unicast from AS47232 accept AS47232
mp-import:      afi ipv6.unicast from AS47292 accept AS-SENTIADK
mp-import:      afi ipv6.unicast from AS47381 accept AS47381
mp-import:      afi ipv6.unicast from AS47443 accept AS47443
mp-import:      afi ipv6.unicast from AS47674 accept AS-DOTSI
mp-import:      afi ipv6.unicast from AS47680 accept AS47680
mp-import:      afi ipv6.unicast from AS47720 accept AS47720:AS-CIX
mp-import:      afi ipv6.unicast from AS47787 accept AS-EDGOO
mp-import:      afi ipv6.unicast from AS47836 accept AS47836
mp-import:      afi ipv6.unicast from AS47866 accept AS47866
mp-import:      afi ipv6.unicast from AS47872 accept AS47872
mp-import:      afi ipv6.unicast from AS47886 accept AS-EQUINIX-EU
mp-import:      afi ipv6.unicast from AS47887 accept AS-SET-NTT
mp-import:      afi ipv6.unicast from AS47950 accept AS-LNK
mp-import:      afi ipv6.unicast from AS47956 accept AS-XFONE
mp-import:      afi ipv6.unicast from AS47969 accept AS47969
mp-import:      afi ipv6.unicast from AS47973 accept AS-DRT
mp-import:      afi ipv6.unicast from AS48006 accept AS48006
mp-import:      afi ipv6.unicast from AS48137 accept AS48137
mp-import:      afi ipv6.unicast from AS48152 accept AS-DLR
mp-import:      afi ipv6.unicast from AS48237 accept AS48237
mp-import:      afi ipv6.unicast from AS48305 accept AS-XPNTI
mp-import:      afi ipv6.unicast from AS48345 accept AS48345
mp-import:      afi ipv6.unicast from AS48348 accept AS-INTERDOMINIOS
mp-import:      afi ipv6.unicast from AS48374 accept AS48374
mp-import:      afi ipv6.unicast from AS48447 accept AS48447
mp-import:      afi ipv6.unicast from AS48452 accept AS-TRAFFICNET
mp-import:      afi ipv6.unicast from AS48559 accept AS48559
mp-import:      afi ipv6.unicast from AS48582 accept AS-SET-NGENA
mp-import:      afi ipv6.unicast from AS48635 accept AS-ASTRALUS
mp-import:      afi ipv6.unicast from AS48638 accept AS-CRONOS
mp-import:      afi ipv6.unicast from AS48659 accept AS48659
mp-import:      afi ipv6.unicast from AS48804 accept AS48804
mp-import:      afi ipv6.unicast from AS48832 accept AS48832
mp-import:      afi ipv6.unicast from AS48849 accept AS48849
mp-import:      afi ipv6.unicast from AS48850 accept AS48850
mp-import:      afi ipv6.unicast from AS48896 accept AS48896
mp-import:      afi ipv6.unicast from AS48910 accept AS48910
mp-import:      afi ipv6.unicast from AS48918 accept AS48918
mp-import:      afi ipv6.unicast from AS48950 accept as-px9
mp-import:      afi ipv6.unicast from AS48957 accept AS48957
mp-import:      afi ipv6.unicast from AS48961 accept AS48961
mp-import:      afi ipv6.unicast from AS48964 accept AS48964
mp-import:      afi ipv6.unicast from AS49088 accept AS49088
mp-import:      afi ipv6.unicast from AS49102 accept AS-CONNECTED
mp-import:      afi ipv6.unicast from AS49158 accept AS49158
mp-import:      afi ipv6.unicast from AS49216 accept AS49216
mp-import:      afi ipv6.unicast from AS49220 accept AS-AIRIT
mp-import:      afi ipv6.unicast from AS49229 accept AS49229
mp-import:      afi ipv6.unicast from AS49289 accept AS-IPROUTE-SET
mp-import:      afi ipv6.unicast from AS49296 accept AS49296
mp-import:      afi ipv6.unicast from AS49405 accept AS49405
mp-import:      afi ipv6.unicast from AS49415 accept AS49415
mp-import:      afi ipv6.unicast from AS49425 accept AS-DLR
mp-import:      afi ipv6.unicast from AS49434 accept AS-HHOSTING
mp-import:      afi ipv6.unicast from AS49515 accept AS-NSC
mp-import:      afi ipv6.unicast from AS49567 accept AS49567
mp-import:      afi ipv6.unicast from AS49600 accept AS-NEARIP
mp-import:      afi ipv6.unicast from AS49605 accept AS49605
mp-import:      afi ipv6.unicast from AS49607 accept AS49607
mp-import:      afi ipv6.unicast from AS49683 accept AS49683
mp-import:      afi ipv6.unicast from AS49765 accept AS49765
mp-import:      afi ipv6.unicast from AS49870 accept AS49870
mp-import:      afi ipv6.unicast from AS49915 accept AS49915
mp-import:      afi ipv6.unicast from AS50121 accept AS50121
mp-import:      afi ipv6.unicast from AS50173 accept AS50173
mp-import:      afi ipv6.unicast from AS50188 accept AS50188
mp-import:      afi ipv6.unicast from AS50226 accept AS50226
mp-import:      afi ipv6.unicast from AS50245 accept AS50245
mp-import:      afi ipv6.unicast from AS50292 accept AS50292
mp-import:      afi ipv6.unicast from AS50300 accept AS50300
mp-import:      afi ipv6.unicast from AS50331 accept AS50331
mp-import:      afi ipv6.unicast from AS50343 accept AS50343
mp-import:      afi ipv6.unicast from AS50360 accept AS-TAMATIYA
mp-import:      afi ipv6.unicast from AS50469 accept AS50469
mp-import:      afi ipv6.unicast from AS50581 accept AS50581
mp-import:      afi ipv6.unicast from AS50625 accept AS50625
mp-import:      afi ipv6.unicast from AS50835 accept AS50835
mp-import:      afi ipv6.unicast from AS50877 accept AS-AIRBEAM
mp-import:      afi ipv6.unicast from AS50974 accept AS50974
mp-import:      afi ipv6.unicast from AS51043 accept AS-ASPIRE
mp-import:      afi ipv6.unicast from AS51088 accept AS-A2B
mp-import:      afi ipv6.unicast from AS51269 accept AS-HEXATOM
mp-import:      afi ipv6.unicast from AS51310 accept AS-MATRONIX
mp-import:      afi ipv6.unicast from AS51394 accept AS51394
mp-import:      afi ipv6.unicast from AS51395 accept AS-SOFTPLUS
mp-import:      afi ipv6.unicast from AS51399 accept AS51399
mp-import:      afi ipv6.unicast from AS51406 accept AS51406
mp-import:      afi ipv6.unicast from AS51407 accept AS-MadaSET
mp-import:      afi ipv6.unicast from AS51483 accept AS51483
mp-import:      afi ipv6.unicast from AS51510 accept AS51510
mp-import:      afi ipv6.unicast from AS51580 accept AS51580
mp-import:      afi ipv6.unicast from AS51582 accept AS51582
mp-import:      afi ipv6.unicast from AS51616 accept AS51616
mp-import:      afi ipv6.unicast from AS51752 accept AS51752
mp-import:      afi ipv6.unicast from AS51796 accept AS51796
mp-import:      afi ipv6.unicast from AS51809 accept AS-BRSK
mp-import:      afi ipv6.unicast from AS51820 accept AS51820
mp-import:      afi ipv6.unicast from AS51852 accept AS51852
mp-import:      afi ipv6.unicast from AS51857 accept AS51857
mp-import:      afi ipv6.unicast from AS51871 accept AS51871
mp-import:      afi ipv6.unicast from AS51890 accept AS51890
mp-import:      afi ipv6.unicast from AS51944 accept AS-PROMEDIA
mp-import:      afi ipv6.unicast from AS52030 accept AS52030
mp-import:      afi ipv6.unicast from AS52106 accept AS-GALATEA
mp-import:      afi ipv6.unicast from AS52320 accept AS-GNT
mp-import:      afi ipv6.unicast from AS52347 accept AS52347
mp-import:      afi ipv6.unicast from AS52393 accept AS52393
mp-import:      afi ipv6.unicast from AS52438 accept AS52438
mp-import:      afi ipv6.unicast from AS52580 accept AS52580
mp-import:      afi ipv6.unicast from AS52873 accept AS52873
mp-import:      afi ipv6.unicast from AS53264 accept AS-CDC
mp-import:      afi ipv6.unicast from AS53292 accept AS53292
mp-import:      afi ipv6.unicast from AS53340 accept AS-FIBERHUB
mp-import:      afi ipv6.unicast from AS53388 accept AS53388
mp-import:      afi ipv6.unicast from AS53428 accept AS53428
mp-import:      afi ipv6.unicast from AS53582 accept AS53582
mp-import:      afi ipv6.unicast from AS53620 accept AS53620
mp-import:      afi ipv6.unicast from AS53667 accept AS-FRANTECH
mp-import:      afi ipv6.unicast from AS53722 accept AS53722
mp-import:      afi ipv6.unicast from AS53726 accept AS53726
mp-import:      afi ipv6.unicast from AS53764 accept AS53764
mp-import:      afi ipv6.unicast from AS53766 accept AS53766
mp-import:      afi ipv6.unicast from AS53813 accept AS53813
mp-import:      afi ipv6.unicast from AS53828 accept AS-53828-CUSTOMERS
mp-import:      afi ipv6.unicast from AS53845 accept AS53845
mp-import:      afi ipv6.unicast from AS53850 accept AS53850
mp-import:      afi ipv6.unicast from AS53856 accept AS-NJIX
mp-import:      afi ipv6.unicast from AS53902 accept AS53902
mp-import:      afi ipv6.unicast from AS53914 accept AS53914
mp-import:      afi ipv6.unicast from AS53939 accept AS53939
mp-import:      afi ipv6.unicast from AS54040 accept AS54040
mp-import:      afi ipv6.unicast from AS54103 accept AS54103
mp-import:      afi ipv6.unicast from AS54125 accept AS54125
mp-import:      afi ipv6.unicast from AS54197 accept AS54197
mp-import:      afi ipv6.unicast from AS54201 accept AS54201
mp-import:      afi ipv6.unicast from AS54235 accept AS54235
mp-import:      afi ipv6.unicast from AS54303 accept AS54303
mp-import:      afi ipv6.unicast from AS54312 accept AS54312
mp-import:      afi ipv6.unicast from AS54329 accept AS54329
mp-import:      afi ipv6.unicast from AS54359 accept AS54359
mp-import:      afi ipv6.unicast from AS54455 accept AS54455
mp-import:      afi ipv6.unicast from AS54483 accept AS54483
mp-import:      afi ipv6.unicast from AS54489 accept AS54489
mp-import:      afi ipv6.unicast from AS54509 accept AS54509
mp-import:      afi ipv6.unicast from AS54527 accept AS54527:AS-GLOBAL
mp-import:      afi ipv6.unicast from AS54588 accept AS-EQUINIX
mp-import:      afi ipv6.unicast from AS54641 accept AS54641
mp-import:      afi ipv6.unicast from AS54652 accept AS54652
mp-import:      afi ipv6.unicast from AS54778 accept AS54778
mp-import:      afi ipv6.unicast from AS54816 accept AS54816
mp-import:      afi ipv6.unicast from AS54825 accept AS-EQUINIX-EMEA
mp-import:      afi ipv6.unicast from AS54913 accept AS54913
mp-import:      afi ipv6.unicast from AS54957 accept AS54957
mp-import:      afi ipv6.unicast from AS54994 accept AS54994
mp-import:      afi ipv6.unicast from AS55002 accept AS55002
mp-import:      afi ipv6.unicast from AS55011 accept AS55011
mp-import:      afi ipv6.unicast from AS55061 accept AS55061
mp-import:      afi ipv6.unicast from AS55081 accept AS-24SHELLS
mp-import:      afi ipv6.unicast from AS55191 accept AS55191
mp-import:      afi ipv6.unicast from AS55195 accept AS55195
mp-import:      afi ipv6.unicast from AS55256 accept AS-NETSKOPE
mp-import:      afi ipv6.unicast from AS55259 accept AS55259
mp-import:      afi ipv6.unicast from AS55891 accept AS55891
mp-import:      afi ipv6.unicast from AS55943 accept AS55943
mp-import:      afi ipv6.unicast from AS56286 accept AS-SET-IXTELECOM
mp-import:      afi ipv6.unicast from AS56381 accept AS56381:AS-ALL
mp-import:      afi ipv6.unicast from AS56474 accept AS56474
mp-import:      afi ipv6.unicast from AS56478 accept AS56478
mp-import:      afi ipv6.unicast from AS56504 accept AS56504
mp-import:      afi ipv6.unicast from AS56511 accept AS56511
mp-import:      afi ipv6.unicast from AS56515 accept AS56515
mp-import:      afi ipv6.unicast from AS56595 accept AS-FLUENCY
mp-import:      afi ipv6.unicast from AS56611 accept AS56611
mp-import:      afi ipv6.unicast from AS56630 accept AS-MELBICOM
mp-import:      afi ipv6.unicast from AS56647 accept AS56647
mp-import:      afi ipv6.unicast from AS56655 accept AS-TERRAHOST
mp-import:      afi ipv6.unicast from AS56683 accept AS56683
mp-import:      afi ipv6.unicast from AS56767 accept AS56767
mp-import:      afi ipv6.unicast from AS56786 accept AS56786
mp-import:      afi ipv6.unicast from AS56894 accept AS56894
mp-import:      afi ipv6.unicast from AS56953 accept AS56953
mp-import:      afi ipv6.unicast from AS56958 accept AS56958
mp-import:      afi ipv6.unicast from AS56990 accept AS56990
mp-import:      afi ipv6.unicast from AS57111 accept AS57111
mp-import:      afi ipv6.unicast from AS57141 accept AS57141
mp-import:      afi ipv6.unicast from AS57169 accept AS57169
mp-import:      afi ipv6.unicast from AS57276 accept AS-OPTIMITY
mp-import:      afi ipv6.unicast from AS57332 accept AS57332
mp-import:      afi ipv6.unicast from AS57344 accept AS-57344
mp-import:      afi ipv6.unicast from AS57607 accept AS57607
mp-import:      afi ipv6.unicast from AS57626 accept AS57626
mp-import:      afi ipv6.unicast from AS57704 accept AS-SPEEDCLICKSET
mp-import:      afi ipv6.unicast from AS57717 accept AS-FBX
mp-import:      afi ipv6.unicast from AS57723 accept AS57723
mp-import:      afi ipv6.unicast from AS57750 accept AS57750
mp-import:      afi ipv6.unicast from AS57795 accept AS57795
mp-import:      afi ipv6.unicast from AS57811 accept AS57811
mp-import:      afi ipv6.unicast from AS57877 accept AS57877
mp-import:      afi ipv6.unicast from AS57896 accept AS57896
mp-import:      afi ipv6.unicast from AS57976 accept AS-BLIZZARD
mp-import:      afi ipv6.unicast from AS58065 accept as-px9
mp-import:      afi ipv6.unicast from AS58246 accept AS58246
mp-import:      afi ipv6.unicast from AS58307 accept AS-RADIX
mp-import:      afi ipv6.unicast from AS58321 accept AS-OXYLION-GLOBAL
mp-import:      afi ipv6.unicast from AS58453 accept AS58453
mp-import:      afi ipv6.unicast from AS58511 accept AS-CIT
mp-import:      afi ipv6.unicast from AS58664 accept AS58664
mp-import:      afi ipv6.unicast from AS59028 accept AS59028
mp-import:      afi ipv6.unicast from AS59253 accept AS59253
mp-import:      afi ipv6.unicast from AS59371 accept AS59371
mp-import:      afi ipv6.unicast from AS59432 accept AS-GINERNET
mp-import:      afi ipv6.unicast from AS59455 accept AS59455
mp-import:      afi ipv6.unicast from AS59524 accept AS59524
mp-import:      afi ipv6.unicast from AS59545 accept AS59545
mp-import:      afi ipv6.unicast from AS59580 accept AS59580
mp-import:      afi ipv6.unicast from AS59605 accept AS-ZAINGP
mp-import:      afi ipv6.unicast from AS59711 accept AS59711
mp-import:      afi ipv6.unicast from AS59816 accept AS-SAFEHOSTS
mp-import:      afi ipv6.unicast from AS59827 accept AS59827
mp-import:      afi ipv6.unicast from AS59842 accept AS59842
mp-import:      afi ipv6.unicast from AS59865 accept AS-IVMOB
mp-import:      afi ipv6.unicast from AS59933 accept AS59933
mp-import:      afi ipv6.unicast from AS60022 accept AS60022
mp-import:      afi ipv6.unicast from AS60033 accept AS-DOTSI
mp-import:      afi ipv6.unicast from AS60038 accept AS60038
mp-import:      afi ipv6.unicast from AS60068 accept AS-CDN77
mp-import:      afi ipv6.unicast from AS60144 accept AS60144
mp-import:      afi ipv6.unicast from AS60193 accept AS60193
mp-import:      afi ipv6.unicast from AS60339 accept AS-H3GUK
mp-import:      afi ipv6.unicast from AS60362 accept AS60362
mp-import:      afi ipv6.unicast from AS60384 accept AS60384
mp-import:      afi ipv6.unicast from AS60404 accept AS60404
mp-import:      afi ipv6.unicast from AS60436 accept AS60436
mp-import:      afi ipv6.unicast from AS60447 accept AS-I-NET
mp-import:      afi ipv6.unicast from AS60475 accept AS60475
mp-import:      afi ipv6.unicast from AS60481 accept AS60481
mp-import:      afi ipv6.unicast from AS60486 accept AS60486
mp-import:      afi ipv6.unicast from AS60497 accept AS-ictmedia01
mp-import:      afi ipv6.unicast from AS60501 accept AS60501
mp-import:      afi ipv6.unicast from AS60624 accept AS60624
mp-import:      afi ipv6.unicast from AS60636 accept AS60636
mp-import:      afi ipv6.unicast from AS60670 accept AS60670
mp-import:      afi ipv6.unicast from AS60706 accept AS60706
mp-import:      afi ipv6.unicast from AS60758 accept AS60758
mp-import:      afi ipv6.unicast from AS60781 accept AS-LEASEWEB-NL
mp-import:      afi ipv6.unicast from AS60798 accept AS-SERVEREASY1
mp-import:      afi ipv6.unicast from AS60800 accept AS-NETWISE
mp-import:      afi ipv6.unicast from AS60893 accept AS60893
mp-import:      afi ipv6.unicast from AS60940 accept AS60940
mp-import:      afi ipv6.unicast from AS61003 accept AS61003
mp-import:      afi ipv6.unicast from AS61046 accept AS-HZ-HOSTING-LTD
mp-import:      afi ipv6.unicast from AS61049 accept AS61049
mp-import:      afi ipv6.unicast from AS61149 accept AS61149
mp-import:      afi ipv6.unicast from AS61154 accept AS61154
mp-import:      afi ipv6.unicast from AS61215 accept AS61215
mp-import:      afi ipv6.unicast from AS61244 accept AS61244
mp-import:      afi ipv6.unicast from AS61266 accept AS61266
mp-import:      afi ipv6.unicast from AS61273 accept AS61273
mp-import:      afi ipv6.unicast from AS61315 accept AS-SEDMULTITEL
mp-import:      afi ipv6.unicast from AS61317 accept AS61317
mp-import:      afi ipv6.unicast from AS61323 accept AS-UKFAST
mp-import:      afi ipv6.unicast from AS61349 accept AS-MAXITEL
mp-import:      afi ipv6.unicast from AS61373 accept AS61373
mp-import:      afi ipv6.unicast from AS61430 accept AS61430
mp-import:      afi ipv6.unicast from AS61461 accept AS61461
mp-import:      afi ipv6.unicast from AS61573 accept AS61573:AS-CUSTOMERS
mp-import:      afi ipv6.unicast from AS62044 accept AS62044
mp-import:      afi ipv6.unicast from AS62068 accept AS62068
mp-import:      afi ipv6.unicast from AS62081 accept AS62081
mp-import:      afi ipv6.unicast from AS62087 accept AS62087
mp-import:      afi ipv6.unicast from AS62167 accept AS62167
mp-import:      afi ipv6.unicast from AS62168 accept AS62168
mp-import:      afi ipv6.unicast from AS62184 accept AS62184
mp-import:      afi ipv6.unicast from AS62190 accept AS62190
mp-import:      afi ipv6.unicast from AS62234 accept AS62234
mp-import:      afi ipv6.unicast from AS62240 accept AS-CLOUVIDER
mp-import:      afi ipv6.unicast from AS62244 accept AS62244
mp-import:      afi ipv6.unicast from AS62363 accept AS-EGW-IPv4
mp-import:      afi ipv6.unicast from AS62488 accept AS62488
mp-import:      afi ipv6.unicast from AS62542 accept AS62542
mp-import:      afi ipv6.unicast from AS62563 accept AS-GTHOST
mp-import:      afi ipv6.unicast from AS62597 accept AS-NSONE
mp-import:      afi ipv6.unicast from AS62638 accept AS62638
mp-import:      afi ipv6.unicast from AS62646 accept AS62646
mp-import:      afi ipv6.unicast from AS62648 accept AS62648
mp-import:      afi ipv6.unicast from AS62698 accept AS62698
mp-import:      afi ipv6.unicast from AS62710 accept AS62710
mp-import:      afi ipv6.unicast from AS62713 accept AS62713
mp-import:      afi ipv6.unicast from AS62728 accept AS62728
mp-import:      afi ipv6.unicast from AS62799 accept AS62799
mp-import:      afi ipv6.unicast from AS62815 accept AS62815
mp-import:      afi ipv6.unicast from AS62833 accept AS-62833-ny4
mp-import:      afi ipv6.unicast from AS62874 accept AS62874:AS-ALL
mp-import:      afi ipv6.unicast from AS62887 accept AS62887
mp-import:      afi ipv6.unicast from AS62955 accept AS-EBAYMTBB
mp-import:      afi ipv6.unicast from AS63008 accept AS63008
mp-import:      afi ipv6.unicast from AS63023 accept AS-GTHOST
mp-import:      afi ipv6.unicast from AS63086 accept AS63086
mp-import:      afi ipv6.unicast from AS63110 accept AS63110
mp-import:      afi ipv6.unicast from AS63157 accept AS63157
mp-import:      afi ipv6.unicast from AS63199 accept AS63199
mp-import:      afi ipv6.unicast from AS63213 accept AS63213:AS-GLOBAL
mp-import:      afi ipv6.unicast from AS63267 accept AS63267
mp-import:      afi ipv6.unicast from AS63287 accept AS63287
mp-import:      afi ipv6.unicast from AS63311 accept AS-20C
mp-import:      afi ipv6.unicast from AS63351 accept AS63351
mp-import:      afi ipv6.unicast from AS63365 accept AS63365
mp-import:      afi ipv6.unicast from AS63383 accept AS63383
mp-import:      afi ipv6.unicast from AS63399 accept AS-SWITCHCO
mp-import:      afi ipv6.unicast from AS63452 accept AS63452
mp-import:      afi ipv6.unicast from AS63916 accept AS63916
mp-import:      afi ipv6.unicast from AS63949 accept AS63949
mp-import:      afi ipv6.unicast from AS64022 accept AS-Cloudwm
mp-import:      afi ipv6.unicast from AS64096 accept AS64096
mp-import:      afi ipv6.unicast from AS64122 accept AS64122
mp-import:      afi ipv6.unicast from AS64275 accept AS64275
mp-import:      afi ipv6.unicast from AS64277 accept AS64277
mp-import:      afi ipv6.unicast from AS64304 accept AS64304
mp-import:      afi ipv6.unicast from AS64426 accept AS64426
mp-import:      afi ipv6.unicast from AS131274 accept AS131274
mp-import:      afi ipv6.unicast from AS131314 accept AS131314
mp-import:      afi ipv6.unicast from AS133335 accept AS133335
mp-import:      afi ipv6.unicast from AS133752 accept AS133752
mp-import:      afi ipv6.unicast from AS134345 accept AS134345
mp-import:      afi ipv6.unicast from AS134351 accept AS134351
mp-import:      afi ipv6.unicast from AS135356 accept AS135356
mp-import:      afi ipv6.unicast from AS135391 accept AS135391
mp-import:      afi ipv6.unicast from AS136897 accept AS136897
mp-import:      afi ipv6.unicast from AS137753 accept AS137753
mp-import:      afi ipv6.unicast from AS137816 accept AS137816
mp-import:      afi ipv6.unicast from AS137912 accept AS137912
mp-import:      afi ipv6.unicast from AS138005 accept AS138005
mp-import:      afi ipv6.unicast from AS138576 accept AS138576
mp-import:      afi ipv6.unicast from AS138611 accept AS138611
mp-import:      afi ipv6.unicast from AS141039 accept AS141039
mp-import:      afi ipv6.unicast from AS147049 accept AS147049
mp-import:      afi ipv6.unicast from AS196640 accept AS196640
mp-import:      afi ipv6.unicast from AS196670 accept AS196670
mp-import:      afi ipv6.unicast from AS196729 accept AS196729
mp-import:      afi ipv6.unicast from AS196755 accept AS196755
mp-import:      afi ipv6.unicast from AS196975 accept AS196975
mp-import:      afi ipv6.unicast from AS197036 accept AS-IPLINE
mp-import:      afi ipv6.unicast from AS197071 accept AS197071
mp-import:      afi ipv6.unicast from AS197075 accept AS197075
mp-import:      afi ipv6.unicast from AS197106 accept AS197106
mp-import:      afi ipv6.unicast from AS197116 accept AS197116
mp-import:      afi ipv6.unicast from AS197156 accept AS197156
mp-import:      afi ipv6.unicast from AS197226 accept AS-SPRINT-SDC
mp-import:      afi ipv6.unicast from AS197308 accept AS197308
mp-import:      afi ipv6.unicast from AS197437 accept AS197437
mp-import:      afi ipv6.unicast from AS197447 accept AS197447
mp-import:      afi ipv6.unicast from AS197518 accept AS197518
mp-import:      afi ipv6.unicast from AS197549 accept AS197549
mp-import:      afi ipv6.unicast from AS197573 accept AS197573
mp-import:      afi ipv6.unicast from AS197592 accept AS197592
mp-import:      afi ipv6.unicast from AS197610 accept AS197610
mp-import:      afi ipv6.unicast from AS197651 accept AS197651
mp-import:      afi ipv6.unicast from AS197669 accept AS197669
mp-import:      afi ipv6.unicast from AS197690 accept AS197690
mp-import:      afi ipv6.unicast from AS197712 accept AS197712
mp-import:      afi ipv6.unicast from AS197727 accept AS197727
mp-import:      afi ipv6.unicast from AS197883 accept AS197883
mp-import:      afi ipv6.unicast from AS197902 accept AS197902
mp-import:      afi ipv6.unicast from AS198040 accept AS198040
mp-import:      afi ipv6.unicast from AS198203 accept AS198203
mp-import:      afi ipv6.unicast from AS198211 accept AS198211
mp-import:      afi ipv6.unicast from AS198260 accept AS198260
mp-import:      afi ipv6.unicast from AS198279 accept AS-ATU-SET
mp-import:      afi ipv6.unicast from AS198334 accept AS198334
mp-import:      afi ipv6.unicast from AS198374 accept AS198374
mp-import:      afi ipv6.unicast from AS198440 accept AS-M12
mp-import:      afi ipv6.unicast from AS198452 accept AS198452
mp-import:      afi ipv6.unicast from AS198471 accept AS198471
mp-import:      afi ipv6.unicast from AS198651 accept AS198651
mp-import:      afi ipv6.unicast from AS198726 accept AS198726
mp-import:      afi ipv6.unicast from AS198761 accept AS198761
mp-import:      afi ipv6.unicast from AS198847 accept AS198847
mp-import:      afi ipv6.unicast from AS198890 accept AS198890
mp-import:      afi ipv6.unicast from AS198949 accept AS198949:AS-SD
mp-import:      afi ipv6.unicast from AS199081 accept AS199081
mp-import:      afi ipv6.unicast from AS199113 accept AS199113
mp-import:      afi ipv6.unicast from AS199156 accept AS199156
mp-import:      afi ipv6.unicast from AS199163 accept AS199163
mp-import:      afi ipv6.unicast from AS199237 accept AS199237
mp-import:      afi ipv6.unicast from AS199250 accept AS199250
mp-import:      afi ipv6.unicast from AS199283 accept AS199283
mp-import:      afi ipv6.unicast from AS199338 accept AS199338
mp-import:      afi ipv6.unicast from AS199358 accept AS199358
mp-import:      afi ipv6.unicast from AS199410 accept AS199410
mp-import:      afi ipv6.unicast from AS199483 accept AS199483
mp-import:      afi ipv6.unicast from AS199496 accept AS199496
mp-import:      afi ipv6.unicast from AS199524 accept AS-GCORE
mp-import:      afi ipv6.unicast from AS199559 accept AS199559
mp-import:      afi ipv6.unicast from AS199569 accept AS199569
mp-import:      afi ipv6.unicast from AS199710 accept AS199710
mp-import:      afi ipv6.unicast from AS199713 accept AS199713
mp-import:      afi ipv6.unicast from AS199775 accept AS199775
mp-import:      afi ipv6.unicast from AS199790 accept AS199790
mp-import:      afi ipv6.unicast from AS199799 accept AS199799
mp-import:      afi ipv6.unicast from AS199880 accept AS199880
mp-import:      afi ipv6.unicast from AS199892 accept AS199892
mp-import:      afi ipv6.unicast from AS200032 accept AS200032
mp-import:      afi ipv6.unicast from AS200052 accept AS-FERAL
mp-import:      afi ipv6.unicast from AS200099 accept AS200099
mp-import:      afi ipv6.unicast from AS200187 accept AS200187
mp-import:      afi ipv6.unicast from AS200271 accept AS200271
mp-import:      afi ipv6.unicast from AS200410 accept AS200410
mp-import:      afi ipv6.unicast from AS200416 accept AS200416
mp-import:      afi ipv6.unicast from AS200425 accept AS200425
mp-import:      afi ipv6.unicast from AS200462 accept AS-ETH
mp-import:      afi ipv6.unicast from AS200552 accept AS-WHOLESAIL
mp-import:      afi ipv6.unicast from AS200562 accept AS200562
mp-import:      afi ipv6.unicast from AS200573 accept AS200573
mp-import:      afi ipv6.unicast from AS200596 accept AS200596
mp-import:      afi ipv6.unicast from AS200612 accept AS-SETGBI
mp-import:      afi ipv6.unicast from AS200653 accept AS200653
mp-import:      afi ipv6.unicast from AS200705 accept AS200705
mp-import:      afi ipv6.unicast from AS200713 accept AS200713
mp-import:      afi ipv6.unicast from AS200738 accept AS200738
mp-import:      afi ipv6.unicast from AS200758 accept AS200758
mp-import:      afi ipv6.unicast from AS200780 accept AS-APPLIWAVE
mp-import:      afi ipv6.unicast from AS200845 accept AS-AVATEL-TRANSIT
mp-import:      afi ipv6.unicast from AS200861 accept AS200861
mp-import:      afi ipv6.unicast from AS200899 accept AS200899
mp-import:      afi ipv6.unicast from AS200904 accept AS200904
mp-import:      afi ipv6.unicast from AS200961 accept AS200961
mp-import:      afi ipv6.unicast from AS200994 accept AS200994
mp-import:      afi ipv6.unicast from AS201067 accept AS201067
mp-import:      afi ipv6.unicast from AS201126 accept AS201126
mp-import:      afi ipv6.unicast from AS201133 accept AS201133
mp-import:      afi ipv6.unicast from AS201188 accept AS201188
mp-import:      afi ipv6.unicast from AS201196 accept AS201196
mp-import:      afi ipv6.unicast from AS201213 accept AS201213
mp-import:      afi ipv6.unicast from AS201222 accept AS201222
mp-import:      afi ipv6.unicast from AS201246 accept AS201246
mp-import:      afi ipv6.unicast from AS201324 accept AS201324
mp-import:      afi ipv6.unicast from AS201333 accept AS201333
mp-import:      afi ipv6.unicast from AS201525 accept AS201525
mp-import:      afi ipv6.unicast from AS201565 accept AS201565
mp-import:      afi ipv6.unicast from AS201602 accept AS201602
mp-import:      afi ipv6.unicast from AS201731 accept AS201731
mp-import:      afi ipv6.unicast from AS201789 accept AS-NETOPS
mp-import:      afi ipv6.unicast from AS201895 accept AS201895
mp-import:      afi ipv6.unicast from AS201942 accept AS-SOLTIA
mp-import:      afi ipv6.unicast from AS201947 accept AS201947
mp-import:      afi ipv6.unicast from AS201958 accept AS201958
mp-import:      afi ipv6.unicast from AS201971 accept AS-CREEPERHOSTLTD
mp-import:      afi ipv6.unicast from AS201990 accept AS201990
mp-import:      afi ipv6.unicast from AS202010 accept AS202010
mp-import:      afi ipv6.unicast from AS202032 accept AS202032
mp-import:      afi ipv6.unicast from AS202075 accept AS202075
mp-import:      afi ipv6.unicast from AS202623 accept AS202623
mp-import:      afi ipv6.unicast from AS202713 accept AS202713
mp-import:      afi ipv6.unicast from AS202766 accept AS202766
mp-import:      afi ipv6.unicast from AS203050 accept AS203050
mp-import:      afi ipv6.unicast from AS203055 accept AS203055
mp-import:      afi ipv6.unicast from AS203182 accept AS203182
mp-import:      afi ipv6.unicast from AS203223 accept AS203223
mp-import:      afi ipv6.unicast from AS203256 accept AS203256
mp-import:      afi ipv6.unicast from AS203316 accept AS203316
mp-import:      afi ipv6.unicast from AS203346 accept AS-232web
mp-import:      afi ipv6.unicast from AS203351 accept AS203351
mp-import:      afi ipv6.unicast from AS203410 accept AS203410
mp-import:      afi ipv6.unicast from AS203608 accept AS203608
mp-import:      afi ipv6.unicast from AS203639 accept AS203639
mp-import:      afi ipv6.unicast from AS203649 accept AS203649
mp-import:      afi ipv6.unicast from AS203724 accept AS203724
mp-import:      afi ipv6.unicast from AS204126 accept AS204126
mp-import:      afi ipv6.unicast from AS204188 accept AS204188
mp-import:      afi ipv6.unicast from AS204258 accept AS204258
mp-import:      afi ipv6.unicast from AS204260 accept AS-DOTSI
mp-import:      afi ipv6.unicast from AS204353 accept AS204353
mp-import:      afi ipv6.unicast from AS204419 accept AS204419
mp-import:      afi ipv6.unicast from AS204476 accept AS204476
mp-import:      afi ipv6.unicast from AS204536 accept AS204536
mp-import:      afi ipv6.unicast from AS204548 accept AS204548
mp-import:      afi ipv6.unicast from AS204563 accept AS204563
mp-import:      afi ipv6.unicast from AS204577 accept AS-LINZNET
mp-import:      afi ipv6.unicast from AS204641 accept AS204641
mp-import:      afi ipv6.unicast from AS204801 accept AS204801
mp-import:      afi ipv6.unicast from AS204807 accept AS204807
mp-import:      afi ipv6.unicast from AS204959 accept AS204959
mp-import:      afi ipv6.unicast from AS204981 accept AS-204981
mp-import:      afi ipv6.unicast from AS205016 accept AS-OPERA
mp-import:      afi ipv6.unicast from AS205025 accept AS205025
mp-import:      afi ipv6.unicast from AS205039 accept AS205039
mp-import:      afi ipv6.unicast from AS205041 accept AS205041
mp-import:      afi ipv6.unicast from AS205142 accept AS205142
mp-import:      afi ipv6.unicast from AS205185 accept AS205185
mp-import:      afi ipv6.unicast from AS205394 accept AS205394
mp-import:      afi ipv6.unicast from AS205476 accept AS205476
mp-import:      afi ipv6.unicast from AS205544 accept AS205544
mp-import:      afi ipv6.unicast from AS205668 accept AS205668
mp-import:      afi ipv6.unicast from AS205697 accept AS205697
mp-import:      afi ipv6.unicast from AS205736 accept AS205736
mp-import:      afi ipv6.unicast from AS205809 accept AS205809
mp-import:      afi ipv6.unicast from AS205842 accept AS205842
mp-import:      afi ipv6.unicast from AS205943 accept AS205943
mp-import:      afi ipv6.unicast from AS206067 accept AS-H3GUK
mp-import:      afi ipv6.unicast from AS206121 accept AS206121
mp-import:      afi ipv6.unicast from AS206168 accept AS206168
mp-import:      afi ipv6.unicast from AS206264 accept AS206264
mp-import:      afi ipv6.unicast from AS206370 accept AS206370
mp-import:      afi ipv6.unicast from AS206372 accept AS206372
mp-import:      afi ipv6.unicast from AS206383 accept AS206383
mp-import:      afi ipv6.unicast from AS206399 accept AS206399
mp-import:      afi ipv6.unicast from AS206459 accept AS206459
mp-import:      afi ipv6.unicast from AS206537 accept AS206537
mp-import:      afi ipv6.unicast from AS206567 accept AS206567
mp-import:      afi ipv6.unicast from AS206576 accept AS-ADEPT
mp-import:      afi ipv6.unicast from AS206614 accept AS206614
mp-import:      afi ipv6.unicast from AS206701 accept AS206701
mp-import:      afi ipv6.unicast from AS206747 accept AS-NCSC-DNS
mp-import:      afi ipv6.unicast from AS206793 accept AS206793
mp-import:      afi ipv6.unicast from AS206892 accept AS206892
mp-import:      afi ipv6.unicast from AS206983 accept AS206983
mp-import:      afi ipv6.unicast from AS206984 accept AS206984
mp-import:      afi ipv6.unicast from AS207044 accept AS-AIRSPEED
mp-import:      afi ipv6.unicast from AS207045 accept AS207045
mp-import:      afi ipv6.unicast from AS207063 accept AS207063
mp-import:      afi ipv6.unicast from AS207127 accept AS207127
mp-import:      afi ipv6.unicast from AS207137 accept AS-SET-207137
mp-import:      afi ipv6.unicast from AS207176 accept AS207176
mp-import:      afi ipv6.unicast from AS207367 accept AS207367
mp-import:      afi ipv6.unicast from AS207543 accept AS207543
mp-import:      afi ipv6.unicast from AS207686 accept AS207686
mp-import:      afi ipv6.unicast from AS207747 accept AS207747
mp-import:      afi ipv6.unicast from AS207784 accept AS207784
mp-import:      afi ipv6.unicast from AS207995 accept AS207995
mp-import:      afi ipv6.unicast from AS208350 accept AS208350
mp-import:      afi ipv6.unicast from AS208374 accept AS-LU-CIX-2
mp-import:      afi ipv6.unicast from AS208416 accept AS208416
mp-import:      afi ipv6.unicast from AS208586 accept AS208586
mp-import:      afi ipv6.unicast from AS208625 accept AS208625
mp-import:      afi ipv6.unicast from AS208693 accept AS208693
mp-import:      afi ipv6.unicast from AS208877 accept AS208877
mp-import:      afi ipv6.unicast from AS209181 accept AS209181
mp-import:      afi ipv6.unicast from AS209282 accept AS209282
mp-import:      afi ipv6.unicast from AS209311 accept AS-VTNKS
mp-import:      afi ipv6.unicast from AS209549 accept AS-Provide
mp-import:      afi ipv6.unicast from AS209704 accept AS209704
mp-import:      afi ipv6.unicast from AS209811 accept AS209811
mp-import:      afi ipv6.unicast from AS210211 accept AS210211
mp-import:      afi ipv6.unicast from AS210253 accept AS210253
mp-import:      afi ipv6.unicast from AS210269 accept AS210269:AS-ALL
mp-import:      afi ipv6.unicast from AS210321 accept AS-OPERADORS
mp-import:      afi ipv6.unicast from AS210329 accept AS210329
mp-import:      afi ipv6.unicast from AS211029 accept AS211029
mp-import:      afi ipv6.unicast from AS211526 accept AS211526
mp-import:      afi ipv6.unicast from AS211597 accept AS-LITFIBRE
mp-import:      afi ipv6.unicast from AS212045 accept AS212045
mp-import:      afi ipv6.unicast from AS212055 accept AS212055
mp-import:      afi ipv6.unicast from AS212097 accept AS-VIMTEL
mp-import:      afi ipv6.unicast from AS212175 accept AS-ICONIC
mp-import:      afi ipv6.unicast from AS212708 accept AS212708
mp-import:      afi ipv6.unicast from AS212882 accept as-dnxnetwork-set
mp-import:      afi ipv6.unicast from AS213039 accept AS213039
mp-import:      afi ipv6.unicast from AS213094 accept AS-FULLFIBRE
mp-import:      afi ipv6.unicast from AS213101 accept AS213101
mp-import:      afi ipv6.unicast from AS213202 accept AS-CSG
mp-import:      afi ipv6.unicast from AS213205 accept AS213205
mp-import:      afi ipv6.unicast from AS213308 accept AS213308
mp-import:      afi ipv6.unicast from AS213373 accept AS213373
mp-import:      afi ipv6.unicast from AS262206 accept AS262206:AS-GLOBAL
mp-import:      afi ipv6.unicast from AS262287 accept AS262287
mp-import:      afi ipv6.unicast from AS262589 accept AS-ITXBR1
mp-import:      afi ipv6.unicast from AS262916 accept AS262916
mp-import:      afi ipv6.unicast from AS263179 accept AS263179
mp-import:      afi ipv6.unicast from AS263735 accept AS263735
mp-import:      afi ipv6.unicast from AS264409 accept AS-HUGENET-CUSTOMERS
mp-import:      afi ipv6.unicast from AS264763 accept AS-DOSBUFF
mp-import:      afi ipv6.unicast from AS265556 accept AS265556
mp-import:      afi ipv6.unicast from AS265680 accept AS-FEZ11
mp-import:      afi ipv6.unicast from AS393234 accept AS393234
mp-import:      afi ipv6.unicast from AS393241 accept AS393241
mp-import:      afi ipv6.unicast from AS393246 accept AS393246
mp-import:      afi ipv6.unicast from AS393544 accept AS393544
mp-import:      afi ipv6.unicast from AS393676 accept AS-ZENEDGE
mp-import:      afi ipv6.unicast from AS393845 accept AS393845
mp-import:      afi ipv6.unicast from AS393886 accept AS393886
mp-import:      afi ipv6.unicast from AS393900 accept AS393900
mp-import:      afi ipv6.unicast from AS394015 accept AS394015
mp-import:      afi ipv6.unicast from AS394102 accept AS394102
mp-import:      afi ipv6.unicast from AS394141 accept AS394141
mp-import:      afi ipv6.unicast from AS394186 accept AS394186
mp-import:      afi ipv6.unicast from AS394232 accept AS394232
mp-import:      afi ipv6.unicast from AS394303 accept AS394303
mp-import:      afi ipv6.unicast from AS394308 accept AS394308
mp-import:      afi ipv6.unicast from AS394346 accept AS394346
mp-import:      afi ipv6.unicast from AS394354 accept AS-394354
mp-import:      afi ipv6.unicast from AS394380 accept AS394380
mp-import:      afi ipv6.unicast from AS394434 accept AS394434
mp-import:      afi ipv6.unicast from AS394479 accept AS394479
mp-import:      afi ipv6.unicast from AS394501 accept AS394501
mp-import:      afi ipv6.unicast from AS394625 accept AS394625
mp-import:      afi ipv6.unicast from AS394851 accept AS394851
mp-import:      afi ipv6.unicast from AS394855 accept AS394855
mp-import:      afi ipv6.unicast from AS394935 accept AS394935
mp-import:      afi ipv6.unicast from AS394977 accept AS394977
mp-import:      afi ipv6.unicast from AS395052 accept AS395052
mp-import:      afi ipv6.unicast from AS395186 accept AS395186
mp-import:      afi ipv6.unicast from AS395308 accept AS395308
mp-import:      afi ipv6.unicast from AS395309 accept AS395309
mp-import:      afi ipv6.unicast from AS395354 accept AS395354
mp-import:      afi ipv6.unicast from AS395403 accept AS395403
mp-import:      afi ipv6.unicast from AS395598 accept AS395598
mp-import:      afi ipv6.unicast from AS395654 accept AS395654
mp-import:      afi ipv6.unicast from AS395662 accept AS395662
mp-import:      afi ipv6.unicast from AS395717 accept AS395717
mp-import:      afi ipv6.unicast from AS395747 accept AS395747
mp-import:      afi ipv6.unicast from AS395849 accept AS395849
mp-import:      afi ipv6.unicast from AS395954 accept AS395954
mp-import:      afi ipv6.unicast from AS395978 accept AS395978
mp-import:      afi ipv6.unicast from AS396026 accept AS396026
mp-import:      afi ipv6.unicast from AS396055 accept AS396055:AS-FIBERXPR
mp-import:      afi ipv6.unicast from AS396158 accept AS396158:AS-ALL
mp-import:      afi ipv6.unicast from AS396190 accept AS396190
mp-import:      afi ipv6.unicast from AS396356 accept AS-MAXIHOST
mp-import:      afi ipv6.unicast from AS396362 accept AS396362
mp-import:      afi ipv6.unicast from AS396417 accept AS396417
mp-import:      afi ipv6.unicast from AS396426 accept AS396426
mp-import:      afi ipv6.unicast from AS396472 accept AS396472
mp-import:      afi ipv6.unicast from AS396515 accept AS396515
mp-import:      afi ipv6.unicast from AS396535 accept AS396535
mp-import:      afi ipv6.unicast from AS396871 accept AS396871
mp-import:      afi ipv6.unicast from AS396948 accept AS396948
mp-import:      afi ipv6.unicast from AS396949 accept AS396949
mp-import:      afi ipv6.unicast from AS396970 accept AS396970
mp-import:      afi ipv6.unicast from AS396984 accept AS396984
mp-import:      afi ipv6.unicast from AS396986 accept AS396986
mp-import:      afi ipv6.unicast from AS396998 accept AS396998:AS-ALL
mp-import:      afi ipv6.unicast from AS397027 accept AS397027
mp-import:      afi ipv6.unicast from AS397041 accept AS397041
mp-import:      afi ipv6.unicast from AS397174 accept AS397174
mp-import:      afi ipv6.unicast from AS397308 accept AS397308
mp-import:      afi ipv6.unicast from AS397391 accept AS397391
mp-import:      afi ipv6.unicast from AS397404 accept AS397404
mp-import:      afi ipv6.unicast from AS397418 accept AS397418
mp-import:      afi ipv6.unicast from AS397494 accept AS397494
mp-import:      afi ipv6.unicast from AS397505 accept AS397505
mp-import:      afi ipv6.unicast from AS397545 accept AS397545
mp-import:      afi ipv6.unicast from AS397601 accept AS397601
mp-import:      afi ipv6.unicast from AS397727 accept AS397727
mp-import:      afi ipv6.unicast from AS397912 accept AS397912
mp-import:      afi ipv6.unicast from AS397925 accept AS397925
mp-import:      afi ipv6.unicast from AS398044 accept AS398044
mp-import:      afi ipv6.unicast from AS398107 accept AS398107
mp-import:      afi ipv6.unicast from AS398324 accept AS398324
mp-import:      afi ipv6.unicast from AS398427 accept AS398427
mp-import:      afi ipv6.unicast from AS398465 accept AS398465
mp-import:      afi ipv6.unicast from AS398698 accept AS-NETASSIST
mp-import:      afi ipv6.unicast from AS398712 accept AS-ISPCON
mp-import:      afi ipv6.unicast from AS398764 accept AS398764
mp-import:      afi ipv6.unicast from AS398765 accept AS398765
mp-import:      afi ipv6.unicast from AS398808 accept AS398808
mp-import:      afi ipv6.unicast from AS398814 accept AS398814
mp-import:      afi ipv6.unicast from AS398913 accept AS398913
mp-import:      afi ipv6.unicast from AS399065 accept AS399065
mp-import:      afi ipv6.unicast from AS399143 accept AS399143
mp-import:      afi ipv6.unicast from AS399289 accept AS399289
mp-import:      afi ipv6.unicast from AS399458 accept AS399458
mp-import:      afi ipv6.unicast from AS399480 accept AS399480
mp-import:      afi ipv6.unicast from AS399515 accept AS399515
mp-import:      afi ipv6.unicast from AS399558 accept AS399558
mp-import:      afi ipv6.unicast from AS399587 accept AS399587:AS-ALL
mp-import:      afi ipv6.unicast from AS399647 accept AS399647
mp-import:      afi ipv6.unicast from AS399808 accept AS399808
mp-import:      afi ipv6.unicast from AS399809 accept AS399809
mp-import:      afi ipv6.unicast from AS399810 accept AS399810
mp-import:      afi ipv6.unicast from AS399814 accept AS399814
mp-import:      afi ipv6.unicast from AS399816 accept AS399816
mp-import:      afi ipv6.unicast from AS399817 accept AS399817
mp-import:      afi ipv6.unicast from AS399818 accept AS399818
mp-import:      afi ipv6.unicast from AS399920 accept AS399920
mp-import:      afi ipv6.unicast from AS399989 accept AS-ALL
mp-import:      afi ipv6.unicast from AS399998 accept AS399998
mp-import:      afi ipv6.unicast from AS400042 accept AS-RIGHTFORGE
mp-import:      afi ipv6.unicast from AS400146 accept AS400146
mp-import:      afi ipv6.unicast from AS400202 accept AS400202
mp-import:      afi ipv6.unicast from AS400282 accept AS400282
mp-import:      afi ipv6.unicast from AS400302 accept AS400302
mp-import:      afi ipv6.unicast from AS400309 accept AS-GLOBALFRAG
mp-import:      afi ipv6.unicast from AS400475 accept AS400475
mp-import:      afi ipv6.unicast from AS400511 accept AS400511
mp-import:      afi ipv6.unicast from AS400541 accept AS400541
mp-import:      afi ipv6.unicast from AS400662 accept AS400662
mp-import:      afi ipv6.unicast from AS400666 accept AS400666
mp-import:      afi ipv6.unicast from AS400687 accept AS400687
mp-import:      afi ipv6.unicast from AS400692 accept AS400692
mp-import:      afi ipv6.unicast from AS400802 accept AS400802
export:         to AS12 announce ANY
export:         to AS14 announce ANY
export:         to AS21 announce ANY
export:         to AS57 announce ANY
export:         to AS62 announce ANY
export:         to AS97 announce ANY
export:         to AS109 announce ANY
export:         to AS260 announce ANY
export:         to AS286 announce ANY
export:         to AS288 announce ANY
export:         to AS376 announce ANY
export:         to AS517 announce ANY
export:         to AS559 announce ANY
export:         to AS572 announce ANY
export:         to AS577 announce ANY
export:         to AS600 announce ANY
export:         to AS612 announce ANY
export:         to AS714 announce ANY
export:         to AS766 announce ANY
export:         to AS792 announce ANY
export:         to AS812 announce ANY
export:         to AS852 announce ANY
export:         to AS855 announce ANY
export:         to AS979 announce ANY
export:         to AS1017 announce ANY
export:         to AS1065 announce ANY
export:         to AS1100 announce ANY
export:         to AS1103 announce ANY
export:         to AS1213 announce ANY
export:         to AS1215 announce ANY
export:         to AS1216 announce ANY
export:         to AS1219 announce ANY
export:         to AS1257 announce ANY
export:         to AS1258 announce ANY
export:         to AS1261 announce ANY
export:         to AS1267 announce ANY
export:         to AS1311 announce ANY
export:         to AS1341 announce ANY
export:         to AS1445 announce ANY
export:         to AS1449 announce ANY
export:         to AS1605 announce ANY
export:         to AS1610 announce ANY
export:         to AS1612 announce ANY
export:         to AS1678 announce ANY
export:         to AS1680 announce ANY
export:         to AS1764 announce ANY
export:         to AS1803 announce ANY
export:         to AS1820 announce ANY
export:         to AS1828 announce ANY
export:         to AS1968 announce ANY
export:         to AS2121 announce ANY
export:         to AS2147 announce ANY
export:         to AS2200 announce ANY
export:         to AS2381 announce ANY
export:         to AS2484 announce ANY
export:         to AS2495 announce ANY
export:         to AS2516 announce ANY
export:         to AS2572 announce ANY
export:         to AS2609 announce ANY
export:         to AS2611 announce ANY
export:         to AS2698 announce ANY
export:         to AS2721 announce ANY
export:         to AS2728 announce ANY
export:         to AS2734 announce ANY
export:         to AS3165 announce ANY
export:         to AS3170 announce ANY
export:         to AS3206 announce ANY
export:         to AS3212 announce ANY
export:         to AS3214 announce ANY
export:         to AS3215 announce ANY
export:         to AS3252 announce ANY
export:         to AS3255 announce ANY
export:         to AS3264 announce ANY
export:         to AS3291 announce ANY
export:         to AS3292 announce ANY
export:         to AS3302 announce ANY
export:         to AS3352 announce ANY
export:         to AS3367 announce ANY
export:         to AS3399 announce ANY
export:         to AS3573 announce ANY
export:         to AS3584 announce ANY
export:         to AS3676 announce ANY
export:         to AS3722 announce ANY
export:         to AS3728 announce ANY
export:         to AS3737 announce ANY
export:         to AS3842 announce ANY
export:         to AS3908 announce ANY
export:         to AS3925 announce ANY
export:         to AS3943 announce ANY
export:         to AS4058 announce ANY
export:         to AS4150 announce ANY
export:         to AS4181 announce ANY
export:         to AS4229 announce ANY
export:         to AS4230 announce ANY
export:         to AS4250 announce ANY
export:         to AS4385 announce ANY
export:         to AS4436 announce ANY
export:         to AS4540 announce ANY
export:         to AS4556 announce ANY
export:         to AS4565 announce ANY
export:         to AS4589 announce ANY
export:         to AS4648 announce ANY
export:         to AS4788 announce ANY
export:         to AS4826 announce ANY
export:         to AS4867 announce ANY
export:         to AS4882 announce ANY
export:         to AS4889 announce ANY
export:         to AS4893 announce ANY
export:         to AS5008 announce ANY
export:         to AS5009 announce ANY
export:         to AS5078 announce ANY
export:         to AS5091 announce ANY
export:         to AS5394 announce ANY
export:         to AS5396 announce ANY
export:         to AS5398 announce ANY
export:         to AS5409 announce ANY
export:         to AS5459 announce ANY
export:         to AS5463 announce ANY
export:         to AS5486 announce ANY
export:         to AS5524 announce ANY
export:         to AS5580 announce ANY
export:         to AS5582 announce ANY
export:         to AS5602 announce ANY
export:         to AS5606 announce ANY
export:         to AS5607 announce ANY
export:         to AS5645 announce ANY
export:         to AS5669 announce ANY
export:         to AS5670 announce ANY
export:         to AS5697 announce ANY
export:         to AS5715 announce ANY
export:         to AS5738 announce ANY
export:         to AS5742 announce ANY
export:         to AS5760 announce ANY
export:         to AS5769 announce ANY
export:         to AS5777 announce ANY
export:         to AS5784 announce ANY
export:         to AS6059 announce ANY
export:         to AS6067 announce ANY
export:         to AS6071 announce ANY
export:         to AS6072 announce ANY
export:         to AS6079 announce ANY
export:         to AS6095 announce ANY
export:         to AS6142 announce ANY
export:         to AS6169 announce ANY
export:         to AS6181 announce ANY
export:         to AS6199 announce ANY
export:         to AS6220 announce ANY
export:         to AS6267 announce ANY
export:         to AS6325 announce ANY
export:         to AS6327 announce ANY
export:         to AS6391 announce ANY
export:         to AS6407 announce ANY
export:         to AS6459 announce ANY
export:         to AS6462 announce ANY
export:         to AS6471 announce ANY
export:         to AS6493 announce ANY
export:         to AS6498 announce ANY
export:         to AS6507 announce ANY
export:         to AS6508 announce ANY
export:         to AS6517 announce ANY
export:         to AS6566 announce ANY
export:         to AS6597 announce ANY
export:         to AS6621 announce ANY
export:         to AS6643 announce ANY
export:         to AS6659 announce ANY
export:         to AS6663 announce ANY
export:         to AS6667 announce ANY
export:         to AS6696 announce ANY
export:         to AS6713 announce ANY
export:         to AS6717 announce ANY
export:         to AS6723 announce ANY
export:         to AS6738 announce ANY
export:         to AS6747 announce ANY
export:         to AS6752 announce ANY
export:         to AS6768 announce ANY
export:         to AS6770 announce ANY
export:         to AS6774 announce ANY
export:         to AS6779 announce ANY
export:         to AS6805 announce ANY
export:         to AS6812 announce ANY
export:         to AS6830 announce ANY
export:         to AS6848 announce ANY
export:         to AS6866 announce ANY
export:         to AS6894 announce ANY
export:         to AS6898 announce ANY
export:         to AS6907 announce ANY
export:         to AS6951 announce ANY
export:         to AS7012 announce ANY
export:         to AS7014 announce ANY
export:         to AS7029 announce ANY
export:         to AS7148 announce ANY
export:         to AS7153 announce ANY
export:         to AS7155 announce ANY
export:         to AS7158 announce ANY
export:         to AS7160 announce ANY
export:         to AS7203 announce ANY
export:         to AS7219 announce ANY
export:         to AS7270 announce ANY
export:         to AS7296 announce ANY
export:         to AS7303 announce ANY
export:         to AS7311 announce ANY
export:         to AS7334 announce ANY
export:         to AS7384 announce ANY
export:         to AS7459 announce ANY
export:         to AS7473 announce ANY
export:         to AS7500 announce ANY
export:         to AS7713 announce ANY
export:         to AS7738 announce ANY
export:         to AS7752 announce ANY
export:         to AS7754 announce ANY
export:         to AS7768 announce ANY
export:         to AS7784 announce ANY
export:         to AS7786 announce ANY
export:         to AS7795 announce ANY
export:         to AS7843 announce ANY
export:         to AS7859 announce ANY
export:         to AS7896 announce ANY
export:         to AS7944 announce ANY
export:         to AS7992 announce ANY
export:         to AS8001 announce ANY
export:         to AS8018 announce ANY
export:         to AS8038 announce ANY
export:         to AS8057 announce ANY
export:         to AS8069 announce ANY
export:         to AS8075 announce ANY
export:         to AS8084 announce ANY
export:         to AS8092 announce ANY
export:         to AS8100 announce ANY
export:         to AS8111 announce ANY
export:         to AS8131 announce ANY
export:         to AS8151 announce ANY
export:         to AS8190 announce ANY
export:         to AS8201 announce ANY
export:         to AS8245 announce ANY
export:         to AS8247 announce ANY
export:         to AS8262 announce ANY
export:         to AS8301 announce ANY
export:         to AS8304 announce ANY
export:         to AS8308 announce ANY
export:         to AS8315 announce ANY
export:         to AS8318 announce ANY
export:         to AS8323 announce ANY
export:         to AS8328 announce ANY
export:         to AS8368 announce ANY
export:         to AS8399 announce ANY
export:         to AS8400 announce ANY
export:         to AS8426 announce ANY
export:         to AS8452 announce ANY
export:         to AS8453 announce ANY
export:         to AS8468 announce ANY
export:         to AS8476 announce ANY
export:         to AS8487 announce ANY
export:         to AS8495 announce ANY
export:         to AS8513 announce ANY
export:         to AS8523 announce ANY
export:         to AS8551 announce ANY
export:         to AS8554 announce ANY
export:         to AS8560 announce ANY
export:         to AS8587 announce ANY
export:         to AS8607 announce ANY
export:         to AS8612 announce ANY
export:         to AS8648 announce ANY
export:         to AS8657 announce ANY
export:         to AS8751 announce ANY
export:         to AS8757 announce ANY
export:         to AS8781 announce ANY
export:         to AS8784 announce ANY
export:         to AS8793 announce ANY
export:         to AS8816 announce ANY
export:         to AS8822 announce ANY
export:         to AS8849 announce ANY
export:         to AS8851 announce ANY
export:         to AS8859 announce ANY
export:         to AS8895 announce ANY
export:         to AS8902 announce ANY
export:         to AS8903 announce ANY
export:         to AS8918 announce ANY
export:         to AS8922 announce ANY
export:         to AS8928 announce ANY
export:         to AS8954 announce ANY
export:         to AS8966 announce ANY
export:         to AS8978 announce ANY
export:         to AS8990 announce ANY
export:         to AS9002 announce ANY
export:         to AS9009 announce ANY
export:         to AS9031 announce ANY
export:         to AS9038 announce ANY
export:         to AS9050 announce ANY
export:         to AS9070 announce ANY
export:         to AS9116 announce ANY
export:         to AS9137 announce ANY
export:         to AS9142 announce ANY
export:         to AS9186 announce ANY
export:         to AS9192 announce ANY
export:         to AS9211 announce ANY
export:         to AS9269 announce ANY
export:         to AS9304 announce ANY
export:         to AS9381 announce ANY
export:         to AS9498 announce ANY
export:         to AS9658 announce ANY
export:         to AS9744 announce ANY
export:         to AS9821 announce ANY
export:         to AS9829 announce ANY
export:         to AS10030 announce ANY
export:         to AS10098 announce ANY
export:         to AS10099 announce ANY
export:         to AS10122 announce ANY
export:         to AS10325 announce ANY
export:         to AS10361 announce ANY
export:         to AS10397 announce ANY
export:         to AS10461 announce ANY
export:         to AS10490 announce ANY
export:         to AS10561 announce ANY
export:         to AS10625 announce ANY
export:         to AS10661 announce ANY
export:         to AS10674 announce ANY
export:         to AS10700 announce ANY
export:         to AS10747 announce ANY
export:         to AS10780 announce ANY
export:         to AS10835 announce ANY
export:         to AS10886 announce ANY
export:         to AS10905 announce ANY
export:         to AS10910 announce ANY
export:         to AS10982 announce ANY
export:         to AS10996 announce ANY
export:         to AS11013 announce ANY
export:         to AS11019 announce ANY
export:         to AS11036 announce ANY
export:         to AS11049 announce ANY
export:         to AS11071 announce ANY
export:         to AS11074 announce ANY
export:         to AS11082 announce ANY
export:         to AS11158 announce ANY
export:         to AS11174 announce ANY
export:         to AS11208 announce ANY
export:         to AS11215 announce ANY
export:         to AS11232 announce ANY
export:         to AS11251 announce ANY
export:         to AS11260 announce ANY
export:         to AS11262 announce ANY
export:         to AS11267 announce ANY
export:         to AS11290 announce ANY
export:         to AS11320 announce ANY
export:         to AS11323 announce ANY
export:         to AS11403 announce ANY
export:         to AS11404 announce ANY
export:         to AS11468 announce ANY
export:         to AS11478 announce ANY
export:         to AS11522 announce ANY
export:         to AS11528 announce ANY
export:         to AS11618 announce ANY
export:         to AS11641 announce ANY
export:         to AS11647 announce ANY
export:         to AS11653 announce ANY
export:         to AS11682 announce ANY
export:         to AS11696 announce ANY
export:         to AS11711 announce ANY
export:         to AS11731 announce ANY
export:         to AS11747 announce ANY
export:         to AS11807 announce ANY
export:         to AS11849 announce ANY
export:         to AS11852 announce ANY
export:         to AS11856 announce ANY
export:         to AS11866 announce ANY
export:         to AS11876 announce ANY
export:         to AS11878 announce ANY
export:         to AS11889 announce ANY
export:         to AS11924 announce ANY
export:         to AS11931 announce ANY
export:         to AS11954 announce ANY
export:         to AS11966 announce ANY
export:         to AS12008 announce ANY
export:         to AS12041 announce ANY
export:         to AS12042 announce ANY
export:         to AS12059 announce ANY
export:         to AS12083 announce ANY
export:         to AS12085 announce ANY
export:         to AS12096 announce ANY
export:         to AS12105 announce ANY
export:         to AS12129 announce ANY
export:         to AS12132 announce ANY
export:         to AS12133 announce ANY
export:         to AS12168 announce ANY
export:         to AS12175 announce ANY
export:         to AS12189 announce ANY
export:         to AS12200 announce ANY
export:         to AS12252 announce ANY
export:         to AS12287 announce ANY
export:         to AS12301 announce ANY
export:         to AS12312 announce ANY
export:         to AS12333 announce ANY
export:         to AS12348 announce ANY
export:         to AS12355 announce ANY
export:         to AS12360 announce ANY
export:         to AS12362 announce ANY
export:         to AS12372 announce ANY
export:         to AS12387 announce ANY
export:         to AS12389 announce ANY
export:         to AS12409 announce ANY
export:         to AS12414 announce ANY
export:         to AS12470 announce ANY
export:         to AS12474 announce ANY
export:         to AS12480 announce ANY
export:         to AS12488 announce ANY
export:         to AS12498 announce ANY
export:         to AS12533 announce ANY
export:         to AS12541 announce ANY
export:         to AS12546 announce ANY
export:         to AS12570 announce ANY
export:         to AS12578 announce ANY
export:         to AS12580 announce ANY
export:         to AS12581 announce ANY
export:         to AS12586 announce ANY
export:         to AS12601 announce ANY
export:         to AS12615 announce ANY
export:         to AS12625 announce ANY
export:         to AS12655 announce ANY
export:         to AS12676 announce ANY
export:         to AS12678 announce ANY
export:         to AS12684 announce ANY
export:         to AS12693 announce ANY
export:         to AS12703 announce ANY
export:         to AS12731 announce ANY
export:         to AS12732 announce ANY
export:         to AS12741 announce ANY
export:         to AS12754 announce ANY
export:         to AS12775 announce ANY
export:         to AS12779 announce ANY
export:         to AS12786 announce ANY
export:         to AS12787 announce ANY
export:         to AS12801 announce ANY
export:         to AS12831 announce ANY
export:         to AS12843 announce ANY
export:         to AS12859 announce ANY
export:         to AS12883 announce ANY
export:         to AS12884 announce ANY
export:         to AS12897 announce ANY
export:         to AS12905 announce ANY
export:         to AS12906 announce ANY
export:         to AS12945 announce ANY
export:         to AS12963 announce ANY
export:         to AS12968 announce ANY
export:         to AS12989 announce ANY
export:         to AS12993 announce ANY
export:         to AS13000 announce ANY
export:         to AS13006 announce ANY
export:         to AS13039 announce ANY
export:         to AS13046 announce ANY
export:         to AS13101 announce ANY
export:         to AS13105 announce ANY
export:         to AS13119 announce ANY
export:         to AS13126 announce ANY
export:         to AS13132 announce ANY
export:         to AS13150 announce ANY
export:         to AS13194 announce ANY
export:         to AS13213 announce ANY
export:         to AS13237 announce ANY
export:         to AS13250 announce ANY
export:         to AS13280 announce ANY
export:         to AS13285 announce ANY
export:         to AS13287 announce ANY
export:         to AS13331 announce ANY
export:         to AS13333 announce ANY
export:         to AS13335 announce ANY
export:         to AS13360 announce ANY
export:         to AS13414 announce ANY
export:         to AS13428 announce ANY
export:         to AS13431 announce ANY
export:         to AS13443 announce ANY
export:         to AS13446 announce ANY
export:         to AS13448 announce ANY
export:         to AS13464 announce ANY
export:         to AS13471 announce ANY
export:         to AS13480 announce ANY
export:         to AS13490 announce ANY
export:         to AS13491 announce ANY
export:         to AS13511 announce ANY
export:         to AS13517 announce ANY
export:         to AS13524 announce ANY
export:         to AS13537 announce ANY
export:         to AS13556 announce ANY
export:         to AS13557 announce ANY
export:         to AS13628 announce ANY
export:         to AS13631 announce ANY
export:         to AS13649 announce ANY
export:         to AS13658 announce ANY
export:         to AS13739 announce ANY
export:         to AS13760 announce ANY
export:         to AS13768 announce ANY
export:         to AS13778 announce ANY
export:         to AS13789 announce ANY
export:         to AS13798 announce ANY
export:         to AS13821 announce ANY
export:         to AS13860 announce ANY
export:         to AS13876 announce ANY
export:         to AS13887 announce ANY
export:         to AS13909 announce ANY
export:         to AS13938 announce ANY
export:         to AS13971 announce ANY
export:         to AS13981 announce ANY
export:         to AS13984 announce ANY
export:         to AS13988 announce ANY
export:         to AS14010 announce ANY
export:         to AS14014 announce ANY
export:         to AS14016 announce ANY
export:         to AS14037 announce ANY
export:         to AS14049 announce ANY
export:         to AS14074 announce ANY
export:         to AS14080 announce ANY
export:         to AS14086 announce ANY
export:         to AS14108 announce ANY
export:         to AS14135 announce ANY
export:         to AS14148 announce ANY
export:         to AS14157 announce ANY
export:         to AS14170 announce ANY
export:         to AS14201 announce ANY
export:         to AS14210 announce ANY
export:         to AS14237 announce ANY
export:         to AS14253 announce ANY
export:         to AS14332 announce ANY
export:         to AS14335 announce ANY
export:         to AS14343 announce ANY
export:         to AS14361 announce ANY
export:         to AS14365 announce ANY
export:         to AS14371 announce ANY
export:         to AS14395 announce ANY
export:         to AS14398 announce ANY
export:         to AS14409 announce ANY
export:         to AS14492 announce ANY
export:         to AS14500 announce ANY
export:         to AS14525 announce ANY
export:         to AS14544 announce ANY
export:         to AS14585 announce ANY
export:         to AS14589 announce ANY
export:         to AS14593 announce ANY
export:         to AS14601 announce ANY
export:         to AS14616 announce ANY
export:         to AS14630 announce ANY
export:         to AS14643 announce ANY
export:         to AS14665 announce ANY
export:         to AS14689 announce ANY
export:         to AS14707 announce ANY
export:         to AS14717 announce ANY
export:         to AS14743 announce ANY
export:         to AS14745 announce ANY
export:         to AS14746 announce ANY
export:         to AS14753 announce ANY
export:         to AS14754 announce ANY
export:         to AS14762 announce ANY
export:         to AS14817 announce ANY
export:         to AS14821 announce ANY
export:         to AS14862 announce ANY
export:         to AS14879 announce ANY
export:         to AS14928 announce ANY
export:         to AS14973 announce ANY
export:         to AS14986 announce ANY
export:         to AS14987 announce ANY
export:         to AS15003 announce ANY
export:         to AS15042 announce ANY
export:         to AS15092 announce ANY
export:         to AS15093 announce ANY
export:         to AS15128 announce ANY
export:         to AS15133 announce ANY
export:         to AS15146 announce ANY
export:         to AS15206 announce ANY
export:         to AS15211 announce ANY
export:         to AS15220 announce ANY
export:         to AS15225 announce ANY
export:         to AS15238 announce ANY
export:         to AS15247 announce ANY
export:         to AS15277 announce ANY
export:         to AS15317 announce ANY
export:         to AS15324 announce ANY
export:         to AS15346 announce ANY
export:         to AS15421 announce ANY
export:         to AS15435 announce ANY
export:         to AS15447 announce ANY
export:         to AS15557 announce ANY
export:         to AS15562 announce ANY
export:         to AS15570 announce ANY
export:         to AS15576 announce ANY
export:         to AS15587 announce ANY
export:         to AS15605 announce ANY
export:         to AS15694 announce ANY
export:         to AS15695 announce ANY
export:         to AS15703 announce ANY
export:         to AS15735 announce ANY
export:         to AS15782 announce ANY
export:         to AS15806 announce ANY
export:         to AS15830 announce ANY
export:         to AS15879 announce ANY
export:         to AS15919 announce ANY
export:         to AS15923 announce ANY
export:         to AS15924 announce ANY
export:         to AS15943 announce ANY
export:         to AS15953 announce ANY
export:         to AS15954 announce ANY
export:         to AS15966 announce ANY
export:         to AS15967 announce ANY
export:         to AS15989 announce ANY
export:         to AS15994 announce ANY
export:         to AS16080 announce ANY
export:         to AS16097 announce ANY
export:         to AS16110 announce ANY
export:         to AS16131 announce ANY
export:         to AS16147 announce ANY
export:         to AS16162 announce ANY
export:         to AS16168 announce ANY
export:         to AS16189 announce ANY
export:         to AS16236 announce ANY
export:         to AS16238 announce ANY
export:         to AS16297 announce ANY
export:         to AS16360 announce ANY
export:         to AS16364 announce ANY
export:         to AS16406 announce ANY
export:         to AS16501 announce ANY
export:         to AS16504 announce ANY
export:         to AS16509 announce ANY
export:         to AS16524 announce ANY
export:         to AS16551 announce ANY
export:         to AS16552 announce ANY
export:         to AS16570 announce ANY
export:         to AS16573 announce ANY
export:         to AS16591 announce ANY
export:         to AS16625 announce ANY
export:         to AS16633 announce ANY
export:         to AS16647 announce ANY
export:         to AS16668 announce ANY
export:         to AS16676 announce ANY
export:         to AS16733 announce ANY
export:         to AS16750 announce ANY
export:         to AS16761 announce ANY
export:         to AS16815 announce ANY
export:         to AS16820 announce ANY
export:         to AS16823 announce ANY
export:         to AS16832 announce ANY
export:         to AS16839 announce ANY
export:         to AS16851 announce ANY
export:         to AS16863 announce ANY
export:         to AS16876 announce ANY
export:         to AS16940 announce ANY
export:         to AS17012 announce ANY
export:         to AS17035 announce ANY
export:         to AS17045 announce ANY
export:         to AS17088 announce ANY
export:         to AS17130 announce ANY
export:         to AS17139 announce ANY
export:         to AS17149 announce ANY
export:         to AS17151 announce ANY
export:         to AS17184 announce ANY
export:         to AS17204 announce ANY
export:         to AS17240 announce ANY
export:         to AS17316 announce ANY
export:         to AS17330 announce ANY
export:         to AS17352 announce ANY
export:         to AS17378 announce ANY
export:         to AS17466 announce ANY
export:         to AS17666 announce ANY
export:         to AS17814 announce ANY
export:         to AS18119 announce ANY
export:         to AS18214 announce ANY
export:         to AS18434 announce ANY
export:         to AS18450 announce ANY
export:         to AS18451 announce ANY
export:         to AS18456 announce ANY
export:         to AS18465 announce ANY
export:         to AS18474 announce ANY
export:         to AS18485 announce ANY
export:         to AS18518 announce ANY
export:         to AS18540 announce ANY
export:         to AS18549 announce ANY
export:         to AS18566 announce ANY
export:         to AS18588 announce ANY
export:         to AS18608 announce ANY
export:         to AS18619 announce ANY
export:         to AS18622 announce ANY
export:         to AS18670 announce ANY
export:         to AS18712 announce ANY
export:         to AS18717 announce ANY
export:         to AS18723 announce ANY
export:         to AS18734 announce ANY
export:         to AS18747 announce ANY
export:         to AS18777 announce ANY
export:         to AS18779 announce ANY
export:         to AS18854 announce ANY
export:         to AS18880 announce ANY
export:         to AS18882 announce ANY
export:         to AS18919 announce ANY
export:         to AS18929 announce ANY
export:         to AS18966 announce ANY
export:         to AS18978 announce ANY
export:         to AS18990 announce ANY
export:         to AS18994 announce ANY
export:         to AS19001 announce ANY
export:         to AS19006 announce ANY
export:         to AS19037 announce ANY
export:         to AS19108 announce ANY
export:         to AS19137 announce ANY
export:         to AS19165 announce ANY
export:         to AS19186 announce ANY
export:         to AS19193 announce ANY
export:         to AS19208 announce ANY
export:         to AS19214 announce ANY
export:         to AS19222 announce ANY
export:         to AS19231 announce ANY
export:         to AS19237 announce ANY
export:         to AS19305 announce ANY
export:         to AS19318 announce ANY
export:         to AS19324 announce ANY
export:         to AS19380 announce ANY
export:         to AS19397 announce ANY
export:         to AS19398 announce ANY
export:         to AS19416 announce ANY
export:         to AS19448 announce ANY
export:         to AS19457 announce ANY
export:         to AS19460 announce ANY
export:         to AS19515 announce ANY
export:         to AS19531 announce ANY
export:         to AS19551 announce ANY
export:         to AS19602 announce ANY
export:         to AS19637 announce ANY
export:         to AS19679 announce ANY
export:         to AS19683 announce ANY
export:         to AS19710 announce ANY
export:         to AS19740 announce ANY
export:         to AS19750 announce ANY
export:         to AS19752 announce ANY
export:         to AS19773 announce ANY
export:         to AS19803 announce ANY
export:         to AS19806 announce ANY
export:         to AS19808 announce ANY
export:         to AS19811 announce ANY
export:         to AS19868 announce ANY
export:         to AS19894 announce ANY
export:         to AS19905 announce ANY
export:         to AS19911 announce ANY
export:         to AS19920 announce ANY
export:         to AS19936 announce ANY
export:         to AS19950 announce ANY
export:         to AS19966 announce ANY
export:         to AS19969 announce ANY
export:         to AS19982 announce ANY
export:         to AS19993 announce ANY
export:         to AS20054 announce ANY
export:         to AS20055 announce ANY
export:         to AS20070 announce ANY
export:         to AS20077 announce ANY
export:         to AS20115 announce ANY
export:         to AS20135 announce ANY
export:         to AS20144 announce ANY
export:         to AS20205 announce ANY
export:         to AS20216 announce ANY
export:         to AS20220 announce ANY
export:         to AS20223 announce ANY
export:         to AS20249 announce ANY
export:         to AS20278 announce ANY
export:         to AS20284 announce ANY
export:         to AS20285 announce ANY
export:         to AS20326 announce ANY
export:         to AS20331 announce ANY
export:         to AS20340 announce ANY
export:         to AS20355 announce ANY
export:         to AS20384 announce ANY
export:         to AS20385 announce ANY
export:         to AS20429 announce ANY
export:         to AS20462 announce ANY
export:         to AS20473 announce ANY
export:         to AS20565 announce ANY
export:         to AS20621 announce ANY
export:         to AS20640 announce ANY
export:         to AS20645 announce ANY
export:         to AS20650 announce ANY
export:         to AS20676 announce ANY
export:         to AS20681 announce ANY
export:         to AS20694 announce ANY
export:         to AS20776 announce ANY
export:         to AS20847 announce ANY
export:         to AS20853 announce ANY
export:         to AS20857 announce ANY
export:         to AS20878 announce ANY
export:         to AS20896 announce ANY
export:         to AS20912 announce ANY
export:         to AS20914 announce ANY
export:         to AS20917 announce ANY
export:         to AS20924 announce ANY
export:         to AS20928 announce ANY
export:         to AS20940 announce ANY
export:         to AS20953 announce ANY
export:         to AS20976 announce ANY
export:         to AS21013 announce ANY
export:         to AS21034 announce ANY
export:         to AS21056 announce ANY
export:         to AS21057 announce ANY
export:         to AS21069 announce ANY
export:         to AS21094 announce ANY
export:         to AS21188 announce ANY
export:         to AS21221 announce ANY
export:         to AS21235 announce ANY
export:         to AS21254 announce ANY
export:         to AS21267 announce ANY
export:         to AS21277 announce ANY
export:         to AS21321 announce ANY
export:         to AS21345 announce ANY
export:         to AS21357 announce ANY
export:         to AS21371 announce ANY
export:         to AS21409 announce ANY
export:         to AS21433 announce ANY
export:         to AS21459 announce ANY
export:         to AS21488 announce ANY
export:         to AS21497 announce ANY
export:         to AS21509 announce ANY
export:         to AS21513 announce ANY
export:         to AS21534 announce ANY
export:         to AS21537 announce ANY
export:         to AS21559 announce ANY
export:         to AS21570 announce ANY
export:         to AS21589 announce ANY
export:         to AS21636 announce ANY
export:         to AS21646 announce ANY
export:         to AS21655 announce ANY
export:         to AS21693 announce ANY
export:         to AS21700 announce ANY
export:         to AS21723 announce ANY
export:         to AS21724 announce ANY
export:         to AS21743 announce ANY
export:         to AS21755 announce ANY
export:         to AS21777 announce ANY
export:         to AS21802 announce ANY
export:         to AS21804 announce ANY
export:         to AS21859 announce ANY
export:         to AS21886 announce ANY
export:         to AS21947 announce ANY
export:         to AS21983 announce ANY
export:         to AS22075 announce ANY
export:         to AS22124 announce ANY
export:         to AS22191 announce ANY
export:         to AS22208 announce ANY
export:         to AS22298 announce ANY
export:         to AS22317 announce ANY
export:         to AS22332 announce ANY
export:         to AS22356 announce ANY
export:         to AS22363 announce ANY
export:         to AS22393 announce ANY
export:         to AS22404 announce ANY
export:         to AS22413 announce ANY
export:         to AS22418 announce ANY
export:         to AS22512 announce ANY
export:         to AS22537 announce ANY
export:         to AS22541 announce ANY
export:         to AS22549 announce ANY
export:         to AS22557 announce ANY
export:         to AS22611 announce ANY
export:         to AS22612 announce ANY
export:         to AS22616 announce ANY
export:         to AS22620 announce ANY
export:         to AS22645 announce ANY
export:         to AS22646 announce ANY
export:         to AS22652 announce ANY
export:         to AS22653 announce ANY
export:         to AS22683 announce ANY
export:         to AS22741 announce ANY
export:         to AS22742 announce ANY
export:         to AS22768 announce ANY
export:         to AS22769 announce ANY
export:         to AS22773 announce ANY
export:         to AS22792 announce ANY
export:         to AS22803 announce ANY
export:         to AS22822 announce ANY
export:         to AS22838 announce ANY
export:         to AS22911 announce ANY
export:         to AS22915 announce ANY
export:         to AS22925 announce ANY
export:         to AS22957 announce ANY
export:         to AS22964 announce ANY
export:         to AS22973 announce ANY
export:         to AS22987 announce ANY
export:         to AS22995 announce ANY
export:         to AS23010 announce ANY
export:         to AS23028 announce ANY
export:         to AS23029 announce ANY
export:         to AS23081 announce ANY
export:         to AS23108 announce ANY
export:         to AS23114 announce ANY
export:         to AS23132 announce ANY
export:         to AS23136 announce ANY
export:         to AS23148 announce ANY
export:         to AS23161 announce ANY
export:         to AS23232 announce ANY
export:         to AS23241 announce ANY
export:         to AS23247 announce ANY
export:         to AS23262 announce ANY
export:         to AS23312 announce ANY
export:         to AS23314 announce ANY
export:         to AS23316 announce ANY
export:         to AS23342 announce ANY
export:         to AS23352 announce ANY
export:         to AS23367 announce ANY
export:         to AS23393 announce ANY
export:         to AS23420 announce ANY
export:         to AS23442 announce ANY
export:         to AS23470 announce ANY
export:         to AS23487 announce ANY
export:         to AS23498 announce ANY
export:         to AS23507 announce ANY
export:         to AS23528 announce ANY
export:         to AS23533 announce ANY
export:         to AS23547 announce ANY
export:         to AS23576 announce ANY
export:         to AS23655 announce ANY
export:         to AS23764 announce ANY
export:         to AS23947 announce ANY
export:         to AS24232 announce ANY
export:         to AS24331 announce ANY
export:         to AS24413 announce ANY
export:         to AS24514 announce ANY
export:         to AS24637 announce ANY
export:         to AS24724 announce ANY
export:         to AS24730 announce ANY
export:         to AS24750 announce ANY
export:         to AS24753 announce ANY
export:         to AS24776 announce ANY
export:         to AS24778 announce ANY
export:         to AS24817 announce ANY
export:         to AS24835 announce ANY
export:         to AS24875 announce ANY
export:         to AS24940 announce ANY
export:         to AS24953 announce ANY
export:         to AS24958 announce ANY
export:         to AS24989 announce ANY
export:         to AS24990 announce ANY
export:         to AS24993 announce ANY
export:         to AS25003 announce ANY
export:         to AS25030 announce ANY
export:         to AS25038 announce ANY
export:         to AS25056 announce ANY
export:         to AS25089 announce ANY
export:         to AS25091 announce ANY
export:         to AS25148 announce ANY
export:         to AS25182 announce ANY
export:         to AS25194 announce ANY
export:         to AS25198 announce ANY
export:         to AS25220 announce ANY
export:         to AS25268 announce ANY
export:         to AS25286 announce ANY
export:         to AS25369 announce ANY
export:         to AS25376 announce ANY
export:         to AS25407 announce ANY
export:         to AS25421 announce ANY
export:         to AS25433 announce ANY
export:         to AS25441 announce ANY
export:         to AS25459 announce ANY
export:         to AS25465 announce ANY
export:         to AS25472 announce ANY
export:         to AS25542 announce ANY
export:         to AS25562 announce ANY
export:         to AS25575 announce ANY
export:         to AS25577 announce ANY
export:         to AS25593 announce ANY
export:         to AS25596 announce ANY
export:         to AS25605 announce ANY
export:         to AS25614 announce ANY
export:         to AS25653 announce ANY
export:         to AS25657 announce ANY
export:         to AS25697 announce ANY
export:         to AS25717 announce ANY
export:         to AS25738 announce ANY
export:         to AS25773 announce ANY
export:         to AS25818 announce ANY
export:         to AS25841 announce ANY
export:         to AS25844 announce ANY
export:         to AS25864 announce ANY
export:         to AS25875 announce ANY
export:         to AS25882 announce ANY
export:         to AS25894 announce ANY
export:         to AS25896 announce ANY
export:         to AS25898 announce ANY
export:         to AS25934 announce ANY
export:         to AS25940 announce ANY
export:         to AS25956 announce ANY
export:         to AS25973 announce ANY
export:         to AS25981 announce ANY
export:         to AS26001 announce ANY
export:         to AS26008 announce ANY
export:         to AS26063 announce ANY
export:         to AS26097 announce ANY
export:         to AS26120 announce ANY
export:         to AS26156 announce ANY
export:         to AS26167 announce ANY
export:         to AS26237 announce ANY
export:         to AS26245 announce ANY
export:         to AS26258 announce ANY
export:         to AS26265 announce ANY
export:         to AS26278 announce ANY
export:         to AS26282 announce ANY
export:         to AS26342 announce ANY
export:         to AS26362 announce ANY
export:         to AS26378 announce ANY
export:         to AS26380 announce ANY
export:         to AS26462 announce ANY
export:         to AS26476 announce ANY
export:         to AS26512 announce ANY
export:         to AS26523 announce ANY
export:         to AS26546 announce ANY
export:         to AS26554 announce ANY
export:         to AS26558 announce ANY
export:         to AS26577 announce ANY
export:         to AS26582 announce ANY
export:         to AS26637 announce ANY
export:         to AS26642 announce ANY
export:         to AS26649 announce ANY
export:         to AS26667 announce ANY
export:         to AS26669 announce ANY
export:         to AS26673 announce ANY
export:         to AS26688 announce ANY
export:         to AS26744 announce ANY
export:         to AS26757 announce ANY
export:         to AS26759 announce ANY
export:         to AS26769 announce ANY
export:         to AS26804 announce ANY
export:         to AS26848 announce ANY
export:         to AS26863 announce ANY
export:         to AS26878 announce ANY
export:         to AS26914 announce ANY
export:         to AS26931 announce ANY
export:         to AS26962 announce ANY
export:         to AS26967 announce ANY
export:         to AS26972 announce ANY
export:         to AS27177 announce ANY
export:         to AS27263 announce ANY
export:         to AS27299 announce ANY
export:         to AS27301 announce ANY
export:         to AS27311 announce ANY
export:         to AS27364 announce ANY
export:         to AS27381 announce ANY
export:         to AS27385 announce ANY
export:         to AS27393 announce ANY
export:         to AS27401 announce ANY
export:         to AS27405 announce ANY
export:         to AS27439 announce ANY
export:         to AS27458 announce ANY
export:         to AS27471 announce ANY
export:         to AS27506 announce ANY
export:         to AS27508 announce ANY
export:         to AS27536 announce ANY
export:         to AS27566 announce ANY
export:         to AS27592 announce ANY
export:         to AS27596 announce ANY
export:         to AS27612 announce ANY
export:         to AS27621 announce ANY
export:         to AS27646 announce ANY
export:         to AS27647 announce ANY
export:         to AS27768 announce ANY
export:         to AS27908 announce ANY
export:         to AS27978 announce ANY
export:         to AS28007 announce ANY
export:         to AS28398 announce ANY
export:         to AS28458 announce ANY
export:         to AS28513 announce ANY
export:         to AS28663 announce ANY
export:         to AS28677 announce ANY
export:         to AS28685 announce ANY
export:         to AS28707 announce ANY
export:         to AS28729 announce ANY
export:         to AS28753 announce ANY
export:         to AS28757 announce ANY
export:         to AS28760 announce ANY
export:         to AS28776 announce ANY
export:         to AS28780 announce ANY
export:         to AS28786 announce ANY
export:         to AS28792 announce ANY
export:         to AS28806 announce ANY
export:         to AS28817 announce ANY
export:         to AS28858 announce ANY
export:         to AS28889 announce ANY
export:         to AS28909 announce ANY
export:         to AS28917 announce ANY
export:         to AS28920 announce ANY
export:         to AS28928 announce ANY
export:         to AS28929 announce ANY
export:         to AS28959 announce ANY
export:         to AS28971 announce ANY
export:         to AS29006 announce ANY
export:         to AS29019 announce ANY
export:         to AS29045 announce ANY
export:         to AS29049 announce ANY
export:         to AS29056 announce ANY
export:         to AS29066 announce ANY
export:         to AS29081 announce ANY
export:         to AS29097 announce ANY
export:         to AS29107 announce ANY
export:         to AS29119 announce ANY
export:         to AS29120 announce ANY
export:         to AS29140 announce ANY
export:         to AS29152 announce ANY
export:         to AS29169 announce ANY
export:         to AS29177 announce ANY
export:         to AS29208 announce ANY
export:         to AS29259 announce ANY
export:         to AS29269 announce ANY
export:         to AS29278 announce ANY
export:         to AS29286 announce ANY
export:         to AS29297 announce ANY
export:         to AS29314 announce ANY
export:         to AS29386 announce ANY
export:         to AS29396 announce ANY
export:         to AS29405 announce ANY
export:         to AS29419 announce ANY
export:         to AS29430 announce ANY
export:         to AS29435 announce ANY
export:         to AS29446 announce ANY
export:         to AS29449 announce ANY
export:         to AS29457 announce ANY
export:         to AS29467 announce ANY
export:         to AS29518 announce ANY
export:         to AS29535 announce ANY
export:         to AS29550 announce ANY
export:         to AS29551 announce ANY
export:         to AS29591 announce ANY
export:         to AS29617 announce ANY
export:         to AS29636 announce ANY
export:         to AS29644 announce ANY
export:         to AS29646 announce ANY
export:         to AS29655 announce ANY
export:         to AS29680 announce ANY
export:         to AS29697 announce ANY
export:         to AS29732 announce ANY
export:         to AS29748 announce ANY
export:         to AS29757 announce ANY
export:         to AS29761 announce ANY
export:         to AS29770 announce ANY
export:         to AS29802 announce ANY
export:         to AS29838 announce ANY
export:         to AS29866 announce ANY
export:         to AS29884 announce ANY
export:         to AS29907 announce ANY
export:         to AS29909 announce ANY
export:         to AS29960 announce ANY
export:         to AS29967 announce ANY
export:         to AS29976 announce ANY
export:         to AS30012 announce ANY
export:         to AS30029 announce ANY
export:         to AS30036 announce ANY
export:         to AS30041 announce ANY
export:         to AS30056 announce ANY
export:         to AS30071 announce ANY
export:         to AS30079 announce ANY
export:         to AS30081 announce ANY
export:         to AS30094 announce ANY
export:         to AS30103 announce ANY
export:         to AS30114 announce ANY
export:         to AS30146 announce ANY
export:         to AS30148 announce ANY
export:         to AS30188 announce ANY
export:         to AS30197 announce ANY
export:         to AS30215 announce ANY
export:         to AS30231 announce ANY
export:         to AS30238 announce ANY
export:         to AS30286 announce ANY
export:         to AS30303 announce ANY
export:         to AS30366 announce ANY
export:         to AS30367 announce ANY
export:         to AS30394 announce ANY
export:         to AS30403 announce ANY
export:         to AS30404 announce ANY
export:         to AS30456 announce ANY
export:         to AS30475 announce ANY
export:         to AS30524 announce ANY
export:         to AS30588 announce ANY
export:         to AS30600 announce ANY
export:         to AS30607 announce ANY
export:         to AS30616 announce ANY
export:         to AS30633 announce ANY
export:         to AS30643 announce ANY
export:         to AS30742 announce ANY
export:         to AS30762 announce ANY
export:         to AS30818 announce ANY
export:         to AS30827 announce ANY
export:         to AS30838 announce ANY
export:         to AS30848 announce ANY
export:         to AS30891 announce ANY
export:         to AS30925 announce ANY
export:         to AS30931 announce ANY
export:         to AS30937 announce ANY
export:         to AS30961 announce ANY
export:         to AS30967 announce ANY
export:         to AS31029 announce ANY
export:         to AS31042 announce ANY
export:         to AS31050 announce ANY
export:         to AS31059 announce ANY
export:         to AS31078 announce ANY
export:         to AS31080 announce ANY
export:         to AS31083 announce ANY
export:         to AS31084 announce ANY
export:         to AS31108 announce ANY
export:         to AS31115 announce ANY
export:         to AS31116 announce ANY
export:         to AS31122 announce ANY
export:         to AS31131 announce ANY
export:         to AS31147 announce ANY
export:         to AS31154 announce ANY
export:         to AS31221 announce ANY
export:         to AS31235 announce ANY
export:         to AS31241 announce ANY
export:         to AS31242 announce ANY
export:         to AS31250 announce ANY
export:         to AS31263 announce ANY
export:         to AS31270 announce ANY
export:         to AS31287 announce ANY
export:         to AS31293 announce ANY
export:         to AS31298 announce ANY
export:         to AS31317 announce ANY
export:         to AS31400 announce ANY
export:         to AS31402 announce ANY
export:         to AS31404 announce ANY
export:         to AS31424 announce ANY
export:         to AS31428 announce ANY
export:         to AS31445 announce ANY
export:         to AS31463 announce ANY
export:         to AS31474 announce ANY
export:         to AS31479 announce ANY
export:         to AS31529 announce ANY
export:         to AS31570 announce ANY
export:         to AS31595 announce ANY
export:         to AS31612 announce ANY
export:         to AS31631 announce ANY
export:         to AS31641 announce ANY
export:         to AS31651 announce ANY
export:         to AS31654 announce ANY
export:         to AS31655 announce ANY
export:         to AS31669 announce ANY
export:         to AS31672 announce ANY
export:         to AS31688 announce ANY
export:         to AS31708 announce ANY
export:         to AS31712 announce ANY
export:         to AS31727 announce ANY
export:         to AS31743 announce ANY
export:         to AS31760 announce ANY
export:         to AS31798 announce ANY
export:         to AS31858 announce ANY
export:         to AS31898 announce ANY
export:         to AS31917 announce ANY
export:         to AS31936 announce ANY
export:         to AS31980 announce ANY
export:         to AS31983 announce ANY
export:         to AS32030 announce ANY
export:         to AS32035 announce ANY
export:         to AS32059 announce ANY
export:         to AS32098 announce ANY
export:         to AS32133 announce ANY
export:         to AS32155 announce ANY
export:         to AS32181 announce ANY
export:         to AS32201 announce ANY
export:         to AS32211 announce ANY
export:         to AS32212 announce ANY
export:         to AS32217 announce ANY
export:         to AS32222 announce ANY
export:         to AS32256 announce ANY
export:         to AS32261 announce ANY
export:         to AS32281 announce ANY
export:         to AS32286 announce ANY
export:         to AS32323 announce ANY
export:         to AS32354 announce ANY
export:         to AS32385 announce ANY
export:         to AS32389 announce ANY
export:         to AS32425 announce ANY
export:         to AS32432 announce ANY
export:         to AS32440 announce ANY
export:         to AS32444 announce ANY
export:         to AS32475 announce ANY
export:         to AS32478 announce ANY
export:         to AS32484 announce ANY
export:         to AS32489 announce ANY
export:         to AS32578 announce ANY
export:         to AS32596 announce ANY
export:         to AS32613 announce ANY
export:         to AS32624 announce ANY
export:         to AS32648 announce ANY
export:         to AS32662 announce ANY
export:         to AS32669 announce ANY
export:         to AS32671 announce ANY
export:         to AS32710 announce ANY
export:         to AS32780 announce ANY
export:         to AS32798 announce ANY
export:         to AS32805 announce ANY
export:         to AS32806 announce ANY
export:         to AS32880 announce ANY
export:         to AS32881 announce ANY
export:         to AS32886 announce ANY
export:         to AS32899 announce ANY
export:         to AS32934 announce ANY
export:         to AS32943 announce ANY
export:         to AS32987 announce ANY
export:         to AS33007 announce ANY
export:         to AS33016 announce ANY
export:         to AS33040 announce ANY
export:         to AS33047 announce ANY
export:         to AS33058 announce ANY
export:         to AS33071 announce ANY
export:         to AS33132 announce ANY
export:         to AS33154 announce ANY
export:         to AS33164 announce ANY
export:         to AS33185 announce ANY
export:         to AS33189 announce ANY
export:         to AS33247 announce ANY
export:         to AS33257 announce ANY
export:         to AS33280 announce ANY
export:         to AS33288 announce ANY
export:         to AS33361 announce ANY
export:         to AS33368 announce ANY
export:         to AS33371 announce ANY
export:         to AS33404 announce ANY
export:         to AS33419 announce ANY
export:         to AS33438 announce ANY
export:         to AS33445 announce ANY
export:         to AS33459 announce ANY
export:         to AS33494 announce ANY
export:         to AS33529 announce ANY
export:         to AS33532 announce ANY
export:         to AS33536 announce ANY
export:         to AS33549 announce ANY
export:         to AS33576 announce ANY
export:         to AS33597 announce ANY
export:         to AS33619 announce ANY
export:         to AS33633 announce ANY
export:         to AS33675 announce ANY
export:         to AS33694 announce ANY
export:         to AS33724 announce ANY
export:         to AS33802 announce ANY
export:         to AS33831 announce ANY
export:         to AS33835 announce ANY
export:         to AS33874 announce ANY
export:         to AS33891 announce ANY
export:         to AS33923 announce ANY
export:         to AS33941 announce ANY
export:         to AS33968 announce ANY
export:         to AS33986 announce ANY
export:         to AS34002 announce ANY
export:         to AS34006 announce ANY
export:         to AS34074 announce ANY
export:         to AS34080 announce ANY
export:         to AS34164 announce ANY
export:         to AS34178 announce ANY
export:         to AS34191 announce ANY
export:         to AS34197 announce ANY
export:         to AS34209 announce ANY
export:         to AS34224 announce ANY
export:         to AS34245 announce ANY
export:         to AS34279 announce ANY
export:         to AS34290 announce ANY
export:         to AS34305 announce ANY
export:         to AS34308 announce ANY
export:         to AS34309 announce ANY
export:         to AS34386 announce ANY
export:         to AS34393 announce ANY
export:         to AS34409 announce ANY
export:         to AS34428 announce ANY
export:         to AS34442 announce ANY
export:         to AS34510 announce ANY
export:         to AS34523 announce ANY
export:         to AS34525 announce ANY
export:         to AS34549 announce ANY
export:         to AS34569 announce ANY
export:         to AS34589 announce ANY
export:         to AS34697 announce ANY
export:         to AS34715 announce ANY
export:         to AS34737 announce ANY
export:         to AS34762 announce ANY
export:         to AS34764 announce ANY
export:         to AS34788 announce ANY
export:         to AS34814 announce ANY
export:         to AS34854 announce ANY
export:         to AS34863 announce ANY
export:         to AS34895 announce ANY
export:         to AS34922 announce ANY
export:         to AS34927 announce ANY
export:         to AS34966 announce ANY
export:         to AS34967 announce ANY
export:         to AS34968 announce ANY
export:         to AS34973 announce ANY
export:         to AS34979 announce ANY
export:         to AS34984 announce ANY
export:         to AS35030 announce ANY
export:         to AS35056 announce ANY
export:         to AS35066 announce ANY
export:         to AS35070 announce ANY
export:         to AS35176 announce ANY
export:         to AS35180 announce ANY
export:         to AS35228 announce ANY
export:         to AS35259 announce ANY
export:         to AS35266 announce ANY
export:         to AS35289 announce ANY
export:         to AS35311 announce ANY
export:         to AS35313 announce ANY
export:         to AS35315 announce ANY
export:         to AS35327 announce ANY
export:         to AS35370 announce ANY
export:         to AS35421 announce ANY
export:         to AS35426 announce ANY
export:         to AS35444 announce ANY
export:         to AS35461 announce ANY
export:         to AS35491 announce ANY
export:         to AS35522 announce ANY
export:         to AS35548 announce ANY
export:         to AS35574 announce ANY
export:         to AS35593 announce ANY
export:         to AS35643 announce ANY
export:         to AS35679 announce ANY
export:         to AS35695 announce ANY
export:         to AS35699 announce ANY
export:         to AS35745 announce ANY
export:         to AS35760 announce ANY
export:         to AS35787 announce ANY
export:         to AS35825 announce ANY
export:         to AS35834 announce ANY
export:         to AS35838 announce ANY
export:         to AS35872 announce ANY
export:         to AS35890 announce ANY
export:         to AS35906 announce ANY
export:         to AS35908 announce ANY
export:         to AS35928 announce ANY
export:         to AS35953 announce ANY
export:         to AS35974 announce ANY
export:         to AS35975 announce ANY
export:         to AS35985 announce ANY
export:         to AS35993 announce ANY
export:         to AS35994 announce ANY
export:         to AS36007 announce ANY
export:         to AS36040 announce ANY
export:         to AS36062 announce ANY
export:         to AS36073 announce ANY
export:         to AS36077 announce ANY
export:         to AS36086 announce ANY
export:         to AS36103 announce ANY
export:         to AS36184 announce ANY
export:         to AS36187 announce ANY
export:         to AS36224 announce ANY
export:         to AS36236 announce ANY
export:         to AS36243 announce ANY
export:         to AS36306 announce ANY
export:         to AS36352 announce ANY
export:         to AS36385 announce ANY
export:         to AS36399 announce ANY
export:         to AS36408 announce ANY
export:         to AS36444 announce ANY
export:         to AS36459 announce ANY
export:         to AS36473 announce ANY
export:         to AS36483 announce ANY
export:         to AS36493 announce ANY
export:         to AS36589 announce ANY
export:         to AS36613 announce ANY
export:         to AS36614 announce ANY
export:         to AS36657 announce ANY
export:         to AS36671 announce ANY
export:         to AS36692 announce ANY
export:         to AS36734 announce ANY
export:         to AS36776 announce ANY
export:         to AS36853 announce ANY
export:         to AS36884 announce ANY
export:         to AS37100 announce ANY
export:         to AS37271 announce ANY
export:         to AS37468 announce ANY
export:         to AS37518 announce ANY
export:         to AS37721 announce ANY
export:         to AS37958 announce ANY
export:         to AS38082 announce ANY
export:         to AS38880 announce ANY
export:         to AS38915 announce ANY
export:         to AS38930 announce ANY
export:         to AS38949 announce ANY
export:         to AS38963 announce ANY
export:         to AS38966 announce ANY
export:         to AS38983 announce ANY
export:         to AS39063 announce ANY
export:         to AS39090 announce ANY
export:         to AS39116 announce ANY
export:         to AS39120 announce ANY
export:         to AS39175 announce ANY
export:         to AS39179 announce ANY
export:         to AS39180 announce ANY
export:         to AS39233 announce ANY
export:         to AS39234 announce ANY
export:         to AS39251 announce ANY
export:         to AS39271 announce ANY
export:         to AS39343 announce ANY
export:         to AS39372 announce ANY
export:         to AS39392 announce ANY
export:         to AS39447 announce ANY
export:         to AS39449 announce ANY
export:         to AS39474 announce ANY
export:         to AS39477 announce ANY
export:         to AS39498 announce ANY
export:         to AS39505 announce ANY
export:         to AS39506 announce ANY
export:         to AS39512 announce ANY
export:         to AS39526 announce ANY
export:         to AS39545 announce ANY
export:         to AS39560 announce ANY
export:         to AS39572 announce ANY
export:         to AS39584 announce ANY
export:         to AS39591 announce ANY
export:         to AS39636 announce ANY
export:         to AS39637 announce ANY
export:         to AS39648 announce ANY
export:         to AS39686 announce ANY
export:         to AS39704 announce ANY
export:         to AS39729 announce ANY
export:         to AS39766 announce ANY
export:         to AS39781 announce ANY
export:         to AS39816 announce ANY
export:         to AS39822 announce ANY
export:         to AS39829 announce ANY
export:         to AS39832 announce ANY
export:         to AS39852 announce ANY
export:         to AS39855 announce ANY
export:         to AS39878 announce ANY
export:         to AS39884 announce ANY
export:         to AS39892 announce ANY
export:         to AS39912 announce ANY
export:         to AS39923 announce ANY
export:         to AS39964 announce ANY
export:         to AS40028 announce ANY
export:         to AS40029 announce ANY
export:         to AS40065 announce ANY
export:         to AS40089 announce ANY
export:         to AS40123 announce ANY
export:         to AS40136 announce ANY
export:         to AS40160 announce ANY
export:         to AS40165 announce ANY
export:         to AS40167 announce ANY
export:         to AS40193 announce ANY
export:         to AS40224 announce ANY
export:         to AS40317 announce ANY
export:         to AS40350 announce ANY
export:         to AS40401 announce ANY
export:         to AS40402 announce ANY
export:         to AS40418 announce ANY
export:         to AS40430 announce ANY
export:         to AS40446 announce ANY
export:         to AS40467 announce ANY
export:         to AS40490 announce ANY
export:         to AS40491 announce ANY
export:         to AS40521 announce ANY
export:         to AS40523 announce ANY
export:         to AS40528 announce ANY
export:         to AS40578 announce ANY
export:         to AS40581 announce ANY
export:         to AS40584 announce ANY
export:         to AS40624 announce ANY
export:         to AS40657 announce ANY
export:         to AS40669 announce ANY
export:         to AS40676 announce ANY
export:         to AS40729 announce ANY
export:         to AS40731 announce ANY
export:         to AS40739 announce ANY
export:         to AS40763 announce ANY
export:         to AS40769 announce ANY
export:         to AS40788 announce ANY
export:         to AS40841 announce ANY
export:         to AS40844 announce ANY
export:         to AS40858 announce ANY
export:         to AS40885 announce ANY
export:         to AS40889 announce ANY
export:         to AS40922 announce ANY
export:         to AS40926 announce ANY
export:         to AS40934 announce ANY
export:         to AS40988 announce ANY
export:         to AS41041 announce ANY
export:         to AS41057 announce ANY
export:         to AS41073 announce ANY
export:         to AS41135 announce ANY
export:         to AS41146 announce ANY
export:         to AS41157 announce ANY
export:         to AS41160 announce ANY
export:         to AS41204 announce ANY
export:         to AS41230 announce ANY
export:         to AS41265 announce ANY
export:         to AS41291 announce ANY
export:         to AS41313 announce ANY
export:         to AS41319 announce ANY
export:         to AS41327 announce ANY
export:         to AS41354 announce ANY
export:         to AS41357 announce ANY
export:         to AS41364 announce ANY
export:         to AS41410 announce ANY
export:         to AS41415 announce ANY
export:         to AS41435 announce ANY
export:         to AS41436 announce ANY
export:         to AS41477 announce ANY
export:         to AS41488 announce ANY
export:         to AS41495 announce ANY
export:         to AS41497 announce ANY
export:         to AS41508 announce ANY
export:         to AS41511 announce ANY
export:         to AS41538 announce ANY
export:         to AS41549 announce ANY
export:         to AS41564 announce ANY
export:         to AS41653 announce ANY
export:         to AS41764 announce ANY
export:         to AS41765 announce ANY
export:         to AS41803 announce ANY
export:         to AS41883 announce ANY
export:         to AS41887 announce ANY
export:         to AS41931 announce ANY
export:         to AS41935 announce ANY
export:         to AS41945 announce ANY
export:         to AS41960 announce ANY
export:         to AS41966 announce ANY
export:         to AS42004 announce ANY
export:         to AS42005 announce ANY
export:         to AS42013 announce ANY
export:         to AS42040 announce ANY
export:         to AS42044 announce ANY
export:         to AS42128 announce ANY
export:         to AS42172 announce ANY
export:         to AS42176 announce ANY
export:         to AS42177 announce ANY
export:         to AS42184 announce ANY
export:         to AS42211 announce ANY
export:         to AS42213 announce ANY
export:         to AS42229 announce ANY
export:         to AS42266 announce ANY
export:         to AS42293 announce ANY
export:         to AS42344 announce ANY
export:         to AS42366 announce ANY
export:         to AS42385 announce ANY
export:         to AS42392 announce ANY
export:         to AS42401 announce ANY
export:         to AS42416 announce ANY
export:         to AS42459 announce ANY
export:         to AS42463 announce ANY
export:         to AS42466 announce ANY
export:         to AS42467 announce ANY
export:         to AS42475 announce ANY
export:         to AS42479 announce ANY
export:         to AS42555 announce ANY
export:         to AS42607 announce ANY
export:         to AS42612 announce ANY
export:         to AS42624 announce ANY
export:         to AS42633 announce ANY
export:         to AS42643 announce ANY
export:         to AS42673 announce ANY
export:         to AS42689 announce ANY
export:         to AS42804 announce ANY
export:         to AS42808 announce ANY
export:         to AS42816 announce ANY
export:         to AS42830 announce ANY
export:         to AS42831 announce ANY
export:         to AS42836 announce ANY
export:         to AS42845 announce ANY
export:         to AS42880 announce ANY
export:         to AS42912 announce ANY
export:         to AS42927 announce ANY
export:         to AS42944 announce ANY
export:         to AS42989 announce ANY
export:         to AS43074 announce ANY
export:         to AS43142 announce ANY
export:         to AS43187 announce ANY
export:         to AS43205 announce ANY
export:         to AS43251 announce ANY
export:         to AS43266 announce ANY
export:         to AS43289 announce ANY
export:         to AS43311 announce ANY
export:         to AS43338 announce ANY
export:         to AS43372 announce ANY
export:         to AS43406 announce ANY
export:         to AS43437 announce ANY
export:         to AS43438 announce ANY
export:         to AS43440 announce ANY
export:         to AS43494 announce ANY
export:         to AS43515 announce ANY
export:         to AS43519 announce ANY
export:         to AS43520 announce ANY
export:         to AS43534 announce ANY
export:         to AS43545 announce ANY
export:         to AS43578 announce ANY
export:         to AS43599 announce ANY
export:         to AS43639 announce ANY
export:         to AS43641 announce ANY
export:         to AS43829 announce ANY
export:         to AS43843 announce ANY
export:         to AS43848 announce ANY
export:         to AS43872 announce ANY
export:         to AS43885 announce ANY
export:         to AS43894 announce ANY
export:         to AS43898 announce ANY
export:         to AS43915 announce ANY
export:         to AS43935 announce ANY
export:         to AS43984 announce ANY
export:         to AS44062 announce ANY
export:         to AS44066 announce ANY
export:         to AS44086 announce ANY
export:         to AS44124 announce ANY
export:         to AS44134 announce ANY
export:         to AS44150 announce ANY
export:         to AS44166 announce ANY
export:         to AS44212 announce ANY
export:         to AS44217 announce ANY
export:         to AS44226 announce ANY
export:         to AS44227 announce ANY
export:         to AS44356 announce ANY
export:         to AS44384 announce ANY
export:         to AS44411 announce ANY
export:         to AS44426 announce ANY
export:         to AS44431 announce ANY
export:         to AS44444 announce ANY
export:         to AS44451 announce ANY
export:         to AS44454 announce ANY
export:         to AS44473 announce ANY
export:         to AS44521 announce ANY
export:         to AS44600 announce ANY
export:         to AS44608 announce ANY
export:         to AS44765 announce ANY
export:         to AS44776 announce ANY
export:         to AS44784 announce ANY
export:         to AS44786 announce ANY
export:         to AS44788 announce ANY
export:         to AS44806 announce ANY
export:         to AS44814 announce ANY
export:         to AS44815 announce ANY
export:         to AS44829 announce ANY
export:         to AS44898 announce ANY
export:         to AS44901 announce ANY
export:         to AS44926 announce ANY
export:         to AS44942 announce ANY
export:         to AS44946 announce ANY
export:         to AS44965 announce ANY
export:         to AS44976 announce ANY
export:         to AS45187 announce ANY
export:         to AS45217 announce ANY
export:         to AS45474 announce ANY
export:         to AS45499 announce ANY
export:         to AS45530 announce ANY
export:         to AS45629 announce ANY
export:         to AS45630 announce ANY
export:         to AS45758 announce ANY
export:         to AS45896 announce ANY
export:         to AS45899 announce ANY
export:         to AS46130 announce ANY
export:         to AS46160 announce ANY
export:         to AS46168 announce ANY
export:         to AS46199 announce ANY
export:         to AS46261 announce ANY
export:         to AS46272 announce ANY
export:         to AS46281 announce ANY
export:         to AS46340 announce ANY
export:         to AS46363 announce ANY
export:         to AS46371 announce ANY
export:         to AS46375 announce ANY
export:         to AS46379 announce ANY
export:         to AS46395 announce ANY
export:         to AS46401 announce ANY
export:         to AS46454 announce ANY
export:         to AS46455 announce ANY
export:         to AS46475 announce ANY
export:         to AS46489 announce ANY
export:         to AS46556 announce ANY
export:         to AS46558 announce ANY
export:         to AS46559 announce ANY
export:         to AS46562 announce ANY
export:         to AS46573 announce ANY
export:         to AS46609 announce ANY
export:         to AS46621 announce ANY
export:         to AS46632 announce ANY
export:         to AS46635 announce ANY
export:         to AS46664 announce ANY
export:         to AS46687 announce ANY
export:         to AS46711 announce ANY
export:         to AS46762 announce ANY
export:         to AS46805 announce ANY
export:         to AS46844 announce ANY
export:         to AS46847 announce ANY
export:         to AS46852 announce ANY
export:         to AS46865 announce ANY
export:         to AS46887 announce ANY
export:         to AS46889 announce ANY
export:         to AS46922 announce ANY
export:         to AS46931 announce ANY
export:         to AS46956 announce ANY
export:         to AS46994 announce ANY
export:         to AS47099 announce ANY
export:         to AS47167 announce ANY
export:         to AS47169 announce ANY
export:         to AS47195 announce ANY
export:         to AS47232 announce ANY
export:         to AS47242 announce ANY
export:         to AS47292 announce ANY
export:         to AS47381 announce ANY
export:         to AS47443 announce ANY
export:         to AS47494 announce ANY
export:         to AS47532 announce ANY
export:         to AS47544 announce ANY
export:         to AS47572 announce ANY
export:         to AS47674 announce ANY
export:         to AS47680 announce ANY
export:         to AS47720 announce ANY
export:         to AS47754 announce ANY
export:         to AS47762 announce ANY
export:         to AS47771 announce ANY
export:         to AS47787 announce ANY
export:         to AS47793 announce ANY
export:         to AS47836 announce ANY
export:         to AS47850 announce ANY
export:         to AS47866 announce ANY
export:         to AS47872 announce ANY
export:         to AS47874 announce ANY
export:         to AS47886 announce ANY
export:         to AS47887 announce ANY
export:         to AS47892 announce ANY
export:         to AS47927 announce ANY
export:         to AS47946 announce ANY
export:         to AS47950 announce ANY
export:         to AS47956 announce ANY
export:         to AS47961 announce ANY
export:         to AS47969 announce ANY
export:         to AS47973 announce ANY
export:         to AS48006 announce ANY
export:         to AS48083 announce ANY
export:         to AS48119 announce ANY
export:         to AS48134 announce ANY
export:         to AS48135 announce ANY
export:         to AS48137 announce ANY
export:         to AS48152 announce ANY
export:         to AS48237 announce ANY
export:         to AS48305 announce ANY
export:         to AS48339 announce ANY
export:         to AS48345 announce ANY
export:         to AS48348 announce ANY
export:         to AS48374 announce ANY
export:         to AS48426 announce ANY
export:         to AS48447 announce ANY
export:         to AS48452 announce ANY
export:         to AS48468 announce ANY
export:         to AS48493 announce ANY
export:         to AS48505 announce ANY
export:         to AS48544 announce ANY
export:         to AS48545 announce ANY
export:         to AS48559 announce ANY
export:         to AS48582 announce ANY
export:         to AS48635 announce ANY
export:         to AS48638 announce ANY
export:         to AS48659 announce ANY
export:         to AS48804 announce ANY
export:         to AS48809 announce ANY
export:         to AS48832 announce ANY
export:         to AS48846 announce ANY
export:         to AS48849 announce ANY
export:         to AS48850 announce ANY
export:         to AS48851 announce ANY
export:         to AS48896 announce ANY
export:         to AS48910 announce ANY
export:         to AS48918 announce ANY
export:         to AS48950 announce ANY
export:         to AS48957 announce ANY
export:         to AS48961 announce ANY
export:         to AS48967 announce ANY
export:         to AS48968 announce ANY
export:         to AS49088 announce ANY
export:         to AS49102 announce ANY
export:         to AS49158 announce ANY
export:         to AS49216 announce ANY
export:         to AS49220 announce ANY
export:         to AS49229 announce ANY
export:         to AS49233 announce ANY
export:         to AS49289 announce ANY
export:         to AS49296 announce ANY
export:         to AS49375 announce ANY
export:         to AS49405 announce ANY
export:         to AS49415 announce ANY
export:         to AS49425 announce ANY
export:         to AS49434 announce ANY
export:         to AS49493 announce ANY
export:         to AS49515 announce ANY
export:         to AS49524 announce ANY
export:         to AS49567 announce ANY
export:         to AS49600 announce ANY
export:         to AS49605 announce ANY
export:         to AS49607 announce ANY
export:         to AS49650 announce ANY
export:         to AS49677 announce ANY
export:         to AS49683 announce ANY
export:         to AS49699 announce ANY
export:         to AS49709 announce ANY
export:         to AS49744 announce ANY
export:         to AS49761 announce ANY
export:         to AS49765 announce ANY
export:         to AS49785 announce ANY
export:         to AS49823 announce ANY
export:         to AS49838 announce ANY
export:         to AS49849 announce ANY
export:         to AS49870 announce ANY
export:         to AS49915 announce ANY
export:         to AS49958 announce ANY
export:         to AS50020 announce ANY
export:         to AS50121 announce ANY
export:         to AS50153 announce ANY
export:         to AS50173 announce ANY
export:         to AS50183 announce ANY
export:         to AS50185 announce ANY
export:         to AS50188 announce ANY
export:         to AS50202 announce ANY
export:         to AS50226 announce ANY
export:         to AS50245 announce ANY
export:         to AS50287 announce ANY
export:         to AS50292 announce ANY
export:         to AS50300 announce ANY
export:         to AS50314 announce ANY
export:         to AS50326 announce ANY
export:         to AS50331 announce ANY
export:         to AS50343 announce ANY
export:         to AS50360 announce ANY
export:         to AS50411 announce ANY
export:         to AS50429 announce ANY
export:         to AS50463 announce ANY
export:         to AS50469 announce ANY
export:         to AS50550 announce ANY
export:         to AS50581 announce ANY
export:         to AS50584 announce ANY
export:         to AS50597 announce ANY
export:         to AS50607 announce ANY
export:         to AS50625 announce ANY
export:         to AS50835 announce ANY
export:         to AS50877 announce ANY
export:         to AS50889 announce ANY
export:         to AS50965 announce ANY
export:         to AS50974 announce ANY
export:         to AS50994 announce ANY
export:         to AS51043 announce ANY
export:         to AS51060 announce ANY
export:         to AS51068 announce ANY
export:         to AS51088 announce ANY
export:         to AS51269 announce ANY
export:         to AS51270 announce ANY
export:         to AS51294 announce ANY
export:         to AS51303 announce ANY
export:         to AS51310 announce ANY
export:         to AS51337 announce ANY
export:         to AS51390 announce ANY
export:         to AS51394 announce ANY
export:         to AS51395 announce ANY
export:         to AS51399 announce ANY
export:         to AS51406 announce ANY
export:         to AS51407 announce ANY
export:         to AS51483 announce ANY
export:         to AS51510 announce ANY
export:         to AS51553 announce ANY
export:         to AS51580 announce ANY
export:         to AS51582 announce ANY
export:         to AS51606 announce ANY
export:         to AS51616 announce ANY
export:         to AS51664 announce ANY
export:         to AS51677 announce ANY
export:         to AS51752 announce ANY
export:         to AS51761 announce ANY
export:         to AS51796 announce ANY
export:         to AS51809 announce ANY
export:         to AS51820 announce ANY
export:         to AS51823 announce ANY
export:         to AS51852 announce ANY
export:         to AS51857 announce ANY
export:         to AS51863 announce ANY
export:         to AS51871 announce ANY
export:         to AS51890 announce ANY
export:         to AS51934 announce ANY
export:         to AS51944 announce ANY
export:         to AS51960 announce ANY
export:         to AS51984 announce ANY
export:         to AS52030 announce ANY
export:         to AS52101 announce ANY
export:         to AS52106 announce ANY
export:         to AS52183 announce ANY
export:         to AS52320 announce ANY
export:         to AS52347 announce ANY
export:         to AS52393 announce ANY
export:         to AS52438 announce ANY
export:         to AS52580 announce ANY
export:         to AS52873 announce ANY
export:         to AS53258 announce ANY
export:         to AS53264 announce ANY
export:         to AS53292 announce ANY
export:         to AS53316 announce ANY
export:         to AS53321 announce ANY
export:         to AS53340 announce ANY
export:         to AS53342 announce ANY
export:         to AS53345 announce ANY
export:         to AS53346 announce ANY
export:         to AS53362 announce ANY
export:         to AS53369 announce ANY
export:         to AS53388 announce ANY
export:         to AS53398 announce ANY
export:         to AS53400 announce ANY
export:         to AS53428 announce ANY
export:         to AS53440 announce ANY
export:         to AS53464 announce ANY
export:         to AS53483 announce ANY
export:         to AS53487 announce ANY
export:         to AS53502 announce ANY
export:         to AS53521 announce ANY
export:         to AS53560 announce ANY
export:         to AS53582 announce ANY
export:         to AS53620 announce ANY
export:         to AS53639 announce ANY
export:         to AS53640 announce ANY
export:         to AS53667 announce ANY
export:         to AS53699 announce ANY
export:         to AS53722 announce ANY
export:         to AS53723 announce ANY
export:         to AS53726 announce ANY
export:         to AS53764 announce ANY
export:         to AS53766 announce ANY
export:         to AS53813 announce ANY
export:         to AS53828 announce ANY
export:         to AS53831 announce ANY
export:         to AS53845 announce ANY
export:         to AS53850 announce ANY
export:         to AS53856 announce ANY
export:         to AS53889 announce ANY
export:         to AS53902 announce ANY
export:         to AS53913 announce ANY
export:         to AS53914 announce ANY
export:         to AS53939 announce ANY
export:         to AS53973 announce ANY
export:         to AS54036 announce ANY
export:         to AS54040 announce ANY
export:         to AS54092 announce ANY
export:         to AS54103 announce ANY
export:         to AS54107 announce ANY
export:         to AS54119 announce ANY
export:         to AS54125 announce ANY
export:         to AS54128 announce ANY
export:         to AS54197 announce ANY
export:         to AS54201 announce ANY
export:         to AS54235 announce ANY
export:         to AS54247 announce ANY
export:         to AS54293 announce ANY
export:         to AS54301 announce ANY
export:         to AS54303 announce ANY
export:         to AS54312 announce ANY
export:         to AS54329 announce ANY
export:         to AS54359 announce ANY
export:         to AS54455 announce ANY
export:         to AS54460 announce ANY
export:         to AS54483 announce ANY
export:         to AS54489 announce ANY
export:         to AS54498 announce ANY
export:         to AS54509 announce ANY
export:         to AS54527 announce ANY
export:         to AS54531 announce ANY
export:         to AS54535 announce ANY
export:         to AS54588 announce ANY
export:         to AS54593 announce ANY
export:         to AS54600 announce ANY
export:         to AS54618 announce ANY
export:         to AS54624 announce ANY
export:         to AS54641 announce ANY
export:         to AS54652 announce ANY
export:         to AS54706 announce ANY
export:         to AS54717 announce ANY
export:         to AS54778 announce ANY
export:         to AS54816 announce ANY
export:         to AS54825 announce ANY
export:         to AS54913 announce ANY
export:         to AS54934 announce ANY
export:         to AS54957 announce ANY
export:         to AS54963 announce ANY
export:         to AS54994 announce ANY
export:         to AS55002 announce ANY
export:         to AS55011 announce ANY
export:         to AS55061 announce ANY
export:         to AS55081 announce ANY
export:         to AS55129 announce ANY
export:         to AS55191 announce ANY
export:         to AS55256 announce ANY
export:         to AS55259 announce ANY
export:         to AS55786 announce ANY
export:         to AS55891 announce ANY
export:         to AS55943 announce ANY
export:         to AS56286 announce ANY
export:         to AS56320 announce ANY
export:         to AS56381 announce ANY
export:         to AS56474 announce ANY
export:         to AS56478 announce ANY
export:         to AS56504 announce ANY
export:         to AS56511 announce ANY
export:         to AS56515 announce ANY
export:         to AS56575 announce ANY
export:         to AS56595 announce ANY
export:         to AS56611 announce ANY
export:         to AS56630 announce ANY
export:         to AS56647 announce ANY
export:         to AS56655 announce ANY
export:         to AS56675 announce ANY
export:         to AS56683 announce ANY
export:         to AS56767 announce ANY
export:         to AS56773 announce ANY
export:         to AS56778 announce ANY
export:         to AS56786 announce ANY
export:         to AS56894 announce ANY
export:         to AS56953 announce ANY
export:         to AS56958 announce ANY
export:         to AS56990 announce ANY
export:         to AS57111 announce ANY
export:         to AS57141 announce ANY
export:         to AS57169 announce ANY
export:         to AS57263 announce ANY
export:         to AS57276 announce ANY
export:         to AS57286 announce ANY
export:         to AS57332 announce ANY
export:         to AS57344 announce ANY
export:         to AS57476 announce ANY
export:         to AS57478 announce ANY
export:         to AS57480 announce ANY
export:         to AS57546 announce ANY
export:         to AS57607 announce ANY
export:         to AS57626 announce ANY
export:         to AS57704 announce ANY
export:         to AS57717 announce ANY
export:         to AS57723 announce ANY
export:         to AS57750 announce ANY
export:         to AS57795 announce ANY
export:         to AS57811 announce ANY
export:         to AS57846 announce ANY
export:         to AS57877 announce ANY
export:         to AS57896 announce ANY
export:         to AS57976 announce ANY
export:         to AS57987 announce ANY
export:         to AS58065 announce ANY
export:         to AS58082 announce ANY
export:         to AS58131 announce ANY
export:         to AS58246 announce ANY
export:         to AS58307 announce ANY
export:         to AS58321 announce ANY
export:         to AS58453 announce ANY
export:         to AS58511 announce ANY
export:         to AS58664 announce ANY
export:         to AS59028 announce ANY
export:         to AS59253 announce ANY
export:         to AS59371 announce ANY
export:         to AS59432 announce ANY
export:         to AS59455 announce ANY
export:         to AS59492 announce ANY
export:         to AS59524 announce ANY
export:         to AS59545 announce ANY
export:         to AS59580 announce ANY
export:         to AS59582 announce ANY
export:         to AS59605 announce ANY
export:         to AS59611 announce ANY
export:         to AS59655 announce ANY
export:         to AS59711 announce ANY
export:         to AS59816 announce ANY
export:         to AS59827 announce ANY
export:         to AS59842 announce ANY
export:         to AS59865 announce ANY
export:         to AS59874 announce ANY
export:         to AS59933 announce ANY
export:         to AS59950 announce ANY
export:         to AS60015 announce ANY
export:         to AS60022 announce ANY
export:         to AS60038 announce ANY
export:         to AS60068 announce ANY
export:         to AS60144 announce ANY
export:         to AS60191 announce ANY
export:         to AS60193 announce ANY
export:         to AS60219 announce ANY
export:         to AS60277 announce ANY
export:         to AS60339 announce ANY
export:         to AS60362 announce ANY
export:         to AS60384 announce ANY
export:         to AS60436 announce ANY
export:         to AS60447 announce ANY
export:         to AS60475 announce ANY
export:         to AS60481 announce ANY
export:         to AS60486 announce ANY
export:         to AS60497 announce ANY
export:         to AS60501 announce ANY
export:         to AS60624 announce ANY
export:         to AS60636 announce ANY
export:         to AS60669 announce ANY
export:         to AS60670 announce ANY
export:         to AS60706 announce ANY
export:         to AS60736 announce ANY
export:         to AS60750 announce ANY
export:         to AS60752 announce ANY
export:         to AS60758 announce ANY
export:         to AS60781 announce ANY
export:         to AS60798 announce ANY
export:         to AS60800 announce ANY
export:         to AS60822 announce ANY
export:         to AS60893 announce ANY
export:         to AS60923 announce ANY
export:         to AS60940 announce ANY
export:         to AS61003 announce ANY
export:         to AS61018 announce ANY
export:         to AS61046 announce ANY
export:         to AS61049 announce ANY
export:         to AS61149 announce ANY
export:         to AS61154 announce ANY
export:         to AS61181 announce ANY
export:         to AS61215 announce ANY
export:         to AS61234 announce ANY
export:         to AS61244 announce ANY
export:         to AS61266 announce ANY
export:         to AS61273 announce ANY
export:         to AS61315 announce ANY
export:         to AS61317 announce ANY
export:         to AS61323 announce ANY
export:         to AS61349 announce ANY
export:         to AS61373 announce ANY
export:         to AS61429 announce ANY
export:         to AS61430 announce ANY
export:         to AS61461 announce ANY
export:         to AS61573 announce ANY
export:         to AS62001 announce ANY
export:         to AS62021 announce ANY
export:         to AS62044 announce ANY
export:         to AS62068 announce ANY
export:         to AS62081 announce ANY
export:         to AS62087 announce ANY
export:         to AS62112 announce ANY
export:         to AS62129 announce ANY
export:         to AS62134 announce ANY
export:         to AS62167 announce ANY
export:         to AS62168 announce ANY
export:         to AS62184 announce ANY
export:         to AS62190 announce ANY
export:         to AS62234 announce ANY
export:         to AS62240 announce ANY
export:         to AS62244 announce ANY
export:         to AS62363 announce ANY
export:         to AS62488 announce ANY
export:         to AS62490 announce ANY
export:         to AS62519 announce ANY
export:         to AS62523 announce ANY
export:         to AS62542 announce ANY
export:         to AS62563 announce ANY
export:         to AS62594 announce ANY
export:         to AS62597 announce ANY
export:         to AS62638 announce ANY
export:         to AS62646 announce ANY
export:         to AS62648 announce ANY
export:         to AS62664 announce ANY
export:         to AS62665 announce ANY
export:         to AS62668 announce ANY
export:         to AS62698 announce ANY
export:         to AS62703 announce ANY
export:         to AS62710 announce ANY
export:         to AS62713 announce ANY
export:         to AS62728 announce ANY
export:         to AS62738 announce ANY
export:         to AS62746 announce ANY
export:         to AS62769 announce ANY
export:         to AS62780 announce ANY
export:         to AS62784 announce ANY
export:         to AS62798 announce ANY
export:         to AS62799 announce ANY
export:         to AS62804 announce ANY
export:         to AS62833 announce ANY
export:         to AS62834 announce ANY
export:         to AS62874 announce ANY
export:         to AS62887 announce ANY
export:         to AS62905 announce ANY
export:         to AS62918 announce ANY
export:         to AS62955 announce ANY
export:         to AS62982 announce ANY
export:         to AS63008 announce ANY
export:         to AS63023 announce ANY
export:         to AS63086 announce ANY
export:         to AS63103 announce ANY
export:         to AS63110 announce ANY
export:         to AS63120 announce ANY
export:         to AS63140 announce ANY
export:         to AS63157 announce ANY
export:         to AS63199 announce ANY
export:         to AS63213 announce ANY
export:         to AS63226 announce ANY
export:         to AS63267 announce ANY
export:         to AS63287 announce ANY
export:         to AS63300 announce ANY
export:         to AS63311 announce ANY
export:         to AS63351 announce ANY
export:         to AS63365 announce ANY
export:         to AS63382 announce ANY
export:         to AS63383 announce ANY
export:         to AS63395 announce ANY
export:         to AS63399 announce ANY
export:         to AS63402 announce ANY
export:         to AS63428 announce ANY
export:         to AS63452 announce ANY
export:         to AS63454 announce ANY
export:         to AS63471 announce ANY
export:         to AS63476 announce ANY
export:         to AS63916 announce ANY
export:         to AS63949 announce ANY
export:         to AS64000 announce ANY
export:         to AS64022 announce ANY
export:         to AS64096 announce ANY
export:         to AS64122 announce ANY
export:         to AS64240 announce ANY
export:         to AS64266 announce ANY
export:         to AS64275 announce ANY
export:         to AS64277 announce ANY
export:         to AS64294 announce ANY
export:         to AS64304 announce ANY
export:         to AS64426 announce ANY
export:         to AS64485 announce ANY
export:         to AS65538 announce ANY
export:         to AS65540 announce ANY
export:         to AS65542 announce ANY
export:         to AS131189 announce ANY
export:         to AS131274 announce ANY
export:         to AS131314 announce ANY
export:         to AS132057 announce ANY
export:         to AS132168 announce ANY
export:         to AS133012 announce ANY
export:         to AS133335 announce ANY
export:         to AS133486 announce ANY
export:         to AS133752 announce ANY
export:         to AS133936 announce ANY
export:         to AS133942 announce ANY
export:         to AS134345 announce ANY
export:         to AS134351 announce ANY
export:         to AS134406 announce ANY
export:         to AS135354 announce ANY
export:         to AS135356 announce ANY
export:         to AS135391 announce ANY
export:         to AS135530 announce ANY
export:         to AS135607 announce ANY
export:         to AS136455 announce ANY
export:         to AS136897 announce ANY
export:         to AS137753 announce ANY
export:         to AS137816 announce ANY
export:         to AS137819 announce ANY
export:         to AS137912 announce ANY
export:         to AS138005 announce ANY
export:         to AS138576 announce ANY
export:         to AS138611 announce ANY
export:         to AS139062 announce ANY
export:         to AS141039 announce ANY
export:         to AS141235 announce ANY
export:         to AS142111 announce ANY
export:         to AS142268 announce ANY
export:         to AS142578 announce ANY
export:         to AS147049 announce ANY
export:         to AS196640 announce ANY
export:         to AS196670 announce ANY
export:         to AS196681 announce ANY
export:         to AS196729 announce ANY
export:         to AS196755 announce ANY
export:         to AS196933 announce ANY
export:         to AS196956 announce ANY
export:         to AS196975 announce ANY
export:         to AS196983 announce ANY
export:         to AS196987 announce ANY
export:         to AS196998 announce ANY
export:         to AS197009 announce ANY
export:         to AS197036 announce ANY
export:         to AS197071 announce ANY
export:         to AS197075 announce ANY
export:         to AS197106 announce ANY
export:         to AS197116 announce ANY
export:         to AS197156 announce ANY
export:         to AS197181 announce ANY
export:         to AS197206 announce ANY
export:         to AS197226 announce ANY
export:         to AS197262 announce ANY
export:         to AS197264 announce ANY
export:         to AS197308 announce ANY
export:         to AS197355 announce ANY
export:         to AS197429 announce ANY
export:         to AS197437 announce ANY
export:         to AS197447 announce ANY
export:         to AS197479 announce ANY
export:         to AS197518 announce ANY
export:         to AS197549 announce ANY
export:         to AS197572 announce ANY
export:         to AS197573 announce ANY
export:         to AS197592 announce ANY
export:         to AS197610 announce ANY
export:         to AS197651 announce ANY
export:         to AS197664 announce ANY
export:         to AS197667 announce ANY
export:         to AS197669 announce ANY
export:         to AS197690 announce ANY
export:         to AS197711 announce ANY
export:         to AS197712 announce ANY
export:         to AS197727 announce ANY
export:         to AS197809 announce ANY
export:         to AS197880 announce ANY
export:         to AS197883 announce ANY
export:         to AS197902 announce ANY
export:         to AS197985 announce ANY
export:         to AS198040 announce ANY
export:         to AS198045 announce ANY
export:         to AS198085 announce ANY
export:         to AS198187 announce ANY
export:         to AS198193 announce ANY
export:         to AS198203 announce ANY
export:         to AS198211 announce ANY
export:         to AS198216 announce ANY
export:         to AS198260 announce ANY
export:         to AS198279 announce ANY
export:         to AS198301 announce ANY
export:         to AS198330 announce ANY
export:         to AS198334 announce ANY
export:         to AS198374 announce ANY
export:         to AS198386 announce ANY
export:         to AS198440 announce ANY
export:         to AS198452 announce ANY
export:         to AS198471 announce ANY
export:         to AS198651 announce ANY
export:         to AS198726 announce ANY
export:         to AS198760 announce ANY
export:         to AS198761 announce ANY
export:         to AS198847 announce ANY
export:         to AS198858 announce ANY
export:         to AS198890 announce ANY
export:         to AS198935 announce ANY
export:         to AS198939 announce ANY
export:         to AS198948 announce ANY
export:         to AS198949 announce ANY
export:         to AS199047 announce ANY
export:         to AS199064 announce ANY
export:         to AS199081 announce ANY
export:         to AS199095 announce ANY
export:         to AS199113 announce ANY
export:         to AS199114 announce ANY
export:         to AS199156 announce ANY
export:         to AS199163 announce ANY
export:         to AS199190 announce ANY
export:         to AS199237 announce ANY
export:         to AS199250 announce ANY
export:         to AS199283 announce ANY
export:         to AS199338 announce ANY
export:         to AS199358 announce ANY
export:         to AS199403 announce ANY
export:         to AS199410 announce ANY
export:         to AS199483 announce ANY
export:         to AS199496 announce ANY
export:         to AS199503 announce ANY
export:         to AS199509 announce ANY
export:         to AS199524 announce ANY
export:         to AS199559 announce ANY
export:         to AS199569 announce ANY
export:         to AS199617 announce ANY
export:         to AS199649 announce ANY
export:         to AS199710 announce ANY
export:         to AS199713 announce ANY
export:         to AS199759 announce ANY
export:         to AS199775 announce ANY
export:         to AS199790 announce ANY
export:         to AS199799 announce ANY
export:         to AS199880 announce ANY
export:         to AS199892 announce ANY
export:         to AS200031 announce ANY
export:         to AS200032 announce ANY
export:         to AS200052 announce ANY
export:         to AS200089 announce ANY
export:         to AS200099 announce ANY
export:         to AS200125 announce ANY
export:         to AS200147 announce ANY
export:         to AS200187 announce ANY
export:         to AS200271 announce ANY
export:         to AS200410 announce ANY
export:         to AS200416 announce ANY
export:         to AS200425 announce ANY
export:         to AS200462 announce ANY
export:         to AS200552 announce ANY
export:         to AS200562 announce ANY
export:         to AS200573 announce ANY
export:         to AS200585 announce ANY
export:         to AS200587 announce ANY
export:         to AS200596 announce ANY
export:         to AS200604 announce ANY
export:         to AS200612 announce ANY
export:         to AS200653 announce ANY
export:         to AS200692 announce ANY
export:         to AS200705 announce ANY
export:         to AS200713 announce ANY
export:         to AS200738 announce ANY
export:         to AS200758 announce ANY
export:         to AS200780 announce ANY
export:         to AS200845 announce ANY
export:         to AS200861 announce ANY
export:         to AS200884 announce ANY
export:         to AS200899 announce ANY
export:         to AS200904 announce ANY
export:         to AS200961 announce ANY
export:         to AS200994 announce ANY
export:         to AS200998 announce ANY
export:         to AS201053 announce ANY
export:         to AS201067 announce ANY
export:         to AS201099 announce ANY
export:         to AS201101 announce ANY
export:         to AS201126 announce ANY
export:         to AS201133 announce ANY
export:         to AS201188 announce ANY
export:         to AS201196 announce ANY
export:         to AS201213 announce ANY
export:         to AS201222 announce ANY
export:         to AS201246 announce ANY
export:         to AS201324 announce ANY
export:         to AS201333 announce ANY
export:         to AS201338 announce ANY
export:         to AS201352 announce ANY
export:         to AS201375 announce ANY
export:         to AS201408 announce ANY
export:         to AS201474 announce ANY
export:         to AS201478 announce ANY
export:         to AS201525 announce ANY
export:         to AS201542 announce ANY
export:         to AS201565 announce ANY
export:         to AS201602 announce ANY
export:         to AS201637 announce ANY
export:         to AS201710 announce ANY
export:         to AS201731 announce ANY
export:         to AS201747 announce ANY
export:         to AS201789 announce ANY
export:         to AS201887 announce ANY
export:         to AS201895 announce ANY
export:         to AS201942 announce ANY
export:         to AS201947 announce ANY
export:         to AS201958 announce ANY
export:         to AS201971 announce ANY
export:         to AS201990 announce ANY
export:         to AS201991 announce ANY
export:         to AS202010 announce ANY
export:         to AS202032 announce ANY
export:         to AS202063 announce ANY
export:         to AS202075 announce ANY
export:         to AS202149 announce ANY
export:         to AS202166 announce ANY
export:         to AS202219 announce ANY
export:         to AS202321 announce ANY
export:         to AS202596 announce ANY
export:         to AS202623 announce ANY
export:         to AS202688 announce ANY
export:         to AS202713 announce ANY
export:         to AS202766 announce ANY
export:         to AS202885 announce ANY
export:         to AS202964 announce ANY
export:         to AS203050 announce ANY
export:         to AS203055 announce ANY
export:         to AS203096 announce ANY
export:         to AS203182 announce ANY
export:         to AS203184 announce ANY
export:         to AS203222 announce ANY
export:         to AS203223 announce ANY
export:         to AS203256 announce ANY
export:         to AS203316 announce ANY
export:         to AS203327 announce ANY
export:         to AS203346 announce ANY
export:         to AS203351 announce ANY
export:         to AS203380 announce ANY
export:         to AS203400 announce ANY
export:         to AS203410 announce ANY
export:         to AS203585 announce ANY
export:         to AS203591 announce ANY
export:         to AS203608 announce ANY
export:         to AS203639 announce ANY
export:         to AS203649 announce ANY
export:         to AS203682 announce ANY
export:         to AS203689 announce ANY
export:         to AS203724 announce ANY
export:         to AS203955 announce ANY
export:         to AS204121 announce ANY
export:         to AS204126 announce ANY
export:         to AS204188 announce ANY
export:         to AS204258 announce ANY
export:         to AS204260 announce ANY
export:         to AS204264 announce ANY
export:         to AS204353 announce ANY
export:         to AS204419 announce ANY
export:         to AS204453 announce ANY
export:         to AS204476 announce ANY
export:         to AS204536 announce ANY
export:         to AS204548 announce ANY
export:         to AS204563 announce ANY
export:         to AS204577 announce ANY
export:         to AS204597 announce ANY
export:         to AS204622 announce ANY
export:         to AS204641 announce ANY
export:         to AS204777 announce ANY
export:         to AS204801 announce ANY
export:         to AS204807 announce ANY
export:         to AS204890 announce ANY
export:         to AS204959 announce ANY
export:         to AS204981 announce ANY
export:         to AS205016 announce ANY
export:         to AS205025 announce ANY
export:         to AS205039 announce ANY
export:         to AS205041 announce ANY
export:         to AS205142 announce ANY
export:         to AS205185 announce ANY
export:         to AS205263 announce ANY
export:         to AS205394 announce ANY
export:         to AS205476 announce ANY
export:         to AS205544 announce ANY
export:         to AS205615 announce ANY
export:         to AS205668 announce ANY
export:         to AS205697 announce ANY
export:         to AS205736 announce ANY
export:         to AS205809 announce ANY
export:         to AS205817 announce ANY
export:         to AS205842 announce ANY
export:         to AS205855 announce ANY
export:         to AS205860 announce ANY
export:         to AS205882 announce ANY
export:         to AS205943 announce ANY
export:         to AS206067 announce ANY
export:         to AS206082 announce ANY
export:         to AS206121 announce ANY
export:         to AS206168 announce ANY
export:         to AS206264 announce ANY
export:         to AS206370 announce ANY
export:         to AS206372 announce ANY
export:         to AS206383 announce ANY
export:         to AS206399 announce ANY
export:         to AS206459 announce ANY
export:         to AS206537 announce ANY
export:         to AS206539 announce ANY
export:         to AS206567 announce ANY
export:         to AS206576 announce ANY
export:         to AS206600 announce ANY
export:         to AS206614 announce ANY
export:         to AS206662 announce ANY
export:         to AS206701 announce ANY
export:         to AS206720 announce ANY
export:         to AS206741 announce ANY
export:         to AS206747 announce ANY
export:         to AS206776 announce ANY
export:         to AS206793 announce ANY
export:         to AS206870 announce ANY
export:         to AS206892 announce ANY
export:         to AS206958 announce ANY
export:         to AS206983 announce ANY
export:         to AS206984 announce ANY
export:         to AS207044 announce ANY
export:         to AS207045 announce ANY
export:         to AS207063 announce ANY
export:         to AS207087 announce ANY
export:         to AS207127 announce ANY
export:         to AS207137 announce ANY
export:         to AS207176 announce ANY
export:         to AS207367 announce ANY
export:         to AS207543 announce ANY
export:         to AS207685 announce ANY
export:         to AS207686 announce ANY
export:         to AS207747 announce ANY
export:         to AS207784 announce ANY
export:         to AS207856 announce ANY
export:         to AS207937 announce ANY
export:         to AS207995 announce ANY
export:         to AS208098 announce ANY
export:         to AS208180 announce ANY
export:         to AS208270 announce ANY
export:         to AS208350 announce ANY
export:         to AS208374 announce ANY
export:         to AS208416 announce ANY
export:         to AS208586 announce ANY
export:         to AS208625 announce ANY
export:         to AS208693 announce ANY
export:         to AS208781 announce ANY
export:         to AS208877 announce ANY
export:         to AS209181 announce ANY
export:         to AS209282 announce ANY
export:         to AS209311 announce ANY
export:         to AS209324 announce ANY
export:         to AS209549 announce ANY
export:         to AS209704 announce ANY
export:         to AS209765 announce ANY
export:         to AS209811 announce ANY
export:         to AS209875 announce ANY
export:         to AS210040 announce ANY
export:         to AS210043 announce ANY
export:         to AS210136 announce ANY
export:         to AS210211 announce ANY
export:         to AS210253 announce ANY
export:         to AS210269 announce ANY
export:         to AS210321 announce ANY
export:         to AS210329 announce ANY
export:         to AS210657 announce ANY
export:         to AS211029 announce ANY
export:         to AS211152 announce ANY
export:         to AS211156 announce ANY
export:         to AS211526 announce ANY
export:         to AS211597 announce ANY
export:         to AS211826 announce ANY
export:         to AS212045 announce ANY
export:         to AS212055 announce ANY
export:         to AS212097 announce ANY
export:         to AS212175 announce ANY
export:         to AS212195 announce ANY
export:         to AS212646 announce ANY
export:         to AS212708 announce ANY
export:         to AS212882 announce ANY
export:         to AS213035 announce ANY
export:         to AS213039 announce ANY
export:         to AS213094 announce ANY
export:         to AS213101 announce ANY
export:         to AS213130 announce ANY
export:         to AS213202 announce ANY
export:         to AS213205 announce ANY
export:         to AS213287 announce ANY
export:         to AS213308 announce ANY
export:         to AS213373 announce ANY
export:         to AS262206 announce ANY
export:         to AS262287 announce ANY
export:         to AS262589 announce ANY
export:         to AS262916 announce ANY
export:         to AS263179 announce ANY
export:         to AS263735 announce ANY
export:         to AS264409 announce ANY
export:         to AS264763 announce ANY
export:         to AS265556 announce ANY
export:         to AS265680 announce ANY
export:         to AS329214 announce ANY
export:         to AS393226 announce ANY
export:         to AS393234 announce ANY
export:         to AS393235 announce ANY
export:         to AS393241 announce ANY
export:         to AS393246 announce ANY
export:         to AS393284 announce ANY
export:         to AS393303 announce ANY
export:         to AS393316 announce ANY
export:         to AS393544 announce ANY
export:         to AS393606 announce ANY
export:         to AS393646 announce ANY
export:         to AS393676 announce ANY
export:         to AS393681 announce ANY
export:         to AS393725 announce ANY
export:         to AS393767 announce ANY
export:         to AS393791 announce ANY
export:         to AS393826 announce ANY
export:         to AS393845 announce ANY
export:         to AS393848 announce ANY
export:         to AS393886 announce ANY
export:         to AS393895 announce ANY
export:         to AS393900 announce ANY
export:         to AS393950 announce ANY
export:         to AS393981 announce ANY
export:         to AS394015 announce ANY
export:         to AS394085 announce ANY
export:         to AS394093 announce ANY
export:         to AS394102 announce ANY
export:         to AS394122 announce ANY
export:         to AS394141 announce ANY
export:         to AS394146 announce ANY
export:         to AS394186 announce ANY
export:         to AS394218 announce ANY
export:         to AS394232 announce ANY
export:         to AS394244 announce ANY
export:         to AS394303 announce ANY
export:         to AS394308 announce ANY
export:         to AS394346 announce ANY
export:         to AS394354 announce ANY
export:         to AS394380 announce ANY
export:         to AS394381 announce ANY
export:         to AS394409 announce ANY
export:         to AS394430 announce ANY
export:         to AS394434 announce ANY
export:         to AS394479 announce ANY
export:         to AS394480 announce ANY
export:         to AS394501 announce ANY
export:         to AS394562 announce ANY
export:         to AS394584 announce ANY
export:         to AS394620 announce ANY
export:         to AS394625 announce ANY
export:         to AS394628 announce ANY
export:         to AS394646 announce ANY
export:         to AS394663 announce ANY
export:         to AS394687 announce ANY
export:         to AS394814 announce ANY
export:         to AS394851 announce ANY
export:         to AS394855 announce ANY
export:         to AS394933 announce ANY
export:         to AS394935 announce ANY
export:         to AS394973 announce ANY
export:         to AS394977 announce ANY
export:         to AS395052 announce ANY
export:         to AS395119 announce ANY
export:         to AS395186 announce ANY
export:         to AS395247 announce ANY
export:         to AS395276 announce ANY
export:         to AS395308 announce ANY
export:         to AS395309 announce ANY
export:         to AS395354 announce ANY
export:         to AS395363 announce ANY
export:         to AS395369 announce ANY
export:         to AS395487 announce ANY
export:         to AS395505 announce ANY
export:         to AS395598 announce ANY
export:         to AS395636 announce ANY
export:         to AS395654 announce ANY
export:         to AS395662 announce ANY
export:         to AS395717 announce ANY
export:         to AS395743 announce ANY
export:         to AS395747 announce ANY
export:         to AS395753 announce ANY
export:         to AS395849 announce ANY
export:         to AS395923 announce ANY
export:         to AS395954 announce ANY
export:         to AS395978 announce ANY
export:         to AS396026 announce ANY
export:         to AS396055 announce ANY
export:         to AS396133 announce ANY
export:         to AS396158 announce ANY
export:         to AS396188 announce ANY
export:         to AS396190 announce ANY
export:         to AS396356 announce ANY
export:         to AS396362 announce ANY
export:         to AS396417 announce ANY
export:         to AS396426 announce ANY
export:         to AS396442 announce ANY
export:         to AS396472 announce ANY
export:         to AS396515 announce ANY
export:         to AS396535 announce ANY
export:         to AS396871 announce ANY
export:         to AS396884 announce ANY
export:         to AS396948 announce ANY
export:         to AS396949 announce ANY
export:         to AS396970 announce ANY
export:         to AS396984 announce ANY
export:         to AS396986 announce ANY
export:         to AS396998 announce ANY
export:         to AS397025 announce ANY
export:         to AS397027 announce ANY
export:         to AS397041 announce ANY
export:         to AS397048 announce ANY
export:         to AS397174 announce ANY
export:         to AS397289 announce ANY
export:         to AS397301 announce ANY
export:         to AS397308 announce ANY
export:         to AS397358 announce ANY
export:         to AS397369 announce ANY
export:         to AS397391 announce ANY
export:         to AS397404 announce ANY
export:         to AS397418 announce ANY
export:         to AS397473 announce ANY
export:         to AS397494 announce ANY
export:         to AS397505 announce ANY
export:         to AS397545 announce ANY
export:         to AS397599 announce ANY
export:         to AS397601 announce ANY
export:         to AS397642 announce ANY
export:         to AS397686 announce ANY
export:         to AS397689 announce ANY
export:         to AS397701 announce ANY
export:         to AS397727 announce ANY
export:         to AS397751 announce ANY
export:         to AS397760 announce ANY
export:         to AS397815 announce ANY
export:         to AS397912 announce ANY
export:         to AS397925 announce ANY
export:         to AS398044 announce ANY
export:         to AS398107 announce ANY
export:         to AS398175 announce ANY
export:         to AS398198 announce ANY
export:         to AS398240 announce ANY
export:         to AS398324 announce ANY
export:         to AS398424 announce ANY
export:         to AS398427 announce ANY
export:         to AS398448 announce ANY
export:         to AS398465 announce ANY
export:         to AS398698 announce ANY
export:         to AS398712 announce ANY
export:         to AS398764 announce ANY
export:         to AS398765 announce ANY
export:         to AS398808 announce ANY
export:         to AS398809 announce ANY
export:         to AS398814 announce ANY
export:         to AS398913 announce ANY
export:         to AS398969 announce ANY
export:         to AS399024 announce ANY
export:         to AS399065 announce ANY
export:         to AS399081 announce ANY
export:         to AS399143 announce ANY
export:         to AS399230 announce ANY
export:         to AS399289 announce ANY
export:         to AS399301 announce ANY
export:         to AS399424 announce ANY
export:         to AS399458 announce ANY
export:         to AS399480 announce ANY
export:         to AS399515 announce ANY
export:         to AS399539 announce ANY
export:         to AS399558 announce ANY
export:         to AS399587 announce ANY
export:         to AS399647 announce ANY
export:         to AS399678 announce ANY
export:         to AS399712 announce ANY
export:         to AS399759 announce ANY
export:         to AS399808 announce ANY
export:         to AS399809 announce ANY
export:         to AS399810 announce ANY
export:         to AS399814 announce ANY
export:         to AS399816 announce ANY
export:         to AS399817 announce ANY
export:         to AS399818 announce ANY
export:         to AS399920 announce ANY
export:         to AS399989 announce ANY
export:         to AS399998 announce ANY
export:         to AS400042 announce ANY
export:         to AS400146 announce ANY
export:         to AS400202 announce ANY
export:         to AS400282 announce ANY
export:         to AS400302 announce ANY
export:         to AS400309 announce ANY
export:         to AS400381 announce ANY
export:         to AS400444 announce ANY
export:         to AS400475 announce ANY
export:         to AS400511 announce ANY
export:         to AS400541 announce ANY
export:         to AS400662 announce ANY
export:         to AS400666 announce ANY
export:         to AS400687 announce ANY
export:         to AS400692 announce ANY
export:         to AS400802 announce ANY
export:         to AS400852 announce ANY
mp-export:      afi ipv6.unicast to AS12 announce ANY
mp-export:      afi ipv6.unicast to AS14 announce ANY
mp-export:      afi ipv6.unicast to AS57 announce ANY
mp-export:      afi ipv6.unicast to AS62 announce ANY
mp-export:      afi ipv6.unicast to AS97 announce ANY
mp-export:      afi ipv6.unicast to AS109 announce ANY
mp-export:      afi ipv6.unicast to AS260 announce ANY
mp-export:      afi ipv6.unicast to AS286 announce ANY
mp-export:      afi ipv6.unicast to AS376 announce ANY
mp-export:      afi ipv6.unicast to AS517 announce ANY
mp-export:      afi ipv6.unicast to AS559 announce ANY
mp-export:      afi ipv6.unicast to AS577 announce ANY
mp-export:      afi ipv6.unicast to AS600 announce ANY
mp-export:      afi ipv6.unicast to AS766 announce ANY
mp-export:      afi ipv6.unicast to AS792 announce ANY
mp-export:      afi ipv6.unicast to AS812 announce ANY
mp-export:      afi ipv6.unicast to AS852 announce ANY
mp-export:      afi ipv6.unicast to AS855 announce ANY
mp-export:      afi ipv6.unicast to AS1017 announce ANY
mp-export:      afi ipv6.unicast to AS1100 announce ANY
mp-export:      afi ipv6.unicast to AS1103 announce ANY
mp-export:      afi ipv6.unicast to AS1213 announce ANY
mp-export:      afi ipv6.unicast to AS1215 announce ANY
mp-export:      afi ipv6.unicast to AS1216 announce ANY
mp-export:      afi ipv6.unicast to AS1219 announce ANY
mp-export:      afi ipv6.unicast to AS1257 announce ANY
mp-export:      afi ipv6.unicast to AS1267 announce ANY
mp-export:      afi ipv6.unicast to AS1341 announce ANY
mp-export:      afi ipv6.unicast to AS1449 announce ANY
mp-export:      afi ipv6.unicast to AS1610 announce ANY
mp-export:      afi ipv6.unicast to AS1612 announce ANY
mp-export:      afi ipv6.unicast to AS1680 announce ANY
mp-export:      afi ipv6.unicast to AS1764 announce ANY
mp-export:      afi ipv6.unicast to AS1820 announce ANY
mp-export:      afi ipv6.unicast to AS1828 announce ANY
mp-export:      afi ipv6.unicast to AS2121 announce ANY
mp-export:      afi ipv6.unicast to AS2200 announce ANY
mp-export:      afi ipv6.unicast to AS2381 announce ANY
mp-export:      afi ipv6.unicast to AS2484 announce ANY
mp-export:      afi ipv6.unicast to AS2516 announce ANY
mp-export:      afi ipv6.unicast to AS2609 announce ANY
mp-export:      afi ipv6.unicast to AS2611 announce ANY
mp-export:      afi ipv6.unicast to AS2698 announce ANY
mp-export:      afi ipv6.unicast to AS2721 announce ANY
mp-export:      afi ipv6.unicast to AS2728 announce ANY
mp-export:      afi ipv6.unicast to AS2734 announce ANY
mp-export:      afi ipv6.unicast to AS3170 announce ANY
mp-export:      afi ipv6.unicast to AS3214 announce ANY
mp-export:      afi ipv6.unicast to AS3252 announce ANY
mp-export:      afi ipv6.unicast to AS3255 announce ANY
mp-export:      afi ipv6.unicast to AS3264 announce ANY
mp-export:      afi ipv6.unicast to AS3302 announce ANY
mp-export:      afi ipv6.unicast to AS3367 announce ANY
mp-export:      afi ipv6.unicast to AS3399 announce ANY
mp-export:      afi ipv6.unicast to AS3584 announce ANY
mp-export:      afi ipv6.unicast to AS3595 announce ANY
mp-export:      afi ipv6.unicast to AS3676 announce ANY
mp-export:      afi ipv6.unicast to AS3722 announce ANY
mp-export:      afi ipv6.unicast to AS3728 announce ANY
mp-export:      afi ipv6.unicast to AS3737 announce ANY
mp-export:      afi ipv6.unicast to AS3842 announce ANY
mp-export:      afi ipv6.unicast to AS3908 announce ANY
mp-export:      afi ipv6.unicast to AS3943 announce ANY
mp-export:      afi ipv6.unicast to AS4058 announce ANY
mp-export:      afi ipv6.unicast to AS4150 announce ANY
mp-export:      afi ipv6.unicast to AS4181 announce ANY
mp-export:      afi ipv6.unicast to AS4229 announce ANY
mp-export:      afi ipv6.unicast to AS4230 announce ANY
mp-export:      afi ipv6.unicast to AS4250 announce ANY
mp-export:      afi ipv6.unicast to AS4385 announce ANY
mp-export:      afi ipv6.unicast to AS4436 announce ANY
mp-export:      afi ipv6.unicast to AS4556 announce ANY
mp-export:      afi ipv6.unicast to AS4589 announce ANY
mp-export:      afi ipv6.unicast to AS4648 announce ANY
mp-export:      afi ipv6.unicast to AS4788 announce ANY
mp-export:      afi ipv6.unicast to AS4826 announce ANY
mp-export:      afi ipv6.unicast to AS4867 announce ANY
mp-export:      afi ipv6.unicast to AS4882 announce ANY
mp-export:      afi ipv6.unicast to AS5008 announce ANY
mp-export:      afi ipv6.unicast to AS5009 announce ANY
mp-export:      afi ipv6.unicast to AS5078 announce ANY
mp-export:      afi ipv6.unicast to AS5091 announce ANY
mp-export:      afi ipv6.unicast to AS5394 announce ANY
mp-export:      afi ipv6.unicast to AS5398 announce ANY
mp-export:      afi ipv6.unicast to AS5409 announce ANY
mp-export:      afi ipv6.unicast to AS5524 announce ANY
mp-export:      afi ipv6.unicast to AS5580 announce ANY
mp-export:      afi ipv6.unicast to AS5582 announce ANY
mp-export:      afi ipv6.unicast to AS5602 announce ANY
mp-export:      afi ipv6.unicast to AS5606 announce ANY
mp-export:      afi ipv6.unicast to AS5607 announce ANY
mp-export:      afi ipv6.unicast to AS5645 announce ANY
mp-export:      afi ipv6.unicast to AS5669 announce ANY
mp-export:      afi ipv6.unicast to AS5670 announce ANY
mp-export:      afi ipv6.unicast to AS5697 announce ANY
mp-export:      afi ipv6.unicast to AS5738 announce ANY
mp-export:      afi ipv6.unicast to AS5742 announce ANY
mp-export:      afi ipv6.unicast to AS5760 announce ANY
mp-export:      afi ipv6.unicast to AS5769 announce ANY
mp-export:      afi ipv6.unicast to AS5777 announce ANY
mp-export:      afi ipv6.unicast to AS6059 announce ANY
mp-export:      afi ipv6.unicast to AS6067 announce ANY
mp-export:      afi ipv6.unicast to AS6071 announce ANY
mp-export:      afi ipv6.unicast to AS6072 announce ANY
mp-export:      afi ipv6.unicast to AS6079 announce ANY
mp-export:      afi ipv6.unicast to AS6142 announce ANY
mp-export:      afi ipv6.unicast to AS6169 announce ANY
mp-export:      afi ipv6.unicast to AS6181 announce ANY
mp-export:      afi ipv6.unicast to AS6325 announce ANY
mp-export:      afi ipv6.unicast to AS6327 announce ANY
mp-export:      afi ipv6.unicast to AS6391 announce ANY
mp-export:      afi ipv6.unicast to AS6459 announce ANY
mp-export:      afi ipv6.unicast to AS6498 announce ANY
mp-export:      afi ipv6.unicast to AS6517 announce ANY
mp-export:      afi ipv6.unicast to AS6566 announce ANY
mp-export:      afi ipv6.unicast to AS6597 announce ANY
mp-export:      afi ipv6.unicast to AS6621 announce ANY
mp-export:      afi ipv6.unicast to AS6643 announce ANY
mp-export:      afi ipv6.unicast to AS6659 announce ANY
mp-export:      afi ipv6.unicast to AS6663 announce ANY
mp-export:      afi ipv6.unicast to AS6667 announce ANY
mp-export:      afi ipv6.unicast to AS6696 announce ANY
mp-export:      afi ipv6.unicast to AS6713 announce ANY
mp-export:      afi ipv6.unicast to AS6717 announce ANY
mp-export:      afi ipv6.unicast to AS6723 announce ANY
mp-export:      afi ipv6.unicast to AS6738 announce ANY
mp-export:      afi ipv6.unicast to AS6752 announce ANY
mp-export:      afi ipv6.unicast to AS6768 announce ANY
mp-export:      afi ipv6.unicast to AS6770 announce ANY
mp-export:      afi ipv6.unicast to AS6774 announce ANY
mp-export:      afi ipv6.unicast to AS6779 announce ANY
mp-export:      afi ipv6.unicast to AS6805 announce ANY
mp-export:      afi ipv6.unicast to AS6812 announce ANY
mp-export:      afi ipv6.unicast to AS6848 announce ANY
mp-export:      afi ipv6.unicast to AS6866 announce ANY
mp-export:      afi ipv6.unicast to AS6894 announce ANY
mp-export:      afi ipv6.unicast to AS6898 announce ANY
mp-export:      afi ipv6.unicast to AS7012 announce ANY
mp-export:      afi ipv6.unicast to AS7029 announce ANY
mp-export:      afi ipv6.unicast to AS7155 announce ANY
mp-export:      afi ipv6.unicast to AS7160 announce ANY
mp-export:      afi ipv6.unicast to AS7203 announce ANY
mp-export:      afi ipv6.unicast to AS7219 announce ANY
mp-export:      afi ipv6.unicast to AS7226 announce ANY
mp-export:      afi ipv6.unicast to AS7296 announce ANY
mp-export:      afi ipv6.unicast to AS7311 announce ANY
mp-export:      afi ipv6.unicast to AS7459 announce ANY
mp-export:      afi ipv6.unicast to AS7473 announce ANY
mp-export:      afi ipv6.unicast to AS7500 announce ANY
mp-export:      afi ipv6.unicast to AS7713 announce ANY
mp-export:      afi ipv6.unicast to AS7738 announce ANY
mp-export:      afi ipv6.unicast to AS7752 announce ANY
mp-export:      afi ipv6.unicast to AS7784 announce ANY
mp-export:      afi ipv6.unicast to AS7786 announce ANY
mp-export:      afi ipv6.unicast to AS7795 announce ANY
mp-export:      afi ipv6.unicast to AS7843 announce ANY
mp-export:      afi ipv6.unicast to AS7859 announce ANY
mp-export:      afi ipv6.unicast to AS7992 announce ANY
mp-export:      afi ipv6.unicast to AS8001 announce ANY
mp-export:      afi ipv6.unicast to AS8018 announce ANY
mp-export:      afi ipv6.unicast to AS8038 announce ANY
mp-export:      afi ipv6.unicast to AS8057 announce ANY
mp-export:      afi ipv6.unicast to AS8069 announce ANY
mp-export:      afi ipv6.unicast to AS8075 announce ANY
mp-export:      afi ipv6.unicast to AS8100 announce ANY
mp-export:      afi ipv6.unicast to AS8111 announce ANY
mp-export:      afi ipv6.unicast to AS8151 announce ANY
mp-export:      afi ipv6.unicast to AS8190 announce ANY
mp-export:      afi ipv6.unicast to AS8245 announce ANY
mp-export:      afi ipv6.unicast to AS8262 announce ANY
mp-export:      afi ipv6.unicast to AS8301 announce ANY
mp-export:      afi ipv6.unicast to AS8304 announce ANY
mp-export:      afi ipv6.unicast to AS8308 announce ANY
mp-export:      afi ipv6.unicast to AS8315 announce ANY
mp-export:      afi ipv6.unicast to AS8328 announce ANY
mp-export:      afi ipv6.unicast to AS8368 announce ANY
mp-export:      afi ipv6.unicast to AS8399 announce ANY
mp-export:      afi ipv6.unicast to AS8400 announce ANY
mp-export:      afi ipv6.unicast to AS8426 announce ANY
mp-export:      afi ipv6.unicast to AS8452 announce ANY
mp-export:      afi ipv6.unicast to AS8453 announce ANY
mp-export:      afi ipv6.unicast to AS8468 announce ANY
mp-export:      afi ipv6.unicast to AS8487 announce ANY
mp-export:      afi ipv6.unicast to AS8495 announce ANY
mp-export:      afi ipv6.unicast to AS8513 announce ANY
mp-export:      afi ipv6.unicast to AS8523 announce ANY
mp-export:      afi ipv6.unicast to AS8551 announce ANY
mp-export:      afi ipv6.unicast to AS8554 announce ANY
mp-export:      afi ipv6.unicast to AS8560 announce ANY
mp-export:      afi ipv6.unicast to AS8587 announce ANY
mp-export:      afi ipv6.unicast to AS8607 announce ANY
mp-export:      afi ipv6.unicast to AS8612 announce ANY
mp-export:      afi ipv6.unicast to AS8648 announce ANY
mp-export:      afi ipv6.unicast to AS8657 announce ANY
mp-export:      afi ipv6.unicast to AS8751 announce ANY
mp-export:      afi ipv6.unicast to AS8757 announce ANY
mp-export:      afi ipv6.unicast to AS8781 announce ANY
mp-export:      afi ipv6.unicast to AS8784 announce ANY
mp-export:      afi ipv6.unicast to AS8793 announce ANY
mp-export:      afi ipv6.unicast to AS8816 announce ANY
mp-export:      afi ipv6.unicast to AS8822 announce ANY
mp-export:      afi ipv6.unicast to AS8849 announce ANY
mp-export:      afi ipv6.unicast to AS8851 announce ANY
mp-export:      afi ipv6.unicast to AS8895 announce ANY
mp-export:      afi ipv6.unicast to AS8902 announce ANY
mp-export:      afi ipv6.unicast to AS8922 announce ANY
mp-export:      afi ipv6.unicast to AS8928 announce ANY
mp-export:      afi ipv6.unicast to AS8954 announce ANY
mp-export:      afi ipv6.unicast to AS8966 announce ANY
mp-export:      afi ipv6.unicast to AS8978 announce ANY
mp-export:      afi ipv6.unicast to AS8990 announce ANY
mp-export:      afi ipv6.unicast to AS9002 announce ANY
mp-export:      afi ipv6.unicast to AS9009 announce ANY
mp-export:      afi ipv6.unicast to AS9031 announce ANY
mp-export:      afi ipv6.unicast to AS9038 announce ANY
mp-export:      afi ipv6.unicast to AS9050 announce ANY
mp-export:      afi ipv6.unicast to AS9070 announce ANY
mp-export:      afi ipv6.unicast to AS9116 announce ANY
mp-export:      afi ipv6.unicast to AS9211 announce ANY
mp-export:      afi ipv6.unicast to AS9269 announce ANY
mp-export:      afi ipv6.unicast to AS9304 announce ANY
mp-export:      afi ipv6.unicast to AS9381 announce ANY
mp-export:      afi ipv6.unicast to AS9498 announce ANY
mp-export:      afi ipv6.unicast to AS9658 announce ANY
mp-export:      afi ipv6.unicast to AS9744 announce ANY
mp-export:      afi ipv6.unicast to AS9821 announce ANY
mp-export:      afi ipv6.unicast to AS9829 announce ANY
mp-export:      afi ipv6.unicast to AS10030 announce ANY
mp-export:      afi ipv6.unicast to AS10098 announce ANY
mp-export:      afi ipv6.unicast to AS10099 announce ANY
mp-export:      afi ipv6.unicast to AS10122 announce ANY
mp-export:      afi ipv6.unicast to AS10490 announce ANY
mp-export:      afi ipv6.unicast to AS10674 announce ANY
mp-export:      afi ipv6.unicast to AS10700 announce ANY
mp-export:      afi ipv6.unicast to AS10780 announce ANY
mp-export:      afi ipv6.unicast to AS10835 announce ANY
mp-export:      afi ipv6.unicast to AS10886 announce ANY
mp-export:      afi ipv6.unicast to AS10910 announce ANY
mp-export:      afi ipv6.unicast to AS10982 announce ANY
mp-export:      afi ipv6.unicast to AS10996 announce ANY
mp-export:      afi ipv6.unicast to AS11013 announce ANY
mp-export:      afi ipv6.unicast to AS11019 announce ANY
mp-export:      afi ipv6.unicast to AS11049 announce ANY
mp-export:      afi ipv6.unicast to AS11071 announce ANY
mp-export:      afi ipv6.unicast to AS11074 announce ANY
mp-export:      afi ipv6.unicast to AS11158 announce ANY
mp-export:      afi ipv6.unicast to AS11215 announce ANY
mp-export:      afi ipv6.unicast to AS11232 announce ANY
mp-export:      afi ipv6.unicast to AS11251 announce ANY
mp-export:      afi ipv6.unicast to AS11260 announce ANY
mp-export:      afi ipv6.unicast to AS11290 announce ANY
mp-export:      afi ipv6.unicast to AS11320 announce ANY
mp-export:      afi ipv6.unicast to AS11403 announce ANY
mp-export:      afi ipv6.unicast to AS11404 announce ANY
mp-export:      afi ipv6.unicast to AS11468 announce ANY
mp-export:      afi ipv6.unicast to AS11478 announce ANY
mp-export:      afi ipv6.unicast to AS11522 announce ANY
mp-export:      afi ipv6.unicast to AS11618 announce ANY
mp-export:      afi ipv6.unicast to AS11647 announce ANY
mp-export:      afi ipv6.unicast to AS11682 announce ANY
mp-export:      afi ipv6.unicast to AS11696 announce ANY
mp-export:      afi ipv6.unicast to AS11711 announce ANY
mp-export:      afi ipv6.unicast to AS11807 announce ANY
mp-export:      afi ipv6.unicast to AS11878 announce ANY
mp-export:      afi ipv6.unicast to AS11889 announce ANY
mp-export:      afi ipv6.unicast to AS11924 announce ANY
mp-export:      afi ipv6.unicast to AS12008 announce ANY
mp-export:      afi ipv6.unicast to AS12041 announce ANY
mp-export:      afi ipv6.unicast to AS12042 announce ANY
mp-export:      afi ipv6.unicast to AS12083 announce ANY
mp-export:      afi ipv6.unicast to AS12085 announce ANY
mp-export:      afi ipv6.unicast to AS12129 announce ANY
mp-export:      afi ipv6.unicast to AS12133 announce ANY
mp-export:      afi ipv6.unicast to AS12189 announce ANY
mp-export:      afi ipv6.unicast to AS12200 announce ANY
mp-export:      afi ipv6.unicast to AS12252 announce ANY
mp-export:      afi ipv6.unicast to AS12287 announce ANY
mp-export:      afi ipv6.unicast to AS12301 announce ANY
mp-export:      afi ipv6.unicast to AS12312 announce ANY
mp-export:      afi ipv6.unicast to AS12348 announce ANY
mp-export:      afi ipv6.unicast to AS12355 announce ANY
mp-export:      afi ipv6.unicast to AS12360 announce ANY
mp-export:      afi ipv6.unicast to AS12372 announce ANY
mp-export:      afi ipv6.unicast to AS12387 announce ANY
mp-export:      afi ipv6.unicast to AS12389 announce ANY
mp-export:      afi ipv6.unicast to AS12409 announce ANY
mp-export:      afi ipv6.unicast to AS12414 announce ANY
mp-export:      afi ipv6.unicast to AS12470 announce ANY
mp-export:      afi ipv6.unicast to AS12480 announce ANY
mp-export:      afi ipv6.unicast to AS12488 announce ANY
mp-export:      afi ipv6.unicast to AS12498 announce ANY
mp-export:      afi ipv6.unicast to AS12533 announce ANY
mp-export:      afi ipv6.unicast to AS12541 announce ANY
mp-export:      afi ipv6.unicast to AS12570 announce ANY
mp-export:      afi ipv6.unicast to AS12578 announce ANY
mp-export:      afi ipv6.unicast to AS12581 announce ANY
mp-export:      afi ipv6.unicast to AS12586 announce ANY
mp-export:      afi ipv6.unicast to AS12615 announce ANY
mp-export:      afi ipv6.unicast to AS12625 announce ANY
mp-export:      afi ipv6.unicast to AS12655 announce ANY
mp-export:      afi ipv6.unicast to AS12676 announce ANY
mp-export:      afi ipv6.unicast to AS12678 announce ANY
mp-export:      afi ipv6.unicast to AS12684 announce ANY
mp-export:      afi ipv6.unicast to AS12693 announce ANY
mp-export:      afi ipv6.unicast to AS12703 announce ANY
mp-export:      afi ipv6.unicast to AS12731 announce ANY
mp-export:      afi ipv6.unicast to AS12732 announce ANY
mp-export:      afi ipv6.unicast to AS12741 announce ANY
mp-export:      afi ipv6.unicast to AS12754 announce ANY
mp-export:      afi ipv6.unicast to AS12775 announce ANY
mp-export:      afi ipv6.unicast to AS12779 announce ANY
mp-export:      afi ipv6.unicast to AS12831 announce ANY
mp-export:      afi ipv6.unicast to AS12843 announce ANY
mp-export:      afi ipv6.unicast to AS12859 announce ANY
mp-export:      afi ipv6.unicast to AS12883 announce ANY
mp-export:      afi ipv6.unicast to AS12897 announce ANY
mp-export:      afi ipv6.unicast to AS12905 announce ANY
mp-export:      afi ipv6.unicast to AS12906 announce ANY
mp-export:      afi ipv6.unicast to AS12945 announce ANY
mp-export:      afi ipv6.unicast to AS12963 announce ANY
mp-export:      afi ipv6.unicast to AS12968 announce ANY
mp-export:      afi ipv6.unicast to AS12989 announce ANY
mp-export:      afi ipv6.unicast to AS13000 announce ANY
mp-export:      afi ipv6.unicast to AS13006 announce ANY
mp-export:      afi ipv6.unicast to AS13039 announce ANY
mp-export:      afi ipv6.unicast to AS13101 announce ANY
mp-export:      afi ipv6.unicast to AS13105 announce ANY
mp-export:      afi ipv6.unicast to AS13126 announce ANY
mp-export:      afi ipv6.unicast to AS13132 announce ANY
mp-export:      afi ipv6.unicast to AS13150 announce ANY
mp-export:      afi ipv6.unicast to AS13194 announce ANY
mp-export:      afi ipv6.unicast to AS13213 announce ANY
mp-export:      afi ipv6.unicast to AS13237 announce ANY
mp-export:      afi ipv6.unicast to AS13250 announce ANY
mp-export:      afi ipv6.unicast to AS13280 announce ANY
mp-export:      afi ipv6.unicast to AS13285 announce ANY
mp-export:      afi ipv6.unicast to AS13287 announce ANY
mp-export:      afi ipv6.unicast to AS13331 announce ANY
mp-export:      afi ipv6.unicast to AS13333 announce ANY
mp-export:      afi ipv6.unicast to AS13335 announce ANY
mp-export:      afi ipv6.unicast to AS13414 announce ANY
mp-export:      afi ipv6.unicast to AS13428 announce ANY
mp-export:      afi ipv6.unicast to AS13431 announce ANY
mp-export:      afi ipv6.unicast to AS13443 announce ANY
mp-export:      afi ipv6.unicast to AS13448 announce ANY
mp-export:      afi ipv6.unicast to AS13464 announce ANY
mp-export:      afi ipv6.unicast to AS13490 announce ANY
mp-export:      afi ipv6.unicast to AS13517 announce ANY
mp-export:      afi ipv6.unicast to AS13524 announce ANY
mp-export:      afi ipv6.unicast to AS13649 announce ANY
mp-export:      afi ipv6.unicast to AS13658 announce ANY
mp-export:      afi ipv6.unicast to AS13739 announce ANY
mp-export:      afi ipv6.unicast to AS13760 announce ANY
mp-export:      afi ipv6.unicast to AS13768 announce ANY
mp-export:      afi ipv6.unicast to AS13789 announce ANY
mp-export:      afi ipv6.unicast to AS13821 announce ANY
mp-export:      afi ipv6.unicast to AS13860 announce ANY
mp-export:      afi ipv6.unicast to AS13876 announce ANY
mp-export:      afi ipv6.unicast to AS13971 announce ANY
mp-export:      afi ipv6.unicast to AS13984 announce ANY
mp-export:      afi ipv6.unicast to AS14014 announce ANY
mp-export:      afi ipv6.unicast to AS14016 announce ANY
mp-export:      afi ipv6.unicast to AS14037 announce ANY
mp-export:      afi ipv6.unicast to AS14061 announce ANY
mp-export:      afi ipv6.unicast to AS14074 announce ANY
mp-export:      afi ipv6.unicast to AS14080 announce ANY
mp-export:      afi ipv6.unicast to AS14086 announce ANY
mp-export:      afi ipv6.unicast to AS14135 announce ANY
mp-export:      afi ipv6.unicast to AS14148 announce ANY
mp-export:      afi ipv6.unicast to AS14157 announce ANY
mp-export:      afi ipv6.unicast to AS14210 announce ANY
mp-export:      afi ipv6.unicast to AS14237 announce ANY
mp-export:      afi ipv6.unicast to AS14253 announce ANY
mp-export:      afi ipv6.unicast to AS14332 announce ANY
mp-export:      afi ipv6.unicast to AS14335 announce ANY
mp-export:      afi ipv6.unicast to AS14343 announce ANY
mp-export:      afi ipv6.unicast to AS14361 announce ANY
mp-export:      afi ipv6.unicast to AS14365 announce ANY
mp-export:      afi ipv6.unicast to AS14371 announce ANY
mp-export:      afi ipv6.unicast to AS14398 announce ANY
mp-export:      afi ipv6.unicast to AS14525 announce ANY
mp-export:      afi ipv6.unicast to AS14544 announce ANY
mp-export:      afi ipv6.unicast to AS14585 announce ANY
mp-export:      afi ipv6.unicast to AS14589 announce ANY
mp-export:      afi ipv6.unicast to AS14593 announce ANY
mp-export:      afi ipv6.unicast to AS14616 announce ANY
mp-export:      afi ipv6.unicast to AS14630 announce ANY
mp-export:      afi ipv6.unicast to AS14643 announce ANY
mp-export:      afi ipv6.unicast to AS14707 announce ANY
mp-export:      afi ipv6.unicast to AS14717 announce ANY
mp-export:      afi ipv6.unicast to AS14743 announce ANY
mp-export:      afi ipv6.unicast to AS14745 announce ANY
mp-export:      afi ipv6.unicast to AS14746 announce ANY
mp-export:      afi ipv6.unicast to AS14821 announce ANY
mp-export:      afi ipv6.unicast to AS14928 announce ANY
mp-export:      afi ipv6.unicast to AS14973 announce ANY
mp-export:      afi ipv6.unicast to AS14987 announce ANY
mp-export:      afi ipv6.unicast to AS15003 announce ANY
mp-export:      afi ipv6.unicast to AS15042 announce ANY
mp-export:      afi ipv6.unicast to AS15092 announce ANY
mp-export:      afi ipv6.unicast to AS15093 announce ANY
mp-export:      afi ipv6.unicast to AS15128 announce ANY
mp-export:      afi ipv6.unicast to AS15133 announce ANY
mp-export:      afi ipv6.unicast to AS15146 announce ANY
mp-export:      afi ipv6.unicast to AS15206 announce ANY
mp-export:      afi ipv6.unicast to AS15211 announce ANY
mp-export:      afi ipv6.unicast to AS15317 announce ANY
mp-export:      afi ipv6.unicast to AS15421 announce ANY
mp-export:      afi ipv6.unicast to AS15435 announce ANY
mp-export:      afi ipv6.unicast to AS15570 announce ANY
mp-export:      afi ipv6.unicast to AS15576 announce ANY
mp-export:      afi ipv6.unicast to AS15587 announce ANY
mp-export:      afi ipv6.unicast to AS15694 announce ANY
mp-export:      afi ipv6.unicast to AS15695 announce ANY
mp-export:      afi ipv6.unicast to AS15703 announce ANY
mp-export:      afi ipv6.unicast to AS15735 announce ANY
mp-export:      afi ipv6.unicast to AS15782 announce ANY
mp-export:      afi ipv6.unicast to AS15830 announce ANY
mp-export:      afi ipv6.unicast to AS15879 announce ANY
mp-export:      afi ipv6.unicast to AS15919 announce ANY
mp-export:      afi ipv6.unicast to AS15924 announce ANY
mp-export:      afi ipv6.unicast to AS15943 announce ANY
mp-export:      afi ipv6.unicast to AS15953 announce ANY
mp-export:      afi ipv6.unicast to AS15954 announce ANY
mp-export:      afi ipv6.unicast to AS15966 announce ANY
mp-export:      afi ipv6.unicast to AS15967 announce ANY
mp-export:      afi ipv6.unicast to AS15989 announce ANY
mp-export:      afi ipv6.unicast to AS15994 announce ANY
mp-export:      afi ipv6.unicast to AS16080 announce ANY
mp-export:      afi ipv6.unicast to AS16097 announce ANY
mp-export:      afi ipv6.unicast to AS16110 announce ANY
mp-export:      afi ipv6.unicast to AS16131 announce ANY
mp-export:      afi ipv6.unicast to AS16147 announce ANY
mp-export:      afi ipv6.unicast to AS16162 announce ANY
mp-export:      afi ipv6.unicast to AS16189 announce ANY
mp-export:      afi ipv6.unicast to AS16236 announce ANY
mp-export:      afi ipv6.unicast to AS16406 announce ANY
mp-export:      afi ipv6.unicast to AS16504 announce ANY
mp-export:      afi ipv6.unicast to AS16509 announce ANY
mp-export:      afi ipv6.unicast to AS16524 announce ANY
mp-export:      afi ipv6.unicast to AS16552 announce ANY
mp-export:      afi ipv6.unicast to AS16570 announce ANY
mp-export:      afi ipv6.unicast to AS16591 announce ANY
mp-export:      afi ipv6.unicast to AS16625 announce ANY
mp-export:      afi ipv6.unicast to AS16626 announce ANY
mp-export:      afi ipv6.unicast to AS16633 announce ANY
mp-export:      afi ipv6.unicast to AS16668 announce ANY
mp-export:      afi ipv6.unicast to AS16733 announce ANY
mp-export:      afi ipv6.unicast to AS16750 announce ANY
mp-export:      afi ipv6.unicast to AS16832 announce ANY
mp-export:      afi ipv6.unicast to AS16839 announce ANY
mp-export:      afi ipv6.unicast to AS16851 announce ANY
mp-export:      afi ipv6.unicast to AS16863 announce ANY
mp-export:      afi ipv6.unicast to AS16876 announce ANY
mp-export:      afi ipv6.unicast to AS16940 announce ANY
mp-export:      afi ipv6.unicast to AS17012 announce ANY
mp-export:      afi ipv6.unicast to AS17035 announce ANY
mp-export:      afi ipv6.unicast to AS17045 announce ANY
mp-export:      afi ipv6.unicast to AS17088 announce ANY
mp-export:      afi ipv6.unicast to AS17139 announce ANY
mp-export:      afi ipv6.unicast to AS17149 announce ANY
mp-export:      afi ipv6.unicast to AS17151 announce ANY
mp-export:      afi ipv6.unicast to AS17184 announce ANY
mp-export:      afi ipv6.unicast to AS17204 announce ANY
mp-export:      afi ipv6.unicast to AS17330 announce ANY
mp-export:      afi ipv6.unicast to AS17378 announce ANY
mp-export:      afi ipv6.unicast to AS17666 announce ANY
mp-export:      afi ipv6.unicast to AS18119 announce ANY
mp-export:      afi ipv6.unicast to AS18450 announce ANY
mp-export:      afi ipv6.unicast to AS18451 announce ANY
mp-export:      afi ipv6.unicast to AS18465 announce ANY
mp-export:      afi ipv6.unicast to AS18474 announce ANY
mp-export:      afi ipv6.unicast to AS18485 announce ANY
mp-export:      afi ipv6.unicast to AS18540 announce ANY
mp-export:      afi ipv6.unicast to AS18549 announce ANY
mp-export:      afi ipv6.unicast to AS18588 announce ANY
mp-export:      afi ipv6.unicast to AS18622 announce ANY
mp-export:      afi ipv6.unicast to AS18712 announce ANY
mp-export:      afi ipv6.unicast to AS18717 announce ANY
mp-export:      afi ipv6.unicast to AS18734 announce ANY
mp-export:      afi ipv6.unicast to AS18779 announce ANY
mp-export:      afi ipv6.unicast to AS18966 announce ANY
mp-export:      afi ipv6.unicast to AS18978 announce ANY
mp-export:      afi ipv6.unicast to AS19001 announce ANY
mp-export:      afi ipv6.unicast to AS19006 announce ANY
mp-export:      afi ipv6.unicast to AS19037 announce ANY
mp-export:      afi ipv6.unicast to AS19108 announce ANY
mp-export:      afi ipv6.unicast to AS19165 announce ANY
mp-export:      afi ipv6.unicast to AS19186 announce ANY
mp-export:      afi ipv6.unicast to AS19214 announce ANY
mp-export:      afi ipv6.unicast to AS19237 announce ANY
mp-export:      afi ipv6.unicast to AS19305 announce ANY
mp-export:      afi ipv6.unicast to AS19318 announce ANY
mp-export:      afi ipv6.unicast to AS19324 announce ANY
mp-export:      afi ipv6.unicast to AS19397 announce ANY
mp-export:      afi ipv6.unicast to AS19448 announce ANY
mp-export:      afi ipv6.unicast to AS19515 announce ANY
mp-export:      afi ipv6.unicast to AS19531 announce ANY
mp-export:      afi ipv6.unicast to AS19551 announce ANY
mp-export:      afi ipv6.unicast to AS19637 announce ANY
mp-export:      afi ipv6.unicast to AS19679 announce ANY
mp-export:      afi ipv6.unicast to AS19740 announce ANY
mp-export:      afi ipv6.unicast to AS19750 announce ANY
mp-export:      afi ipv6.unicast to AS19752 announce ANY
mp-export:      afi ipv6.unicast to AS19773 announce ANY
mp-export:      afi ipv6.unicast to AS19803 announce ANY
mp-export:      afi ipv6.unicast to AS19806 announce ANY
mp-export:      afi ipv6.unicast to AS19808 announce ANY
mp-export:      afi ipv6.unicast to AS19868 announce ANY
mp-export:      afi ipv6.unicast to AS19905 announce ANY
mp-export:      afi ipv6.unicast to AS19966 announce ANY
mp-export:      afi ipv6.unicast to AS19969 announce ANY
mp-export:      afi ipv6.unicast to AS19982 announce ANY
mp-export:      afi ipv6.unicast to AS20054 announce ANY
mp-export:      afi ipv6.unicast to AS20055 announce ANY
mp-export:      afi ipv6.unicast to AS20115 announce ANY
mp-export:      afi ipv6.unicast to AS20144 announce ANY
mp-export:      afi ipv6.unicast to AS20205 announce ANY
mp-export:      afi ipv6.unicast to AS20220 announce ANY
mp-export:      afi ipv6.unicast to AS20249 announce ANY
mp-export:      afi ipv6.unicast to AS20278 announce ANY
mp-export:      afi ipv6.unicast to AS20284 announce ANY
mp-export:      afi ipv6.unicast to AS20326 announce ANY
mp-export:      afi ipv6.unicast to AS20355 announce ANY
mp-export:      afi ipv6.unicast to AS20385 announce ANY
mp-export:      afi ipv6.unicast to AS20473 announce ANY
mp-export:      afi ipv6.unicast to AS20565 announce ANY
mp-export:      afi ipv6.unicast to AS20621 announce ANY
mp-export:      afi ipv6.unicast to AS20640 announce ANY
mp-export:      afi ipv6.unicast to AS20650 announce ANY
mp-export:      afi ipv6.unicast to AS20681 announce ANY
mp-export:      afi ipv6.unicast to AS20694 announce ANY
mp-export:      afi ipv6.unicast to AS20847 announce ANY
mp-export:      afi ipv6.unicast to AS20853 announce ANY
mp-export:      afi ipv6.unicast to AS20857 announce ANY
mp-export:      afi ipv6.unicast to AS20912 announce ANY
mp-export:      afi ipv6.unicast to AS20917 announce ANY
mp-export:      afi ipv6.unicast to AS20924 announce ANY
mp-export:      afi ipv6.unicast to AS20928 announce ANY
mp-export:      afi ipv6.unicast to AS20940 announce ANY
mp-export:      afi ipv6.unicast to AS20953 announce ANY
mp-export:      afi ipv6.unicast to AS21021 announce ANY
mp-export:      afi ipv6.unicast to AS21034 announce ANY
mp-export:      afi ipv6.unicast to AS21056 announce ANY
mp-export:      afi ipv6.unicast to AS21069 announce ANY
mp-export:      afi ipv6.unicast to AS21221 announce ANY
mp-export:      afi ipv6.unicast to AS21235 announce ANY
mp-export:      afi ipv6.unicast to AS21277 announce ANY
mp-export:      afi ipv6.unicast to AS21321 announce ANY
mp-export:      afi ipv6.unicast to AS21345 announce ANY
mp-export:      afi ipv6.unicast to AS21357 announce ANY
mp-export:      afi ipv6.unicast to AS21371 announce ANY
mp-export:      afi ipv6.unicast to AS21409 announce ANY
mp-export:      afi ipv6.unicast to AS21433 announce ANY
mp-export:      afi ipv6.unicast to AS21488 announce ANY
mp-export:      afi ipv6.unicast to AS21497 announce ANY
mp-export:      afi ipv6.unicast to AS21513 announce ANY
mp-export:      afi ipv6.unicast to AS21534 announce ANY
mp-export:      afi ipv6.unicast to AS21537 announce ANY
mp-export:      afi ipv6.unicast to AS21559 announce ANY
mp-export:      afi ipv6.unicast to AS21570 announce ANY
mp-export:      afi ipv6.unicast to AS21693 announce ANY
mp-export:      afi ipv6.unicast to AS21700 announce ANY
mp-export:      afi ipv6.unicast to AS21723 announce ANY
mp-export:      afi ipv6.unicast to AS21724 announce ANY
mp-export:      afi ipv6.unicast to AS21743 announce ANY
mp-export:      afi ipv6.unicast to AS21755 announce ANY
mp-export:      afi ipv6.unicast to AS21775 announce ANY
mp-export:      afi ipv6.unicast to AS21777 announce ANY
mp-export:      afi ipv6.unicast to AS21804 announce ANY
mp-export:      afi ipv6.unicast to AS21859 announce ANY
mp-export:      afi ipv6.unicast to AS21947 announce ANY
mp-export:      afi ipv6.unicast to AS22208 announce ANY
mp-export:      afi ipv6.unicast to AS22298 announce ANY
mp-export:      afi ipv6.unicast to AS22317 announce ANY
mp-export:      afi ipv6.unicast to AS22356 announce ANY
mp-export:      afi ipv6.unicast to AS22413 announce ANY
mp-export:      afi ipv6.unicast to AS22418 announce ANY
mp-export:      afi ipv6.unicast to AS22512 announce ANY
mp-export:      afi ipv6.unicast to AS22541 announce ANY
mp-export:      afi ipv6.unicast to AS22549 announce ANY
mp-export:      afi ipv6.unicast to AS22557 announce ANY
mp-export:      afi ipv6.unicast to AS22611 announce ANY
mp-export:      afi ipv6.unicast to AS22612 announce ANY
mp-export:      afi ipv6.unicast to AS22616 announce ANY
mp-export:      afi ipv6.unicast to AS22645 announce ANY
mp-export:      afi ipv6.unicast to AS22646 announce ANY
mp-export:      afi ipv6.unicast to AS22652 announce ANY
mp-export:      afi ipv6.unicast to AS22683 announce ANY
mp-export:      afi ipv6.unicast to AS22742 announce ANY
mp-export:      afi ipv6.unicast to AS22768 announce ANY
mp-export:      afi ipv6.unicast to AS22769 announce ANY
mp-export:      afi ipv6.unicast to AS22773 announce ANY
mp-export:      afi ipv6.unicast to AS22792 announce ANY
mp-export:      afi ipv6.unicast to AS22822 announce ANY
mp-export:      afi ipv6.unicast to AS22838 announce ANY
mp-export:      afi ipv6.unicast to AS22911 announce ANY
mp-export:      afi ipv6.unicast to AS22915 announce ANY
mp-export:      afi ipv6.unicast to AS22925 announce ANY
mp-export:      afi ipv6.unicast to AS22957 announce ANY
mp-export:      afi ipv6.unicast to AS22964 announce ANY
mp-export:      afi ipv6.unicast to AS22987 announce ANY
mp-export:      afi ipv6.unicast to AS22995 announce ANY
mp-export:      afi ipv6.unicast to AS23028 announce ANY
mp-export:      afi ipv6.unicast to AS23114 announce ANY
mp-export:      afi ipv6.unicast to AS23132 announce ANY
mp-export:      afi ipv6.unicast to AS23148 announce ANY
mp-export:      afi ipv6.unicast to AS23161 announce ANY
mp-export:      afi ipv6.unicast to AS23314 announce ANY
mp-export:      afi ipv6.unicast to AS23342 announce ANY
mp-export:      afi ipv6.unicast to AS23352 announce ANY
mp-export:      afi ipv6.unicast to AS23367 announce ANY
mp-export:      afi ipv6.unicast to AS23393 announce ANY
mp-export:      afi ipv6.unicast to AS23420 announce ANY
mp-export:      afi ipv6.unicast to AS23470 announce ANY
mp-export:      afi ipv6.unicast to AS23487 announce ANY
mp-export:      afi ipv6.unicast to AS23498 announce ANY
mp-export:      afi ipv6.unicast to AS23655 announce ANY
mp-export:      afi ipv6.unicast to AS23764 announce ANY
mp-export:      afi ipv6.unicast to AS23947 announce ANY
mp-export:      afi ipv6.unicast to AS24232 announce ANY
mp-export:      afi ipv6.unicast to AS24413 announce ANY
mp-export:      afi ipv6.unicast to AS24514 announce ANY
mp-export:      afi ipv6.unicast to AS24637 announce ANY
mp-export:      afi ipv6.unicast to AS24724 announce ANY
mp-export:      afi ipv6.unicast to AS24730 announce ANY
mp-export:      afi ipv6.unicast to AS24776 announce ANY
mp-export:      afi ipv6.unicast to AS24778 announce ANY
mp-export:      afi ipv6.unicast to AS24835 announce ANY
mp-export:      afi ipv6.unicast to AS24875 announce ANY
mp-export:      afi ipv6.unicast to AS24940 announce ANY
mp-export:      afi ipv6.unicast to AS24953 announce ANY
mp-export:      afi ipv6.unicast to AS24958 announce ANY
mp-export:      afi ipv6.unicast to AS24989 announce ANY
mp-export:      afi ipv6.unicast to AS24990 announce ANY
mp-export:      afi ipv6.unicast to AS24993 announce ANY
mp-export:      afi ipv6.unicast to AS25003 announce ANY
mp-export:      afi ipv6.unicast to AS25091 announce ANY
mp-export:      afi ipv6.unicast to AS25148 announce ANY
mp-export:      afi ipv6.unicast to AS25182 announce ANY
mp-export:      afi ipv6.unicast to AS25198 announce ANY
mp-export:      afi ipv6.unicast to AS25220 announce ANY
mp-export:      afi ipv6.unicast to AS25268 announce ANY
mp-export:      afi ipv6.unicast to AS25369 announce ANY
mp-export:      afi ipv6.unicast to AS25376 announce ANY
mp-export:      afi ipv6.unicast to AS25441 announce ANY
mp-export:      afi ipv6.unicast to AS25459 announce ANY
mp-export:      afi ipv6.unicast to AS25472 announce ANY
mp-export:      afi ipv6.unicast to AS25542 announce ANY
mp-export:      afi ipv6.unicast to AS25562 announce ANY
mp-export:      afi ipv6.unicast to AS25575 announce ANY
mp-export:      afi ipv6.unicast to AS25577 announce ANY
mp-export:      afi ipv6.unicast to AS25593 announce ANY
mp-export:      afi ipv6.unicast to AS25596 announce ANY
mp-export:      afi ipv6.unicast to AS25605 announce ANY
mp-export:      afi ipv6.unicast to AS25653 announce ANY
mp-export:      afi ipv6.unicast to AS25697 announce ANY
mp-export:      afi ipv6.unicast to AS25818 announce ANY
mp-export:      afi ipv6.unicast to AS25864 announce ANY
mp-export:      afi ipv6.unicast to AS25875 announce ANY
mp-export:      afi ipv6.unicast to AS25934 announce ANY
mp-export:      afi ipv6.unicast to AS25956 announce ANY
mp-export:      afi ipv6.unicast to AS25973 announce ANY
mp-export:      afi ipv6.unicast to AS26008 announce ANY
mp-export:      afi ipv6.unicast to AS26097 announce ANY
mp-export:      afi ipv6.unicast to AS26120 announce ANY
mp-export:      afi ipv6.unicast to AS26156 announce ANY
mp-export:      afi ipv6.unicast to AS26167 announce ANY
mp-export:      afi ipv6.unicast to AS26258 announce ANY
mp-export:      afi ipv6.unicast to AS26265 announce ANY
mp-export:      afi ipv6.unicast to AS26282 announce ANY
mp-export:      afi ipv6.unicast to AS26342 announce ANY
mp-export:      afi ipv6.unicast to AS26380 announce ANY
mp-export:      afi ipv6.unicast to AS26462 announce ANY
mp-export:      afi ipv6.unicast to AS26476 announce ANY
mp-export:      afi ipv6.unicast to AS26512 announce ANY
mp-export:      afi ipv6.unicast to AS26523 announce ANY
mp-export:      afi ipv6.unicast to AS26546 announce ANY
mp-export:      afi ipv6.unicast to AS26554 announce ANY
mp-export:      afi ipv6.unicast to AS26558 announce ANY
mp-export:      afi ipv6.unicast to AS26637 announce ANY
mp-export:      afi ipv6.unicast to AS26667 announce ANY
mp-export:      afi ipv6.unicast to AS26673 announce ANY
mp-export:      afi ipv6.unicast to AS26744 announce ANY
mp-export:      afi ipv6.unicast to AS26769 announce ANY
mp-export:      afi ipv6.unicast to AS26848 announce ANY
mp-export:      afi ipv6.unicast to AS26863 announce ANY
mp-export:      afi ipv6.unicast to AS26878 announce ANY
mp-export:      afi ipv6.unicast to AS26967 announce ANY
mp-export:      afi ipv6.unicast to AS27299 announce ANY
mp-export:      afi ipv6.unicast to AS27311 announce ANY
mp-export:      afi ipv6.unicast to AS27364 announce ANY
mp-export:      afi ipv6.unicast to AS27381 announce ANY
mp-export:      afi ipv6.unicast to AS27385 announce ANY
mp-export:      afi ipv6.unicast to AS27393 announce ANY
mp-export:      afi ipv6.unicast to AS27439 announce ANY
mp-export:      afi ipv6.unicast to AS27471 announce ANY
mp-export:      afi ipv6.unicast to AS27506 announce ANY
mp-export:      afi ipv6.unicast to AS27566 announce ANY
mp-export:      afi ipv6.unicast to AS27647 announce ANY
mp-export:      afi ipv6.unicast to AS27908 announce ANY
mp-export:      afi ipv6.unicast to AS27978 announce ANY
mp-export:      afi ipv6.unicast to AS28007 announce ANY
mp-export:      afi ipv6.unicast to AS28398 announce ANY
mp-export:      afi ipv6.unicast to AS28458 announce ANY
mp-export:      afi ipv6.unicast to AS28513 announce ANY
mp-export:      afi ipv6.unicast to AS28663 announce ANY
mp-export:      afi ipv6.unicast to AS28677 announce ANY
mp-export:      afi ipv6.unicast to AS28685 announce ANY
mp-export:      afi ipv6.unicast to AS28707 announce ANY
mp-export:      afi ipv6.unicast to AS28729 announce ANY
mp-export:      afi ipv6.unicast to AS28753 announce ANY
mp-export:      afi ipv6.unicast to AS28757 announce ANY
mp-export:      afi ipv6.unicast to AS28760 announce ANY
mp-export:      afi ipv6.unicast to AS28776 announce ANY
mp-export:      afi ipv6.unicast to AS28792 announce ANY
mp-export:      afi ipv6.unicast to AS28858 announce ANY
mp-export:      afi ipv6.unicast to AS28889 announce ANY
mp-export:      afi ipv6.unicast to AS28909 announce ANY
mp-export:      afi ipv6.unicast to AS28917 announce ANY
mp-export:      afi ipv6.unicast to AS28920 announce ANY
mp-export:      afi ipv6.unicast to AS28929 announce ANY
mp-export:      afi ipv6.unicast to AS29006 announce ANY
mp-export:      afi ipv6.unicast to AS29049 announce ANY
mp-export:      afi ipv6.unicast to AS29056 announce ANY
mp-export:      afi ipv6.unicast to AS29066 announce ANY
mp-export:      afi ipv6.unicast to AS29081 announce ANY
mp-export:      afi ipv6.unicast to AS29097 announce ANY
mp-export:      afi ipv6.unicast to AS29107 announce ANY
mp-export:      afi ipv6.unicast to AS29119 announce ANY
mp-export:      afi ipv6.unicast to AS29140 announce ANY
mp-export:      afi ipv6.unicast to AS29152 announce ANY
mp-export:      afi ipv6.unicast to AS29169 announce ANY
mp-export:      afi ipv6.unicast to AS29208 announce ANY
mp-export:      afi ipv6.unicast to AS29259 announce ANY
mp-export:      afi ipv6.unicast to AS29278 announce ANY
mp-export:      afi ipv6.unicast to AS29286 announce ANY
mp-export:      afi ipv6.unicast to AS29314 announce ANY
mp-export:      afi ipv6.unicast to AS29386 announce ANY
mp-export:      afi ipv6.unicast to AS29396 announce ANY
mp-export:      afi ipv6.unicast to AS29405 announce ANY
mp-export:      afi ipv6.unicast to AS29449 announce ANY
mp-export:      afi ipv6.unicast to AS29467 announce ANY
mp-export:      afi ipv6.unicast to AS29518 announce ANY
mp-export:      afi ipv6.unicast to AS29535 announce ANY
mp-export:      afi ipv6.unicast to AS29550 announce ANY
mp-export:      afi ipv6.unicast to AS29551 announce ANY
mp-export:      afi ipv6.unicast to AS29591 announce ANY
mp-export:      afi ipv6.unicast to AS29636 announce ANY
mp-export:      afi ipv6.unicast to AS29644 announce ANY
mp-export:      afi ipv6.unicast to AS29655 announce ANY
mp-export:      afi ipv6.unicast to AS29680 announce ANY
mp-export:      afi ipv6.unicast to AS29748 announce ANY
mp-export:      afi ipv6.unicast to AS29757 announce ANY
mp-export:      afi ipv6.unicast to AS29761 announce ANY
mp-export:      afi ipv6.unicast to AS29802 announce ANY
mp-export:      afi ipv6.unicast to AS29838 announce ANY
mp-export:      afi ipv6.unicast to AS29884 announce ANY
mp-export:      afi ipv6.unicast to AS29907 announce ANY
mp-export:      afi ipv6.unicast to AS29909 announce ANY
mp-export:      afi ipv6.unicast to AS29976 announce ANY
mp-export:      afi ipv6.unicast to AS30012 announce ANY
mp-export:      afi ipv6.unicast to AS30029 announce ANY
mp-export:      afi ipv6.unicast to AS30036 announce ANY
mp-export:      afi ipv6.unicast to AS30041 announce ANY
mp-export:      afi ipv6.unicast to AS30071 announce ANY
mp-export:      afi ipv6.unicast to AS30081 announce ANY
mp-export:      afi ipv6.unicast to AS30103 announce ANY
mp-export:      afi ipv6.unicast to AS30114 announce ANY
mp-export:      afi ipv6.unicast to AS30146 announce ANY
mp-export:      afi ipv6.unicast to AS30148 announce ANY
mp-export:      afi ipv6.unicast to AS30197 announce ANY
mp-export:      afi ipv6.unicast to AS30215 announce ANY
mp-export:      afi ipv6.unicast to AS30238 announce ANY
mp-export:      afi ipv6.unicast to AS30286 announce ANY
mp-export:      afi ipv6.unicast to AS30404 announce ANY
mp-export:      afi ipv6.unicast to AS30456 announce ANY
mp-export:      afi ipv6.unicast to AS30475 announce ANY
mp-export:      afi ipv6.unicast to AS30600 announce ANY
mp-export:      afi ipv6.unicast to AS30607 announce ANY
mp-export:      afi ipv6.unicast to AS30633 announce ANY
mp-export:      afi ipv6.unicast to AS30742 announce ANY
mp-export:      afi ipv6.unicast to AS30818 announce ANY
mp-export:      afi ipv6.unicast to AS30827 announce ANY
mp-export:      afi ipv6.unicast to AS30848 announce ANY
mp-export:      afi ipv6.unicast to AS30925 announce ANY
mp-export:      afi ipv6.unicast to AS30931 announce ANY
mp-export:      afi ipv6.unicast to AS30937 announce ANY
mp-export:      afi ipv6.unicast to AS30967 announce ANY
mp-export:      afi ipv6.unicast to AS31029 announce ANY
mp-export:      afi ipv6.unicast to AS31042 announce ANY
mp-export:      afi ipv6.unicast to AS31059 announce ANY
mp-export:      afi ipv6.unicast to AS31078 announce ANY
mp-export:      afi ipv6.unicast to AS31080 announce ANY
mp-export:      afi ipv6.unicast to AS31083 announce ANY
mp-export:      afi ipv6.unicast to AS31084 announce ANY
mp-export:      afi ipv6.unicast to AS31108 announce ANY
mp-export:      afi ipv6.unicast to AS31115 announce ANY
mp-export:      afi ipv6.unicast to AS31116 announce ANY
mp-export:      afi ipv6.unicast to AS31122 announce ANY
mp-export:      afi ipv6.unicast to AS31147 announce ANY
mp-export:      afi ipv6.unicast to AS31241 announce ANY
mp-export:      afi ipv6.unicast to AS31242 announce ANY
mp-export:      afi ipv6.unicast to AS31250 announce ANY
mp-export:      afi ipv6.unicast to AS31263 announce ANY
mp-export:      afi ipv6.unicast to AS31287 announce ANY
mp-export:      afi ipv6.unicast to AS31293 announce ANY
mp-export:      afi ipv6.unicast to AS31400 announce ANY
mp-export:      afi ipv6.unicast to AS31424 announce ANY
mp-export:      afi ipv6.unicast to AS31445 announce ANY
mp-export:      afi ipv6.unicast to AS31463 announce ANY
mp-export:      afi ipv6.unicast to AS31479 announce ANY
mp-export:      afi ipv6.unicast to AS31529 announce ANY
mp-export:      afi ipv6.unicast to AS31595 announce ANY
mp-export:      afi ipv6.unicast to AS31612 announce ANY
mp-export:      afi ipv6.unicast to AS31631 announce ANY
mp-export:      afi ipv6.unicast to AS31641 announce ANY
mp-export:      afi ipv6.unicast to AS31655 announce ANY
mp-export:      afi ipv6.unicast to AS31669 announce ANY
mp-export:      afi ipv6.unicast to AS31672 announce ANY
mp-export:      afi ipv6.unicast to AS31688 announce ANY
mp-export:      afi ipv6.unicast to AS31708 announce ANY
mp-export:      afi ipv6.unicast to AS31712 announce ANY
mp-export:      afi ipv6.unicast to AS31727 announce ANY
mp-export:      afi ipv6.unicast to AS31743 announce ANY
mp-export:      afi ipv6.unicast to AS31760 announce ANY
mp-export:      afi ipv6.unicast to AS31898 announce ANY
mp-export:      afi ipv6.unicast to AS31936 announce ANY
mp-export:      afi ipv6.unicast to AS32030 announce ANY
mp-export:      afi ipv6.unicast to AS32035 announce ANY
mp-export:      afi ipv6.unicast to AS32098 announce ANY
mp-export:      afi ipv6.unicast to AS32133 announce ANY
mp-export:      afi ipv6.unicast to AS32181 announce ANY
mp-export:      afi ipv6.unicast to AS32217 announce ANY
mp-export:      afi ipv6.unicast to AS32222 announce ANY
mp-export:      afi ipv6.unicast to AS32261 announce ANY
mp-export:      afi ipv6.unicast to AS32281 announce ANY
mp-export:      afi ipv6.unicast to AS32323 announce ANY
mp-export:      afi ipv6.unicast to AS32354 announce ANY
mp-export:      afi ipv6.unicast to AS32425 announce ANY
mp-export:      afi ipv6.unicast to AS32440 announce ANY
mp-export:      afi ipv6.unicast to AS32475 announce ANY
mp-export:      afi ipv6.unicast to AS32478 announce ANY
mp-export:      afi ipv6.unicast to AS32484 announce ANY
mp-export:      afi ipv6.unicast to AS32489 announce ANY
mp-export:      afi ipv6.unicast to AS32578 announce ANY
mp-export:      afi ipv6.unicast to AS32613 announce ANY
mp-export:      afi ipv6.unicast to AS32624 announce ANY
mp-export:      afi ipv6.unicast to AS32671 announce ANY
mp-export:      afi ipv6.unicast to AS32710 announce ANY
mp-export:      afi ipv6.unicast to AS32780 announce ANY
mp-export:      afi ipv6.unicast to AS32798 announce ANY
mp-export:      afi ipv6.unicast to AS32880 announce ANY
mp-export:      afi ipv6.unicast to AS32881 announce ANY
mp-export:      afi ipv6.unicast to AS32899 announce ANY
mp-export:      afi ipv6.unicast to AS32934 announce ANY
mp-export:      afi ipv6.unicast to AS32987 announce ANY
mp-export:      afi ipv6.unicast to AS33040 announce ANY
mp-export:      afi ipv6.unicast to AS33047 announce ANY
mp-export:      afi ipv6.unicast to AS33154 announce ANY
mp-export:      afi ipv6.unicast to AS33185 announce ANY
mp-export:      afi ipv6.unicast to AS33247 announce ANY
mp-export:      afi ipv6.unicast to AS33280 announce ANY
mp-export:      afi ipv6.unicast to AS33361 announce ANY
mp-export:      afi ipv6.unicast to AS33371 announce ANY
mp-export:      afi ipv6.unicast to AS33419 announce ANY
mp-export:      afi ipv6.unicast to AS33438 announce ANY
mp-export:      afi ipv6.unicast to AS33445 announce ANY
mp-export:      afi ipv6.unicast to AS33459 announce ANY
mp-export:      afi ipv6.unicast to AS33494 announce ANY
mp-export:      afi ipv6.unicast to AS33576 announce ANY
mp-export:      afi ipv6.unicast to AS33597 announce ANY
mp-export:      afi ipv6.unicast to AS33619 announce ANY
mp-export:      afi ipv6.unicast to AS33694 announce ANY
mp-export:      afi ipv6.unicast to AS33724 announce ANY
mp-export:      afi ipv6.unicast to AS33802 announce ANY
mp-export:      afi ipv6.unicast to AS33835 announce ANY
mp-export:      afi ipv6.unicast to AS33891 announce ANY
mp-export:      afi ipv6.unicast to AS33923 announce ANY
mp-export:      afi ipv6.unicast to AS33941 announce ANY
mp-export:      afi ipv6.unicast to AS33986 announce ANY
mp-export:      afi ipv6.unicast to AS34002 announce ANY
mp-export:      afi ipv6.unicast to AS34006 announce ANY
mp-export:      afi ipv6.unicast to AS34080 announce ANY
mp-export:      afi ipv6.unicast to AS34164 announce ANY
mp-export:      afi ipv6.unicast to AS34178 announce ANY
mp-export:      afi ipv6.unicast to AS34191 announce ANY
mp-export:      afi ipv6.unicast to AS34197 announce ANY
mp-export:      afi ipv6.unicast to AS34209 announce ANY
mp-export:      afi ipv6.unicast to AS34224 announce ANY
mp-export:      afi ipv6.unicast to AS34245 announce ANY
mp-export:      afi ipv6.unicast to AS34279 announce ANY
mp-export:      afi ipv6.unicast to AS34290 announce ANY
mp-export:      afi ipv6.unicast to AS34305 announce ANY
mp-export:      afi ipv6.unicast to AS34308 announce ANY
mp-export:      afi ipv6.unicast to AS34309 announce ANY
mp-export:      afi ipv6.unicast to AS34409 announce ANY
mp-export:      afi ipv6.unicast to AS34428 announce ANY
mp-export:      afi ipv6.unicast to AS34442 announce ANY
mp-export:      afi ipv6.unicast to AS34510 announce ANY
mp-export:      afi ipv6.unicast to AS34525 announce ANY
mp-export:      afi ipv6.unicast to AS34549 announce ANY
mp-export:      afi ipv6.unicast to AS34569 announce ANY
mp-export:      afi ipv6.unicast to AS34715 announce ANY
mp-export:      afi ipv6.unicast to AS34737 announce ANY
mp-export:      afi ipv6.unicast to AS34762 announce ANY
mp-export:      afi ipv6.unicast to AS34764 announce ANY
mp-export:      afi ipv6.unicast to AS34814 announce ANY
mp-export:      afi ipv6.unicast to AS34854 announce ANY
mp-export:      afi ipv6.unicast to AS34895 announce ANY
mp-export:      afi ipv6.unicast to AS34922 announce ANY
mp-export:      afi ipv6.unicast to AS34927 announce ANY
mp-export:      afi ipv6.unicast to AS34966 announce ANY
mp-export:      afi ipv6.unicast to AS34967 announce ANY
mp-export:      afi ipv6.unicast to AS34968 announce ANY
mp-export:      afi ipv6.unicast to AS34979 announce ANY
mp-export:      afi ipv6.unicast to AS34984 announce ANY
mp-export:      afi ipv6.unicast to AS35070 announce ANY
mp-export:      afi ipv6.unicast to AS35180 announce ANY
mp-export:      afi ipv6.unicast to AS35266 announce ANY
mp-export:      afi ipv6.unicast to AS35289 announce ANY
mp-export:      afi ipv6.unicast to AS35311 announce ANY
mp-export:      afi ipv6.unicast to AS35313 announce ANY
mp-export:      afi ipv6.unicast to AS35315 announce ANY
mp-export:      afi ipv6.unicast to AS35370 announce ANY
mp-export:      afi ipv6.unicast to AS35426 announce ANY
mp-export:      afi ipv6.unicast to AS35444 announce ANY
mp-export:      afi ipv6.unicast to AS35491 announce ANY
mp-export:      afi ipv6.unicast to AS35548 announce ANY
mp-export:      afi ipv6.unicast to AS35574 announce ANY
mp-export:      afi ipv6.unicast to AS35593 announce ANY
mp-export:      afi ipv6.unicast to AS35699 announce ANY
mp-export:      afi ipv6.unicast to AS35745 announce ANY
mp-export:      afi ipv6.unicast to AS35838 announce ANY
mp-export:      afi ipv6.unicast to AS35908 announce ANY
mp-export:      afi ipv6.unicast to AS35953 announce ANY
mp-export:      afi ipv6.unicast to AS35975 announce ANY
mp-export:      afi ipv6.unicast to AS35993 announce ANY
mp-export:      afi ipv6.unicast to AS35994 announce ANY
mp-export:      afi ipv6.unicast to AS36007 announce ANY
mp-export:      afi ipv6.unicast to AS36040 announce ANY
mp-export:      afi ipv6.unicast to AS36062 announce ANY
mp-export:      afi ipv6.unicast to AS36077 announce ANY
mp-export:      afi ipv6.unicast to AS36086 announce ANY
mp-export:      afi ipv6.unicast to AS36103 announce ANY
mp-export:      afi ipv6.unicast to AS36236 announce ANY
mp-export:      afi ipv6.unicast to AS36243 announce ANY
mp-export:      afi ipv6.unicast to AS36352 announce ANY
mp-export:      afi ipv6.unicast to AS36385 announce ANY
mp-export:      afi ipv6.unicast to AS36408 announce ANY
mp-export:      afi ipv6.unicast to AS36444 announce ANY
mp-export:      afi ipv6.unicast to AS36459 announce ANY
mp-export:      afi ipv6.unicast to AS36473 announce ANY
mp-export:      afi ipv6.unicast to AS36483 announce ANY
mp-export:      afi ipv6.unicast to AS36493 announce ANY
mp-export:      afi ipv6.unicast to AS36692 announce ANY
mp-export:      afi ipv6.unicast to AS36734 announce ANY
mp-export:      afi ipv6.unicast to AS36776 announce ANY
mp-export:      afi ipv6.unicast to AS36884 announce ANY
mp-export:      afi ipv6.unicast to AS37100 announce ANY
mp-export:      afi ipv6.unicast to AS37271 announce ANY
mp-export:      afi ipv6.unicast to AS37468 announce ANY
mp-export:      afi ipv6.unicast to AS37721 announce ANY
mp-export:      afi ipv6.unicast to AS38082 announce ANY
mp-export:      afi ipv6.unicast to AS38880 announce ANY
mp-export:      afi ipv6.unicast to AS38915 announce ANY
mp-export:      afi ipv6.unicast to AS38930 announce ANY
mp-export:      afi ipv6.unicast to AS38983 announce ANY
mp-export:      afi ipv6.unicast to AS39063 announce ANY
mp-export:      afi ipv6.unicast to AS39090 announce ANY
mp-export:      afi ipv6.unicast to AS39116 announce ANY
mp-export:      afi ipv6.unicast to AS39120 announce ANY
mp-export:      afi ipv6.unicast to AS39175 announce ANY
mp-export:      afi ipv6.unicast to AS39179 announce ANY
mp-export:      afi ipv6.unicast to AS39180 announce ANY
mp-export:      afi ipv6.unicast to AS39233 announce ANY
mp-export:      afi ipv6.unicast to AS39234 announce ANY
mp-export:      afi ipv6.unicast to AS39372 announce ANY
mp-export:      afi ipv6.unicast to AS39392 announce ANY
mp-export:      afi ipv6.unicast to AS39447 announce ANY
mp-export:      afi ipv6.unicast to AS39477 announce ANY
mp-export:      afi ipv6.unicast to AS39498 announce ANY
mp-export:      afi ipv6.unicast to AS39505 announce ANY
mp-export:      afi ipv6.unicast to AS39506 announce ANY
mp-export:      afi ipv6.unicast to AS39512 announce ANY
mp-export:      afi ipv6.unicast to AS39526 announce ANY
mp-export:      afi ipv6.unicast to AS39545 announce ANY
mp-export:      afi ipv6.unicast to AS39560 announce ANY
mp-export:      afi ipv6.unicast to AS39572 announce ANY
mp-export:      afi ipv6.unicast to AS39591 announce ANY
mp-export:      afi ipv6.unicast to AS39637 announce ANY
mp-export:      afi ipv6.unicast to AS39648 announce ANY
mp-export:      afi ipv6.unicast to AS39686 announce ANY
mp-export:      afi ipv6.unicast to AS39704 announce ANY
mp-export:      afi ipv6.unicast to AS39729 announce ANY
mp-export:      afi ipv6.unicast to AS39766 announce ANY
mp-export:      afi ipv6.unicast to AS39781 announce ANY
mp-export:      afi ipv6.unicast to AS39816 announce ANY
mp-export:      afi ipv6.unicast to AS39822 announce ANY
mp-export:      afi ipv6.unicast to AS39832 announce ANY
mp-export:      afi ipv6.unicast to AS39855 announce ANY
mp-export:      afi ipv6.unicast to AS39878 announce ANY
mp-export:      afi ipv6.unicast to AS39892 announce ANY
mp-export:      afi ipv6.unicast to AS39912 announce ANY
mp-export:      afi ipv6.unicast to AS39923 announce ANY
mp-export:      afi ipv6.unicast to AS39964 announce ANY
mp-export:      afi ipv6.unicast to AS40028 announce ANY
mp-export:      afi ipv6.unicast to AS40029 announce ANY
mp-export:      afi ipv6.unicast to AS40065 announce ANY
mp-export:      afi ipv6.unicast to AS40165 announce ANY
mp-export:      afi ipv6.unicast to AS40193 announce ANY
mp-export:      afi ipv6.unicast to AS40224 announce ANY
mp-export:      afi ipv6.unicast to AS40317 announce ANY
mp-export:      afi ipv6.unicast to AS40401 announce ANY
mp-export:      afi ipv6.unicast to AS40402 announce ANY
mp-export:      afi ipv6.unicast to AS40430 announce ANY
mp-export:      afi ipv6.unicast to AS40490 announce ANY
mp-export:      afi ipv6.unicast to AS40523 announce ANY
mp-export:      afi ipv6.unicast to AS40528 announce ANY
mp-export:      afi ipv6.unicast to AS40581 announce ANY
mp-export:      afi ipv6.unicast to AS40676 announce ANY
mp-export:      afi ipv6.unicast to AS40729 announce ANY
mp-export:      afi ipv6.unicast to AS40739 announce ANY
mp-export:      afi ipv6.unicast to AS40763 announce ANY
mp-export:      afi ipv6.unicast to AS40769 announce ANY
mp-export:      afi ipv6.unicast to AS40788 announce ANY
mp-export:      afi ipv6.unicast to AS40841 announce ANY
mp-export:      afi ipv6.unicast to AS40885 announce ANY
mp-export:      afi ipv6.unicast to AS40889 announce ANY
mp-export:      afi ipv6.unicast to AS40934 announce ANY
mp-export:      afi ipv6.unicast to AS41041 announce ANY
mp-export:      afi ipv6.unicast to AS41073 announce ANY
mp-export:      afi ipv6.unicast to AS41135 announce ANY
mp-export:      afi ipv6.unicast to AS41146 announce ANY
mp-export:      afi ipv6.unicast to AS41157 announce ANY
mp-export:      afi ipv6.unicast to AS41160 announce ANY
mp-export:      afi ipv6.unicast to AS41204 announce ANY
mp-export:      afi ipv6.unicast to AS41230 announce ANY
mp-export:      afi ipv6.unicast to AS41313 announce ANY
mp-export:      afi ipv6.unicast to AS41327 announce ANY
mp-export:      afi ipv6.unicast to AS41354 announce ANY
mp-export:      afi ipv6.unicast to AS41357 announce ANY
mp-export:      afi ipv6.unicast to AS41364 announce ANY
mp-export:      afi ipv6.unicast to AS41410 announce ANY
mp-export:      afi ipv6.unicast to AS41415 announce ANY
mp-export:      afi ipv6.unicast to AS41435 announce ANY
mp-export:      afi ipv6.unicast to AS41436 announce ANY
mp-export:      afi ipv6.unicast to AS41495 announce ANY
mp-export:      afi ipv6.unicast to AS41497 announce ANY
mp-export:      afi ipv6.unicast to AS41549 announce ANY
mp-export:      afi ipv6.unicast to AS41564 announce ANY
mp-export:      afi ipv6.unicast to AS41653 announce ANY
mp-export:      afi ipv6.unicast to AS41765 announce ANY
mp-export:      afi ipv6.unicast to AS41883 announce ANY
mp-export:      afi ipv6.unicast to AS41887 announce ANY
mp-export:      afi ipv6.unicast to AS41935 announce ANY
mp-export:      afi ipv6.unicast to AS41960 announce ANY
mp-export:      afi ipv6.unicast to AS41966 announce ANY
mp-export:      afi ipv6.unicast to AS42004 announce ANY
mp-export:      afi ipv6.unicast to AS42005 announce ANY
mp-export:      afi ipv6.unicast to AS42013 announce ANY
mp-export:      afi ipv6.unicast to AS42040 announce ANY
mp-export:      afi ipv6.unicast to AS42044 announce ANY
mp-export:      afi ipv6.unicast to AS42177 announce ANY
mp-export:      afi ipv6.unicast to AS42184 announce ANY
mp-export:      afi ipv6.unicast to AS42211 announce ANY
mp-export:      afi ipv6.unicast to AS42344 announce ANY
mp-export:      afi ipv6.unicast to AS42366 announce ANY
mp-export:      afi ipv6.unicast to AS42385 announce ANY
mp-export:      afi ipv6.unicast to AS42392 announce ANY
mp-export:      afi ipv6.unicast to AS42416 announce ANY
mp-export:      afi ipv6.unicast to AS42459 announce ANY
mp-export:      afi ipv6.unicast to AS42463 announce ANY
mp-export:      afi ipv6.unicast to AS42466 announce ANY
mp-export:      afi ipv6.unicast to AS42607 announce ANY
mp-export:      afi ipv6.unicast to AS42612 announce ANY
mp-export:      afi ipv6.unicast to AS42624 announce ANY
mp-export:      afi ipv6.unicast to AS42633 announce ANY
mp-export:      afi ipv6.unicast to AS42673 announce ANY
mp-export:      afi ipv6.unicast to AS42689 announce ANY
mp-export:      afi ipv6.unicast to AS42830 announce ANY
mp-export:      afi ipv6.unicast to AS42831 announce ANY
mp-export:      afi ipv6.unicast to AS42836 announce ANY
mp-export:      afi ipv6.unicast to AS42845 announce ANY
mp-export:      afi ipv6.unicast to AS42912 announce ANY
mp-export:      afi ipv6.unicast to AS42927 announce ANY
mp-export:      afi ipv6.unicast to AS42989 announce ANY
mp-export:      afi ipv6.unicast to AS43074 announce ANY
mp-export:      afi ipv6.unicast to AS43142 announce ANY
mp-export:      afi ipv6.unicast to AS43205 announce ANY
mp-export:      afi ipv6.unicast to AS43251 announce ANY
mp-export:      afi ipv6.unicast to AS43266 announce ANY
mp-export:      afi ipv6.unicast to AS43289 announce ANY
mp-export:      afi ipv6.unicast to AS43311 announce ANY
mp-export:      afi ipv6.unicast to AS43313 announce ANY
mp-export:      afi ipv6.unicast to AS43372 announce ANY
mp-export:      afi ipv6.unicast to AS43406 announce ANY
mp-export:      afi ipv6.unicast to AS43440 announce ANY
mp-export:      afi ipv6.unicast to AS43494 announce ANY
mp-export:      afi ipv6.unicast to AS43515 announce ANY
mp-export:      afi ipv6.unicast to AS43519 announce ANY
mp-export:      afi ipv6.unicast to AS43545 announce ANY
mp-export:      afi ipv6.unicast to AS43578 announce ANY
mp-export:      afi ipv6.unicast to AS43599 announce ANY
mp-export:      afi ipv6.unicast to AS43639 announce ANY
mp-export:      afi ipv6.unicast to AS43641 announce ANY
mp-export:      afi ipv6.unicast to AS43848 announce ANY
mp-export:      afi ipv6.unicast to AS43872 announce ANY
mp-export:      afi ipv6.unicast to AS43885 announce ANY
mp-export:      afi ipv6.unicast to AS43894 announce ANY
mp-export:      afi ipv6.unicast to AS43898 announce ANY
mp-export:      afi ipv6.unicast to AS43915 announce ANY
mp-export:      afi ipv6.unicast to AS44066 announce ANY
mp-export:      afi ipv6.unicast to AS44124 announce ANY
mp-export:      afi ipv6.unicast to AS44134 announce ANY
mp-export:      afi ipv6.unicast to AS44150 announce ANY
mp-export:      afi ipv6.unicast to AS44212 announce ANY
mp-export:      afi ipv6.unicast to AS44217 announce ANY
mp-export:      afi ipv6.unicast to AS44227 announce ANY
mp-export:      afi ipv6.unicast to AS44356 announce ANY
mp-export:      afi ipv6.unicast to AS44384 announce ANY
mp-export:      afi ipv6.unicast to AS44444 announce ANY
mp-export:      afi ipv6.unicast to AS44451 announce ANY
mp-export:      afi ipv6.unicast to AS44454 announce ANY
mp-export:      afi ipv6.unicast to AS44521 announce ANY
mp-export:      afi ipv6.unicast to AS44600 announce ANY
mp-export:      afi ipv6.unicast to AS44608 announce ANY
mp-export:      afi ipv6.unicast to AS44776 announce ANY
mp-export:      afi ipv6.unicast to AS44786 announce ANY
mp-export:      afi ipv6.unicast to AS44788 announce ANY
mp-export:      afi ipv6.unicast to AS44806 announce ANY
mp-export:      afi ipv6.unicast to AS44814 announce ANY
mp-export:      afi ipv6.unicast to AS44898 announce ANY
mp-export:      afi ipv6.unicast to AS44901 announce ANY
mp-export:      afi ipv6.unicast to AS44926 announce ANY
mp-export:      afi ipv6.unicast to AS44946 announce ANY
mp-export:      afi ipv6.unicast to AS44965 announce ANY
mp-export:      afi ipv6.unicast to AS44976 announce ANY
mp-export:      afi ipv6.unicast to AS45187 announce ANY
mp-export:      afi ipv6.unicast to AS45474 announce ANY
mp-export:      afi ipv6.unicast to AS45629 announce ANY
mp-export:      afi ipv6.unicast to AS45630 announce ANY
mp-export:      afi ipv6.unicast to AS45758 announce ANY
mp-export:      afi ipv6.unicast to AS45896 announce ANY
mp-export:      afi ipv6.unicast to AS45899 announce ANY
mp-export:      afi ipv6.unicast to AS46160 announce ANY
mp-export:      afi ipv6.unicast to AS46261 announce ANY
mp-export:      afi ipv6.unicast to AS46371 announce ANY
mp-export:      afi ipv6.unicast to AS46375 announce ANY
mp-export:      afi ipv6.unicast to AS46379 announce ANY
mp-export:      afi ipv6.unicast to AS46455 announce ANY
mp-export:      afi ipv6.unicast to AS46475 announce ANY
mp-export:      afi ipv6.unicast to AS46489 announce ANY
mp-export:      afi ipv6.unicast to AS46558 announce ANY
mp-export:      afi ipv6.unicast to AS46562 announce ANY
mp-export:      afi ipv6.unicast to AS46573 announce ANY
mp-export:      afi ipv6.unicast to AS46609 announce ANY
mp-export:      afi ipv6.unicast to AS46632 announce ANY
mp-export:      afi ipv6.unicast to AS46664 announce ANY
mp-export:      afi ipv6.unicast to AS46687 announce ANY
mp-export:      afi ipv6.unicast to AS46844 announce ANY
mp-export:      afi ipv6.unicast to AS46887 announce ANY
mp-export:      afi ipv6.unicast to AS46994 announce ANY
mp-export:      afi ipv6.unicast to AS47167 announce ANY
mp-export:      afi ipv6.unicast to AS47169 announce ANY
mp-export:      afi ipv6.unicast to AS47195 announce ANY
mp-export:      afi ipv6.unicast to AS47232 announce ANY
mp-export:      afi ipv6.unicast to AS47292 announce ANY
mp-export:      afi ipv6.unicast to AS47381 announce ANY
mp-export:      afi ipv6.unicast to AS47443 announce ANY
mp-export:      afi ipv6.unicast to AS47674 announce ANY
mp-export:      afi ipv6.unicast to AS47680 announce ANY
mp-export:      afi ipv6.unicast to AS47720 announce ANY
mp-export:      afi ipv6.unicast to AS47787 announce ANY
mp-export:      afi ipv6.unicast to AS47836 announce ANY
mp-export:      afi ipv6.unicast to AS47866 announce ANY
mp-export:      afi ipv6.unicast to AS47872 announce ANY
mp-export:      afi ipv6.unicast to AS47886 announce ANY
mp-export:      afi ipv6.unicast to AS47887 announce ANY
mp-export:      afi ipv6.unicast to AS47950 announce ANY
mp-export:      afi ipv6.unicast to AS47956 announce ANY
mp-export:      afi ipv6.unicast to AS47969 announce ANY
mp-export:      afi ipv6.unicast to AS47973 announce ANY
mp-export:      afi ipv6.unicast to AS48006 announce ANY
mp-export:      afi ipv6.unicast to AS48137 announce ANY
mp-export:      afi ipv6.unicast to AS48152 announce ANY
mp-export:      afi ipv6.unicast to AS48237 announce ANY
mp-export:      afi ipv6.unicast to AS48305 announce ANY
mp-export:      afi ipv6.unicast to AS48345 announce ANY
mp-export:      afi ipv6.unicast to AS48348 announce ANY
mp-export:      afi ipv6.unicast to AS48374 announce ANY
mp-export:      afi ipv6.unicast to AS48447 announce ANY
mp-export:      afi ipv6.unicast to AS48452 announce ANY
mp-export:      afi ipv6.unicast to AS48559 announce ANY
mp-export:      afi ipv6.unicast to AS48582 announce ANY
mp-export:      afi ipv6.unicast to AS48635 announce ANY
mp-export:      afi ipv6.unicast to AS48638 announce ANY
mp-export:      afi ipv6.unicast to AS48659 announce ANY
mp-export:      afi ipv6.unicast to AS48804 announce ANY
mp-export:      afi ipv6.unicast to AS48832 announce ANY
mp-export:      afi ipv6.unicast to AS48849 announce ANY
mp-export:      afi ipv6.unicast to AS48850 announce ANY
mp-export:      afi ipv6.unicast to AS48896 announce ANY
mp-export:      afi ipv6.unicast to AS48910 announce ANY
mp-export:      afi ipv6.unicast to AS48918 announce ANY
mp-export:      afi ipv6.unicast to AS48950 announce ANY
mp-export:      afi ipv6.unicast to AS48957 announce ANY
mp-export:      afi ipv6.unicast to AS48961 announce ANY
mp-export:      afi ipv6.unicast to AS48964 announce ANY
mp-export:      afi ipv6.unicast to AS49088 announce ANY
mp-export:      afi ipv6.unicast to AS49102 announce ANY
mp-export:      afi ipv6.unicast to AS49158 announce ANY
mp-export:      afi ipv6.unicast to AS49216 announce ANY
mp-export:      afi ipv6.unicast to AS49220 announce ANY
mp-export:      afi ipv6.unicast to AS49229 announce ANY
mp-export:      afi ipv6.unicast to AS49289 announce ANY
mp-export:      afi ipv6.unicast to AS49296 announce ANY
mp-export:      afi ipv6.unicast to AS49405 announce ANY
mp-export:      afi ipv6.unicast to AS49415 announce ANY
mp-export:      afi ipv6.unicast to AS49425 announce ANY
mp-export:      afi ipv6.unicast to AS49434 announce ANY
mp-export:      afi ipv6.unicast to AS49515 announce ANY
mp-export:      afi ipv6.unicast to AS49567 announce ANY
mp-export:      afi ipv6.unicast to AS49600 announce ANY
mp-export:      afi ipv6.unicast to AS49605 announce ANY
mp-export:      afi ipv6.unicast to AS49607 announce ANY
mp-export:      afi ipv6.unicast to AS49683 announce ANY
mp-export:      afi ipv6.unicast to AS49765 announce ANY
mp-export:      afi ipv6.unicast to AS49870 announce ANY
mp-export:      afi ipv6.unicast to AS49915 announce ANY
mp-export:      afi ipv6.unicast to AS50121 announce ANY
mp-export:      afi ipv6.unicast to AS50173 announce ANY
mp-export:      afi ipv6.unicast to AS50188 announce ANY
mp-export:      afi ipv6.unicast to AS50226 announce ANY
mp-export:      afi ipv6.unicast to AS50245 announce ANY
mp-export:      afi ipv6.unicast to AS50292 announce ANY
mp-export:      afi ipv6.unicast to AS50300 announce ANY
mp-export:      afi ipv6.unicast to AS50331 announce ANY
mp-export:      afi ipv6.unicast to AS50343 announce ANY
mp-export:      afi ipv6.unicast to AS50360 announce ANY
mp-export:      afi ipv6.unicast to AS50469 announce ANY
mp-export:      afi ipv6.unicast to AS50581 announce ANY
mp-export:      afi ipv6.unicast to AS50625 announce ANY
mp-export:      afi ipv6.unicast to AS50835 announce ANY
mp-export:      afi ipv6.unicast to AS50877 announce ANY
mp-export:      afi ipv6.unicast to AS50974 announce ANY
mp-export:      afi ipv6.unicast to AS51043 announce ANY
mp-export:      afi ipv6.unicast to AS51088 announce ANY
mp-export:      afi ipv6.unicast to AS51269 announce ANY
mp-export:      afi ipv6.unicast to AS51310 announce ANY
mp-export:      afi ipv6.unicast to AS51394 announce ANY
mp-export:      afi ipv6.unicast to AS51395 announce ANY
mp-export:      afi ipv6.unicast to AS51399 announce ANY
mp-export:      afi ipv6.unicast to AS51406 announce ANY
mp-export:      afi ipv6.unicast to AS51407 announce ANY
mp-export:      afi ipv6.unicast to AS51483 announce ANY
mp-export:      afi ipv6.unicast to AS51510 announce ANY
mp-export:      afi ipv6.unicast to AS51580 announce ANY
mp-export:      afi ipv6.unicast to AS51582 announce ANY
mp-export:      afi ipv6.unicast to AS51616 announce ANY
mp-export:      afi ipv6.unicast to AS51752 announce ANY
mp-export:      afi ipv6.unicast to AS51796 announce ANY
mp-export:      afi ipv6.unicast to AS51809 announce ANY
mp-export:      afi ipv6.unicast to AS51820 announce ANY
mp-export:      afi ipv6.unicast to AS51852 announce ANY
mp-export:      afi ipv6.unicast to AS51857 announce ANY
mp-export:      afi ipv6.unicast to AS51871 announce ANY
mp-export:      afi ipv6.unicast to AS51890 announce ANY
mp-export:      afi ipv6.unicast to AS51944 announce ANY
mp-export:      afi ipv6.unicast to AS52030 announce ANY
mp-export:      afi ipv6.unicast to AS52106 announce ANY
mp-export:      afi ipv6.unicast to AS52320 announce ANY
mp-export:      afi ipv6.unicast to AS52347 announce ANY
mp-export:      afi ipv6.unicast to AS52393 announce ANY
mp-export:      afi ipv6.unicast to AS52438 announce ANY
mp-export:      afi ipv6.unicast to AS52580 announce ANY
mp-export:      afi ipv6.unicast to AS52873 announce ANY
mp-export:      afi ipv6.unicast to AS53264 announce ANY
mp-export:      afi ipv6.unicast to AS53292 announce ANY
mp-export:      afi ipv6.unicast to AS53340 announce ANY
mp-export:      afi ipv6.unicast to AS53388 announce ANY
mp-export:      afi ipv6.unicast to AS53428 announce ANY
mp-export:      afi ipv6.unicast to AS53582 announce ANY
mp-export:      afi ipv6.unicast to AS53620 announce ANY
mp-export:      afi ipv6.unicast to AS53667 announce ANY
mp-export:      afi ipv6.unicast to AS53722 announce ANY
mp-export:      afi ipv6.unicast to AS53726 announce ANY
mp-export:      afi ipv6.unicast to AS53764 announce ANY
mp-export:      afi ipv6.unicast to AS53766 announce ANY
mp-export:      afi ipv6.unicast to AS53813 announce ANY
mp-export:      afi ipv6.unicast to AS53828 announce ANY
mp-export:      afi ipv6.unicast to AS53845 announce ANY
mp-export:      afi ipv6.unicast to AS53850 announce ANY
mp-export:      afi ipv6.unicast to AS53856 announce ANY
mp-export:      afi ipv6.unicast to AS53902 announce ANY
mp-export:      afi ipv6.unicast to AS53914 announce ANY
mp-export:      afi ipv6.unicast to AS53939 announce ANY
mp-export:      afi ipv6.unicast to AS54040 announce ANY
mp-export:      afi ipv6.unicast to AS54103 announce ANY
mp-export:      afi ipv6.unicast to AS54125 announce ANY
mp-export:      afi ipv6.unicast to AS54197 announce ANY
mp-export:      afi ipv6.unicast to AS54201 announce ANY
mp-export:      afi ipv6.unicast to AS54235 announce ANY
mp-export:      afi ipv6.unicast to AS54303 announce ANY
mp-export:      afi ipv6.unicast to AS54312 announce ANY
mp-export:      afi ipv6.unicast to AS54329 announce ANY
mp-export:      afi ipv6.unicast to AS54359 announce ANY
mp-export:      afi ipv6.unicast to AS54455 announce ANY
mp-export:      afi ipv6.unicast to AS54483 announce ANY
mp-export:      afi ipv6.unicast to AS54489 announce ANY
mp-export:      afi ipv6.unicast to AS54509 announce ANY
mp-export:      afi ipv6.unicast to AS54527 announce ANY
mp-export:      afi ipv6.unicast to AS54588 announce ANY
mp-export:      afi ipv6.unicast to AS54641 announce ANY
mp-export:      afi ipv6.unicast to AS54652 announce ANY
mp-export:      afi ipv6.unicast to AS54778 announce ANY
mp-export:      afi ipv6.unicast to AS54816 announce ANY
mp-export:      afi ipv6.unicast to AS54825 announce ANY
mp-export:      afi ipv6.unicast to AS54913 announce ANY
mp-export:      afi ipv6.unicast to AS54957 announce ANY
mp-export:      afi ipv6.unicast to AS54994 announce ANY
mp-export:      afi ipv6.unicast to AS55002 announce ANY
mp-export:      afi ipv6.unicast to AS55011 announce ANY
mp-export:      afi ipv6.unicast to AS55061 announce ANY
mp-export:      afi ipv6.unicast to AS55081 announce ANY
mp-export:      afi ipv6.unicast to AS55191 announce ANY
mp-export:      afi ipv6.unicast to AS55195 announce ANY
mp-export:      afi ipv6.unicast to AS55256 announce ANY
mp-export:      afi ipv6.unicast to AS55259 announce ANY
mp-export:      afi ipv6.unicast to AS55891 announce ANY
mp-export:      afi ipv6.unicast to AS55943 announce ANY
mp-export:      afi ipv6.unicast to AS56286 announce ANY
mp-export:      afi ipv6.unicast to AS56381 announce ANY
mp-export:      afi ipv6.unicast to AS56474 announce ANY
mp-export:      afi ipv6.unicast to AS56478 announce ANY
mp-export:      afi ipv6.unicast to AS56504 announce ANY
mp-export:      afi ipv6.unicast to AS56511 announce ANY
mp-export:      afi ipv6.unicast to AS56515 announce ANY
mp-export:      afi ipv6.unicast to AS56595 announce ANY
mp-export:      afi ipv6.unicast to AS56611 announce ANY
mp-export:      afi ipv6.unicast to AS56630 announce ANY
mp-export:      afi ipv6.unicast to AS56647 announce ANY
mp-export:      afi ipv6.unicast to AS56655 announce ANY
mp-export:      afi ipv6.unicast to AS56683 announce ANY
mp-export:      afi ipv6.unicast to AS56767 announce ANY
mp-export:      afi ipv6.unicast to AS56786 announce ANY
mp-export:      afi ipv6.unicast to AS56894 announce ANY
mp-export:      afi ipv6.unicast to AS56953 announce ANY
mp-export:      afi ipv6.unicast to AS56958 announce ANY
mp-export:      afi ipv6.unicast to AS56990 announce ANY
mp-export:      afi ipv6.unicast to AS57111 announce ANY
mp-export:      afi ipv6.unicast to AS57141 announce ANY
mp-export:      afi ipv6.unicast to AS57169 announce ANY
mp-export:      afi ipv6.unicast to AS57276 announce ANY
mp-export:      afi ipv6.unicast to AS57332 announce ANY
mp-export:      afi ipv6.unicast to AS57344 announce ANY
mp-export:      afi ipv6.unicast to AS57607 announce ANY
mp-export:      afi ipv6.unicast to AS57626 announce ANY
mp-export:      afi ipv6.unicast to AS57704 announce ANY
mp-export:      afi ipv6.unicast to AS57717 announce ANY
mp-export:      afi ipv6.unicast to AS57723 announce ANY
mp-export:      afi ipv6.unicast to AS57750 announce ANY
mp-export:      afi ipv6.unicast to AS57795 announce ANY
mp-export:      afi ipv6.unicast to AS57811 announce ANY
mp-export:      afi ipv6.unicast to AS57877 announce ANY
mp-export:      afi ipv6.unicast to AS57896 announce ANY
mp-export:      afi ipv6.unicast to AS57976 announce ANY
mp-export:      afi ipv6.unicast to AS58065 announce ANY
mp-export:      afi ipv6.unicast to AS58246 announce ANY
mp-export:      afi ipv6.unicast to AS58307 announce ANY
mp-export:      afi ipv6.unicast to AS58321 announce ANY
mp-export:      afi ipv6.unicast to AS58453 announce ANY
mp-export:      afi ipv6.unicast to AS58511 announce ANY
mp-export:      afi ipv6.unicast to AS58664 announce ANY
mp-export:      afi ipv6.unicast to AS59028 announce ANY
mp-export:      afi ipv6.unicast to AS59253 announce ANY
mp-export:      afi ipv6.unicast to AS59371 announce ANY
mp-export:      afi ipv6.unicast to AS59432 announce ANY
mp-export:      afi ipv6.unicast to AS59455 announce ANY
mp-export:      afi ipv6.unicast to AS59524 announce ANY
mp-export:      afi ipv6.unicast to AS59545 announce ANY
mp-export:      afi ipv6.unicast to AS59580 announce ANY
mp-export:      afi ipv6.unicast to AS59605 announce ANY
mp-export:      afi ipv6.unicast to AS59711 announce ANY
mp-export:      afi ipv6.unicast to AS59816 announce ANY
mp-export:      afi ipv6.unicast to AS59827 announce ANY
mp-export:      afi ipv6.unicast to AS59842 announce ANY
mp-export:      afi ipv6.unicast to AS59865 announce ANY
mp-export:      afi ipv6.unicast to AS59933 announce ANY
mp-export:      afi ipv6.unicast to AS60022 announce ANY
mp-export:      afi ipv6.unicast to AS60033 announce ANY
mp-export:      afi ipv6.unicast to AS60038 announce ANY
mp-export:      afi ipv6.unicast to AS60068 announce ANY
mp-export:      afi ipv6.unicast to AS60144 announce ANY
mp-export:      afi ipv6.unicast to AS60193 announce ANY
mp-export:      afi ipv6.unicast to AS60339 announce ANY
mp-export:      afi ipv6.unicast to AS60362 announce ANY
mp-export:      afi ipv6.unicast to AS60384 announce ANY
mp-export:      afi ipv6.unicast to AS60404 announce ANY
mp-export:      afi ipv6.unicast to AS60436 announce ANY
mp-export:      afi ipv6.unicast to AS60447 announce ANY
mp-export:      afi ipv6.unicast to AS60475 announce ANY
mp-export:      afi ipv6.unicast to AS60481 announce ANY
mp-export:      afi ipv6.unicast to AS60486 announce ANY
mp-export:      afi ipv6.unicast to AS60497 announce ANY
mp-export:      afi ipv6.unicast to AS60501 announce ANY
mp-export:      afi ipv6.unicast to AS60624 announce ANY
mp-export:      afi ipv6.unicast to AS60636 announce ANY
mp-export:      afi ipv6.unicast to AS60670 announce ANY
mp-export:      afi ipv6.unicast to AS60706 announce ANY
mp-export:      afi ipv6.unicast to AS60758 announce ANY
mp-export:      afi ipv6.unicast to AS60781 announce ANY
mp-export:      afi ipv6.unicast to AS60798 announce ANY
mp-export:      afi ipv6.unicast to AS60800 announce ANY
mp-export:      afi ipv6.unicast to AS60893 announce ANY
mp-export:      afi ipv6.unicast to AS60940 announce ANY
mp-export:      afi ipv6.unicast to AS61003 announce ANY
mp-export:      afi ipv6.unicast to AS61046 announce ANY
mp-export:      afi ipv6.unicast to AS61049 announce ANY
mp-export:      afi ipv6.unicast to AS61149 announce ANY
mp-export:      afi ipv6.unicast to AS61154 announce ANY
mp-export:      afi ipv6.unicast to AS61215 announce ANY
mp-export:      afi ipv6.unicast to AS61244 announce ANY
mp-export:      afi ipv6.unicast to AS61266 announce ANY
mp-export:      afi ipv6.unicast to AS61273 announce ANY
mp-export:      afi ipv6.unicast to AS61315 announce ANY
mp-export:      afi ipv6.unicast to AS61317 announce ANY
mp-export:      afi ipv6.unicast to AS61323 announce ANY
mp-export:      afi ipv6.unicast to AS61349 announce ANY
mp-export:      afi ipv6.unicast to AS61373 announce ANY
mp-export:      afi ipv6.unicast to AS61430 announce ANY
mp-export:      afi ipv6.unicast to AS61461 announce ANY
mp-export:      afi ipv6.unicast to AS61573 announce ANY
mp-export:      afi ipv6.unicast to AS62044 announce ANY
mp-export:      afi ipv6.unicast to AS62068 announce ANY
mp-export:      afi ipv6.unicast to AS62081 announce ANY
mp-export:      afi ipv6.unicast to AS62087 announce ANY
mp-export:      afi ipv6.unicast to AS62167 announce ANY
mp-export:      afi ipv6.unicast to AS62168 announce ANY
mp-export:      afi ipv6.unicast to AS62184 announce ANY
mp-export:      afi ipv6.unicast to AS62190 announce ANY
mp-export:      afi ipv6.unicast to AS62234 announce ANY
mp-export:      afi ipv6.unicast to AS62240 announce ANY
mp-export:      afi ipv6.unicast to AS62244 announce ANY
mp-export:      afi ipv6.unicast to AS62363 announce ANY
mp-export:      afi ipv6.unicast to AS62488 announce ANY
mp-export:      afi ipv6.unicast to AS62542 announce ANY
mp-export:      afi ipv6.unicast to AS62563 announce ANY
mp-export:      afi ipv6.unicast to AS62597 announce ANY
mp-export:      afi ipv6.unicast to AS62638 announce ANY
mp-export:      afi ipv6.unicast to AS62646 announce ANY
mp-export:      afi ipv6.unicast to AS62648 announce ANY
mp-export:      afi ipv6.unicast to AS62698 announce ANY
mp-export:      afi ipv6.unicast to AS62710 announce ANY
mp-export:      afi ipv6.unicast to AS62713 announce ANY
mp-export:      afi ipv6.unicast to AS62728 announce ANY
mp-export:      afi ipv6.unicast to AS62799 announce ANY
mp-export:      afi ipv6.unicast to AS62815 announce ANY
mp-export:      afi ipv6.unicast to AS62833 announce ANY
mp-export:      afi ipv6.unicast to AS62874 announce ANY
mp-export:      afi ipv6.unicast to AS62887 announce ANY
mp-export:      afi ipv6.unicast to AS62955 announce ANY
mp-export:      afi ipv6.unicast to AS63008 announce ANY
mp-export:      afi ipv6.unicast to AS63023 announce ANY
mp-export:      afi ipv6.unicast to AS63086 announce ANY
mp-export:      afi ipv6.unicast to AS63110 announce ANY
mp-export:      afi ipv6.unicast to AS63157 announce ANY
mp-export:      afi ipv6.unicast to AS63199 announce ANY
mp-export:      afi ipv6.unicast to AS63213 announce ANY
mp-export:      afi ipv6.unicast to AS63267 announce ANY
mp-export:      afi ipv6.unicast to AS63287 announce ANY
mp-export:      afi ipv6.unicast to AS63311 announce ANY
mp-export:      afi ipv6.unicast to AS63351 announce ANY
mp-export:      afi ipv6.unicast to AS63365 announce ANY
mp-export:      afi ipv6.unicast to AS63383 announce ANY
mp-export:      afi ipv6.unicast to AS63399 announce ANY
mp-export:      afi ipv6.unicast to AS63452 announce ANY
mp-export:      afi ipv6.unicast to AS63916 announce ANY
mp-export:      afi ipv6.unicast to AS63949 announce ANY
mp-export:      afi ipv6.unicast to AS64022 announce ANY
mp-export:      afi ipv6.unicast to AS64096 announce ANY
mp-export:      afi ipv6.unicast to AS64122 announce ANY
mp-export:      afi ipv6.unicast to AS64275 announce ANY
mp-export:      afi ipv6.unicast to AS64277 announce ANY
mp-export:      afi ipv6.unicast to AS64304 announce ANY
mp-export:      afi ipv6.unicast to AS64426 announce ANY
mp-export:      afi ipv6.unicast to AS131274 announce ANY
mp-export:      afi ipv6.unicast to AS131314 announce ANY
mp-export:      afi ipv6.unicast to AS133335 announce ANY
mp-export:      afi ipv6.unicast to AS133752 announce ANY
mp-export:      afi ipv6.unicast to AS134345 announce ANY
mp-export:      afi ipv6.unicast to AS134351 announce ANY
mp-export:      afi ipv6.unicast to AS135356 announce ANY
mp-export:      afi ipv6.unicast to AS135391 announce ANY
mp-export:      afi ipv6.unicast to AS136897 announce ANY
mp-export:      afi ipv6.unicast to AS137753 announce ANY
mp-export:      afi ipv6.unicast to AS137816 announce ANY
mp-export:      afi ipv6.unicast to AS137912 announce ANY
mp-export:      afi ipv6.unicast to AS138005 announce ANY
mp-export:      afi ipv6.unicast to AS138576 announce ANY
mp-export:      afi ipv6.unicast to AS138611 announce ANY
mp-export:      afi ipv6.unicast to AS141039 announce ANY
mp-export:      afi ipv6.unicast to AS147049 announce ANY
mp-export:      afi ipv6.unicast to AS196640 announce ANY
mp-export:      afi ipv6.unicast to AS196670 announce ANY
mp-export:      afi ipv6.unicast to AS196729 announce ANY
mp-export:      afi ipv6.unicast to AS196755 announce ANY
mp-export:      afi ipv6.unicast to AS196975 announce ANY
mp-export:      afi ipv6.unicast to AS197036 announce ANY
mp-export:      afi ipv6.unicast to AS197071 announce ANY
mp-export:      afi ipv6.unicast to AS197075 announce ANY
mp-export:      afi ipv6.unicast to AS197106 announce ANY
mp-export:      afi ipv6.unicast to AS197116 announce ANY
mp-export:      afi ipv6.unicast to AS197156 announce ANY
mp-export:      afi ipv6.unicast to AS197226 announce ANY
mp-export:      afi ipv6.unicast to AS197308 announce ANY
mp-export:      afi ipv6.unicast to AS197437 announce ANY
mp-export:      afi ipv6.unicast to AS197447 announce ANY
mp-export:      afi ipv6.unicast to AS197518 announce ANY
mp-export:      afi ipv6.unicast to AS197549 announce ANY
mp-export:      afi ipv6.unicast to AS197573 announce ANY
mp-export:      afi ipv6.unicast to AS197592 announce ANY
mp-export:      afi ipv6.unicast to AS197610 announce ANY
mp-export:      afi ipv6.unicast to AS197651 announce ANY
mp-export:      afi ipv6.unicast to AS197669 announce ANY
mp-export:      afi ipv6.unicast to AS197690 announce ANY
mp-export:      afi ipv6.unicast to AS197712 announce ANY
mp-export:      afi ipv6.unicast to AS197727 announce ANY
mp-export:      afi ipv6.unicast to AS197883 announce ANY
mp-export:      afi ipv6.unicast to AS197902 announce ANY
mp-export:      afi ipv6.unicast to AS198040 announce ANY
mp-export:      afi ipv6.unicast to AS198203 announce ANY
mp-export:      afi ipv6.unicast to AS198211 announce ANY
mp-export:      afi ipv6.unicast to AS198260 announce ANY
mp-export:      afi ipv6.unicast to AS198279 announce ANY
mp-export:      afi ipv6.unicast to AS198334 announce ANY
mp-export:      afi ipv6.unicast to AS198374 announce ANY
mp-export:      afi ipv6.unicast to AS198440 announce ANY
mp-export:      afi ipv6.unicast to AS198452 announce ANY
mp-export:      afi ipv6.unicast to AS198471 announce ANY
mp-export:      afi ipv6.unicast to AS198651 announce ANY
mp-export:      afi ipv6.unicast to AS198726 announce ANY
mp-export:      afi ipv6.unicast to AS198761 announce ANY
mp-export:      afi ipv6.unicast to AS198847 announce ANY
mp-export:      afi ipv6.unicast to AS198890 announce ANY
mp-export:      afi ipv6.unicast to AS198949 announce ANY
mp-export:      afi ipv6.unicast to AS199081 announce ANY
mp-export:      afi ipv6.unicast to AS199113 announce ANY
mp-export:      afi ipv6.unicast to AS199156 announce ANY
mp-export:      afi ipv6.unicast to AS199163 announce ANY
mp-export:      afi ipv6.unicast to AS199237 announce ANY
mp-export:      afi ipv6.unicast to AS199250 announce ANY
mp-export:      afi ipv6.unicast to AS199283 announce ANY
mp-export:      afi ipv6.unicast to AS199338 announce ANY
mp-export:      afi ipv6.unicast to AS199358 announce ANY
mp-export:      afi ipv6.unicast to AS199410 announce ANY
mp-export:      afi ipv6.unicast to AS199483 announce ANY
mp-export:      afi ipv6.unicast to AS199496 announce ANY
mp-export:      afi ipv6.unicast to AS199524 announce ANY
mp-export:      afi ipv6.unicast to AS199559 announce ANY
mp-export:      afi ipv6.unicast to AS199569 announce ANY
mp-export:      afi ipv6.unicast to AS199710 announce ANY
mp-export:      afi ipv6.unicast to AS199713 announce ANY
mp-export:      afi ipv6.unicast to AS199775 announce ANY
mp-export:      afi ipv6.unicast to AS199790 announce ANY
mp-export:      afi ipv6.unicast to AS199799 announce ANY
mp-export:      afi ipv6.unicast to AS199880 announce ANY
mp-export:      afi ipv6.unicast to AS199892 announce ANY
mp-export:      afi ipv6.unicast to AS200032 announce ANY
mp-export:      afi ipv6.unicast to AS200052 announce ANY
mp-export:      afi ipv6.unicast to AS200099 announce ANY
mp-export:      afi ipv6.unicast to AS200187 announce ANY
mp-export:      afi ipv6.unicast to AS200271 announce ANY
mp-export:      afi ipv6.unicast to AS200410 announce ANY
mp-export:      afi ipv6.unicast to AS200416 announce ANY
mp-export:      afi ipv6.unicast to AS200425 announce ANY
mp-export:      afi ipv6.unicast to AS200462 announce ANY
mp-export:      afi ipv6.unicast to AS200552 announce ANY
mp-export:      afi ipv6.unicast to AS200562 announce ANY
mp-export:      afi ipv6.unicast to AS200573 announce ANY
mp-export:      afi ipv6.unicast to AS200596 announce ANY
mp-export:      afi ipv6.unicast to AS200612 announce ANY
mp-export:      afi ipv6.unicast to AS200653 announce ANY
mp-export:      afi ipv6.unicast to AS200705 announce ANY
mp-export:      afi ipv6.unicast to AS200713 announce ANY
mp-export:      afi ipv6.unicast to AS200738 announce ANY
mp-export:      afi ipv6.unicast to AS200758 announce ANY
mp-export:      afi ipv6.unicast to AS200780 announce ANY
mp-export:      afi ipv6.unicast to AS200845 announce ANY
mp-export:      afi ipv6.unicast to AS200861 announce ANY
mp-export:      afi ipv6.unicast to AS200899 announce ANY
mp-export:      afi ipv6.unicast to AS200904 announce ANY
mp-export:      afi ipv6.unicast to AS200961 announce ANY
mp-export:      afi ipv6.unicast to AS200994 announce ANY
mp-export:      afi ipv6.unicast to AS201067 announce ANY
mp-export:      afi ipv6.unicast to AS201126 announce ANY
mp-export:      afi ipv6.unicast to AS201133 announce ANY
mp-export:      afi ipv6.unicast to AS201188 announce ANY
mp-export:      afi ipv6.unicast to AS201196 announce ANY
mp-export:      afi ipv6.unicast to AS201213 announce ANY
mp-export:      afi ipv6.unicast to AS201222 announce ANY
mp-export:      afi ipv6.unicast to AS201246 announce ANY
mp-export:      afi ipv6.unicast to AS201324 announce ANY
mp-export:      afi ipv6.unicast to AS201333 announce ANY
mp-export:      afi ipv6.unicast to AS201525 announce ANY
mp-export:      afi ipv6.unicast to AS201565 announce ANY
mp-export:      afi ipv6.unicast to AS201602 announce ANY
mp-export:      afi ipv6.unicast to AS201731 announce ANY
mp-export:      afi ipv6.unicast to AS201789 announce ANY
mp-export:      afi ipv6.unicast to AS201895 announce ANY
mp-export:      afi ipv6.unicast to AS201942 announce ANY
mp-export:      afi ipv6.unicast to AS201947 announce ANY
mp-export:      afi ipv6.unicast to AS201958 announce ANY
mp-export:      afi ipv6.unicast to AS201971 announce ANY
mp-export:      afi ipv6.unicast to AS201990 announce ANY
mp-export:      afi ipv6.unicast to AS202010 announce ANY
mp-export:      afi ipv6.unicast to AS202032 announce ANY
mp-export:      afi ipv6.unicast to AS202075 announce ANY
mp-export:      afi ipv6.unicast to AS202623 announce ANY
mp-export:      afi ipv6.unicast to AS202713 announce ANY
mp-export:      afi ipv6.unicast to AS202766 announce ANY
mp-export:      afi ipv6.unicast to AS203050 announce ANY
mp-export:      afi ipv6.unicast to AS203055 announce ANY
mp-export:      afi ipv6.unicast to AS203182 announce ANY
mp-export:      afi ipv6.unicast to AS203223 announce ANY
mp-export:      afi ipv6.unicast to AS203256 announce ANY
mp-export:      afi ipv6.unicast to AS203316 announce ANY
mp-export:      afi ipv6.unicast to AS203346 announce ANY
mp-export:      afi ipv6.unicast to AS203351 announce ANY
mp-export:      afi ipv6.unicast to AS203410 announce ANY
mp-export:      afi ipv6.unicast to AS203608 announce ANY
mp-export:      afi ipv6.unicast to AS203639 announce ANY
mp-export:      afi ipv6.unicast to AS203649 announce ANY
mp-export:      afi ipv6.unicast to AS203724 announce ANY
mp-export:      afi ipv6.unicast to AS204126 announce ANY
mp-export:      afi ipv6.unicast to AS204188 announce ANY
mp-export:      afi ipv6.unicast to AS204258 announce ANY
mp-export:      afi ipv6.unicast to AS204260 announce ANY
mp-export:      afi ipv6.unicast to AS204353 announce ANY
mp-export:      afi ipv6.unicast to AS204419 announce ANY
mp-export:      afi ipv6.unicast to AS204476 announce ANY
mp-export:      afi ipv6.unicast to AS204536 announce ANY
mp-export:      afi ipv6.unicast to AS204548 announce ANY
mp-export:      afi ipv6.unicast to AS204563 announce ANY
mp-export:      afi ipv6.unicast to AS204577 announce ANY
mp-export:      afi ipv6.unicast to AS204641 announce ANY
mp-export:      afi ipv6.unicast to AS204801 announce ANY
mp-export:      afi ipv6.unicast to AS204807 announce ANY
mp-export:      afi ipv6.unicast to AS204959 announce ANY
mp-export:      afi ipv6.unicast to AS204981 announce ANY
mp-export:      afi ipv6.unicast to AS205016 announce ANY
mp-export:      afi ipv6.unicast to AS205025 announce ANY
mp-export:      afi ipv6.unicast to AS205039 announce ANY
mp-export:      afi ipv6.unicast to AS205041 announce ANY
mp-export:      afi ipv6.unicast to AS205142 announce ANY
mp-export:      afi ipv6.unicast to AS205185 announce ANY
mp-export:      afi ipv6.unicast to AS205394 announce ANY
mp-export:      afi ipv6.unicast to AS205476 announce ANY
mp-export:      afi ipv6.unicast to AS205544 announce ANY
mp-export:      afi ipv6.unicast to AS205668 announce ANY
mp-export:      afi ipv6.unicast to AS205697 announce ANY
mp-export:      afi ipv6.unicast to AS205736 announce ANY
mp-export:      afi ipv6.unicast to AS205809 announce ANY
mp-export:      afi ipv6.unicast to AS205842 announce ANY
mp-export:      afi ipv6.unicast to AS205943 announce ANY
mp-export:      afi ipv6.unicast to AS206067 announce ANY
mp-export:      afi ipv6.unicast to AS206121 announce ANY
mp-export:      afi ipv6.unicast to AS206168 announce ANY
mp-export:      afi ipv6.unicast to AS206264 announce ANY
mp-export:      afi ipv6.unicast to AS206370 announce ANY
mp-export:      afi ipv6.unicast to AS206372 announce ANY
mp-export:      afi ipv6.unicast to AS206383 announce ANY
mp-export:      afi ipv6.unicast to AS206399 announce ANY
mp-export:      afi ipv6.unicast to AS206459 announce ANY
mp-export:      afi ipv6.unicast to AS206537 announce ANY
mp-export:      afi ipv6.unicast to AS206567 announce ANY
mp-export:      afi ipv6.unicast to AS206576 announce ANY
mp-export:      afi ipv6.unicast to AS206614 announce ANY
mp-export:      afi ipv6.unicast to AS206701 announce ANY
mp-export:      afi ipv6.unicast to AS206747 announce ANY
mp-export:      afi ipv6.unicast to AS206793 announce ANY
mp-export:      afi ipv6.unicast to AS206892 announce ANY
mp-export:      afi ipv6.unicast to AS206983 announce ANY
mp-export:      afi ipv6.unicast to AS206984 announce ANY
mp-export:      afi ipv6.unicast to AS207044 announce ANY
mp-export:      afi ipv6.unicast to AS207045 announce ANY
mp-export:      afi ipv6.unicast to AS207063 announce ANY
mp-export:      afi ipv6.unicast to AS207127 announce ANY
mp-export:      afi ipv6.unicast to AS207137 announce ANY
mp-export:      afi ipv6.unicast to AS207176 announce ANY
mp-export:      afi ipv6.unicast to AS207367 announce ANY
mp-export:      afi ipv6.unicast to AS207543 announce ANY
mp-export:      afi ipv6.unicast to AS207686 announce ANY
mp-export:      afi ipv6.unicast to AS207747 announce ANY
mp-export:      afi ipv6.unicast to AS207784 announce ANY
mp-export:      afi ipv6.unicast to AS207995 announce ANY
mp-export:      afi ipv6.unicast to AS208350 announce ANY
mp-export:      afi ipv6.unicast to AS208374 announce ANY
mp-export:      afi ipv6.unicast to AS208416 announce ANY
mp-export:      afi ipv6.unicast to AS208586 announce ANY
mp-export:      afi ipv6.unicast to AS208625 announce ANY
mp-export:      afi ipv6.unicast to AS208693 announce ANY
mp-export:      afi ipv6.unicast to AS208877 announce ANY
mp-export:      afi ipv6.unicast to AS209181 announce ANY
mp-export:      afi ipv6.unicast to AS209282 announce ANY
mp-export:      afi ipv6.unicast to AS209311 announce ANY
mp-export:      afi ipv6.unicast to AS209549 announce ANY
mp-export:      afi ipv6.unicast to AS209704 announce ANY
mp-export:      afi ipv6.unicast to AS209811 announce ANY
mp-export:      afi ipv6.unicast to AS210211 announce ANY
mp-export:      afi ipv6.unicast to AS210253 announce ANY
mp-export:      afi ipv6.unicast to AS210269 announce ANY
mp-export:      afi ipv6.unicast to AS210321 announce ANY
mp-export:      afi ipv6.unicast to AS210329 announce ANY
mp-export:      afi ipv6.unicast to AS211029 announce ANY
mp-export:      afi ipv6.unicast to AS211526 announce ANY
mp-export:      afi ipv6.unicast to AS211597 announce ANY
mp-export:      afi ipv6.unicast to AS212045 announce ANY
mp-export:      afi ipv6.unicast to AS212055 announce ANY
mp-export:      afi ipv6.unicast to AS212097 announce ANY
mp-export:      afi ipv6.unicast to AS212175 announce ANY
mp-export:      afi ipv6.unicast to AS212708 announce ANY
mp-export:      afi ipv6.unicast to AS212882 announce ANY
mp-export:      afi ipv6.unicast to AS213039 announce ANY
mp-export:      afi ipv6.unicast to AS213094 announce ANY
mp-export:      afi ipv6.unicast to AS213101 announce ANY
mp-export:      afi ipv6.unicast to AS213202 announce ANY
mp-export:      afi ipv6.unicast to AS213205 announce ANY
mp-export:      afi ipv6.unicast to AS213308 announce ANY
mp-export:      afi ipv6.unicast to AS213373 announce ANY
mp-export:      afi ipv6.unicast to AS262206 announce ANY
mp-export:      afi ipv6.unicast to AS262287 announce ANY
mp-export:      afi ipv6.unicast to AS262589 announce ANY
mp-export:      afi ipv6.unicast to AS262916 announce ANY
mp-export:      afi ipv6.unicast to AS263179 announce ANY
mp-export:      afi ipv6.unicast to AS263735 announce ANY
mp-export:      afi ipv6.unicast to AS264409 announce ANY
mp-export:      afi ipv6.unicast to AS264763 announce ANY
mp-export:      afi ipv6.unicast to AS265556 announce ANY
mp-export:      afi ipv6.unicast to AS265680 announce ANY
mp-export:      afi ipv6.unicast to AS393234 announce ANY
mp-export:      afi ipv6.unicast to AS393241 announce ANY
mp-export:      afi ipv6.unicast to AS393246 announce ANY
mp-export:      afi ipv6.unicast to AS393544 announce ANY
mp-export:      afi ipv6.unicast to AS393676 announce ANY
mp-export:      afi ipv6.unicast to AS393845 announce ANY
mp-export:      afi ipv6.unicast to AS393886 announce ANY
mp-export:      afi ipv6.unicast to AS393900 announce ANY
mp-export:      afi ipv6.unicast to AS394015 announce ANY
mp-export:      afi ipv6.unicast to AS394102 announce ANY
mp-export:      afi ipv6.unicast to AS394141 announce ANY
mp-export:      afi ipv6.unicast to AS394186 announce ANY
mp-export:      afi ipv6.unicast to AS394232 announce ANY
mp-export:      afi ipv6.unicast to AS394303 announce ANY
mp-export:      afi ipv6.unicast to AS394308 announce ANY
mp-export:      afi ipv6.unicast to AS394346 announce ANY
mp-export:      afi ipv6.unicast to AS394354 announce ANY
mp-export:      afi ipv6.unicast to AS394380 announce ANY
mp-export:      afi ipv6.unicast to AS394434 announce ANY
mp-export:      afi ipv6.unicast to AS394479 announce ANY
mp-export:      afi ipv6.unicast to AS394501 announce ANY
mp-export:      afi ipv6.unicast to AS394625 announce ANY
mp-export:      afi ipv6.unicast to AS394851 announce ANY
mp-export:      afi ipv6.unicast to AS394855 announce ANY
mp-export:      afi ipv6.unicast to AS394935 announce ANY
mp-export:      afi ipv6.unicast to AS394977 announce ANY
mp-export:      afi ipv6.unicast to AS395052 announce ANY
mp-export:      afi ipv6.unicast to AS395186 announce ANY
mp-export:      afi ipv6.unicast to AS395308 announce ANY
mp-export:      afi ipv6.unicast to AS395309 announce ANY
mp-export:      afi ipv6.unicast to AS395354 announce ANY
mp-export:      afi ipv6.unicast to AS395403 announce ANY
mp-export:      afi ipv6.unicast to AS395598 announce ANY
mp-export:      afi ipv6.unicast to AS395654 announce ANY
mp-export:      afi ipv6.unicast to AS395662 announce ANY
mp-export:      afi ipv6.unicast to AS395717 announce ANY
mp-export:      afi ipv6.unicast to AS395747 announce ANY
mp-export:      afi ipv6.unicast to AS395849 announce ANY
mp-export:      afi ipv6.unicast to AS395954 announce ANY
mp-export:      afi ipv6.unicast to AS395978 announce ANY
mp-export:      afi ipv6.unicast to AS396026 announce ANY
mp-export:      afi ipv6.unicast to AS396055 announce ANY
mp-export:      afi ipv6.unicast to AS396158 announce ANY
mp-export:      afi ipv6.unicast to AS396190 announce ANY
mp-export:      afi ipv6.unicast to AS396356 announce ANY
mp-export:      afi ipv6.unicast to AS396362 announce ANY
mp-export:      afi ipv6.unicast to AS396417 announce ANY
mp-export:      afi ipv6.unicast to AS396426 announce ANY
mp-export:      afi ipv6.unicast to AS396472 announce ANY
mp-export:      afi ipv6.unicast to AS396515 announce ANY
mp-export:      afi ipv6.unicast to AS396535 announce ANY
mp-export:      afi ipv6.unicast to AS396871 announce ANY
mp-export:      afi ipv6.unicast to AS396948 announce ANY
mp-export:      afi ipv6.unicast to AS396949 announce ANY
mp-export:      afi ipv6.unicast to AS396970 announce ANY
mp-export:      afi ipv6.unicast to AS396984 announce ANY
mp-export:      afi ipv6.unicast to AS396986 announce ANY
mp-export:      afi ipv6.unicast to AS396998 announce ANY
mp-export:      afi ipv6.unicast to AS397027 announce ANY
mp-export:      afi ipv6.unicast to AS397041 announce ANY
mp-export:      afi ipv6.unicast to AS397174 announce ANY
mp-export:      afi ipv6.unicast to AS397308 announce ANY
mp-export:      afi ipv6.unicast to AS397391 announce ANY
mp-export:      afi ipv6.unicast to AS397404 announce ANY
mp-export:      afi ipv6.unicast to AS397418 announce ANY
mp-export:      afi ipv6.unicast to AS397494 announce ANY
mp-export:      afi ipv6.unicast to AS397505 announce ANY
mp-export:      afi ipv6.unicast to AS397545 announce ANY
mp-export:      afi ipv6.unicast to AS397601 announce ANY
mp-export:      afi ipv6.unicast to AS397727 announce ANY
mp-export:      afi ipv6.unicast to AS397912 announce ANY
mp-export:      afi ipv6.unicast to AS397925 announce ANY
mp-export:      afi ipv6.unicast to AS398044 announce ANY
mp-export:      afi ipv6.unicast to AS398107 announce ANY
mp-export:      afi ipv6.unicast to AS398324 announce ANY
mp-export:      afi ipv6.unicast to AS398427 announce ANY
mp-export:      afi ipv6.unicast to AS398465 announce ANY
mp-export:      afi ipv6.unicast to AS398698 announce ANY
mp-export:      afi ipv6.unicast to AS398712 announce ANY
mp-export:      afi ipv6.unicast to AS398764 announce ANY
mp-export:      afi ipv6.unicast to AS398765 announce ANY
mp-export:      afi ipv6.unicast to AS398808 announce ANY
mp-export:      afi ipv6.unicast to AS398814 announce ANY
mp-export:      afi ipv6.unicast to AS398913 announce ANY
mp-export:      afi ipv6.unicast to AS399065 announce ANY
mp-export:      afi ipv6.unicast to AS399143 announce ANY
mp-export:      afi ipv6.unicast to AS399289 announce ANY
mp-export:      afi ipv6.unicast to AS399458 announce ANY
mp-export:      afi ipv6.unicast to AS399480 announce ANY
mp-export:      afi ipv6.unicast to AS399515 announce ANY
mp-export:      afi ipv6.unicast to AS399558 announce ANY
mp-export:      afi ipv6.unicast to AS399587 announce ANY
mp-export:      afi ipv6.unicast to AS399647 announce ANY
mp-export:      afi ipv6.unicast to AS399808 announce ANY
mp-export:      afi ipv6.unicast to AS399809 announce ANY
mp-export:      afi ipv6.unicast to AS399810 announce ANY
mp-export:      afi ipv6.unicast to AS399814 announce ANY
mp-export:      afi ipv6.unicast to AS399816 announce ANY
mp-export:      afi ipv6.unicast to AS399817 announce ANY
mp-export:      afi ipv6.unicast to AS399818 announce ANY
mp-export:      afi ipv6.unicast to AS399920 announce ANY
mp-export:      afi ipv6.unicast to AS399989 announce ANY
mp-export:      afi ipv6.unicast to AS399998 announce ANY
mp-export:      afi ipv6.unicast to AS400042 announce ANY
mp-export:      afi ipv6.unicast to AS400146 announce ANY
mp-export:      afi ipv6.unicast to AS400202 announce ANY
mp-export:      afi ipv6.unicast to AS400282 announce ANY
mp-export:      afi ipv6.unicast to AS400302 announce ANY
mp-export:      afi ipv6.unicast to AS400309 announce ANY
mp-export:      afi ipv6.unicast to AS400475 announce ANY
mp-export:      afi ipv6.unicast to AS400511 announce ANY
mp-export:      afi ipv6.unicast to AS400541 announce ANY
mp-export:      afi ipv6.unicast to AS400662 announce ANY
mp-export:      afi ipv6.unicast to AS400666 announce ANY
mp-export:      afi ipv6.unicast to AS400687 announce ANY
mp-export:      afi ipv6.unicast to AS400692 announce ANY
mp-export:      afi ipv6.unicast to AS400802 announce ANY
remarks:        -----------------------------------------------------------
remarks:        Send peering requests and issues to peering@gtt.net
remarks:        -----------------------------------------------------------
remarks:        Send trouble queries or problems to noc@gtt.net
remarks:        -----------------------------------------------------------
remarks:        SPAM or net abuse please mail to abuse@gtt.net
remarks:        -----------------------------------------------------------
remarks:        For more information see http://www.gtt.net/
remarks:        -----------------------------------------------------------
admin-c:        SE33-RIPE
tech-c:         NET3257-RIPE
status:         ASSIGNED
mnt-by:         RIPE-NCC-END-MNT
mnt-by:         AS3257-ROUTE-MNT
created:        2002-09-20T10:45:34Z
last-modified:  2023-07-21T10:03:34Z
source:         RIPE
"""

rpsl_object_from_text(AS3257)
