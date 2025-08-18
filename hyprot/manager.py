import click
import os
import shutil
from setup import hyprot_config_path


class ThemeManager:
    def __init__(self, theme_name):
        self.theme_name = theme_name
        self.theme_folder = os.path.join(hyprot_config_path, self.theme_name)

    def create_theme(self):
        try:
            os.mkdir(self.theme_folder)
        except FileExistsError:
            click.echo("You've already created this theme.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")

    def rename_theme(self, new_theme_folder_name):
        try:
            os.rename(self.theme_folder, new_theme_folder_name)
        except FileNotFoundError:
            click.echo(f"{new_theme_folder_name} folder doesn't exist")
        except FileExistsError:
            click.echo(f"{new_theme_folder_name} folder already exists")
        except OSError as e:
            click.echo(f"An unexpect OS error occured: {e}")

    def delete_theme(self):
        try:
            shutil.rmtree(self.theme_folder)
        except FileNotFoundError:
            click.echo(f"{self.theme_folder} doesn't exist.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
