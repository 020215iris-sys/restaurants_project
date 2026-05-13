# services/stats.py
from collections import Counter
from models.restaurant import Restaurant


def total_count(restaurants: list[Restaurant]) -> int:
    """전체 가게 수."""
    return len(restaurants)


def average_rating(restaurants: list[Restaurant]) -> float:
    """평균 평점 (소수점 둘째 자리까지)."""
    if not restaurants:
        return 0.0
    return round(sum(r.rating for r in restaurants) / len(restaurants), 2)


def best_rated(restaurants: list[Restaurant]) -> Restaurant | None:
    """최고 평점 가게 한 곳."""
    if not restaurants:
        return None
    return max(restaurants, key=lambda r: r.rating)


def count_by_category(restaurants: list[Restaurant]) -> dict[str, int]:
    """카테고리별 가게 수를 dict로 반환한다."""
    return dict(Counter(r.category for r in restaurants))

def average_price(restaurants: list[Restaurant]) -> int:
    """평균 가격 계산 (일부러 에러가 나게 만든 함수)"""
    return sum(r.price for r in restaurants) / len(restaurants)