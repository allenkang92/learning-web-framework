# 서버 만들기
from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def hello():
#     return 'hello'

@app.get("/data")
def hello():
    return {'hello' : 1234}

from fastapi.responses import FileResponse

# html 파일 전송
@app.get("/")
def hello():
    return FileResponse('index.html')


from pydantic import BaseModel
class Model(BaseModel):
    name : str
    phone : int

@app.post("/send")
def hello(data : Model):
    print(data)
    return '전송완료'

