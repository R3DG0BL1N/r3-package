#!/usr/bin/env python3
#======================================================================
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# -------------------------------- R3 ---------------------------------
# r3-pkg/lazy_scan [r3101]
# v/0.1-alpha
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: python3 r3_lazy_scan.py -h HOST [-r FILE_PATH] [-w PORT] [-v] [-mt]
# -h : Defines the host to scan. *REQ*
# -r : Defines the report output file.
# -w : Defines the HTTP port to scan. Use AUTO if not known.
# -v : Prints output on shell.
# -mt : Runs on multiple shells at the same time*.
# (?) : 
# (X) : python3 r3_lazy_scan.py -h 10.10.23.52 -w AUTO -v
# ------------------------------ NOTES --------------------------------
# As the name suggests, this is just a lazy scan. It can miss critical
# information, alert the blue team, or return useless data.
# * -mt : Faster, but each scan runs independently.
# ---------------------------- DISCLAIMER -----------------------------
# Use only with explicit permission of the system owner.
# Breaking things or getting arrested is on you, I'm just a goblin.
# ----------------------------- LICENSE -------------------------------
# Licensed under the MIT License (see LICENSE file in repo).
#======================================================================

#============================ ALPHA TABLE =============================
#------------------------------- bugs ---------------------------------
# [ ]
#----------------------------- features -------------------------------
# [ ]
#======================================================================
#----------------------------------------------------------------------
#\ PRE

import sys, os.path as P;
sys.path.insert(0, P.abspath(P.join(P.dirname(__file__), "../../lib")));
from r3 import Core;

def _pre(argv) -> Core:
    c = Core("r3101", argv, { 
        "-h%": True,
        "-r%": False,
        "-w%": False,
        "-v": False,
        "-mt": False
    })
    c.set_err({
        3: "Could not establish connection with host",
    });
    return c;

if __name__ == "__main__":
    _core = _pre(sys.argv);
    _core.load(); # EXIT

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials



#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions



#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - MAIN

if __name__ == "__main__":
    pass

#/ SRC - MAIN
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?