from subprocess import Popen, PIPE

p = Popen("C:/cygwin/bin/bash.exe", stdin=PIPE, stdout=PIPE)
#p.stdin.write(b"ls")
#p.stdin.write(b"/home/ephucle/moshell/moshell")
p.stdin.write(b"/home/ephucle/moshell/moshell /home/ephucle/test_esi/junggu-buyong-TA5_200805_160204_KST_MSRBS-L_CXP9024418-15_R7C92_dcgm.zip")

p.stdin.close()
out = p.stdout.read()
print (out)