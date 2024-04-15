from dataclasses import dataclass

@dataclass
class Forum:
    db_id: int
    uuid: str
    url_name: str
    display_name: str
    creation_timestamp: str

    @property
    def url(self):
        return "/forum/"+self.url_name
