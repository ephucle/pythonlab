from skt_5g_cd_tool import *

#"<!ULL1MDBFUNR.64!> ull1nrmdbfupe_prac rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114      HY32856
#"CMC supervision.nIllegal access by rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114 HY36589
#Extra: was set to {} rpc/ue/variant/nr/protocol/rrc/util/impl/src/cell_group_config_builder_factory_impl.cc:480     HX98707
#"<!ULL1MDBFUNR.64!> ull1nrmdbfupe_pra rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1011       HY32856
#Trying to free a cm ptr that points o rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114       HY32659
#Program Crash. Program: rbsNcLm. Signal: SIGABRT. PMD: pmd-nc_main_thread   HY33439
#Extra: UeRef has not been allocated ue/variant/access/handler/context/src/ue_context_handler_impl.cc:201    HY33548
#"ulmacpe_cell_release.c:207: UPULMACPE /local/lmr-lm-builds_gmake_small_fem111/workspace/LM_BUILD_lratBbomAasArmLm/bbmc/bbOmMeBl/bbOmMeRcsSwU/src/bbomme_svc_basic_handling_eh_rcs.cc:169HY15947
#"bbiItc_distrib_16bSigMap.c:72: OSE-signal 0xffff0819 (-63463) cannot be mapped to LPP-signal"      HY34122
#LPP fatal error detected. Faultcode = 1639 rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1011  HY34324
#<!UPCDL.2663!> dlmacce_process_dlsu_thread.c:1235: DBC: dlsr.id     HY34532
#Extra: Unexpected handleCgci        HY31400
#Program: rhsd_bb6630. Signal: SIGABRT. PMD: pmd-fn_exc_queue        HY35583
#"<!ULL1MDBFUNR.64!> ull1nrmdbfupe_pra rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114       HY36061
#"<!UPCUL.2045!> ulmacce_catmscheduler.c:1776: DBC: fifoCnt == 1n"   HY36762
#"<!BBMC.542!> bbueme_releaseue_ovl.c:231: DBC: nrOfBearersForUe == req.nrOfRelRadioBearersn"        HY36767


crash_string = '"<!ULL1MDBFUNR.64!> ull1nrmdbfupe_prac rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114'
print(crash_string)
print(create_python_regex_string(crash_string))

print('-'*30)

crash_string = '"CMC supervision.nIllegal access by rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114'
print(crash_string)
print(create_python_regex_string(crash_string))



print('-'*30)
crash_string = '2020-04-08 08:29:09 LLOG  0001 DUS5201     No:   17. Program restart. Reason: Restart request. Program: lratBbomArmLm.bin. Rank: Program. Signal: SIGABRT. PMD: pmd-bbmcBbOmMeThrea-7659-20200408-082909. Extra: Recovery action initiated by BB via BCI, faultId: 0x301 (SwError), faultDescription: Emca 4:DSP 0: "LDM Alloc error: Out of memorynalloc /local/lmr-lm-builds_gmake_small_fem111/workspace/LM_BUILD_lratBbomAasArmLm/bbmc/bbOmMeBl/bbOmMeRcsSwU/src/bbomme_svc_basic_handling_eh_rcs.cc:169'
print(crash_string)
print(create_python_regex_string(crash_string))


print('-'*30)
crash_string = '2020-04-05 16:09:06 LLOG  BXP_2052         Board restart Ordered. Restart ordered due to Link timeout'
print(crash_string)
print(create_python_regex_string(crash_string))


print('-'*30)
crash_string = '2019-09-16 22:52:08 LLOG  0001 DUS5201     No:    6. Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-20762-20190916-225208. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x199"'
print(crash_string)
print(create_python_regex_string(crash_string))


