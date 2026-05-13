# data_manager.py

import json
from pathlib import Path
from models.restaurant import Restaurant

DATA_PATH = Path("data/restaurants.json")

def load_restaurants() -> list[Restaurant]:
    '''JSON 파일에서 맛집 목록 불러오기'''
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)
    return [Restaurant.from_dict(item) for item in data]

def save_resuarants(resuarants: list[Restaurant]) -> None:
    '''맛집 목록을 JSON 파일로 저장'''
    DATA_PATH.parent.mkdir(exist_ok=True)
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(
            [r.to_dict() for r in resuarants],
            f,
            ensure_ascii=False,
            indent=2,
        )