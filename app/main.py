from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.controllers.index import user
from app.controllers.user import graphql_app

app = FastAPI(title="FastAPI GraphQl", debug=True)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_credentials = True, 
    allow_headers = ["*"]
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

@app.get("/", tags = ["Server Health Check"])
def server_health_check():
    return {"Message": "Server working fine"}

app.include_router(user)
app.include_router(graphql_app, prefix="/graphql")