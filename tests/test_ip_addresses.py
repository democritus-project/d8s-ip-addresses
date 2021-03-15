import pytest

from d8s_ip_addresses import (
    ip_addresses_find,
    ip_current,
    ip_in_network_block,
    ip_is_private,
    ip_is_reserved,
    ip_network_block_contains_ip,
    ip_network_block_enumerate,
    ip_network_block_first_address,
    ip_network_block_ip_count,
    ip_network_block_last_address,
    ip_network_block_to_range,
    ip_range_to_network_block,
    ip_version,
    ip_whois,
    ipv4_address_examples,
    ipv4_addresses_find,
    ipv4_is_possible_version_number,
    ipv4_private_addresses,
    ipv4_sum,
    ipv6_address_examples,
    ipv6_addresses_find,
    ipv6_compress,
    ipv6_expand,
    ipv6_private_addresses,
    ipv6_threatconnect_form,
    is_ip_address,
)


def test_ip_current_1():
    result = ip_current()
    assert isinstance(result, dict)
    assert is_ip_address(result['ip'])


def test_ip_addresses_find_1():
    from democritus_lists import lists_have_same_items

    s = '2001:db8::1000 2001:0db8:0000:0000:0000:0000:0000:1000 8.8.8.8 1.4.33.255'
    assert lists_have_same_items(
        ip_addresses_find(s), ['2001:0db8:0000:0000:0000:0000:0000:1000', '2001:db8::1000', '8.8.8.8', '1.4.33.255']
    )


@pytest.mark.network
def test_ip_whois_1():
    response = ip_whois('8.8.8.8')
    assert response['ip'] == '8.8.8.8'
    assert response['city'] == 'Mountain View'


def test_ipv4_address_examples_1():
    assert len(ipv4_address_examples()) == 10
    for ip in ipv4_address_examples():
        assert is_ip_address(ip)
    assert len(ipv4_address_examples(n=101)) == 101


def test_ipv6_address_examples_1():
    assert len(ipv6_address_examples()) == 10
    for ip in ipv6_address_examples():
        assert is_ip_address(ip)
    assert len(ipv6_address_examples(n=101)) == 101


def test_ip_in_network_block_docs_1():
    assert ip_in_network_block('10.0.0.1', '10.0.0.0/24') == True
    assert ip_in_network_block('10.0.1.0', '10.0.0.0/24') == False
    assert ip_in_network_block('10.0.1.0', '10.0.0.0/16') == True
    assert ip_in_network_block('10.1.0.0', '10.0.0.0/16') == False


def test_ip_is_private_docs_1():
    assert ip_is_private('10.0.0.1') == True
    assert ip_is_private('8.8.8.8') == False


def test_ip_is_reserved_docs_1():
    assert ip_is_reserved('127.0.0.1') == False
    assert ip_is_reserved('8.8.0.1') == False


def test_ip_network_block_contains_ip_docs_1():
    assert ip_network_block_contains_ip('10.0.0.0/24', '10.0.0.1') == True
    assert ip_network_block_contains_ip('10.0.0.0/24', '10.0.1.0') == False
    assert ip_network_block_contains_ip('10.0.0.0/16', '10.0.1.0') == True
    assert ip_network_block_contains_ip('10.0.0.0/16', '10.1.0.0') == False


def test_ip_network_block_enumerate_docs_1():
    assert ip_network_block_enumerate('8.8.8.0/30') == ['8.8.8.0', '8.8.8.1', '8.8.8.2', '8.8.8.3']


def test_ip_network_block_first_address_docs_1():
    assert ip_network_block_first_address('10.0.0.0/24') == '10.0.0.0'


def test_ip_network_block_ip_count_docs_1():
    assert ip_network_block_ip_count('8.8.8.0/24') == 256


def test_ip_network_block_last_address_docs_1():
    assert ip_network_block_last_address('10.0.0.0/24') == '10.0.0.255'


def test_ip_network_block_to_range_docs_1():
    assert ip_network_block_to_range('8.8.8.0/24') == '8.8.8.0 - 8.8.8.255'


# def test_ip_range_to_network_block_docs_1():
# assert ip_range_to_network_block('ip_range_string') == 'fill'  # fill


def test_ip_version_docs_1():
    assert ip_version('8.8.8.0') == 4
    assert ip_version('2001:0db8:0000:0000:0000:0000:0000:1000') == 6
    assert ip_version('2001:db8::1000') == 6


# def test_ipv4_addresses_find_docs_1():
# assert ipv4_addresses_find('text') == 'fill'  # fill


def test_ipv4_is_possible_version_number_docs_1():
    assert ipv4_is_possible_version_number('8.8.8.8') == False
    assert ipv4_is_possible_version_number('1.0.1.2') == True
    assert ipv4_is_possible_version_number('2.0.1.2') == True
    assert ipv4_is_possible_version_number('1.1.1.2') == True
    assert ipv4_is_possible_version_number('23.0.1.2') == True
    assert ipv4_is_possible_version_number('123.0.1.2') == False


def test_ipv4_private_addresses_docs_1():
    assert tuple(ipv4_private_addresses()) == (
        {
            'Address Block': '0.0.0.0/8',
            'Name': '"This network"',
            'RFC': '[RFC791], Section 3.2',
            'Allocation Date': '1981-09',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '0.0.0.0/32',
            'Name': '"This host on this network"',
            'RFC': '[RFC1122], Section 3.2.1.3',
            'Allocation Date': '1981-09',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '10.0.0.0/8',
            'Name': 'Private-Use',
            'RFC': '[RFC1918]',
            'Allocation Date': '1996-02',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '100.64.0.0/10',
            'Name': 'Shared Address Space',
            'RFC': '[RFC6598]',
            'Allocation Date': '2012-04',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '127.0.0.0/8',
            'Name': 'Loopback',
            'RFC': '[RFC1122], Section 3.2.1.3',
            'Allocation Date': '1981-09',
            'Termination Date': 'N/A',
            'Source': 'False [1]',
            'Destination': 'False [1]',
            'Forwardable': 'False [1]',
            'Globally Reachable': 'False [1]',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '169.254.0.0/16',
            'Name': 'Link Local',
            'RFC': '[RFC3927]',
            'Allocation Date': '2005-05',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '172.16.0.0/12',
            'Name': 'Private-Use',
            'RFC': '[RFC1918]',
            'Allocation Date': '1996-02',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.0/24 [2]',
            'Name': 'IETF Protocol Assignments',
            'RFC': '[RFC6890], Section 2.1',
            'Allocation Date': '2010-01',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.0/29',
            'Name': 'IPv4 Service Continuity Prefix',
            'RFC': '[RFC7335]',
            'Allocation Date': '2011-06',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.8/32',
            'Name': 'IPv4 dummy address',
            'RFC': '[RFC7600]',
            'Allocation Date': '2015-03',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.9/32',
            'Name': 'Port Control Protocol Anycast',
            'RFC': '[RFC7723]',
            'Allocation Date': '2015-10',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.10/32',
            'Name': 'Traversal Using Relays around NAT Anycast',
            'RFC': '[RFC8155]',
            'Allocation Date': '2017-02',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.0.0.170/32, 192.0.0.171/32',
            'Name': 'NAT64/DNS64 Discovery',
            'RFC': '[RFC8880][RFC7050], Section 2.2',
            'Allocation Date': '2013-02',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '192.0.2.0/24',
            'Name': 'Documentation (TEST-NET-1)',
            'RFC': '[RFC5737]',
            'Allocation Date': '2010-01',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.31.196.0/24',
            'Name': 'AS112-v4',
            'RFC': '[RFC7535]',
            'Allocation Date': '2014-12',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.52.193.0/24',
            'Name': 'AMT',
            'RFC': '[RFC7450]',
            'Allocation Date': '2014-12',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.88.99.0/24',
            'Name': 'Deprecated (6to4 Relay Anycast)',
            'RFC': '[RFC7526]',
            'Allocation Date': '2001-06',
            'Termination Date': '2015-03',
            'Source': '',
            'Destination': '',
            'Forwardable': '',
            'Globally Reachable': '',
            'Reserved-by-Protocol': '',
        },
        {
            'Address Block': '192.168.0.0/16',
            'Name': 'Private-Use',
            'RFC': '[RFC1918]',
            'Allocation Date': '1996-02',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '192.175.48.0/24',
            'Name': 'Direct Delegation AS112 Service',
            'RFC': '[RFC7534]',
            'Allocation Date': '1996-01',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '198.18.0.0/15',
            'Name': 'Benchmarking',
            'RFC': '[RFC2544]',
            'Allocation Date': '1999-03',
            'Termination Date': 'N/A',
            'Source': 'True',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '198.51.100.0/24',
            'Name': 'Documentation (TEST-NET-2)',
            'RFC': '[RFC5737]',
            'Allocation Date': '2010-01',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '203.0.113.0/24',
            'Name': 'Documentation (TEST-NET-3)',
            'RFC': '[RFC5737]',
            'Allocation Date': '2010-01',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'False',
        },
        {
            'Address Block': '240.0.0.0/4',
            'Name': 'Reserved',
            'RFC': '[RFC1112], Section 4',
            'Allocation Date': '1989-08',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
        {
            'Address Block': '255.255.255.255/32',
            'Name': 'Limited Broadcast',
            'RFC': '[RFC8190]\n        [RFC919], Section 7',
            'Allocation Date': '1984-10',
            'Termination Date': 'N/A',
            'Source': 'False',
            'Destination': 'True',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Reserved-by-Protocol': 'True',
        },
    )


def test_ipv4_sum_docs_1():
    assert ipv4_sum('8.8.8.8') == 32
    assert ipv4_sum('0.0.0.0') == 0
    assert ipv4_sum('192.168.0.5') == 365


# def test_ipv6_address_examples_docs_1():
# assert ipv6_address_examples(n=Num) == 'fill'  # fill


# def test_ipv6_addresses_find_docs_1():
# assert ipv6_addresses_find('text') == 'fill'  # fill


def test_ipv6_compress_docs_1():
    assert ipv6_compress('2001:0db8:0000:0000:0000:0000:0000:1000') == '2001:db8::1000'


def test_ipv6_expand_docs_1():
    assert ipv6_expand('2001:db8::1000') == '2001:0db8:0000:0000:0000:0000:0000:1000'


def test_ipv6_private_addresses_docs_1():
    assert tuple(ipv6_private_addresses()) == (
        {
            'Address Block': '::1/128',
            'Allocation Date': '2006-02',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Name': 'Loopback Address',
            'RFC': '[RFC4291]',
            'Reserved-by-Protocol': 'True',
            'Source': 'False',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '::/128',
            'Allocation Date': '2006-02',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Name': 'Unspecified Address',
            'RFC': '[RFC4291]',
            'Reserved-by-Protocol': 'True',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '::ffff:0:0/96',
            'Allocation Date': '2006-02',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Name': 'IPv4-mapped Address',
            'RFC': '[RFC4291]',
            'Reserved-by-Protocol': 'True',
            'Source': 'False',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '64:ff9b::/96',
            'Allocation Date': '2010-10',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'IPv4-IPv6 Translat.',
            'RFC': '[RFC6052]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '64:ff9b:1::/48',
            'Allocation Date': '2017-06',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Name': 'IPv4-IPv6 Translat.',
            'RFC': '[RFC8215]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '100::/64',
            'Allocation Date': '2012-06',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Name': 'Discard-Only Address Block',
            'RFC': '[RFC6666]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001::/23',
            'Allocation Date': '2000-09',
            'Destination': 'False [1]',
            'Forwardable': 'False [1]',
            'Globally Reachable': 'False [1]',
            'Name': 'IETF Protocol Assignments',
            'RFC': '[RFC2928]',
            'Reserved-by-Protocol': 'False',
            'Source': 'False [1]',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001::/32',
            'Allocation Date': '2006-01',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'N/A [2]',
            'Name': 'TEREDO',
            'RFC': '[RFC4380]\n        [RFC8190]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:1::1/128',
            'Allocation Date': '2015-10',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'Port Control Protocol Anycast',
            'RFC': '[RFC7723]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:1::2/128',
            'Allocation Date': '2017-02',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'Traversal Using Relays around NAT Anycast',
            'RFC': '[RFC8155]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:2::/48',
            'Allocation Date': '2008-04',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False',
            'Name': 'Benchmarking',
            'RFC': '[RFC5180][RFC Errata 1752]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:3::/32',
            'Allocation Date': '2014-12',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'AMT',
            'RFC': '[RFC7450]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:4:112::/48',
            'Allocation Date': '2014-12',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'AS112-v6',
            'RFC': '[RFC7535]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:10::/28',
            'Allocation Date': '2007-03',
            'Destination': '',
            'Forwardable': '',
            'Globally Reachable': '',
            'Name': 'Deprecated (previously ORCHID)',
            'RFC': '[RFC4843]',
            'Reserved-by-Protocol': '',
            'Source': '',
            'Termination Date': '2014-03',
        },
        {
            'Address Block': '2001:20::/28',
            'Allocation Date': '2014-07',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'ORCHIDv2',
            'RFC': '[RFC7343]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2001:db8::/32',
            'Allocation Date': '2004-07',
            'Destination': 'False',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Name': 'Documentation',
            'RFC': '[RFC3849]',
            'Reserved-by-Protocol': 'False',
            'Source': 'False',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2002::/16 [3]',
            'Allocation Date': '2001-02',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'N/A [3]',
            'Name': '6to4',
            'RFC': '[RFC3056]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': '2620:4f:8000::/48',
            'Allocation Date': '2011-05',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'True',
            'Name': 'Direct Delegation AS112 Service',
            'RFC': '[RFC7534]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': 'fc00::/7',
            'Allocation Date': '2005-10',
            'Destination': 'True',
            'Forwardable': 'True',
            'Globally Reachable': 'False [4]',
            'Name': 'Unique-Local',
            'RFC': '[RFC4193]\n        [RFC8190]',
            'Reserved-by-Protocol': 'False',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
        {
            'Address Block': 'fe80::/10',
            'Allocation Date': '2006-02',
            'Destination': 'True',
            'Forwardable': 'False',
            'Globally Reachable': 'False',
            'Name': 'Link-Local Unicast',
            'RFC': '[RFC4291]',
            'Reserved-by-Protocol': 'True',
            'Source': 'True',
            'Termination Date': 'N/A',
        },
    )


def test_ipv6_threatconnect_form_docs_1():
    assert ipv6_threatconnect_form('2001:0db8:0000:0000:0000:0000:0000:1000') == '2001:db8:0:0:0:0:0:1000'
    assert ipv6_threatconnect_form('2001:db8::1000') == '2001:db8:0:0:0:0:0:1000'


def test_is_ip_address_docs_1():
    assert is_ip_address('8.8.8.0') == True
    assert is_ip_address('2001:0db8:0000:0000:0000:0000:0000:1000') == True
    assert is_ip_address('2001:db8::1000') == True
    assert is_ip_address('not an ip address') == False
