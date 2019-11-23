import os
import logger


class MachineHandler:
    def __init__(self, ids):
        self.ids = ids
        self.started = False

    def start_machines(self):
        if self.started:
            return

        for vmid in self.ids:
            os.system("qm start {}".format(vmid))

        logger.debug("machines started")
        self.started = True

    def stop_machines(self):
        if not self.started:
            return

        for vmid in self.ids:
            os.system("qm stop {}".format(vmid))

        logger.debug("machines stopped")
        self.started = False
