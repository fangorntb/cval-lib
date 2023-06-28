from src.patterns.singleton import Singleton


class MainConfig(metaclass=Singleton):
    main_url = 'https://cval.ai/api'
