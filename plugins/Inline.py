import os
import asyncio
from pyrogram import Client
from plugins.translation import Translation
from functions.Xtra  import get_info
from pyrogram.errors import FloodWait
from functions.ytserch import youtube_search
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent




@Client.on_inline_query()
async def inline_search(bot, query: InlineQuery):
    me = []
    try:
        me = await Client.get_me(bot)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    id = query.from_user.id
    results = []
    #
    defaults = await get_info(me.username)
    results.extend(defaults)
    #
    
    #
    search = query.query.strip()
    string = await youtube_search(search)
    for data in string:
        count = data['viewCount']
        thumb = data['thumbnails']
        results.append(
            InlineQueryResultArticle(
                title=data['title'][:35] + "..",
                input_message_content=InputTextMessageContent(
                    message_text=data['link']
                ),
                thumb_url=thumb[0]['url'],
                description=Translation.DESCRIPTION.format(data['duration'], count['text'])
            )
        )
    if string:
        switch_pm_text = Translation.RESULTS_TXT
        try:
            await query.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
    else:
        switch_pm_text = Translation.NO_RESULTS
        try:
            await query.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
