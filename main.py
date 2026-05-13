# main.py
from services.data_manager import load_restaurants
from services.search import search_by_name, filter_by_category, filter_by_min_rating
from services.stats import total_count, average_rating, best_rated, count_by_category, average_price


def show_all(restaurants):
    print(f"\n총 {len(restaurants)}개 가게:")
    for r in restaurants:
        print(f"  • {r}")


def show_stats(restaurants):
    print("\n📊 통계 결과")
    print(f"  • 전체 가게 수: {total_count(restaurants)}개")
    print(f"  • 평균 평점: {average_rating(restaurants)}")
    print(f"  • 평균 가격: {average_price(restaurants):,}원")
    best = best_rated(restaurants)
    if best:
        print(f"  • 최고 평점: {best.name} (⭐{best.rating})")
    print("  • 카테고리별 가게 수:")
    for cat, cnt in count_by_category(restaurants).items():
        print(f"      - {cat}: {cnt}개")


def main():
    restaurants = load_restaurants()

    while True:
        print("\n" + "=" * 40)
        print("🍴 우리 동네 맛집 관리 시스템 v2")
        print("=" * 40)
        print("  1. 전체 목록 보기")
        print("  2. 이름으로 검색")
        print("  3. 카테고리로 필터")
        print("  4. 평점 N점 이상 보기")
        print("  5. 통계 보기")
        print("  6. 종료")

        choice = input("\n선택> ").strip()

        if choice == "1":
            show_all(restaurants)
        elif choice == "2":
            keyword = input("검색어: ")
            show_all(search_by_name(restaurants, keyword))
        elif choice == "3":
            cat = input("카테고리 (한식/분식/카페): ")
            show_all(filter_by_category(restaurants, cat))
        elif choice == "4":
            min_rating = float(input("최소 평점: "))
            show_all(filter_by_min_rating(restaurants, min_rating))
        elif choice == "5":
            show_stats(restaurants)
        elif choice == "6":
            print("👋 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 선택입니다.")


if __name__ == "__main__":
    main()