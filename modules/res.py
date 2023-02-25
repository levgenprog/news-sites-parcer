class ParcingResource:
    id: int
    res_name: str
    res_url: str
    top_tag: str
    link_tag: str
    header_tag: str
    content_link: str
    content_tag: str
    date_tag: str
    pagination_tag: str

    def __init__(self, **kwargs) -> None:
        for attr in ('id', 'res_name', 'res_url', 'top_tag', 'link_tag',
        'header_tag', 'content_link', 'content_tag', 'date_tag', 'pagination_tag'):
            setattr(self, attr, kwargs.get(attr))
