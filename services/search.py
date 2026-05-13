# services/search.py
from models.restaurant import Restaurant


def search_by_name(restaurants: list[Restaurant], keyword: str) -> list[Restaurant]:
    """이름에 keyword가 포함된 가게를 반환한다."""
    keyword = keyword.lower()
    return [r for r in restaurants if keyword in r.name.lower()]


def filter_by_category(restaurants: list[Restaurant], category: str) -> list[Restaurant]:
    """특정 카테고리의 가게만 반환한다."""
    return [r for r in restaurants if r.category == category]


def filter_by_min_rating(restaurants: list[Restaurant], min_rating: float) -> list[Restaurant]:
    """평점이 min_rating 이상인 가게만 반환한다."""
    return [r for r in restaurants if r.rating >= min_rating]