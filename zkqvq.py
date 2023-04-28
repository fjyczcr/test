import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer + " remaining")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Good job on your focused work.")

timer(25)
