import os
import sys
import time

from plugins.translation import Translation
from functions.ytserch import get_reply_markup
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

StartTime = time.time()

async def get_info(username):
    result = []
    set1 = InlineQueryResultArticle(
        title=Translation.DEFAULT_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Translation.DEFAULT_LINK
        ),
        thumb_url=Translation.DEFAULT_THUMB_URL,
        description=Translation.DEFAULT_DESCRIPTION,
        reply_markup=get_reply_markup(username)
    )
    set2 = InlineQueryResultArticle(
        title=Translation.DEV_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Translation.DEV_LINK
        ),
        thumb_url=Translation.DEV_THUMB_URL,
        description=Translation.DEV_DESCRIPTION,
        reply_markup=get_reply_markup(username)
    )
    result.extend([set1, set2])
    return result
