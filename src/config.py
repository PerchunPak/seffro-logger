import dataclasses
import os
import typing as t


class ImproperConfigurationError(Exception): ...


@dataclasses.dataclass
class Config:
    token: str

    @classmethod
    def parse(cls) -> t.Self:
        if "BOT_TOKEN" not in os.environ:
            raise ImproperConfigurationError("Please provide bot token as `BOT_TOKEN` environment variable")

        return cls(
            token=os.environ["BOT_TOKEN"],
        )
