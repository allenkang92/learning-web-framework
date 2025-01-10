# FastAPI 및 필요한 모듈들 임포트
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# 간단한 데이터베이스 역할을 하는 리스트
db = []

# 모델 정의: City
class City(BaseModel):
    name : str
    timezone : str

# 루트 엔드포인트 정의
@app.get("/")
def root():
    return {"hello" : "fastapi"}

# 모든 도시 정보를 반환하는 엔드포인트 정의
@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        # 외부 API를 호출하여 현재 시간 정보를 가져옴
        strs = f"http://worldtimeapi.org/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        # 결과 리스트에 도시 정보 추가
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time})

    return results

# 특정 도시 정보를 반환하는 엔드포인트 정의
@app.get("/cities/{city_id}")
def get_city(city_id : int):
    city = db[city_id-1]
    # 외부 API를 호출하여 현재 시간 정보를 가져옴
    strs = f"http://worldtimeapi.org/timezone/{city['timezone']}"
    r = requests.get(strs)
    
    cur_time = r.json()['datetime']
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time}

# 도시를 추가하는 엔드포인트 정의
@app.post("/cities")
def create_city(city : City):
    print(city)    
    db.append(city.dict())

    # 최근 추가된 데이터 반환
    return db[-1]

# 도시를 삭제하는 엔드포인트 정의
@app.delete("/cities/{city_id}")
def delete_city(city_id : int):
    db.pop(city_id-1)
    
    return {}

# @app.put

# @app.patch