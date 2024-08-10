from urllib import request, error


def html(url: str) -> str:
    response = request.urlopen(url)
    charset = response.headers.get_content_charset()
    if not charset or type(charset) != str:
        charset = "utf8"
    return response.decode(charset)
