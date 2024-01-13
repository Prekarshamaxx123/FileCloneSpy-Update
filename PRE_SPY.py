import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import X64
    import SVR
    X64.Spy()
elif bit=='32bit':
    import X32
    import SVR
    X32.Spy()
