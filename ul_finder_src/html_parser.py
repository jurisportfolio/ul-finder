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

    def restore_li_counter(self):
        if self.stack.is_empty():
            self.li_counter = 0
        else:
            self.li_counter = self.stack.last()["has_li"]

    def handle_starttag(self, tag, _attrs):
        if tag == "ul":
            self.upraise_ul_counter()
            self.reset_li_counter()
            self.stack.push({"ul": self.ul_counter, "has_li": self.li_counter})

        elif tag == "li":
            self.upraise_li_counter()
            current_ul = self.stack.last()
            current_ul["has_li"] = self.li_counter

    def handle_endtag(self, tag):
        if tag == "ul":
            current_ul = self.stack.pop()
            self.storage.append(current_ul)
            self.restore_li_counter()

    def all_uls(self):
        return self.storage


class LiExtractor(HTMLParser):

    def __init__(self):
        super().__init__()
        self.__position = {}
        self.__ul_counter = 0
        self.__li_counter = 0
        self.__last_li_is_open = False
        self.last_li = ""
        self.inner_lis = 0

    def provide_ul(self, position: dict):
        self.__position = position

    def handle_starttag(self, tag, attrs):
        if self.__last_li_founded():
            if self.__last_li_is_open:
                self.__add_to_last_li(tag, attrs, None, "starttag")
            if tag == "li" and self.__last_li_is_open:
                self.inner_lis += 1
        else:
            if tag == "ul":
                self.__upraise_ul_counter()
            if tag == "li" and self.__ul_founded():
                self.__upraise_li_counter()
                if self.__last_li_founded():
                    self.inner_lis += 1
                    self.__last_li_is_open = True
                    self.last_li += "<li>"

    def handle_endtag(self, tag):
        if self.__last_li_founded():
            if self.__last_li_is_open:
                self.__add_to_last_li(tag, None, None, "endtag")
            if tag == "li" and self.__last_li_is_open:
                self.inner_lis -= 1
                if self.inner_lis == 0:
                    self.__last_li_is_open = False

    def handle_data(self, data):
        if self.__last_li_founded():
            if self.__last_li_is_open:
                self.__add_to_last_li(None, None, data, "data")

    def handle_startendtag(self, tag, attrs):
        if self.__last_li_founded():
            if self.__last_li_is_open:
                self.__add_to_last_li(tag, attrs, None, "startendtag")

    def __upraise_ul_counter(self):
        self.__ul_counter += 1

    def __upraise_li_counter(self):
        self.__li_counter += 1

    def __ul_founded(self):
        return True if self.__ul_counter == self.__position["ul"] else False

    def __last_li_founded(self):
        if self.__ul_founded() and self.__li_counter == self.__position["has_li"]:
            return True
        else:
            return False

    def __add_to_last_li(self, tag, attrs, data, kind):
        if kind == "starttag":
            self.last_li += f"<{tag}"
            if attrs:
                for attr in attrs:
                    self.last_li += f" {attr[0]}=\"{attr[1]}\""
            self.last_li += ">"
        if kind == "endtag":
            self.last_li += f"</{tag}>"
        if kind == "data":
            self.last_li += f"{data}"
        if kind == "startendtag":
            self.last_li += f"<{tag}"
            if attrs:
                for attr in attrs:
                    self.last_li += f" {attr[0]}=\"{attr[1]}\""
            self.last_li += "/>"
