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
