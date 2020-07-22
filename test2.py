from new_crash import *

crash1 = "Program restart. Reason: Program Crash. Program: radioapp.elf. Signal: 11. PMD: /var/log/pmd/pmd-faultManagerPro-2406-20200319-101747.tgz. Extra: CXP2030006%7_R23B28"

print(crash1)
print(extract_crash_signature(crash1))

crash2 = "Program restart. Reason: Restart request. Program:. Rank: Program. Signal: SIGABRT. PMD: pmd-tn-sctp-server-7956-20200101-004419. Extra: [SCTP#1] An established SctpAssociation RO with assocId=16777268 is duplicated: shares IP addresses and the port with new one t /local/fem110/workspace/tn-build-all-71285-4/blocks/sctpBl/sctpSwU/files/src/assoc_ro.c:411"

print("-"*30)
print(crash2)
print(extract_crash_signature(crash2))


crash3='Program restart. Reason: Program Crash. Program: radioapp.elf. Signal: 7. PMD: /var/log/pmd/pmd-tmoSchedulerTx-3240-20200326-114120.tgz. Extra: CXP2030006%5_R26C72'
print("-"*30)
print(crash3)
print(extract_crash_signature(crash3))