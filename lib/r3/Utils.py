#!/usr/bin/env python3
#======================================================================
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# -------------------------------- R3 ---------------------------------
# r3-lib/Utils [r3]
# v/0.1-alpha
# --------------------------- INSTRUCTIONS ----------------------------
# Utils module. Provides cool functions.
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

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials

#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions

#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - MAIN

def goblint(txt:str="", **karg) -> None:
    clr = {
        "@0": "\033[0m",
        "@b": "\033[1m",
        "@i": "\033[3m",
        "@c0": "\033[38;5;224m",
        "@c1": "\033[38;5;217m",
        "@c2": "\033[38;5;210m",
        "@c3": "\033[38;5;203m",
        "@c4": "\033[38;5;196m",
        "@c5": "\033[38;5;160m",
        "@r0": "\033[38;5;224m",
        "@r1": "\033[38;5;217m",
        "@r2": "\033[38;5;210m",
        "@r3": "\033[38;5;203m",
        "@r4": "\033[38;5;196m",
        "@r5": "\033[38;5;160m",
        "@c-g0": "\033[38;5;82m",
        "@c-g1": "\033[38;5;193m",
        "@c-y0": "\033[38;5;226m",
        "@rb0": "\033[48;5;124m\033[1m\033[38;5;224m",
        "@ICO-ok": "\033[38;5;82m\033[1m[✔] \033[0m"
    }

    import os;
    if os.environ.get("R3_BLUE", "0") == "1":
        clr["@c0"] = "\033[38;5;231m";
        clr["@c1"] = "\033[38;5;153m";
        clr["@c2"] = "\033[38;5;111m";
        clr["@c3"] = "\033[38;5;69m";
        clr["@c4"] = "\033[38;5;27m";
        clr["@c5"] = "\033[38;5;21m";

    if os.environ.get("R3_BORING", "0") == "1":
        for k, v in clr.items(): txt = txt.replace(k, "");
    else:
        for k, v in clr.items(): txt = txt.replace(k, v);
        
    print(txt, **karg);

def compile_py(src:str, lib:str, on:str, s:bool=False) -> None:
    goblint("@c-y0@bCOMPILING...@0", end="", flush=True);
    
    from time import sleep;
    import subprocess as proc, sys, shutil;
    base = lib + "/..";
    proc.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--windowed", "--noconfirm", "--log-level=ERROR",
        f"--distpath={base}/dist", "--workpath=/tmp/r3_build", f"--paths={lib}",
        f"--specpath=/tmp/r3_build",f"--name={on}", f"{base}/{src}"
    ], stdout=proc.DEVNULL, stderr=proc.DEVNULL, check=True);
    shutil.rmtree("/tmp/r3_build");

    goblint(f"\r\033[K", end="", flush=True);
    goblint(f"@ICO-ok@c-g0@bSUCCESS @c4- @0@c1File located at @b@c-g1dist/{on}");
    sleep(1); # I... I don't know if I'm comfortable with this.

def get_info() -> list:
    import configparser;
    from pathlib import Path;
    cfg = configparser.ConfigParser();
    cfg.read(Path(__file__).resolve().parent / "config.ini");

    l = [];
    for i in cfg:
        if i != "DEFAULT": l.append(get_module_info(i));
    
    return l;

# Yeah, yeah, I can see it too. I'm a little lazy today aight?
def get_module_info(i:str) -> dict:
    import configparser;
    from pathlib import Path;
    cfg = configparser.ConfigParser();
    cfg.read(Path(__file__).resolve().parent / "config.ini");

    if not i in cfg:
        return {
            "id": "r30XX",
            "name": "Module",
            "ver": "0.0-proto",
            "path": "src/goblin.py",
            "usage": "python3 goblin.py"
        };
    else:
        return {
            "id": i,
            "name": cfg[i]["name"],
            "ver": cfg[i]["ver"],
            "path": cfg[i]["path"],
            "usage": cfg[i]["usage"],
            "help": ""
        }

#/ SRC - MAIN
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?