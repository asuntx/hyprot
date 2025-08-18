import click

from manager import ThemeManager


@click.group()
def hyprot():
    """A hyprland theme manager"""
    pass


@hyprot.command()
@click.argument("theme_name")
def create(theme_name):
    manager = ThemeManager(theme_name=theme_name)
    manager.create_theme()


@hyprot.command()
@click.argument("theme_name")
@click.argument("new_name")
def rename(theme_name, new_name):
    manager = ThemeManager(theme_name=theme_name)
    manager.rename_theme(new_theme_folder_name=new_name)


@hyprot.command()
@click.argument("theme_name")
def delete(theme_name):
    manager = ThemeManager(theme_name=theme_name)
    manager.delete_theme()


hyprot.add_command(create)
hyprot.add_command(rename)
hyprot.add_command(delete)
if __name__ == "__main__":
    hyprot()
