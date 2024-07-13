"""Config file for running the code."""

import typing as T

import pydantic


class DataConfig(pydantic.BaseModel):
    """Data-related config."""

    first_month: str = "2021.01"


class ModelConfig(pydantic.BaseModel):
    """Model-related config."""

    some_bool: bool = True
    search_space: T.Dict[str, int] = {"max_depth": 8}


class RunConfig(pydantic.BaseModel):
    """Model-related config."""

    data: DataConfig = pydantic.Field(default_factory=DataConfig)
    model: ModelConfig = pydantic.Field(default_factory=ModelConfig)


if __name__ == "__main__":
    config = RunConfig()
