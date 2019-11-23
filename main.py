import os
import json
import time
from machine_handler import MachineHandler
import logger

settings_file = "settings.json"
with open(settings_file) as f:
    settings = json.loads(f.read())

remote_addr = settings["remoteAddress"]
vm_ids = settings["vmIds"]

mh = MachineHandler(vm_ids)

while True:
    ping_code = os.system("ping -c 1 {}".format(remote_addr))

    if ping_code == 0:
        print("Ping ok")
        mh.stop_machines()
    else:
        logger.debug("Ping returned error; starting machines")
        mh.start_machines()

    time.sleep(20)
