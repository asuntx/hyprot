import os
import shutil
from typing import List, Optional
import click

from hyprot.setup import hyprot_config_path
from hyprot.utils.environment import hypr_dir
from hyprot.utils.environment import environment as conf_files
from hyprot.utils.environment import compare_conf_files


class ThemeManager:
    def __init__(self):
        self.theme_name: Optional[str] = ""

    def set_theme_name(self, value: str):
        self.theme_name = value
        self.theme_folder: str = os.path.join(hyprot_config_path, self.theme_name)

    def list_themes(self) -> None:
        try:
            themes: List[str] = [
                f.path for f in os.scandir(hyprot_config_path) if f.is_dir()
            ]
        except FileNotFoundError:
            # we might change this message
            click.echo(
                "Hyprot folder not found, why did you delete it? run 'hyprot restore' to restore it"
            )
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            if themes is None:
                click.echo(
                    "You dont' have themes! create one with 'hyprot create {theme}"
                )
            else:
                for t in themes:
                    click.echo(t)

    # todo
    def set_theme(self) -> None:
        click.echo(f"{self.theme_name} has been set")

    def sync_themes(self) -> None:
        """syncs all hyprot themes to available conf_files from user"""
        themes: List[str] = [
            f.path for f in os.scandir(hyprot_config_path) if f.is_dir()
        ]
        for t in themes:
            compare_conf_files(t)

    # watch
    def create_theme(self) -> None:
        try:
            os.mkdir(self.theme_folder)
        except FileExistsError:
            click.echo("You've already created this theme.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            if conf_files is not None:
                # copy conf files to hyprot/theme
                for conf_file in conf_files:
                    conf_file_path: str = os.path.join(hypr_dir, conf_file)
                    hypr_conf_file_path: str = os.path.join(
                        self.theme_folder, conf_file
                    )
                    try:
                        shutil.copy(conf_file_path, hypr_conf_file_path)
                    except FileNotFoundError:
                        click.echo("Not found hypr directory or hyprot directory")
                    except OSError as e:
                        click.echo(f"An unexpected OS error occured: {e}")
                else:
                    click.echo(
                        f"Theme created succesfully. You can edit your theme at {self.theme_folder}"
                    )

    def rename_theme(self, new_theme_folder_name) -> None:
        try:
            os.rename(self.theme_folder, new_theme_folder_name)
        except FileNotFoundError:
            click.echo(f"{self.theme_folder} folder doesn't exist")
        except FileExistsError:
            click.echo(f"{new_theme_folder_name} folder already exists")
        except OSError as e:
            click.echo(f"An unexpect OS error occured: {e}")

    def delete_theme(self) -> None:
        try:
            shutil.rmtree(self.theme_folder)
        except FileNotFoundError:
            click.echo(f"{self.theme_folder} doesn't exist.")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            click.echo(f"{self.theme_name} theme deleted successfully")
