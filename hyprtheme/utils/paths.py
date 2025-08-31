import os
from typing import List
from pathlib import Path

# dot_files
# zsh? maybe


def get_xdg_config_home() -> str:
    XDG_CONFIG_HOME: str | None = os.environ.get("XDG_CONFIG_HOME")
    if XDG_CONFIG_HOME and os.path.isabs(XDG_CONFIG_HOME):
        return XDG_CONFIG_HOME
    else:
        return os.path.join(os.path.expanduser("~"), ".config")


def get_project_root() -> Path:
    return Path(__file__).parent.parent


ROOT = get_project_root()
XDG_CONFIG_HOME: str = get_xdg_config_home()
HYPERTHEME_PATH: str = os.path.join(XDG_CONFIG_HOME, "hyprtheme")
HYPRTHEME_CONFIG: str = os.path.join(ROOT, "hyprtheme.ini")

# DOT_FILES_PATHS
HYPR_PATH: str = os.path.join(XDG_CONFIG_HOME, "hypr")
WAYBAR_PATH: str = os.path.join(XDG_CONFIG_HOME, "waybar")
KITTY_PATH: str = os.path.join(XDG_CONFIG_HOME, "kitty")
dot_dirs = [HYPR_PATH, WAYBAR_PATH, KITTY_PATH]


def get_conf_dirs() -> List[str] | None:
    return [dir for dir in dot_dirs if os.path.exists(dir)]
