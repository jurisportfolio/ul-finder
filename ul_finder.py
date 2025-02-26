from ul_finder_src import cli, html_parser, fetch_resource


def greatest_ul(html: str) -> dict:
    extractor = html_parser.UlExtractor()
    extractor.feed(html)
    uls = extractor.all_uls()
    if uls:
        greatest_ul = uls[0]
        for ul in uls:
            if ul["has_li"] > greatest_ul["has_li"]:
                greatest_ul = ul
        return greatest_ul
    else:
        raise ValueError("No <ul> in HTML file")


def last_li(html: str, position: dict) -> str:
    extractor = html_parser.LiExtractor()
    extractor.provide_ul(position)
    extractor.feed(html)
    return extractor.last_li


def main():
    url: str = cli.source_url()
    html: str = fetch_resource.html(url)
    try:
        ul_position: dict = greatest_ul(html)
        li: str = last_li(html, ul_position)
        print(li)
    except ValueError as e:
        print(e)
