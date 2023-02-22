# region Imports

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import routers

# endregion

# region App Options
app = FastAPI(debug=True, docs_url=None, redoc_url=None, description="Fast API Example Article Project", version="1.0.0", title="Article Project", swagger_ui_parameters={"syntaxHighlight.theme": "obsidian", "defaultModelsExpandDepth": -1}, contact={"name": "Doğancan A.", "email": "dogancannavci@makdos.com"})

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
# endregion

# region Routers
app.include_router(routers.router, tags=['Article'], prefix="")


# endregion

# region HomePage
@app.get("/", include_in_schema=False)
async def homepage():
    return get_swagger_ui_html(openapi_url=app.openapi_url, title="Article Project", oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url, swagger_js_url="/static/swagger-ui-bundle.js", swagger_css_url="/static/swagger-ui.css", swagger_favicon_url="/static/favicon.png")  # endregion
