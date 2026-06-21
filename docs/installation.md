# Installation

Follow these steps to install and set up this bspwm configuration on your Arch Linux system.

## Prerequisites

Install the required packages from the official repositories:

```bash
sudo pacman -S bspwm sxhkd xorg-xinit conky rofi thunar qterminal firefox-nightly maim brightnessctl dunst


## Setup

1. Clone or download this repository.

2. Copy the configuration files to your `~/.config/` directory:

```bash
cp -r configs/bspwm/* ~/.config/bspwm/
cp -r configs/sxhkd/* ~/.config/sxhkd/
cp -r config/sxhkd/rofi/* ~/.config/sxhkd/rofi
cp -r configs/conky/* ~/.config/conky/

chmod +x ~/.config/bspwm/bspwmrc
