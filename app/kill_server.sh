#!/bin/bash -e
if ps aux | grep -q "[p]ython /projects/dojo-website/app/app.py"; then
    kill -9 $(ps aux | grep "[p]ython /projects/dojo-website/app/app.py" | awk '{print $2}')
fi
rm -f /tmp/website.sock
