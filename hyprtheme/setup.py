import os
import configparser
import click
from hyprtheme.utils.dirs import DirManager
from hyprtheme.utils.paths import HYPERTHEME_PATH, HYPRTHEME_CONFIG


dir = DirManager(HYPERTHEME_PATH)


def create_hyprtheme_dir():
    config = configparser.ConfigParser()
    config.read(HYPRTHEME_CONFIG)
    dir.create(HYPERTHEME_PATH)
    config["GENERAL"]["setup"] = "true"
    try:
        with open(HYPRTHEME_CONFIG, "w") as f:
            config.write(f)
    except OSError as e:
        click.echo(f"An unexpected OS error has occured: {e}")

    click.echo("Set up! Let's rice!")


def run_setup() -> None:
    config = configparser.ConfigParser()
    config.read(HYPRTHEME_CONFIG)
    setup = config["GENERAL"]["setup"]
    if not os.path.exists(HYPERTHEME_PATH):
        create_hyprtheme_dir()
        return

    if setup == "true":
        click.echo("You've already set up hyprtheme!")
        return
