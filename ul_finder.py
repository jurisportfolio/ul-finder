from ul_finder import cli, html_parser, fetch_resource


def greatest_ul(html):
    extractor = html_parser.UlExtractor()
    extractor.feed(html)
    return extractor.greatest_ul()


# def report(storage):
#     greatest_ul = storage.greatest_ul()
#     last_li = html_parser.restored_li(greatest_ul["last_li"])
#     print(last_li)


def main():
    url = cli.source_url()
    html = fetch_resource.html(url)
    ul = greatest_ul(html)

    print(ul)
