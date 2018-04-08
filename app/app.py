import bjoern
import os
import signal

from api import app

NUM_WORKERS = 2
worker_pids = []

bjoern.listen(app, 'unix:/tmp/website.sock')
for _ in range(NUM_WORKERS):
    pid = os.fork()
    if pid > 0:
        # in master
        worker_pids.append(pid)
    elif pid == 0:
        # in worker
        try:
            bjoern.run()
        except KeyboardInterrupt:
            pass
        exit()
