import hikari

import src.config

config = src.config.Config.parse()
bot = hikari.GatewayBot(intents=hikari.Intents.ALL, token=config.token)
SEFFRO_ID = 379353300887273472  # TODO that's my ID, what's seffro id?


@bot.listen()
async def log_seffro(event: hikari.GuildMessageCreateEvent) -> None:
    if event.author_id != SEFFRO_ID:
        return

    await event.message.respond(event.content)


if __name__ == "__main__":
    bot.run()
