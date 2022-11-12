import os
import anipy_cli as anime

"""ENTRY"""
# A class that saves metadata, it is
# needed for almost every function.
#    class entry:
#        show_name: str = "" # name of show
#        category_url: str = "" # category url of show
#        ep_url: str = "" # ep url with episode corresponding to ep
#        embed_url: str = "" # embed url of ep_url
#        stream_url: str = "" # m3u8/mp4 link of embed_url
#        ep: int = 0 # episode currently played/downloaded or whatever
#        latest_ep: int = 0 # latest episode of the show
#        quality: str = "" # current quality
entry = anime.entry()


"""QUERY"""
# Get results from a query, query(search_param, entry)
query_class = anime.query("naruto", entry)

# query.get_links() -> (self.links: Links[], self.names: Names[])
links, names = query_class.get_links()
# The links are not complete (/category/naruto), needs gogoanime url
print(links)

print(names)


"""EPISODE HANDLING"""

# Episode Handling with epHandler, 
# - it can get the latest episode, 
# - generate episode links,
# - get next episode and previos episode.
# it requires the fields category_url and ep.
ep_class = anime.epHandler(entry)
# get latest episode
latest_ep = ep_class.get_latest()
# generate ep link, returns a entry
entry = ep_class.gen_eplink()
# get next episode, returns a entry
next_ep = ep_class.next_ep()
# get prev episode, returns a entry
prev_ep = ep_class.prev_ep()
# get your entry back
entry = ep_class.get_entry()


"""VIDEO-URL"""
# Extracting the video and emebed url w/ videourl class, 
# it takes an entry that has to at least have ep_url filled.
# It also takes a quality argument which can have
# the standart qualitys (1080, 720 etc.) or worst/best as value.
url_class = anime.videourl(entry, "best")
# generate stream url (this also, automaticlly generates the embed url)
url_class.stream_url()
# get your entry back filled with stream and embed url fields
entry = url_class.get_entry()


"""DOWNLOAD"""
# Download a m3u8/mp4 link:
# this class requires all
# fields of entry to be filled.
dl_class = anime.download(entry, ffmpeg=True)
# downloads a m3u8 or a mp4 link
dl_class.download()


"""HISTORY"""
# Read the save data from the history.json file
# history class: history.history(entry)
# history_class = anime.history(entry)
# save_data = history_class.read_save_data()
# Writing to history file:
# Following entry fields are required
# for writing to history file:
#        - show_name
#        - category_url
#        - ep_url
#        - ep
# history_class.write_hist()


"""ANIME-INFO"""
# Get some metadata about an anime,
anime.get_anime_info("https://gogoanime.gg/category/hyouka")
'''
get_anime_info(category_url) -> {
    image-url,
    anime type, 
    synopsis,
    list w/ genres, 
    release year, 
    status of the anime
}
'''




def main():
    return

if __name__ == '__main__':
    main()
 