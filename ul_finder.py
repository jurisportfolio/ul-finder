#! /usr/bin/env python3

import html_parser
from urllib import request
import cli_args_parser


def html_string(url: str) -> str:
    bite_html = request.urlopen(url).read()
    return bite_html.decode("utf8")


url = cli_args_parser.source_url()
# print(type(url))
html = html_string(url)
# print(html)

extractor = html_parser.UlExtractor()

extractor.feed(html)
