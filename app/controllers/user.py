from fastapi import APIRouter
import strawberry
# from strawberry.asgi import GraphQL
from strawberry.fastapi import GraphQLRouter
from app.types.user import Query, Mutation

user = APIRouter()
schema = strawberry.Schema(Query, Mutation) 
graphql_app = GraphQLRouter(schema=schema)

# user.add_route("/graphql", graphql_app)