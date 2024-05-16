def solution(n):
    # dp table 선언
    dp = [0 for _ in range(2001)]
    # 초기값
    dp[0] = 1
    dp[1] = 1
    # dp 테이블 채우기
    for i in range(2, 2001):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    return dp[n] 