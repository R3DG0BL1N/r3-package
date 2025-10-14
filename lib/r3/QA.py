#!/usr/bin/env python3
#======================================================================
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# -------------------------------- R3 ---------------------------------
# r3-lib/QA [r3]
# v/0.1-alpha
# --------------------------- INSTRUCTIONS ----------------------------
# Question-Answer module. Execute functions depending on user input.
# ------------------------------ NOTES --------------------------------
# My momma once told me, clean yo ass before cleaning somebody else's.
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

from .Utils import goblint;

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials

#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions

def sp_input(pre:str, suf:str) -> str:
    pass

#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - Body

class QA:
    class R:
        def __init__(self, i:str, t:str="", f=lambda *a,**ka:None):
            self.inp:str = i;
            self.text:str = t;
            self.fn = f;

    def __init__(self, t:str, r:list=[], sh:bool=False):
        self.text:str = t;
        self.rules:list = r;
        self.short:bool = sh;
        self.ans:str = "";
        self.start();
    
    def start(self) -> None:
        q:str = "";
        if self.short:
            q += "@0@c3@b--------------------------------------\n";
            q += f"@c1@b{self.text}@0@c0";
            if self.rules: q += " (";
        else:
            q += f"@0@c1@b{self.text}\n";
            q += "@0@c3@b--------------------------------------\n@0";

        for r in self.rules:
            if isinstance(r, QA.R):
                if self.short: q += f"{r.inp}/";
                else: q += f"@0@c3[@c0@b {r.inp} @0@c3] @0@c0@b{r.text}\n";
        if self.short and self.rules: q += "\b)";
        goblint(q, end="");

        valid:bool = False;
        while not valid:
            goblint(f"@c4@b{": " if self.short else "> "}@0@c0", end="");
            self.ans = input().lower().replace(" ", "_");
            
            valid = not self.rules;
            for r in self.rules:
                if isinstance(r, QA.R) and r.inp == self.ans:
                    valid = True;
                    goblint("\r\033[K", end="");
                    r.fn();
                    break;
            
            if not valid:
                n = 2+len(self.ans);
                if self.short: n += len(q)-2;
                goblint(f"@rb0NOT VALID. Try again c:@0", end="");
                goblint(f"\033[F\033[K", end="", flush=True);
                if self.short: goblint(f"{q}", end="");

#/ SRC - Body
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?