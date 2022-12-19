#!/usr/bin/env bash

set -e
set -x

black app tests --check
