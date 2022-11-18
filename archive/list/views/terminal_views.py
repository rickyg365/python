from models.entry import Entry

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


class View:
    def  __init__(self, entry: Entry):
        self.ref_obj = entry

    def __str__(self) -> str:
        data = " ".join([f"[{d}]" for d in self.ref_obj.data])
        
        view = f"""
{self.ref_obj.name} | {self.ref_obj.size} | {data}
"""
        return view


class ComplexView(View):
    def __init__(self, entry: Entry):
        super().__init__(entry)
    
    def __str__(self) -> str:
        data = " > ".join(self.ref_obj.data)
        
        view = f"""
[ {self.ref_obj.name} ] {self.ref_obj.size}
< {data} > 
""" 
        return view


