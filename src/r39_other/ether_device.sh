#!/bin/bash
#======================================================================
# Brought to you by ~ r3dg0bl1n <(¬‿¬)>
# -------------------------------- R3 ---------------------------------
# r3-pkg/ether_device [r3901]
# v/0.1-alpha
# req : cryptsetup, openssl
# --------------------------- INSTRUCTIONS ----------------------------
# Usage: ./ether_device.sh [DEVICE_LABEL]
# DEVICE_LABEL : Specify the device you wish to open. Default is "sdb1".
# (?) : Remember to give execute permissions: chmod +x ether_device.sh
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
# [ ]
#----------------------------- features -------------------------------
# [ ] Better flow of creating/deleting users and mounting/unmounting.
#======================================================================
#----------------------------------------------------------------------
#\ PRE

BASE="/home/"
m=$(find $BASE -maxdepth 1 -type d -name "s3k*" -printf "%f\n" | head -n 1)
d=${1:-sdb1}

if [ -n "$m" ]; then
	sudo umount "$BASE$m/mnt"
	sudo cryptsetup close "$m"
	sudo userdel -r "$m" > /dev/null 2>&1
	echo "[*] Device /dev/$d unmounted and user $m deleted."
else
	un="s3k$(openssl rand -hex 8)"
	sudo cryptsetup open "/dev/$d" "$un" || exit 1
	
	dir="$BASE$un"
	pwd=$(openssl rand -base64 32)
	sudo useradd -s /bin/bash "$un" -m
	sudo usermod -p $(openssl passwd -6 $pwd) "$un"
	
	printf '%s\n' 'umask 077' | sudo tee -a "$dir/.profile" > /dev/null
	printf '%s\n' 'umask 077' | sudo tee -a "$dir/.bashrc"  > /dev/null
	printf '%s\n' 'umask 077' | sudo tee -a "$dir/.zshrc"   > /dev/null
	sudo chown "$un:$un" "$dir/.profile" "$dir/.bashrc" "$dir/.zshrc"

	sudo mkdir -p "$dir/mnt"
	sudo mount "/dev/mapper/$un" "$dir/mnt"
	
	printf '%s\n' "$pwd" | sudo tee "$BASE$un/tmp.creds" > /dev/null
	sudo chmod 400 "$BASE$un/tmp.creds"
	
	sudo chown -R "$un:$un" "$dir"
	sudo chmod -R 600 "$dir"
	sudo find "$dir" -type d -exec chmod 700 {} \;
	sudo find "$dir" -type f -name "*.sh" -exec chmod 700 {} \;
	
	echo "[*] Device /dev/$d mounted at $dir/mnt"
	sudo -u "$un" -i "$SHELL"
fi