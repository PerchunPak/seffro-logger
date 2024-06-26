import hikari

import src.config

config = src.config.Config.parse()
bot = hikari.GatewayBot(intents=hikari.Intents.MESSAGE_CONTENT | hikari.Intents.GUILD_MESSAGES, token=config.token)


@bot.listen()
async def log_seffro(event: hikari.GuildMessageCreateEvent) -> None:
    if event.author_id not in config.seffro_ids:
        return

    print("Seffro wrote:", event.content)
    await event.message.respond(
        event.content,
        attachments=event.message.attachments,
        reply=event.message.referenced_message,
    )

    try:
        await event.message.delete()
    except hikari.errors.NotFoundError:
        print("Siffro was first one who deleted the message!")
    except hikari.errors.ForbiddenError:
        await event.message.respond("(no permission to delete Seffro's message)")


if __name__ == "__main__":
    bot.run()
