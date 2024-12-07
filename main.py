
def extract_header_content(html_content: str) -> str:
    """
    Extracts the content of the <head> tag from the given HTML content.

    :param html_content: The full HTML content as a string.
    :return: The extracted header content.
    """
    start_index = html_content.find("<head>")
    end_index = html_content.find("</head>")
    if start_index != -1 and end_index != -1:
        return html_content[start_index + len("<head>"):end_index].strip()
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
        return html_content[start_index + len("<body>"):end_index].strip()
    print("WARNING could not extract body contents")
    return ""

BLANK_HTML_FILE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
</body>
</html>
"""
