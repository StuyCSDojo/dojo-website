#! /bin/bash -e

sudo ./kill_server.sh
echo "Starting up Dojo Website..."
python /projects/dojo-website/app/app.py &> /dev/null
chmod 666 /tmp/website.sock
# gunicorn -w 4 --worker-class="egg:meinheld#gunicorn_worker" -b unix:/tmp/docs.sock -m 005 api:app --daemon &> /dev/null
