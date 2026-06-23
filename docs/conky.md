# Conky Setup

This configuration features a beautiful **dual conky setup** using the **sqi-conky-theme** on both the left and right sides of your screen.

## sqi-conky-theme

The configuration uses two conky instances:
- **Left panel**: `sqi-left.conkyrc`
- **Right panel**: `sqi-right.conkyrc`


To manually start conky:
conky -c ~/.config/conky/sqi-left.conkyrc &
conky -c ~/.config/conky/sqi-right.conkyrc &
