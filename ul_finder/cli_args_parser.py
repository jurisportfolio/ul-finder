import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", default=None)


def source_url():
    return parser.parse_args().url
