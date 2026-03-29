class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if amount == 0:
            return 0

        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            best = float('inf')
            for coin in coins:
                res = dfs(rem-coin)
                if res != float('inf'):
                    best = min(best, 1+res)

            memo[rem] = best
            return best

        dfs(amount)
        return memo[amount] if memo[amount] != float('inf') else -1
        