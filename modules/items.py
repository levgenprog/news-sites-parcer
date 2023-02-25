from .res import ParcingResource 


class Items:
    id: int
    res: ParcingResource
    link: str
    title: str
    content: str
    nd_date: int
    s_date: int
    not_date: str

    def __init__(self, **kwargs) -> None:
        for attr in ('id', 'res', 'link', 'title', 'content', 'nd_date',
        's_date', 'not_date'):
            setattr(self, attr, kwargs.get(attr))
