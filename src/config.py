import dataclasses
import os
import typing as t


class ImproperConfigurationError(Exception): ...


@dataclasses.dataclass
class Config:
    token: str
    seffro_ids: list[int]

    @classmethod
    def parse(cls) -> t.Self:
        if "BOT_TOKEN" not in os.environ:
            raise ImproperConfigurationError("Please provide bot token as `BOT_TOKEN` environment variable")
        if "SEFFRO_IDS" not in os.environ:
            raise ImproperConfigurationError("Please provide IDs separated by `,` to log in `SEFFRO_IDS`")

        seffro_ids = list(map(int, os.environ["SEFFRO_IDS"].split(",")))
        return cls(
            token=os.environ["BOT_TOKEN"],
            seffro_ids=seffro_ids,
        )
