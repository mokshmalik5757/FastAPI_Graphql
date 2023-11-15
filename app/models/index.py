from connection.db import engine, meta

meta.create_all(engine)