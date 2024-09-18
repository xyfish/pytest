from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import redis

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# 連接 Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int):
    return templates.TemplateResponse("item.html", {"request": request, "item_id": item_id})

# 列出所有 Redis 鍵值
@app.get("/redis-keys", response_class=HTMLResponse)
async def get_redis_keys(request: Request):
    keys = redis_client.keys('*')
    key_values = {key: redis_client.get(key) for key in keys}
    return templates.TemplateResponse("redis_keys.html", {"request": request, "key_values": key_values})

# 讀取指定的 Redis 鍵值
@app.get("/redis-keys/{key}", response_class=JSONResponse)
async def read_redis_key(key: str):
    value = redis_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

# 創建或更新 Redis 鍵值
@app.post("/redis-keys/")
async def create_or_update_redis_key(key: str = Form(...), value: str = Form(...)):
    redis_client.set(key, value)
    return {"message": f"Key '{key}' set to value '{value}'"}

# 刪除指定的 Redis 鍵
@app.delete("/redis-keys/{key}")
async def delete_redis_key(key: str):
    result = redis_client.delete(key)
    if result == 0:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": f"Key '{key}' deleted"}