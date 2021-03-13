#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_ip_addresses/ tests/

black democritus_ip_addresses/ tests/

mypy democritus_ip_addresses/ tests/

pylint --fail-under 9 democritus_ip_addresses/*.py

flake8 democritus_ip_addresses/ tests/

bandit -r democritus_ip_addresses/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_ip_addresses/ tests/
