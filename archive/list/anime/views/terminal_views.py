from models.entry import AnimeEntry

""" 
Abstract these more so they dont neeed the Anime Entry import and so that they are more reusable

Example.

    simple_view(name: str, release_date: str, genres: List[str], notes: str):
        return

def simple_view(anime_entry: AnimeEntry):
    genres = " ".join([f"[{g}]" for g in anime_entry.genres])
    
    view = f'''
{anime_entry.name} | {anime_entry.release_date} | {genres} 
{anime_entry.notes}
'''
    return view


def complex_view(anime_entry: AnimeEntry):
    genres = " > ".join(anime_entry.genres)
    
    view = f'''
[ {anime_entry.name} ] {anime_entry.release_date}
< {genres} > 
{anime_entry.notes}
''' 
    return view
"""

# class BaseView:
#     def  __init__(self, ref_obj: any):
#         self.ref_obj = ref_obj

#     def __str__(self) -> str:
#         raise NotImplementedError


class AnimeView:
    def  __init__(self, anime_entry: AnimeEntry):
        self.ref_obj = anime_entry
    def __str__(self) -> str:
        genres = " ".join([f"[{g}]" for g in self.ref_obj.genres])
        
        view = f"""
{self.ref_obj.name} | {self.ref_obj.release_date} | {genres} 
{self.ref_obj.notes}"""
        return view


class ComplexView(AnimeView):
    def __init__(self, anime_entry: AnimeEntry):
        super().__init__(anime_entry)
    
    def __str__(self) -> str:
        genres = " > ".join(self.ref_obj.genres)
        
        view = f"""
[ {self.ref_obj.name} ] {self.ref_obj.release_date}
< {genres} > 
{self.ref_obj.notes}
""" 
        return view


