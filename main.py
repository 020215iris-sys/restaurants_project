# main.py
from restaurants.korean import get_korean
from restaurants.snack import get_snack
from restaurants.cafe import get_cafe
from restaurants.western import get_western_food

def print_menu():
    print("=" * 40)
    print("🍴 우리 동네 맛집 사전")
    print("=" * 40)

    categories = [
        ("🍚 한식", get_korean()),
        ("🥟 분식", get_snack()),
        ("☕ 카페", get_cafe()),
        ("🍝 양식", get_western_food())
    ]

    total = 0
    for emoji_name, restaurants in categories:
        print(f"\n[{emoji_name}]")
        for r in restaurants:
            print(f"  • {r['name']}  ⭐{r['rating']}  💰{r['price']:,}원")
            total += 1

    print(f"\n총 {total}개 가게가 등록되어 있습니다.")

if __name__ == "__main__":
    print_menu()
