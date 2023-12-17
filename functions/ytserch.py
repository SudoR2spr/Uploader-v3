import os
import wget
from youtubesearchpython import *
from urllib.parse import quote
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.translation import Translation

async def youtube_search(query):
    sear = VideosSearch(query)
    result = sear.result()['result']
    return result

async def yt_link_search(url):
    videoInfo = Video.getInfo(url, mode=ResultMode.dict)
    return videoInfo

async def yt_thumb_dl(thumb_url, m):
    yt_thumb_image_path = os.getcwd() + "/" + "YThumb" + "/" + str(m.from_user.id) + ".jpg"
    yt_thumb_dir = os.getcwd() + "/" + "YThumb" + "/"
    if not os.path.isdir(yt_thumb_dir):
        os.makedirs(yt_thumb_dir)
    else:
        try:
            for f in os.listdir(yt_thumb_dir):
                os.remove(os.path.join(yt_thumb_dir, f))
        except Exception:
            pass
    thumb = wget.download(thumb_url, yt_thumb_image_path, bar=None)
    return thumb
    
def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Translation.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot🔁', url=url),
                InlineKeyboardButton("Search Inline🔄", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share
