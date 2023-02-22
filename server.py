from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel

app = FastAPI(title="Title")


class ArticleInfo(BaseModel):
    title: str
    content: str
    read_time: int = None  ### Gönderilmesi opsiyonel bir alan olduğu be boş değer kabul edebilmek için = None eklenmeli
    is_active: bool = True


class ArticlePut(BaseModel):
    title: str = "default title"
    content: str = "default content"
    read_time: int = 3
    is_active: bool = True


@app.get("/", include_in_schema=False)
async def homepage():
    return get_swagger_ui_html(openapi_url=app.openapi_url, title="Article Project")


@app.get("/get", summary="Get Article", description="Get record by id")
def article_get(article_id: int):
    # print(article_id)
    return {'article_id': article_id}


@app.get("/list", summary="List Article", description="Get all record")
def article_list():
    articles = [{'id': 1, 'isim': 'muslu'}, {'id': 2, 'isim': 'dodo'}]
    return articles


@app.delete("/delete", summary="Delete Article", description="Delete record")
def article_delete(article_id: int):
    return {'deleted': article_id, "status": True, "mesaj": 'Silindi'}


@app.post("/post", summary="Post Article", description="Create record")
def article_post(article_info_scheme: ArticleInfo):
    return {'status': 'created', 'read_time': article_info_scheme.read_time, 'title': article_info_scheme.title}


@app.put("/put", summary="Put Article", description="Update record")
def article_put(article_id: int, article_put_scheme: ArticlePut):
    return {'status': 'updated', 'article_id': article_id, 'content': article_put_scheme.content}


