#!/usr/bin/env python3
#======================================================================
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# -------------------------------- R3 ---------------------------------
# r3-pkg/ether_device [r3901]
# v/0.2-alpha
# req : cryptsetup
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: python3 ether_device.py [-d DEVICE_LABEL] [--open|--close]
# -d : Specifies the device label to work with. (default: sdb)
# --open : Opens the encrypted device.
# --close : Closes the encrypted device.
# (?) : Becareful when specifying device, don't mess with system drives.
# ------------------------------ NOTES --------------------------------
# If your sudo user has a weak password, this script can't do miracles.
# ---------------------------- DISCLAIMER -----------------------------
# Use only with explicit permission of the system owner.
# Breaking things or getting arrested is on you, I'm just a goblin.
# ----------------------------- LICENSE -------------------------------
# Licensed under the MIT License (see LICENSE file in repo).
#======================================================================

#============================ ALPHA TABLE =============================
#------------------------------- bugs ---------------------------------
# [ ] Can't actually check if device is already opened or closed for
# multiple devices. Only first created instance is detected properly.
#----------------------------- features -------------------------------
# [X] Better flow of creating/deleting users and mounting/unmounting.
# [ ] Improve security against local attacks.
# [ ] Q prompt to create new crypted device or destroy existing one.
# [ ] Increase pythonic code style. Reduce use of subprocess where possible.
# [ ] Implement formatting option when device is corrupted or unformatted.
#======================================================================
#----------------------------------------------------------------------
#\ PRE

import sys, os.path as P, os, subprocess;
sys.path.insert(0, P.abspath(P.join(P.dirname(__file__), "../../lib")));
from r3 import Core, ERR, goblint, QA;

def _pre(argv) -> Core:
    c = Core("r3901", argv, { 
        "-d%": False,
        "--open": False,
        "--close": False
    }, False, ["cryptsetup"]);
    c.set_err({
        1: "Device not found.",
        2: "Are you really trying to open and close at the same time?",
        3: "Could not open device. Already opened?",
        4: "Could not close device. Is it opened?",
        5: "Device filesystem is corrupted or not formatted.",
    });
    return c;

if __name__ == "__main__":
    _core = _pre(sys.argv);
    _core.load(); # EXIT

#/ PRE
#----------------------------------------------------------------------
#\ H - Essentials

if __name__ == "__main__":
    def run(cmd, **kwargs) -> str:
        return subprocess.run(cmd, shell=True, capture_output=True, **kwargs).stdout.decode().strip();

    def gusr() -> str:
        return run(f'find /home/ -maxdepth 1 -type d -name "s3k*" -printf "%f\n" | head -n 1')

#/ H - Essentials
#----------------------------------------------------------------------
#\ SRC - Functions

if __name__ == "__main__":
    def chk(usr:str="") -> None:
        e = P.exists(f"/dev/{dev}");
        if not e: _core.stop(ERR.C(1));
        elif _core.arg("open") and _core.arg("close"): _core.stop(ERR.C(2));
        elif _core.arg("open") and usr: _core.stop(ERR.C(3));
        elif _core.arg("close") and not usr: _core.stop(ERR.C(4));

    def open() -> None: # This could be cleaner
        import secrets;
        from passlib.hash import sha512_crypt as crypt;
        usr = "s3k" + secrets.token_hex(8);
        run(f"sudo cryptsetup open /dev/{dev} {usr} || exit 1");

        dir=f"/home/{usr}";
        pwd=secrets.token_hex(16); # Saving password on memory? Hmm...
        run(f"sudo useradd -s /bin/bash {usr} -m");
        run(f"sudo usermod {crypt.hash(pwd)} {usr}");

        for df in [".profile", ".bashrc", ".zshrc"]:
            run(f"printf '%s\n' 'umask 077' | sudo tee -a {dir}/{df} > /dev/null");
            run(f"sudo chown {usr}:{usr} {dir}/{df}");

        run(f"sudo mkdir {dir}/mnt");
        run(f"sudo mount /dev/mapper/{usr} {dir}/mnt");

        run(f"printf '%s\n' {pwd} | sudo tee {dir}/.creds > /dev/null");
        run(f"sudo chmod 400 {dir}/.creds");
    
        run(f"sudo chown -R {usr}:{usr} {dir}");
        run(f"sudo chmod -R 600 {dir}/mnt");

        run(f"sudo find {dir}/mnt -type d -exec chmod 700 {{}} +");
        run(f"sudo find {dir}/mnt -type f -name '*.sh' -exec chmod 700 {{}} +");
        
        goblint(f"@0@c4# @c2Session started for user {usr}. Check ~/.creds for password.@0");
        subprocess.call(["sudo", "-u", usr, "-i", os.environ["SHELL"]]);

    def close(usr) -> None:
        run(f"sudo umount /home/{usr}/mnt");
        run(f"sudo cryptsetup close {usr}");
        run(f"sudo userdel -r {usr}");
        goblint(f"@0@c4# @c2Device closed and user {usr} deleted.@0");

    def create() -> None: # THIS IS BAD, REAL BAD
        ok = run(f"sudo blkid /dev/{dev}") != "";
        if not ok:
            fix = QA(f"@0@r1@bDevice /dev/{dev} is unformatted or corrupted. Do you want to format it now?").confirm();
            if fix:
                run(f"sudo wipefs -a /dev/{dev}");
                run(f"sudo parted /dev/{dev} -- mklabel gpt mkpart primary ext4 1MiB 100%");
                run(f"sudo mkfs.ext4 /dev/{dev}1");
            else: _core.stop(ERR.C(5));

        run(f"sudo cryptsetup luksFormat /dev/{dev}");
        goblint(f"@0@c4# @c2Device /dev/{dev} is now encrypted.@0");

    def destroy() -> None: # THIS IS BAD, REAL BAD
        safe = QA(f"ARE YOU SURE YOU WANT TO DESTROY /dev/{dev}?").confirm();
        if safe:
            run(f"sudo cryptsetup luksErase /dev/{dev}");
            run(f"sudo wipefs -a /dev/{dev}");
            run(f"sgdisk --zap-all /dev/{dev}");
            run(f"sudo dd if=/dev/zero of=/dev/{dev} bs=16M status=progress");
            goblint(f"@0@c4# @c2Device /dev/{dev} encryption destroyed.@0");

#/ SRC - Functions
#----------------------------------------------------------------------
#\ SRC - MAIN

if __name__ == "__main__":
    dev=_core.arg("d","sdb");
    u = gusr();
    chk(u); # EXIT
    
    if _core.arg("open"): open();
    elif _core.arg("close"): close(u);
    else:
        QA(f"@0@c1@bTell me youngz one, what do you wish to do with /dev/{dev}?").complex([
            QA.R("open", "Open the encrypted device", open),
            QA.R("close", "Close the encrypted device", lambda: close(u)),
            #QA.R("create", "Create or regenerate encryption", create),
            #QA.R("destroy", "Destroy an existing device", destroy)
        ]);

    _core.stop(ERR.NO_ERROR);

#/ SRC - MAIN
#----------------------------------------------------------------------

# =====================================================================
# Soy español, ¿a qué quieres que te gane?