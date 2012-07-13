Extracting Mozilla's EV OIDs 
============================

Extracts the list of EV OIDs from the myTrustedEVInfos C structure defined in:

    https://mxr.mozilla.org/mozilla-central/source/security/manager/ssl/src/nsIdentityChecking.cpp?raw=1


Developed for SSLyze:

    https://github.com/iSECPartners/sslyze


Usage
-----

Tested on Python 2.7 on Windows.

### Dependency
- pycparser

### Running the script

    python extract_mozilla_ev_oids.py

The script will first download the source file from Mozilla's website and then output the list of EV OIDs to mozilla_ev_oids.py.
