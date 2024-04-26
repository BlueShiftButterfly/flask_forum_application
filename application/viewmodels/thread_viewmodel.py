from dataclasses import dataclass

@dataclass
class ThreadViewmodel:
    title: str
    content: str
    poster_username: str
    localized_post_date: str
    link: str
