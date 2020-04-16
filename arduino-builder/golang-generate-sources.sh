#!/bin/bash
set -e
REPO_URL="https://github.com/arduino/arduino-builder.git"
REPO_NAME="`basename $REPO_URL | cut -d . -f 1`"

if [ -z "$1" ]; then
    echo "Usage: $0 GIT_TAG"
    echo "Example: $0 1.5.2"
    exit 1
fi

rm -rf $REPO_NAME-$1
git clone --branch $1 --depth=1 $REPO_URL $REPO_NAME-$1

cd $REPO_NAME-$1
GO111MODULE=on go mod vendor
cd ..

rm -f $REPO_NAME-$1.tar.gz
tar --exclude $REPO_NAME-$1/.git -czvf $REPO_NAME-$1.tar.gz $REPO_NAME-$1
rm -rf $REPO_NAME-$1
