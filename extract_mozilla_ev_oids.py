# Author Alban D. - https://github.com/nabla-c0d3/

import pycparser
import urllib


SOURCE_FILE = 'nsIdentityChecking.cpp'
SOURCE_FILE_URL = 'https://mxr.mozilla.org/mozilla-central/source/security/manager/ssl/src/nsIdentityChecking.cpp?raw=1'
EV_OIDS_STRUCT = 'static struct nsMyTrustedEVInfo myTrustedEVInfos[]'
RESULT_FILE = 'mozilla_ev_oids'
RESULT_DECL = '# Generated using extract_mozilla_ev_oids.py \nmozilla_EV_OIDs = '


# Fetch the source file
print 'Fetching ' + SOURCE_FILE
urllib.urlretrieve(SOURCE_FILE_URL, SOURCE_FILE)
print 'Done'

# Open the CPP file and extract the struct we want
nsIdentityChecking = open(SOURCE_FILE,'r')

structs = nsIdentityChecking.read().partition(EV_OIDS_STRUCT)
oids_struct = structs[1] + structs[2]
structs = oids_struct.partition(';')
oids_struct = structs[0] + structs[1] + '\n'

# Parse the struct and recover the list of EV OIDs
oids_struct_temp = open(RESULT_FILE + '.c','w')
oids_struct_temp.write(oids_struct)
oids_struct_temp.close()

parser = pycparser.CParser()
t = pycparser.parse_file('mozilla_ev_oids.c', use_cpp=True, cpp_path='utils\cpp.exe')

ev_oids = []
for exprs in t.ext[0].init.exprs:
    ev_oids.append(exprs.exprs[0].value.strip('"'))

# Write the OID list to a file
ev_oids_file = open(RESULT_FILE + '.py','w')
ev_oids_file.write(RESULT_DECL + str(ev_oids))
print ev_oids

