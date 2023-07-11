import telebot
from loguru import logger


async def start(bot, message):
    _url = "https://github.com/KimmyXYC/Command_Lock_Bot.git"
    _info = "Command Lock Bot\n" \
            "/lock_cmd  锁定命令\n" \
            "/unlock_cmd 解锁命令\n" \
            "/list_locked_cmd 查看已锁定命令\n"
    await bot.reply_to(
        message,
        f"{_info}开源地址: {_url}",
        disable_web_page_preview=True,
    )


async def lock_command(bot, message, cmd, db):
    lock_cmd_list = db.get(str(message.chat.id))
    if lock_cmd_list is None:
        lock_cmd_list = []
    if cmd in lock_cmd_list:
        await bot.reply_to(message, "该命令已被锁定")
    else:
        lock_cmd_list.append(cmd)
        db.set(str(message.chat.id), lock_cmd_list)
        logger.info(f"Lock Command: {cmd} in {message.chat.id}")
        await bot.reply_to(message, f"已锁定命令`{cmd}`", parse_mode='Markdown')


async def unlock_command(bot, message, cmd, db):
    lock_cmd_list = db.get(str(message.chat.id))
    if lock_cmd_list is None:
        lock_cmd_list = []
    if cmd in lock_cmd_list:
        lock_cmd_list.remove(cmd)
        db.set(str(message.chat.id), lock_cmd_list)
        logger.info(f"Unlock Command: {cmd} in {message.chat.id}")
        await bot.reply_to(message, f"已解锁命令`{cmd}`", parse_mode='Markdown')
    else:
        await bot.reply_to(message, "该命令未被锁定")


async def list_locked_command(bot, message, db):
    lock_cmd_list = db.get(str(message.chat.id))
    if lock_cmd_list is None:
        msg = "本群未锁定任何命令"
    else:
        msg = "以下命令在本群中被锁定:\n"
        msg += "\n".join(f"- `{item}`" for item in lock_cmd_list)
    await bot.reply_to(message, msg, parse_mode='Markdown')
