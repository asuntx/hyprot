import click
from hyprtheme.manager import ThemeManager

manager = ThemeManager()


@click.group()
def hyprtheme():
    """A hyprland theme manager"""
    pass


@hyprtheme.command()
def list():
    manager.list_themes()


@hyprtheme.command()
def sync():
    manager.sync_themes()


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
    manager.rename_theme(new_theme_folder_name=new_name)


@hyprtheme.command()
@click.argument("theme_name")
def delete(theme_name):
    manager.set_theme_name(theme_name)
    manager.delete_theme()


hyprtheme.add_command(sync)
hyprtheme.add_command(list)
hyprtheme.add_command(create)
hyprtheme.add_command(rename)
hyprtheme.add_command(delete)
if __name__ == "__main__":
    hyprtheme()
