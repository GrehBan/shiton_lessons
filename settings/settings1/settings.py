from dataclasses import dataclass
from environs import Env


@dataclass
class WebAPIConfig:
    token: str


@dataclass
class DBConfig:
    host: str
    port: int
    username: str
    password: str
    database: str


@dataclass
class Config:
    web_api: WebAPIConfig
    db: DBConfig


def load_config(env_file: str = ".env") -> Config:
    env = Env()
    env.read_env(env_file)

    return Config(
        web_api=WebAPIConfig(
            token=env.str("WEB_API_TOKEN")
        ),
        db=DBConfig(
            host=env.str("DB_HOST"),
            port=env.int("DB_PORT"),
            username=env.str("DB_USER"),
            password=env.str("DB_PASSWORD"),
            database=env.str("DB_DATABASE")
        )
    )
