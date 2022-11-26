from ninja import NinjaAPI, Schema, ModelSchema
from ninja.orm import create_schema
from .models import *
from typing import List

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


SkillSchema = create_schema(Skill, depth=1)
@api.get('/skills', response=List[SkillSchema])
def skills(request):
    return Skill.objects.all()