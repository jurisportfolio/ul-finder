from html.parser import HTMLParser
from ul_finder_src import data_containers


class UlExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = data_containers.Stack()
        self.storage = []
        self.ul_counter = 0
        self.li_counter = 0

    def upraise_ul_counter(self):
        self.ul_counter += 1

    def upraise_li_counter(self):
        self.li_counter += 1

    def reset_li_counter(self):
        self.li_counter = 0

    def handle_starttag(self, tag, _attrs):
        if tag == "ul":
            self.upraise_ul_counter()
            self.reset_li_counter()
            self.stack.push({"ul": self.ul_counter, "has_li": 0})
        elif tag == "li":
            self.upraise_li_counter()
            last_ul = self.stack.last()
            last_ul["has_li"] = self.li_counter

    def handle_endtag(self, tag):
        if tag == "ul":
            last_ul = self.stack.pop()
            self.storage.append(last_ul)

    def __all_uls__(self):
        return self.storage

    def greatest_ul(self) -> dict:
        greatest_ul = self.storage[0]
        for ul in self.storage:
            if ul["has_li"] > greatest_ul["has_li"]:
                greatest_ul = ul
        return greatest_ul


# class LiExtractor(HTMLParser):
#
#     def __init__(self):
#         super().__init__()
#         self.ul_counter = 0
#         self.li_counter = 0
#
#     def upraise_ul_counter(self):
#         self.ul_counter += 1
#
#     def upraise_li_counter(self):
#         self.li_counter += 1
#
#     def handle_starttag(self, tag, attrs):
#
#     def handle_data(self, data):
#         # if not data.startswith("\n"):
#         last_ul_ref = self.stack.last()
#         if last_ul_ref:
#             if "last_li" in last_ul_ref:
#                 last_ul_ref["last_li"].append({"data": data})
#
#     def handle_startendtag(self, tag, attrs):
#         last_ul_ref = self.stack.last()
#         if last_ul_ref:
#             if "last_li" in last_ul_ref:
#                 last_ul_ref["last_li"].append({"self": tag, "attrs": attrs})
#
#

#
#
# def restored_li(raw_li: dict) -> str:
#     li = ""
#     for item in raw_li:
#         if 'start' in item:
#             li += f"<{item['start']}"
#             if 'attrs' in item:
#                 for attr in item['attrs']:
#                     li += f" {attr[0]}=\"{attr[1]}\""
#             li += ">"
#         if 'self' in item:
#             li += f"<{item['self']}"
#             if 'attrs' in item:
#                 for attr in item['attrs']:
#                     li += f" {attr[0]}=\"{attr[1]}\""
#             li += " />"
#         if 'data' in item:
#             li += f"{item['data']}"
#         if 'end' in item:
#             li += f"</{item['end']}>"
#     return li
