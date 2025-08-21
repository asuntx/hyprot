import os
import configparser
import click


def get_xdg_config_home() -> str:
    xdg_config_home: str | None = os.environ.get("XDG_CONFIG_HOME")
    if xdg_config_home and os.path.isabs(xdg_config_home):
        return xdg_config_home
    else:
        return os.path.join(os.path.expanduser("~"), ".config")


xdg_config_home: str = get_xdg_config_home()
hyprtheme_path: str = os.path.join(xdg_config_home, "hypr/hyprtheme")
hyprtheme_config: str = os.path.join(os.path.dirname(__file__), "hyprtheme.ini")


def run_setup() -> None:
    config = configparser.ConfigParser()
    config.read(hyprtheme_config)
    setup = config["GENERAL"]["setup"]

    if not os.path.exists(hyprtheme_path):
        config["GENERAL"]["setup"] = "false"
        try:
            with open(hyprtheme_config, "w") as f:
                config.write(f)
        except OSError as e:
            click.echo(f"An unexpected OS error has occured: {e}")

    if setup == "true":
        click.echo("You've already set up hyprtheme!")
        return

    else:
        try:
            os.mkdir(hyprtheme_path)
        except FileExistsError:
            pass
        except OSError as e:
            click.echo(f"An unexpected OS error has occurred: {e}")
        else:
            click.echo("Set up! Let's rice!")
            config["GENERAL"]["setup"] = "true"
            try:
                with open(hyprtheme_config, "w") as f:
                    config.write(f)
            except OSError as e:
                click.echo(f"An unexpected OS error has occured: {e}")
