

from sanic import Sanic, text
from sanic_ext import Extend

app = Sanic(__name__)
app.config.CORS_ORIGINS = "*"
app.config.CORS_METHODS = ["GET", "POST", "PUT", "DELETE"]
Extend(app)


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")
