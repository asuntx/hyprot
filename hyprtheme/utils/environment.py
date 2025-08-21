import os
import shutil
import click
from typing import Set, List
from hyprtheme.setup import xdg_config_home

# general environment
# kitty
# waybar?
# wofi?
# zsh? maybe

# hypr environment
hypr_dir: str = os.path.join(xdg_config_home, "hypr")
# will i even use this?
# hyprland_conf: str = os.path.join(hypr_dir, "hyprland.conf")
# hyprpaper_conf: str = os.path.join(hypr_dir, "hyprpaper.conf")
# hyprlock_conf: str = os.path.join(hypr_dir, "hypaper.conf")
hyprland_environment: Set[str] = {
    "hyprland.conf",
    "hyprpaper.conf",
    "hyprlock.conf",
}
# hypr_environment: str = ""


def compare_conf_files(themeDir: str) -> None:
    try:
        theme_conf_files: Set[str] = set(os.listdir(themeDir))
    except OSError as e:
        click.echo(f"An unexpected OS error occured: {e}")
    except FileNotFoundError:
        click.echo(f"{themeDir} doesn't exist?")
    else:
        diffs: Set[str] = hyprland_environment - theme_conf_files
        if diffs == set():
            return
        for diff in diffs:
            diff_path: str = os.path.join(hypr_dir, diff)
            try:
                shutil.copy(diff_path, themeDir)
            except FileNotFoundError:
                click.echo(f"Not found {themeDir}")
            except OSError as e:
                click.echo(f"An unexpected OS error occured: {e}")
        else:
            click.echo(
                f"{os.path.basename(themeDir)} theme synced with your dot files: {diffs} added"
            )


def get_conf_files() -> Set[str] | None:
    try:
        read_hypr_dir: List[str] = os.listdir(hypr_dir)
    except OSError as e:
        click.echo(f"An unexpected OS error occurred: {e}")
    except FileNotFoundError:
        click.echo("hypr directory not found maybe you dont' have hyprland installed?")
    else:
        conf_files = hyprland_environment & set(read_hypr_dir)
    return conf_files
