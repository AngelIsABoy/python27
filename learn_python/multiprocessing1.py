# multiprocessing.py
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpis(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

#The program can not work in Windows