# region Imports

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, func, Boolean, DateTime

from base_engine import Base

router = APIRouter()

# endregion

'''
Aşağıdaki tabloları önceden oluşturduğumuz veri tabanında oluşturmuş olmamız gerekiyor.
'''


class ArticleInfo(BaseModel):
    title: str
    content: str
    read_time: int = None ### Gönderilmesi opsiyonel bir alan olduğu be boş değer kabul edebilmek için = None eklenmeli
    is_active: bool = True


class mArticles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    # Başlık alanı String değerde ve doldurulması zorunlu bir alan olarak oluşturuyoruz.
    content = Column(Text)
    # İçerik alanı Text değerde  ve doldurulması zorunlu bir alan olarak oluşturuyoruz.
    read_time = Column(Integer, nullable=True)
    # Okuma zamanı alanı Integer değerde ve boş geçilebilecek bir alan.
    is_active = Column(Boolean)
    # Aktif-pasif alanı Boolean değerde yalnızca içi geçerli değeri var (True/False) ve doldurulması zorunlu bir alan olarak oluşturuyoruz.
    create_time = Column(DateTime, server_default=func.now())
    # Oluşturulma zamanı alanı Datetime değerde kayıt girerken gönderilmezse server zamanına göre otomatik olarak eklenecek.
