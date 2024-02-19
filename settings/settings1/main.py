from settings import load_config, DBConfig, WebAPIConfig


def init_db_service(config: DBConfig) -> None:
    print(config)


def init_web_api_service(config: WebAPIConfig) -> None:
    print(config)


def main():
    config = load_config(env_file=".env.example")

    init_db_service(config=config.db)
    init_web_api_service(config=config.web_api)


if __name__ == '__main__':
    main()
