from system.module.db import DB
from system.module.elasticsearch import ES


class Context:
    def __init__(self):
        self.db = DB()
        self.es = ES()
