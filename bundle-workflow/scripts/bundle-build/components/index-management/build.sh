#!/bin/bash

# Copyright OpenSearch Contributors.
# SPDX-License-Identifier: Apache-2.0

set -ex

function usage() {
    echo "Usage: $0 [args]"
    echo ""
    echo "Arguments:"
    echo -e "-v VERSION\t[Required] OpenSearch version."
    echo -e "-o DEST\t[Required] Full destination path from which to pickup dependent artifacts."
    echo -e "-s SNAPSHOT\t[Optional] Build a snapshot, default is 'false'."
    echo -e "-a ARCHITECTURE\t[Optional] Build architecture, ignored."
    echo -e "-o OUTPUT\t[Optional] Output path, default is 'artifacts'."
    echo -e "-h help"
}

while getopts ":h:v:s:o:a:d:" arg; do
    case $arg in
        h)
            usage
            exit 1
            ;;
        v)
            VERSION=$OPTARG
            ;;
        s)
            SNAPSHOT=$OPTARG
            ;;
        o)
            OUTPUT=$OPTARG
            ;;
        d)
            DEST=$OPTARG
            ;;
        a)
            ARCHITECTURE=$OPTARG
            ;;
        :)
            echo "Error: -${OPTARG} requires an argument"
            usage
            exit 1
            ;;
        ?)
            echo "Invalid option: -${arg}"
            exit 1
            ;;
    esac
done

if [ -z "$VERSION" ]; then
    echo "Error: You must specify the OpenSearch version"
    usage
    exit 1
fi

for plugin in job-scheduler notifications; do
    PLUGIN_VERSION=$VERSION.0
    [[ "$SNAPSHOT" == "true" ]] && PLUGIN_VERSION=$PLUGIN_VERSION-SNAPSHOT
    ZIP=$DEST/plugins/opensearch-$plugin-$PLUGIN_VERSION.zip
    if [[ ! -f $ZIP ]]; then
        echo "error: missing $ZIP, $plugin must be built first"
        exit 1
    fi
    cp $ZIP src/test/resources/$plugin
done

[[ "$SNAPSHOT" == "true" ]] && VERSION=$VERSION-SNAPSHOT
[ -z "$OUTPUT" ] && OUTPUT=artifacts

mkdir -p $OUTPUT
./gradlew assemble --no-daemon --refresh-dependencies -DskipTests=true -Dopensearch.version=$VERSION -Dbuild.snapshot=$SNAPSHOT

zipPath=$(find . -path \*build/distributions/*.zip)
distributions="$(dirname "${zipPath}")"

echo "COPY ${distributions}/*.zip"
mkdir -p $OUTPUT/plugins
cp ${distributions}/*.zip ./$OUTPUT/plugins
