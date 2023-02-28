
class Items:
    res: int
    link: str
    title: str
    content: str
    nd_date: str
    s_date: int
    not_date: str

    def __init__(self, res, link, title, content, nd_date, s_date, not_date) -> None:
        self.res = res
        self.link = link
        self.title = title
        self.content = content
        self.nd_date = nd_date
        self.s_date = s_date
        self.not_date = not_date

