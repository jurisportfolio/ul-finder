from urllib import request, error


def html(url: str) -> str:
    try:
        response = request.urlopen(url)
        charset = response.headers.get_content_charset()
        if charset is not str:
            charset = "utf8"
        return response.read().decode(charset)

    except error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")

    except error.URLError as e:
        print(f"URL Error: {e.reason}")
