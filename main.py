#!/usr/bin/python3.8

import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("start_message")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("help_message")


def charswap(s):
    s = s.lower()
    s = s.replace('а', 'a')
    s = s.replace('б', '6')
    s = s.replace('в', 'B')
    s = s.replace('г', '7')
    s = s.replace('д', 'g')
    s = s.replace('е', 'e')
    s = s.replace('ж', ')I(')
    s = s.replace('з', '3')
    s = s.replace('и', 'u')
    s = s.replace('й', 'ū')
    s = s.replace('к', 'k')
    s = s.replace('л', 'JI')
    s = s.replace('м', 'M')
    s = s.replace('н', 'H')
    s = s.replace('о', '0')
    s = s.replace('п', 'n')
    s = s.replace('р', 'p')
    s = s.replace('с', 'c')
    s = s.replace('т', 'm')
    s = s.replace('у', 'y')
    s = s.replace('ф', 'cp')
    s = s.replace('х', 'x')
    s = s.replace('ч', '4')
    s = s.replace('ш', 'w')
    s = s.replace('щ', 'w')
    s = s.replace('ы', 'bl')
    s = s.replace('ь', 'b')
    s = s.replace('ю', 'l-0')
    s = s.replace('я', '9')
    return s


def langswap(a):
    a = a.replace("f", "а")
    a = a.replace(",", "б")
    a = a.replace("d", "в")
    a = a.replace("u", "г")
    a = a.replace("l", "д")
    a = a.replace("t", "е")
    a = a.replace("`", "ё")
    a = a.replace(";", "ж")
    a = a.replace("p", "з")
    a = a.replace("b", "и")
    a = a.replace("q", "й")
    a = a.replace("r", "к")
    a = a.replace("k", "л")
    a = a.replace("v", "м")
    a = a.replace("y", "н")
    a = a.replace("j", "о")
    a = a.replace("g", "п")
    a = a.replace("h", "р")
    a = a.replace("c", "с")
    a = a.replace("n", "т")
    a = a.replace("e", "у")
    a = a.replace("a", "ф")
    a = a.replace("[", "х")
    a = a.replace("w", "ц")
    a = a.replace("x", "ч")
    a = a.replace("i", "ш")
    a = a.replace("o", "щ")
    a = a.replace("]", "ъ")
    a = a.replace("s", "ы")
    a = a.replace("m", "ь")
    a = a.replace("'", "э")
    a = a.replace(".", "ю")
    a = a.replace("z", "я")
    a = a.replace("F", "А")
    a = a.replace("<", "Б")
    a = a.replace("D", "В")
    a = a.replace("U", "Г")
    a = a.replace("L", "Д")
    a = a.replace("T", "Е")
    a = a.replace("~", "Ё")
    a = a.replace(":", "Ж")
    a = a.replace("P", "З")
    a = a.replace("B", "И")
    a = a.replace("Q", "Й")
    a = a.replace("R", "К")
    a = a.replace("K", "Л")
    a = a.replace("V", "М")
    a = a.replace("Y", "Н")
    a = a.replace("J", "О")
    a = a.replace("G", "П")
    a = a.replace("H", "Р")
    a = a.replace("C", "С")
    a = a.replace("N", "Т")
    a = a.replace("E", "У")
    a = a.replace("A", "Ф")
    a = a.replace("{", "Х")
    a = a.replace("W", "Ц")
    a = a.replace("X", "Ч")
    a = a.replace("I", "Ш")
    a = a.replace("O", "Щ")
    a = a.replace("}", "Ъ")
    a = a.replace("S", "Ы")
    a = a.replace("M", "Ь")
    a = a.replace('''"''', "Э")
    a = a.replace(">", "Ю")
    a = a.replace("Z", "Я")
    a = a.replace("?", ",")
    a = a.replace("&", "?")
    return a


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=charswap(query),
            input_message_content=InputTextMessageContent(charswap(query)),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=langswap(query),
            input_message_content=InputTextMessageContent(langswap(query)),
        ),
    ]

    await update.inline_query.answer(results)


def main() -> None:
    application = Application.builder().token("BOT_TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
