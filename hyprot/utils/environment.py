import os

import click

from hyprot.setup import xdg_config_home

# general environment
# kitty
# zsh? might be

# hypr environment
hypr_dir: str = os.path.join(xdg_config_home, "hypr")
hyprland_conf: str = os.path.join(hypr_dir, "hyprland.conf")
hyprpaper_conf: str = os.path.join(hypr_dir, "hyprpaper.conf")
hyprlock_conf: str = os.path.join(hypr_dir, "hypaper.conf")
hyprot_hyprland_environment: set = {"hyprland.conf", "hyprpaper.conf", "hyprlock.conf"}
hypr_environment: str = ""


def get_conf_files() -> set:
    # hypr ones
    # compare hyprot environment with user hypr one.
    hypr_environment = hyprot_hyprland_environment & set(os.listdir(hypr_dir))
    # return generalenv and hypr
    return hypr_environment


environment = get_conf_files()


def conf_files():
    if not os.path.isdir(hypr_dir):
        click.echo("not found hypr directory maybe you don't have hyprland installed?")
        return None
    elif environment is None:
        click.echo(
            "not matched .conf files in your hyprland setup\n do you even have hyprland?"
        )
    else:
        return environment
