#!/usr/bin/env python3
#
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# v/ 0.1-alpha
#
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: pip install -e .
# (?) : You must execute this command on project folder
# ------------------------------ NOTES --------------------------------
# My momma once told me, clean yo ass before cleaning somebody else's
# ---------------------------- DISCLAIMER -----------------------------
# Use only with explicit permission of the system owner.
# Breaking things or getting arrested is on you, I'm just a goblin.
# ----------------------------- LICENSE -------------------------------
# Licensed under the MIT License (see LICENSE file in repo)
#======================================================================

#============================ ALPHA TABLE =============================
#------------------------------- bugs ---------------------------------
# [ ] 
#----------------------------- features -------------------------------
# [ ]
#======================================================================
#----------------------------------------------------------------------
#\ PRE

import sys;
from typing import Union;

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials

class ERR:
    NO_ERROR = 0;
    UNEXPECTED_ERROR = 1;
    BAD_USAGE = 2;

#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions



#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - Body

class Core:
    def __init__(self, argv:list, param:dict) -> None:
        self._valid:bool = True;
        self._args:dict = {};
        self._err:dict = {};
        
        req:list = [k for k, p in param.items() if p is True]
        for i, a in enumerate(argv):
            if a.startswith("-"):
                for p in param:
                    cp = p.rstrip("%");
                    if cp == a:
                        if p.endswith("%"):
                            try:
                                val = argv[i+1];
                                if not val.startswith("-"):
                                    self._args[cp.lstrip("-")] = val;
                            except IndexError: pass;
                        else:
                            self._args[cp.lstrip("-")] = True;
        
        for ra in req:
            if not ra.rstrip("%").lstrip("-") in self._args:
                self._valid = False;
                break;
    
    def set_err(self, d:dict) -> None:
        for k in d:
            if type(k) is int and type(d[k]) is str:
                self._err[k] = d[k];
    
    def check_format(self) -> None:
        if not self._valid: self.stop(ERR.BAD_USAGE);
    
    def arg(self, a:str) -> Union[str, int, bool]:
        return self._args.get(a, False);
    
    def stop(self, c) -> None:
        if c > ERR.NO_ERROR:
            print(f"ERR[{c}]: ", end="");
            if c == ERR.UNEXPECTED_ERROR: print("Unexpected error.");
            elif c == ERR.BAD_USAGE: print("Bad usage, check help page (-h).");
            else: print(self._err.get(c, "Unexpected error."));
            
        sys.exit(c);

#/ SRC - Body
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?