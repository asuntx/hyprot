import os


def get_xdg_config_home():
    xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
    if xdg_config_home and os.path.isabs(xdg_config_home):
        return xdg_config_home
    else:
        return os.path.join(os.path.expanduser("~"), ".config")


hyprot_config_path = os.path.join(get_xdg_config_home(), "hyprot")


def create_hyprot_folder():
    try:
        os.mkdir(hyprot_config_path)
    except FileExistsError:
        pass
    except OSError as e:
        print("A system error occured while creating hyprot folder", e)
