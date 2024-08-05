#! /usr/bin/env python3

import html_parser
import cli_args_parser

html_url = cli_args_parser.source_url()

html = html_parser.html_string(html_url)

extractor = html_parser.UlExtractor()

extractor.feed(html)

greatest_ul = extractor.greatest_ul()

last_li = html_parser.restored_li(greatest_ul["last_li"])

print(greatest_ul)

print(last_li)
