# Theming

bspwm itself is minimal and doesn't have themes in the traditional sense. However, this configuration includes several theming elements:

## Configuration Files

- **`bspwmrc`**: Main configuration script that sets up bspwm rules, borders, and gaps
- **`sxhkdrc`**: Keyboard shortcuts configuration

## Window Borders

bspwm window borders are configured in the `bspwmrc` file. You can customize:
- Border width
- Border colors (focused, normal, urgent, etc.)
- Window gaps

## Wallpapers

This setup includes a `Wallpapers` directory with beautiful backgrounds including:
- Black and white photography
- Pink Floyd Dark Side of the Moon prism
- San Francisco cityscape

To set a wallpaper manually:

```bash
feh --bg-fill ~/.config/bspwm/Wallpapers/BlackSanFrancisco.jpg
