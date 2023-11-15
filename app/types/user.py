import strawberry
from app.models.index import users
from app.connection.db import conn

@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str
    
@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, id: int) -> User:
        
        return conn.execute(users.select().where(users.c.id == id)).fetchone() # type: ignore
     
    @strawberry.field
    def users(self, info) -> list[User]:
        return conn.execute(users.select()).fetchall() # type: ignore

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name:str, email:str, password:str) -> int:
        result = conn.execute(users.insert().values(name=name, email=email, password=password))
        return int(result.inserted_primary_key[0]) # type: ignore 
    
    @strawberry.mutation
    def update_user(self, info, id: int, name:str, email:str, password:str) -> str:
        result = conn.execute(users.update().where(users.c.id == id).values(name=name, email=email, password=password))
        return str(result.rowcount) + ' rows affected'
    
    @strawberry.mutation
    def delete_user(self, info, id:int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0
    