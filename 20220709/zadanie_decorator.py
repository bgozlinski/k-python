#  Sworz dekoratory bold, italic, ktore udekoruja tekst zwracanay przez inne funcje znacznikami html <b></b>, <i></i>

from functools import wraps


def bold_html_decor(func):
    @wraps(func)
    def wrapper(*args):
        return f'<b>{func(*args)}</b>'

    return wrapper


def italic_html_decor(func):
    @wraps(func)
    def wrapper(*args):
        return f'<i>{func(*args)}</i>'

    return wrapper


@bold_html_decor
def paragraph(text: str) -> str:
    return f'<p>{text}</p>'


assert paragraph('ala ma kota') == '<b><p>ala ma kota</p></b>'


@italic_html_decor
def paragraph(text: str) -> str:
    return f'<p>{text}</p>'


assert paragraph('ala ma kota') == '<i><p>ala ma kota</p></i>'
