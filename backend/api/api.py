from ninja import NinjaAPI
from .models import *

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}