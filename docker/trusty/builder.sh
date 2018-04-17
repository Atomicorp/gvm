#!/bin/bash

if [ ! -f package/version ]; then
        echo
        echo "Error: version not detected $(pwd)"
        echo
	ls -la
        exit 1
fi

source package/version
CI_PIPELINE_ID=$(cat package/release)

pushd package
	dch -c debian/changelog  -b -v $DEB_VERSION-$CI_PIPELINE_ID$DIST -D $(awk -F'=' '/_CODENAME/{print$NF}' /etc/lsb-release)  "$CHANGELOG"

	fakeroot debian/rules clean
	fakeroot debian/rules binary
popd
