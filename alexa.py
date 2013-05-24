#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib.request
import zipfile

# Paths for the data file this module needs.
REMOTE_FILE = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
LOCAL_ZIP_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'top-1m.csv.zip')
LOCAL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'top-1m.csv')

# Store an array of rank to domain and a map of domain to rank
RANK_TO_DOMAIN = [None] * 10000001
DOMAIN_TO_RANK = {}

# Verify that the top million list exists. If not, download it.
if not os.path.exists(LOCAL_FILE):
    urllib.request.urlretrieve(REMOTE_FILE, LOCAL_ZIP_FILE)
    with zipfile.ZipFile(LOCAL_ZIP_FILE) as zfin:
        for file in zfin.namelist():
            zfin.extract(file)

# Load the mappings
# Each line is of the form 'ip min,ip max,ASN'
with open(LOCAL_FILE, 'r') as fin:
    for line in fin:
        line = line.strip().split(',', 2)
        if len(line) != 2: continue
        rank = int(line[0])
        domain = line[1]

        RANK_TO_DOMAIN[rank] = domain
        DOMAIN_TO_RANK[domain] = rank

def is_top_n(domain, n):
    """
    Lookup if domain is in the top n domains.

    n should be in the range [1, 1000000]
    """

    assert 1 <= n <= 1000000
    return get_rank(domain) < n

def get_rank(domain):
    """
    Get the rank of a given domain.

    Return None if the domain is not in the Alexa Top Million."
    """

    if domain in DOMAIN_TO_RANK:
        return DOMAIN_TO_RANK[domain]
    else:
        return None

def get_domain(n):
    """
    Get the nth domain in the Alexa Top Million.

    n should be in the range [1, 1000000]
    """

    assert 1 <= n <= 1000000
    return RANK_TO_DOMAIN[n]
        
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            n = int(arg)
            print('{} => {}'.format(n, get_domain(n)))
        except ValueError as err:
            print('{} => {}'.format(arg, get_rank(arg)))
