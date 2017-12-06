#!/bin/sh

set -e

pushd tests/fail
# this should fail
./manage.py templatecheck && false || true
popd

# This should pass
pushd tests/pass
./manage.py templatecheck
popd
