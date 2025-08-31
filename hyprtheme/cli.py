import click
from hyprtheme.manager import ThemeManager
from hyprtheme.setup import run_setup

manager = ThemeManager()


@click.group()
def hyprtheme():
    """A hyprland theme manager"""
    pass


@hyprtheme.command()
def init():
    run_setup()


@hyprtheme.command()
@click.argument("theme_name")
@click.argument("dot_file")
def add(theme_name, dot_file):
    manager.set_theme_name(theme_name)
    manager.add_dot_file(dot_file=dot_file)


@hyprtheme.command()
@click.argument("theme_name")
def set(theme_name):
    manager.set_theme_name(theme_name)
    manager.set_theme()


@hyprtheme.command()
def list():
    manager.list_themes()

@hyprtheme.command()
@click.argument("theme_name")
def create(theme_name):
    manager.set_theme_name(theme_name)
    manager.create_theme()


@hyprtheme.command()
@click.argument("theme_name")
@click.argument("new_name")
def rename(theme_name, new_name):
    manager.set_theme_name(theme_name)
    manager.rename_theme(new_name)


@hyprtheme.command()
@click.argument("theme_name")
def delete(theme_name):
    manager.set_theme_name(theme_name)
    manager.delete_theme()


hyprtheme.add_command(init)
hyprtheme.add_command(add)
hyprtheme.add_command(set)
hyprtheme.add_command(list)
hyprtheme.add_command(create)
hyprtheme.add_command(rename)
hyprtheme.add_command(delete)
if __name__ == "__main__":
    hyprtheme()
