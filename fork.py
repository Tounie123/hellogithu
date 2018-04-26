import os

print("process (%s) start...\n" % os.getpid())

pid = os.fork()

if pid == 0:
	print("I am child process (%d) and my parent is %s." % (os.getpid(),os.getppid()))
else:
	print("I (%s) just created a child process (%s)." % (os.getpid(),pid))
