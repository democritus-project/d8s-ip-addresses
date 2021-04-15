# Democritus IP Addresses

[![PyPI](https://img.shields.io/pypi/v/d8s-ip-addresses.svg)](https://pypi.python.org/pypi/d8s-ip-addresses)
[![CI](https://github.com/democritus-project/d8s-ip-addresses/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-ip-addresses/actions)
[![Lint](https://github.com/democritus-project/d8s-ip-addresses/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-ip-addresses/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-ip-addresses/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-ip-addresses)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with IP addresses.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def ipv4_address_examples(n: int = 10):
        """Create n ipv4 addresses."""
    ```
  - ```python
    def ipv6_address_examples(n: int = 10):
        """Create n ipv6 addresses."""
    ```
  - ```python
    def ipv4_addresses_find(text):
        """Parse IPv4 addresses from the given text."""
    ```
  - ```python
    def ipv6_addresses_find(text):
        """Parse IPv6 addresses from the given text."""
    ```
  - ```python
    def ip_addresses_find(text):
        """Parse ip addresses from the given text."""
    ```
  - ```python
    def ip_is_private(ip):
        """Check if the IP address is private."""
    ```
  - ```python
    def is_ip_address(text):
        """Determine whether or not the given text is an ip address."""
    ```
  - ```python
    def ip_whois(ip):
        """Get whois information for the given ip address."""
    ```
  - ```python
    def ip_is_reserved(ip):
        """Check if the IP address is IETF (https://www.ietf.org/) reserved."""
    ```
  - ```python
    def ip_version(ip):
        """Get the version number of the ip address (4 or 6)."""
    ```
  - ```python
    def ip_network_block_first_address(network_block: str):
        """Return the first address of the given network_block."""
    ```
  - ```python
    def ip_network_block_last_address(network_block: str):
        """Return the first address of the given network_block."""
    ```
  - ```python
    def ip_network_block_ip_count(network_block_string):
        """Get the number of IP addresses in the given network block."""
    ```
  - ```python
    def ip_network_block_to_range(network_block_string):
        """Return the range of IP addresses covered by the network block in the form "<starting-ip> - <ending-ip>"."""
    ```
  - ```python
    def ip_network_block_enumerate(network_block_string):
        """Return a list of all of the ip addresses in the given network_block_string."""
    ```
  - ```python
    def ip_network_block_contains_ip(network_block: str, ip_address: str):
        """."""
    ```
  - ```python
    def ip_in_network_block(ip_address: str, network_block: str):
        """Return whether or not the given ip_address is in the network_block."""
    ```
  - ```python
    def ip_range_to_network_block(ip_range_string):
        """Take a range like "<starting-ip> - <ending-ip>" and convert this into an IP address network block."""
    ```
  - ```python
    def ipv6_expand(ip_v6):
        """Expand (also known as 'Exploding') an ipv6 address."""
    ```
  - ```python
    def ipv6_compress(ip_v6):
        """Compress an ipv6 address."""
    ```
  - ```python
    def ipv6_threatconnect_form(ip_v6):
        """Format ipv6 address as expected by ThreatConnect."""
    ```
  - ```python
    def ip_current():
        """Get the current ip address."""
    ```
  - ```python
    def ipv4_private_addresses():
        """Get private ipv4 addresses from https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml."""
    ```
  - ```python
    def ipv6_private_addresses():
        """Get private ipv6 addresses from https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml#iana-ipv6-special-registry-1."""
    ```
  - ```python
    def ipv4_sum(ipv4_address):
        """Find the sum of the ip address by adding each section of the ip address. For example, 8.8.8.8 would sum to 32 (calculated by taking 8 + 8 + 8 + 8)"""
    ```
  - ```python
    def ipv4_is_possible_version_number(ipv4_address):
        """Determine whether or not the ipv4 ip address is likely a version number or not. This is a beta function and is a work in progress. The word "Possible" in the function name should be taken seriously; this function will return `True` if the ipv4_address *might* be a version number. The results of this function are conjecture and should not be used definitively."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
