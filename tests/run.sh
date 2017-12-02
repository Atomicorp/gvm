#!/bin/bash

DATAVOL=/var/lib/openvas/
OV_PASSWORD=${OV_PASSWORD:-admin}
OV_UPDATE=${OV_UPDATE:0}
ADDRESS=127.0.0.1
KEY_FILE=/var/lib/openvas/private/CA/clientkey.pem
CERT_FILE=/var/lib/openvas/CA/clientcert.pem
CA_FILE=/var/lib/openvas/CA/cacert.pem


redis-server /etc/redis.conf &

echo "Testing redis status..."
X="$(redis-cli ping)"
while  [ "${X}" != "PONG" ]; do
        echo "Redis not yet ready..."
        sleep 1
        X="$(redis-cli ping)"
done
echo "Redis ready."

#echo
#echo "Initializing persistent directory layout"
#pushd /var/lib/openvas
#
#DATA_DIRS="CA cert-data mgr private/CA plugins scap-data"
#for dir in $DATA_DIRS; do
#	if [ ! -d $dir ]; then
#		mkdir $dir
#	fi
#done
#popd


# Check certs
if [ ! -f /var/lib/openvas/CA/cacert.pem ]; then
	/usr/bin/openvas-manage-certs -a
fi

if [ "$OV_UPDATE" == "yes" ];then
	/usr/sbin/greenbone-nvt-sync 
	/usr/sbin/greenbone-certdata-sync 
	/usr/sbin/greenbone-scapdata-sync
fi

if [  ! -d /usr/share/openvas/gsa/locale ]; then
	mkdir -p /usr/share/openvas/gsa/locale
fi

echo "Restarting services"
/usr/sbin/openvassd 
/usr/sbin/openvasmd 
/usr/sbin/gsad 

echo
echo -n "Checking for scanners: "
SCANNER=$(/usr/sbin/openvasmd --get-scanners)
echo "Done"

if ! echo $SCANNER | grep -q nmap ; then
        echo "Adding nmap scanner"
        /usr/bin/ospd-nmap --bind-address $ADDRESS --port 40001 --key-file $KEY_FILE --cert-file $CERT_FILE --ca-file $CA_FILE &
        /usr/sbin/openvasmd  --create-scanner=ospd-nmap --scanner-host=localhost --scanner-port=40001 --scanner-type=OSP --scanner-ca-pub=/var/lib/openvas/CA/cacert.pem --scanner-key-pub=/var/lib/openvas/CA/clientcert.pem --scanner-key-priv=/var/lib/openvas/private/CA/clientkey.pem
        echo
else
	/usr/bin/ospd-nmap --bind-address $ADDRESS --port 40001 --key-file $KEY_FILE --cert-file $CERT_FILE --ca-file $CA_FILE &

fi


echo "Reloading NVTs"
openvasmd --rebuild --progress

# Check for users, and create admin
if ! [[ $(openvasmd --get-users) ]] ; then 
	/usr/sbin/openvasmd openvasmd --create-user=admin
	/usr/sbin/openvasmd --user=admin --new-password=$OV_PASSWORD
fi

if [ -n "$OV_PASSWORD" ]; then
	echo "Setting admin password"
	/usr/sbin/openvasmd --user=admin --new-password=$OV_PASSWORD
fi

echo "Checking setup"
/usr/bin/openvas-check-setup --v9


if [ -z "$BUILD" ]; then
	echo "Tailing logs"
	tail -F /var/log/openvas/*
fi

