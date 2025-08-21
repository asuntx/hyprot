import os
import shutil
from typing import List, Optional
import click

from hyprtheme.setup import hyprtheme_path
from hyprtheme.utils.environment import hypr_dir
from hyprtheme.utils.environment import get_conf_files
from hyprtheme.utils.environment import compare_conf_files


class ThemeManager:
    def __init__(self):
        self.theme_name: Optional[str] = ""

    def set_theme_name(self, value: str):
        self.theme_name = value
        self.theme_folder: str = os.path.join(hyprtheme_path, self.theme_name)

    def list_themes(self) -> None:
        try:
            themes: List[str] = [
                f.path for f in os.scandir(hyprtheme_path) if f.is_dir()
            ]
        except FileNotFoundError:
            # we might change this message
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

    # todo
    def set_theme(self) -> None:
        click.echo(f"{self.theme_name} has been set")

    def sync_themes(self) -> None:
        """syncs all hyprtheme themes to available conf_files from user"""
        try:
            themes: List[str] = [
                f.path for f in os.scandir(hyprtheme_path) if f.is_dir()
            ]
        except FileNotFoundError:
            click.echo("hyprtheme directory not found run 'hyprtheme init' to fix it")
        except OSError as e:
            click.echo(f"An unexpected OS error occurred: {e}")
        else:
            for t in themes:
                compare_conf_files(t)

    def create_theme(self) -> None:
        try:
            os.mkdir(self.theme_folder)
        except FileNotFoundError:
            click.echo("hyprtheme directory not found run 'hyprtheme init' to fix it")
        except FileExistsError:
            click.echo("You've already created this theme.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            conf_files = get_conf_files()
            if conf_files is not None:
                # copy conf files to hyprtheme/theme
                for file in conf_files:
                    conf_file_path: str = os.path.join(hypr_dir, file)
                    hypr_conf_file_path: str = os.path.join(self.theme_folder, file)
                    try:
                        shutil.copy(conf_file_path, hypr_conf_file_path)
                    except FileNotFoundError:
                        click.echo("Not found hypr directory or hyprtheme directory")
                    except OSError as e:
                        click.echo(f"An unexpected OS error occured: {e}")
                else:
                    click.echo(
                        f"Theme created succesfully. You can edit your theme at {self.theme_folder}"
                    )

    def rename_theme(self, new_theme_folder_name) -> None:
        new_theme_folder_path = os.path.join(hyprtheme_path, new_theme_folder_name)
        try:
            os.rename(self.theme_folder, new_theme_folder_path)
        except FileNotFoundError:
            click.echo(f"{self.theme_folder} folder doesn't exist")
        except FileExistsError:
            click.echo(f"{new_theme_folder_name} folder already exists")
        except OSError as e:
            click.echo(f"An unexpect OS error occured: {e}")
        else:
            click.echo(
                f"'{self.theme_name}' theme changed to '{new_theme_folder_name}' successfuly"
            )

    def delete_theme(self) -> None:
        try:
            shutil.rmtree(self.theme_folder)
        except FileNotFoundError:
            click.echo(f"{self.theme_folder} doesn't exist.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            click.echo(f"'{self.theme_name}' theme deleted successfully")
