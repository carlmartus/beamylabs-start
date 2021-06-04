#!/bin/sh

cd "${0%/*}"

if [ -z "${SIGNALBROKER_IP}" ]; then
  printf "SIGNALBROKER_IP not set, using default values as SIGNALBROKER_IP=\"$(scripts/resolve-ip.sh wlan0)\"\n"
  export SIGNALBROKER_IP=$(scripts/resolve-ip.sh wlan0)
fi

if [ -z "${NODE_NAME}" ]; then
  printf "NODE_NAME not set, using default values as NODE_NAME=\"$(scripts/resolve-ip.sh eth0)\"\n"
  export NODE_NAME=$(scripts/resolve-ip.sh eth0)
fi

rm -f envfile
touch envfile
# trigger-upgrade.sh might pass us an env file
if [ -n "$1" ]; then
  mv -f "$1" envfile
fi

# for any unset *_TAG env vars, the docker-compose yml falls back to "latest"

docker-compose --env-file envfile -f docker-compose-full-system.yml down
docker-compose --env-file envfile -f docker-compose-full-system.yml pull
docker-compose --env-file envfile -f docker-compose-full-system.yml up -d
