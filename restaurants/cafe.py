# restaurants/cafe.py

cafe_list = [
    {"name": "컴포즈커피", "rating": 4.3, "price": 4000},
    {"name": "메가커피", "rating": 4.8, "price": 4500},
    {"name": "스타벅스", "rating": 4.8, "price": 180000},
]

def get_cafe():
    """카페 목록을 반환한다."""
    return cafe_list