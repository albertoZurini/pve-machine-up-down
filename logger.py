from datetime import datetime

DEBUG_FILE = "debug.log"


def debug(msg):
    msg = "{} - {}".format(datetime.now().strftime("%Y-%m-%d %H:%M"), msg)
    print(msg)
    with open(DEBUG_FILE, "a") as f:
        f.write(msg)
