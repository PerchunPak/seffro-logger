import hikari

import src.config

config = src.config.Config.parse()
bot = hikari.GatewayBot(intents=hikari.Intents.MESSAGE_CONTENT | hikari.Intents.GUILD_MESSAGES, token=config.token)
SEFFRO_ID = 379353300887273472  # TODO that's my ID, what's seffro id?


@bot.listen()
async def log_seffro(event: hikari.GuildMessageCreateEvent) -> None:
    if event.author_id != SEFFRO_ID:
        return

    print("Seffro wrote: ", event.content)
    await event.message.respond(
        event.content,
        attachments=event.message.attachments,
    )


if __name__ == "__main__":
    bot.run()
