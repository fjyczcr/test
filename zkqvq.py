import time

def focus_timer(minutes):
    """Starts a focus timer for the specified number of minutes."""

    seconds = minutes * 60

    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer + " remaining")

        time.sleep(1)

        seconds -= 1

    print("Time is up! Good job on your focused work.")
