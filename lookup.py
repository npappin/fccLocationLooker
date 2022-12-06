#!/usr/bin/env python3

import requests, json

TIMEOUT=5
USERAGENT = "locationLookup/0.0.1"

def getUuid():
    headers = {'User-Agent': USERAGENT}
    response = requests.get("https://broadbandmap.fcc.gov/nbm/map/api/published/filing", headers=headers, timeout=TIMEOUT)
    data = json.loads(response.text)
    return data['data'][0]['process_uuid']

def providersByLocation(locationId:int) -> list:
    uuid = getUuid()
    headers = {'User-Agent': USERAGENT}
    url = f"https://broadbandmap.fcc.gov/nbm/map/api/fabric/detail/{uuid}/{locationId}"
    response = requests.get(url, headers=headers)
    parsed = json.loads(response.text)
    data = parsed['data'][0]['detail']
    return data

def coordinatesByLocation(locationId:int) -> tuple:
    uuid = getUuid()
    headers = {'User-Agent': USERAGENT}
    url = f"https://broadbandmap.fcc.gov/nbm/map/api/fabric/detail/{uuid}/{locationId}"
    response = requests.get(url, headers=headers)
    parsed = json.loads(response.text)
    data = parsed['data'][0]['coordinates']
    data = (data[0],data[1])
    return data
