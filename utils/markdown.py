from markdown import markdown as _markdown
from markdown.extensions.fenced_code import FencedCodeExtension as _FencedCodeExtension


def markdown(txt):
    return _markdown(
        txt,
        extensions=[_FencedCodeExtension()]
    )
