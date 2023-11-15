from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:password@127.0.0.1/fastapi_graphql", connect_args=dict(host='localhost', port=3307))
meta = MetaData()
conn = engine.connect()