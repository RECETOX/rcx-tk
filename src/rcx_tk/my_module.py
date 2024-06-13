"""Documentation about the rcx_tk module."""


# FIXME: put actual code here
import datetime


def hello(name):
    """Say hello.

    Function docstring using Google docstring style.

    Args:
        name (str): Name to say hello to

    Returns:
        str: Hello message

    Raises:
        ValueError: If `name` is equal to `nobody`

    Example:
        This function can be called with `Jane Smith` as argument using

        >>> from rcx_tk.my_module import hello
        >>> hello('Jane Smith')
        'Hello Jane Smith!'

    """
    if name == 'nobody':
        raise ValueError('Can not say hello to nobody')
    return f'{get_todays_date()}: Hello {name}!'

def get_todays_date():
    today = datetime.datetime.date(datetime.datetime.now()).strftime("%d.%m.%Y")
    return today
