#!/bin/bash

######################################################################################################################

sudo pacman -S wget --noconfirm --needed

echo "Getting the Adklinux keys from the Adklinux repo"

sudo wget https://github.com/adklinux/adklinux_repo/raw/master/x86_64/adklinux-keyring-20230919-6-any.pkg.tar.zst -O /tmp/adklinux-keyring-20230919-6-any.pkg.tar.zst
sudo pacman -U --noconfirm --needed /tmp/adklinux-keyring-20230919-6-any.pkg.tar.zst

######################################################################################################################

echo "Getting the latest Adklinux mirrors file"

sudo wget https://raw.githubusercontent.com/adklinux/adk-mirrorlist/master/etc/pacman.d/adk-mirrorlist -O /etc/pacman.d/adk-mirrorlist
echo '
#[adk_repo_testing]
#SigLevel = Required DatabaseOptional
#Include = /etc/pacman.d/adk-mirrorlist

[adk_repo]
SigLevel = Required DatabaseOptional
Include = /etc/pacman.d/adk-mirrorlist