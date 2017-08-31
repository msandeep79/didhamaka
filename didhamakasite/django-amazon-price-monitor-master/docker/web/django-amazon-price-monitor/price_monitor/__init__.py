"""Dummy init module for the price_monitor package. It will be overwritten when docker mounts the real package."""


def get_version():
    """
    Returns DEV as version. Just a placeholder while building the web docker image, will be overwritten by mounted docker volume.

    :return: the version identifier
    """
    return 'DEV'
