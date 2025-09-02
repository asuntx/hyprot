import configparser
import click
from hyprtheme.utils.paths import HYPRTHEME_CONFIG


class Config:
    def read_theme(self) -> str | None:
        config = configparser.ConfigParser()
        config.read(HYPRTHEME_CONFIG)
        current_theme = config.get("GENERAL", "theme", fallback="None")
        return current_theme

    def set_theme(self, value: str) -> bool:
        config = configparser.ConfigParser()
        config.read(HYPRTHEME_CONFIG)
        config["GENERAL"]["theme"] = value
        try:
            with open(HYPRTHEME_CONFIG, "w") as f:
                config.write(f)
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
            return False
        else:
            return True
