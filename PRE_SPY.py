import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import PSPY
    PSPY.Spy()
elif bit=='32bit':
    import X32
    X32.Spy()
