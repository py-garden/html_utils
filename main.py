from html import escape
from html.parser import HTMLParser

HTML_TAGS = {
    "html",
    "head",
    "title",
    "base",
    "link",
    "meta",
    "style",
    "script",
    "noscript",
    "body",
    "section",
    "nav",
    "article",
    "aside",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "footer",
    "address",
    "main",
    "p",
    "hr",
    "pre",
    "blockquote",
    "ol",
    "ul",
    "li",
    "dl",
    "dt",
    "dd",
    "figure",
    "figcaption",
    "div",
    "a",
    "em",
    "strong",
    "small",
    "s",
    "cite",
    "q",
    "dfn",
    "abbr",
    "data",
    "time",
    "code",
    "var",
    "samp",
    "kbd",
    "sub",
    "sup",
    "i",
    "b",
    "u",
    "mark",
    "ruby",
    "rt",
    "rp",
    "bdi",
    "bdo",
    "span",
    "br",
    "wbr",
    "ins",
    "del",
    "picture",
    "source",
    "img",
    "iframe",
    "embed",
    "object",
    "param",
    "video",
    "audio",
    "track",
    "map",
    "area",
    "table",
    "caption",
    "colgroup",
    "col",
    "tbody",
    "thead",
    "tfoot",
    "tr",
    "td",
    "th",
    "form",
    "label",
    "input",
    "button",
    "select",
    "datalist",
    "optgroup",
    "option",
    "textarea",
    "output",
    "progress",
    "meter",
    "fieldset",
    "legend",
    "details",
    "summary",
    "dialog",
    "canvas",
    "svg",
    "math",
}


class EscapeTextInsideCodeTags(HTMLParser):
    """
    This class is a html parser which takes in invalid html like this:

    <code>2 < 3 && 5 > 2</code>

    and is able to turn it into this:

    <code>2 &lt; 3 &amp;&amp; 5 &gt; 2</code>

    A dynamic parser is needed in this situation because we need to know when things are and are not tags.

    Additionally it is aware that things like <bloogas> is not a valid html tag.

    """

    def __init__(self):
        super().__init__()
        self.result = []
        self.in_code = False  # track if we are inside a <code> block

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        if tag_lower in HTML_TAGS:
            attrs_str = " ".join(f'{name}="{value}"' for name, value in attrs)
            self.result.append(f"<{tag} {attrs_str}>" if attrs_str else f"<{tag}>")
            if tag_lower == "code":
                self.in_code = True
        else:
            # if not a real html tag, escape it
            self.result.append(escape(f"<{tag}>"))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in HTML_TAGS:
            self.result.append(f"</{tag}>")
            if tag_lower == "code":
                self.in_code = False
        else:
            self.result.append(escape(f"</{tag}>"))

    def handle_data(self, data):
        if self.in_code:
            self.result.append(escape(data))  # escape code inside <code>
        else:
            self.result.append(data)  # normal text

    def get_result(self):
        return "".join(self.result)


def escape_code_tags(html: str) -> str:
    parser = EscapeTextInsideCodeTags()
    parser.feed(html)
    escaped_html = parser.get_result()
    return escaped_html


def escape_html(text: str) -> str:
    """
    Escapes HTML special characters in a string.

    Characters escaped:
        &  -> &amp;
        <  -> &lt;
        >  -> &gt;
        "  -> &quot;
        '  -> &#x27;

    Args:
        text (str): Input string to escape.

    Returns:
        str: Escaped string.
    """
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )


def extract_header_content(html_content: str) -> str:
    """
    Extracts the content of the <head> tag from the given HTML content.

    :param html_content: The full HTML content as a string.
    :return: The extracted header content.
    """
    start_index = html_content.find("<head>")
    end_index = html_content.find("</head>")
    if start_index != -1 and end_index != -1:
        return html_content[start_index + len("<head>") : end_index].strip()
    print("WARNING could not extract header contents")
    return ""


def extract_body_content(html_content: str) -> str:
    """
    Extracts the content of the <body> tag from the given HTML content.

    :param html_content: The full HTML content as a string.
    :return: The extracted body content.
    """
    start_index = html_content.find("<body>")
    end_index = html_content.find("</body>")
    if start_index != -1 and end_index != -1:
        return html_content[start_index + len("<body>") : end_index].strip()
    print("WARNING could not extract body contents")
    return ""


def add_text_to_header_and_body_of_html(
    html_content: str, head_text: str, body_text: str
) -> str:

    # find the closing head tag and insert the head_text before it
    head_index = html_content.find("</head>")
    if head_index != -1:
        html_content = (
            html_content[:head_index] + head_text + "\n" + html_content[head_index:]
        )

    # find the closing body tag and insert the body_text before it
    body_index = html_content.find("</body>")
    if body_index != -1:
        html_content = (
            html_content[:body_index] + body_text + "\n" + html_content[body_index:]
        )

    return html_content


BLANK_HTML_FILE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
</body>
</html>
"""
