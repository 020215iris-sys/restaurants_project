# modles/restaurant.py

class Restaurant:
    '''맛집 한 곳의 정보를 담는 클래스'''

    def __init__(self, name: str, category: str, rating: float, price: int):
        self.name = name
        self.category = category
        self.rating = rating
        self.price = price

    def to_dict(self) -> dict:
        '''JSON 저장용 dict 변환'''
        return {
            "name": self.name,
            "category": self.category,
            "rating": self.rating,
            "price": self.price,
        }
    
    @classmethod
    def from_dict(cls, data:dict)-> 'Restaurant':
        '''json 로드 시  dict -> 객체'''
        return cls(
            name=data["name"],
            category=data["category"],
            rating=data["rating"],
            price=data["price"],
        )
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.category})⭐{self.rating} 💰{self.price:,}원"'