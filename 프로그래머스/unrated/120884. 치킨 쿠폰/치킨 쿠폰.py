def solution(chicken):
    coupon = chicken
    service = chicken // 10
    total_service = service
    while coupon >= 10:
        coupon = service + coupon % 10
        service = coupon // 10
        total_service += service
    return total_service