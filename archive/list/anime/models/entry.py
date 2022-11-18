from typing import List, Dict
from dataclasses import dataclass, field


@dataclass
class AnimeEntry:
    name: str
    release_date: str = "No Release Date"
    genres: List[str] = field(default_factory=lambda: ["No Genre"])
    notes: str = "No Notes"

    def __str__(self) -> str:
        genres = " | ".join(self.genres)
        
        txt = f"\n{self.name}\n[{self.release_date}]\n| {genres} |\n{self.notes}\n"
        return txt

    def export(self):
        return {
            "name": self.name,
            "release_date": self.release_date,
            "genres": self.genres,
            "notes": self.notes
        }

