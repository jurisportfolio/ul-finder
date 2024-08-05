#! /usr/bin/env python3

import html_parser
from urllib import request
import cli_args_parser


def html_string(url: str) -> str:
    bite_html = request.urlopen(url).read()
    return bite_html.decode("utf8")


def restored_li(raw_li: dict) -> str:
    li = ""
    for item in raw_li:
        if 'start' in item:
            li += f"<{item['start']}"
            if 'attrs' in item:
                for attr in item['attrs']:
                    li += f" {attr[0]}=\"{attr[1]}\""
            li += ">"
        if 'data' in item:
            li += f"{item['data']}"
        if 'end' in item:
            li += f"</{item['end']}>"
    return li



url = cli_args_parser.source_url()
# print(type(url))
html = html_string(url)
# print(html)

extractor = html_parser.UlExtractor()

extractor.feed(html)

greatest_ul = extractor.greatest_ul()

print(greatest_ul)

print(restored_li(greatest_ul["last_li"]))



