import time
def countdown_timer(seconds):
    while seconds:
        mins,secs = divmod(seconds,60)
        time_format = "{:02d}:{:02d}".format(mins,secs)
        print(time_format,end="\r")
        time.sleep(1)
        seconds -=1
    print("Now the time is up!")
seconds =int(input("Enter the time in seconds: "))
countdown_timer(seconds)