# Created with reference to http://www.winpilot.com/UsersGuide/UserAirspace.asp

import logging
log = logging.getLogger(__name__)

# Convert a OpenAir file to a list of site dictionaries
def parseFile(filename):
    sites = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line[0] == "*": continue
            token, value = line.split(' ', 1)
            if token == "AC":
                # new site
                site = {}
                sites.append(site)
            elif token in ('AN', 'AL', 'AH', 'AT'):
                site[token] = value.strip()
            elif token == "V":
                key, val = line[1:].split('=')
                site['V'] = site.get('V', {})
                site['V'][key] = val
            elif token in ('DP', 'DA', 'DB', 'DC', 'DY'):
                site[token] = site.get(token, [])
                site[token].append(value)
            elif token in ('SB', 'SP'):
                # ignore lines to set pen and
                pass
            else:
                log.warning('Unhandled token %s: %s' % (token, value))
    return sites
