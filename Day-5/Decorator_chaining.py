
def bold_tag(func):
    def wrapper(text):
        return f"<b>{func(text)}</b>"
    return wrapper

def italic_tag(func):
    def wrapper(text):
        return f"<i>{func(text)}</i>"
    return wrapper

@bold_tag
@italic_tag
def msg(text):
    return text


print(msg("Hello"))