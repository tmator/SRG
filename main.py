import pyHook
import os
import subprocess

i=0;

def OnKeyboardEvent(event):
  global i
  global check
  
  if (event.KeyID==83):
    i+=1
  if (i>110):
    print ('---',i)
    i=0;
    os.system("taskkill /im emulator_multicpu.exe")
    subprocess.Popen(["start", "/MAX", "python", "C:\\SRG\\emu.py"], shell=True)
    #os.system("python.exe C:\\SRG\\emu.py")
  # return True to pass the event to other handlers
  # return False to stop the event from propagating
  return True

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookKeyboard()

subprocess.Popen("python.exe C:\\SRG\\emu.py")

if __name__ == '__main__':
  
  import pythoncom
  pythoncom.PumpMessages()