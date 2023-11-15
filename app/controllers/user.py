from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from app.types.user import Query, Mutation

user = APIRouter()
schema = strawberry.Schema(Query, Mutation) 
graphql_app = GraphQL(schema=schema)

user.add_route("/graphql", graphql_app)