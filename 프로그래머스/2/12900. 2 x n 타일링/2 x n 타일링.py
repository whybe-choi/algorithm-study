def solution(n):
    if n == 0 or n == 1:
        return 1
    # DP 테이블
    dp = [0 for _ in range(n+1)]
    # 초기값
    dp[0] = 1
    dp[1] = 1
    # DP 테이블 채우기
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n]