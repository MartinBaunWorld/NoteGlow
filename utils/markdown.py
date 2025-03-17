from markdown import markdown as _markdown


def markdown(txt):
    return _markdown(
        txt,
        extensions=['fenced_code', 'sane_lists']
    )
