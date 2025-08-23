import os
from typing import List, Optional
import click

from hyprtheme.utils.paths import get_conf_dirs, HYPERTHEME_PATH
from hyprtheme.utils.dirs import DirManager
from hyprtheme.utils.symlinks import Symlinks
from hyprtheme.utils.configReader import Config

config = Config()


class ThemeManager:
    def __init__(self):
        self.theme_name: Optional[str] = ""

    def set_theme_name(self, value: str):
        self.theme_name = value
        self.theme_folder: str = os.path.join(HYPERTHEME_PATH, self.theme_name)
        self.dirs = DirManager(self.theme_name)
        self.symlinks = Symlinks(self.theme_folder)

    # todo
    def add_dot_file(self, dot_file) -> None:
        click.echo(dot_file)
        self.dirs.scan()

    def list_themes(self) -> None:
        try:
            themes: List[str] = [
                f.path for f in os.scandir(HYPERTHEME_PATH) if f.is_dir()
            ]
        except FileNotFoundError:
            click.echo("hyprtheme directory not found, run 'hyprtheme init' to fix it")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            if themes is None or themes == []:
                click.echo(
                    "You don't have themes! create one with 'hyprtheme create {theme}'"
                )
            else:
                for t in themes:
                    click.echo(t)

    def set_theme(self) -> None:
        if config.read_theme() == self.theme_name:
            click.echo("You've already set this theme!")
            return

        for f in self.dirs.scan():
            f_path = os.path.join(self.theme_folder, f)
            self.dirs.delete(f_path)
            self.symlinks.link()
        else:
            if not config.set_theme(self.theme_name):
                click.echo(f"{self.theme_name} couldn't set theme")
                return

            click.echo(f"{self.theme_name} has been set")

    # todo
    def create_theme(self) -> None:
        if os.path.exists(self.theme_folder):
            click.echo(f"{self.theme_name} already exists.")
            return

        ask_copy = click.confirm("Do you wanna copy all yours dot files to this theme?")
        if ask_copy:
            conf_dirs = get_conf_dirs()

            if conf_dirs is None or conf_dirs == []:
                click.echo("It seems like you don't have any supportable dot file")
                return

            click.echo("The following dot files will be copied to your theme!")
            click.echo([os.path.basename(d) for d in conf_dirs])

            confirm = click.confirm("are you sure?")

            if not confirm:
                return

            create_theme_dir = self.dirs.create()
            if not create_theme_dir:
                return

            for dir in conf_dirs:
                hyprtheme_conf_dir = os.path.join(
                    self.theme_folder, os.path.basename(dir)
                )
                if not self.dirs.copy(dir, hyprtheme_conf_dir):
                    return
            else:
                click.echo(
                    f"{self.theme_name} theme has been created in {self.theme_folder}"
                )

        else:
            if self.dirs.create():
                click.echo(
                    f"{self.theme_name} theme has been created in {self.theme_folder}\nYou can add your dots later with 'hyprtheme add theme_name kitty' for example."
                )

    def rename_theme(self, new_theme_name) -> None:
        new_theme_path = os.path.join(HYPERTHEME_PATH, new_theme_name)
        if self.dirs.rename(self.theme_name, new_theme_path):
            click.echo(f"{self.theme_name} has been renamed to {new_theme_name}")

    def delete_theme(self) -> None:
        if self.dirs.delete():
            click.echo(f"{self.theme_name} theme has been deleted.")
