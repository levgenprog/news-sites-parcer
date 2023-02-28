class ParcingResource:
    res_id: int
    res_name: str
    res_url: str
    top_tag: str
    link_tag: str
    header_tag: str
    content_tag: str
    date_tag: str
    pagination_tag: str

    pag_from: int
    pag_to: int
    render: int
    content_here: int


    def __init__(self, id, name, url, top_tag, link_tag, header_tag, content_tag, date_tag, pagination_tag,
                 pag_from, pag_to, render, content_here) -> None:
        self.res_id = id
        self.res_name = name
        self.res_url = url
        self.top_tag = top_tag
        self.link_tag = link_tag
        self.header_tag = header_tag
        self.content_tag = content_tag
        self.date_tag = date_tag
        self.pagination_tag = pagination_tag

        self.pag_from = pag_from
        self.pag_to = pag_to
        self.render = render
        self.content_here = content_here

