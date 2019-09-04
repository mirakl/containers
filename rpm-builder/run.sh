#!/bin/bash

set -e

# Build the rpm
rpmbuild -bb ${SOURCE_DIR}/*.spec

# Install the rpm locally to check that it works
yum install -y ${WORK_DIR}/rpm/x86_64/*.rpm

# Copy to the output folder
cp ${WORK_DIR}/rpm/x86_64/*.rpm ${RPM_DIR}/
