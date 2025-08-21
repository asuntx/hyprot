import os
from typing import List
from hyprtheme.setup import xdg_config_home

# general environment
# zsh? maybe

hypr_dir: str = os.path.join(xdg_config_home, "hypr")
waybar_dir: str = os.path.join(xdg_config_home, "waybar")
kitty_dir: str = os.path.join(xdg_config_home, "kitty")
dot_dirs = [hypr_dir, waybar_dir, kitty_dir]


def get_conf_dirs() -> List[str] | None:
    return [dir for dir in dot_dirs if os.path.exists(dir)]
