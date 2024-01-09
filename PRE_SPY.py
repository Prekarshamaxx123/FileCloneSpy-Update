import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import X64
    X64.Spy()
elif bit=='32bit':
    import X32
    X32.Spy()
