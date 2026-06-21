#!/bin/bash

# Define the options
options="Lock\nSuspend\nReboot\nShutdown\nLogout"

# Show rofi menu
selected=$(echo -e "$options" | rofi -dmenu -p "Power" -config ~/.config/sxhkd/rofi/config.rasi)

# Execute the selected option
case $selected in
    Lock) loginctl lock-session ;;
    Suspend) systemctl suspend ;;
    Reboot) systemctl reboot ;;
    Shutdown) systemctl poweroff ;;
    Logout) systemctl logout ;;
esac
