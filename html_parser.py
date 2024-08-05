from html.parser import HTMLParser



class UlExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.storage = []
        self.ID_COUNTER = 0


    def handle_starttag(self, tag, attrs):
        self.ID_COUNTER += 1
        print(f'{self.ID_COUNTER} {tag} {attrs}')
        if tag == 'ul':
            self.add_to_stack({"count": 0})
        elif tag == 'li':
            last_ul_ref = self.last_on_stack()
            last_ul_ref["count"] += 1
            last_ul_ref["last_li"] = []
        else:
            last_ul_ref = self.last_on_stack()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"start": tag})
                    last_ul_ref["last_li"].append({"attrs": attrs})

    def handle_endtag(self, tag):
        if tag == "ul":
            last_ul_ref = self.del_from_stack()
            self.add_to_storage(last_ul_ref)
        elif tag != "li":
            last_ul_ref = self.last_on_stack()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"end": tag})
                    print(f'stack: {self.stack}')

    def handle_data(self, data):
        if not data.startswith("\n"):
            last_ul_ref = self.last_on_stack()
            if last_ul_ref:
                if "last_li" in last_ul_ref:
                    last_ul_ref["last_li"].append({"data": data})

    def add_to_stack(self, tag: dict):
        self.stack.append(tag)

    def last_on_stack(self):
        print(f'stack: {self.stack}')

        if self.stack:
            print(f'last on stack: {self.stack[-1]}')
            return self.stack[-1]

    def del_from_stack(self):
        return self.stack.pop(-1)

    def add_to_storage(self, last_ul_ref):
        self.storage.append(last_ul_ref)
        print(f'storage: {self.storage}')
