# region Imports

from fastapi import APIRouter

from base_engine import SessionLocal
from models import ArticleInfo, mArticles

router = APIRouter()


# endregion

# region Article

## Create işlemleri için post methodu kullanılır.
@router.post("/create/article", summary="Create Article")
def create_article(article_info: ArticleInfo):
    ## Veri tabanında işlem için oturum açan komut. Tüm işlemler bittikten sonra return den önce db.close() ile oturum düşürülebilir.
    db = SessionLocal()

    # Yeni kayıt oluşturmadan önce girilen kayıdın herhangi bir alanının olup olmadığı kontrolü yapılabilir
    # Opsiyonel bir durumdur. İhtiyaç halinde yapılması gerekir.
    check_record = db.query(mArticles).filter(mArticles.title == article_info.title).first()
    if check_record: return {'status': 'article_title_exist'}

    ### Tablonun alanları ve request ile gelen alanları birbirine eşitleyip kayıt oluşturuyoruz.
    ### Fakat kayıt henüz tabloda oluşmadı
    create_record = mArticles(
        title=article_info.title,
        content=article_info.content,
        read_time=article_info.read_time,
        is_active=article_info.is_active,
    )

    ## Kaydı tabloya ekleyen komut.
    db.add(create_record)

    ## Kaydı tabloya eklendikten sonra tabloyu kaydeden komut.
    db.commit()

    ## Tüm işlemler bittikten sonra yeni kaydın istenilen alanlarıyla birlikte döndürülecek mesaj
    return {'status': 'created', 'id': create_record.id, 'title': article_info.title}


## Get/List işlemleri için get methodu kullanılır.
@router.get("/get/article", summary="Get Article")
def get_article(article_id: int):
    ## Veri tabanında işlem için oturum açan komut. Tüm işlemler bittikten sonra return den önce db.close() ile oturum düşürülebilir.
    db = SessionLocal()

    ## Kaydın istenilen alanına göre tek bir kayıt döndürmek üzere yapılan sorgu.
    ## id yerine tablonun diğer alanları da kullanılabilir.
    check_record = db.query(mArticles).filter(mArticles.id == article_id).first()

    ## Kayıt bulunamazsa döndürülecek mesaj.
    if not check_record: return {'status': 'article_not_found'}

    ## Sorguda eşleşen ve döndürülen kayıt.
    return check_record


## Get/List işlemleri için get methodu kullanılır.
@router.get("/list/article", summary="List Article")
def list_article():
    ## Veri tabanında işlem için oturum açan komut. Tüm işlemler bittikten sonra return den önce db.close() ile oturum düşürülebilir.
    db = SessionLocal()

    ## Tüm kayıtları herhangi bir filtreleme olmadan döndüren bir sorgu.
    check_record = db.query(mArticles).all()

    ## Örneğin sadece aktif kayıtlar getirilmek istenilseydi
    # check_record = db.query(mArticles).filter(mArticles.is_active == True).all()

    ## Kayıt bulunamazsa döndürülecek mesaj.
    if not check_record: return {'status': 'article_not_found'}

    ## Sorgu sonucu dönen kayıt veya kayıtlar.
    return check_record


## Update işlemleri için put methodu kullanılır.
@router.put("/update/article", summary="Update Article")
def update_article(article_id: int, article_info: ArticleInfo):
    ## Veri tabanında işlem için oturum açan komut. Tüm işlemler bittikten sonra return den önce db.close() ile oturum düşürülebilir.
    db = SessionLocal()

    ## Kaydın istenilen alanına göre tek bir kayıt döndürmek üzere güncellenecek kaydı bulmak için yapılan sorgu.
    ## id yerine tablonun diğer alanları da kullanılabilir.
    check_record = db.query(mArticles).filter(mArticles.id == article_id).first()

    ## Kayıt bulunamazsa döndürülecek mesaj.
    if not check_record: return {'status': 'article_not_found'}

    ## Bulunan güncellenmemiş kaydın yeni gelen alanlarla birbirine eşleştirilip güncellenmesi
    check_record.title = article_info.title
    check_record.content = article_info.content
    check_record.read_time = article_info.read_time
    check_record.is_active = article_info.is_active

    ## Güncelleme işlemini veritabanında kaydeden komut
    db.commit()

    ## İşlem sonrası döndürülecek mesaj.
    return {'status': 'updated'}


## Delete işlemleri için delete methodu kullanılır.
@router.delete("/delete/article", summary="Delete Article")
def delete_article(article_id: int):
    ## Veri tabanında işlem için oturum açan komut. Tüm işlemler bittikten sonra return den önce db.close() ile oturum düşürülebilir.
    db = SessionLocal()

    ## Kaydın istenilen alanına göre tek bir kayıt döndürmek üzere yapılan sorgu.
    ## id yerine tablonun diğer alanları da kullanılabilir.
    check_record = db.query(mArticles).filter(mArticles.id == article_id).first()

    ## Kayıt bulunamazsa döndürülecek mesaj.
    if not check_record: return {'status': 'article_not_found'}

    ## Eşleşen kaydı silen komut.
    db.delete(check_record)

    ## Silme işlemini veritabanında kaydeden komut
    db.commit()

    ## İşlem sonrası döndürülecek mesaj.
    return {'status': 'deleted'}

# endregion
