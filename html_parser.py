import operator
from html.parser import HTMLParser
from urllib import request
import data_containers


class UlExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = data_containers.Stack()
        self.storage = data_containers.Storage()
        self.ID_COUNTER = 0

    def handle_starttag(self, tag, attrs):
        self.ID_COUNTER += 1
        print(f'{self.ID_COUNTER} {tag} {attrs}')
        if tag == 'ul':
            self.stack.push({"count": 0})
        elif tag == 'li':
            last_ul_ref = self.stack.last()
            last_ul_ref["count"] += 1
            last_ul_ref["last_li"] = [{"start": tag, "attrs": attrs}]
        else:
            last_ul_ref = self.stack.last()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"start": tag, "attrs": attrs})

    def handle_endtag(self, tag):
        if tag == "ul":
            last_ul_ref = self.stack.pop()
            self.storage.push(last_ul_ref)
        elif tag == "li":
            last_ul_ref = self.stack.last()
            last_ul_ref["last_li"].append({"end": tag})
            print(f'stack: {self.stack}')
        else:
            last_ul_ref = self.stack.last()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"end": tag})
                    print(f'stack: {self.stack}')

    def handle_data(self, data):
        if not data.startswith("\n"):
            last_ul_ref = self.stack.last()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"data": data})


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
