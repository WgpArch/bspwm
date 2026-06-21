# Keybinds

bspwm uses **sxhkd** (Simple X Hotkey Daemon) for keyboard shortcuts. All keybinds are configured in `~/.config/sxhkd/sxhkdrc`.

## WM Independent Hotkeys

### Volume Control

| Shortcut | Action |
|----------|--------|
| `XF86AudioRaiseVolume` | Increase volume by 3% |
| `XF86AudioLowerVolume` | Decrease volume by 3% |
| `XF86AudioMute` | Toggle mute |

### Brightness Control

| Shortcut | Action |
|----------|--------|
| `XF86MonBrightnessUp` | Increase brightness by 5% |
| `XF86MonBrightnessDown` | Decrease brightness by 5% |

### Screenshots

| Shortcut | Action |
|----------|--------|
| `Super + Print` | Full screenshot |
| `Super + Shift + Print` | Select area screenshot |

### Applications

| Shortcut | Action |
|----------|--------|
| `Super + Return` | Open terminal (qterminal) |
| `Super + d` | Open application launcher (rofi) |
| `Super + e` | Open file manager (thunar) |
| `Super + w` | Open web browser (firefox-nightly) |

### System

| Shortcut | Action |
|----------|--------|
| `Super + Escape` | Reload sxhkd configuration |
| `Super + Alt + q` | Quit bspwm |
| `Super + Alt + r` | Restart bspwm |

## bspwm Hotkeys

### Window Management

| Shortcut | Action |
|----------|--------|
| `Super + q` | Close window |
| `Super + Shift + q` | Kill window |
| `Super + m` | Toggle monocle layout |
| `Super + t` | Set tiled state |
| `Super + Shift + t` | Set pseudo-tiled state |
| `Super + s` | Set floating state |
| `Super + f` | Set fullscreen state |

### Focus & Navigation

| Shortcut | Action |
|----------|--------|
| `Super + h/j/k/l` | Focus window in direction |
| `Super + Shift + h/j/k/l` | Swap window in direction |
| `Super + [1-9,0]` | Focus desktop 1-10 |
| `Super + Shift + [1-9,0]` | Send window to desktop 1-10 |
| `Super + Left/Right` | Focus previous/next desktop |
| `Super + Grave` | Focus last node/desktop |
| `Super + Tab` | Focus last node/desktop |

### Preselection

| Shortcut | Action |
|----------|--------|
| `Super + Ctrl + h/j/k/l` | Preselect direction |
| `Super + Ctrl + [1-9]` | Preselect ratio |
| `Super + Ctrl + Space` | Cancel preselection |

### Move & Resize

| Shortcut | Action |
|----------|--------|
| `Super + Alt + h/j/k/l` | Expand window side |
| `Super + Alt + Shift + h/j/k/l` | Contract window side |
| `Super + Arrow Keys` | Move floating window |

## Editing Keybinds

To modify keybinds, edit `~/.config/sxhkd/sxhkdrc` and reload with `Super + Escape`.
