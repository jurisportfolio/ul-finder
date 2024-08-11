from ul_finder_src import cli, html_parser, fetch_resource


def greatest_ul(html) -> dict:
    extractor = html_parser.UlExtractor()
    extractor.feed(html)
    uls = extractor.all_uls()
    if uls:
        greatest_ul = uls[0]
        for ul in uls:
            if ul["has_li"] > greatest_ul["has_li"]:
                greatest_ul = ul
        return greatest_ul


# def report(storage):
#     greatest_ul = storage.greatest_ul()
#     last_li = html_parser.restored_li(greatest_ul["last_li"])
#     print(last_li)


def main():
    url = cli.source_url()
    html = fetch_resource.html(url)
    ul_position = greatest_ul(html)

    print(ul)
