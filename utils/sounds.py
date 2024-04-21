import subprocess

def play_sound(filename, wait=True):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    if wait:
        subprocess.Popen(['ffplay', filename, '-autoexit', '-nodisp'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=startupinfo).wait()
    else:
        subprocess.Popen(['ffplay', filename, '-autoexit', '-nodisp'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=startupinfo)

def play_awake_sound():
    play_sound('./assets/sounds/awake.mp3', wait=False)
    return

def play_process_sound():
    play_sound("./assets/sounds/process.mp3", wait=False)
    return