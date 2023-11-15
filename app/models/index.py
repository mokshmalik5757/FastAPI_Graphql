from app.models.user import users
from app.connection.db import engine, meta

meta.create_all(engine)