class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        memo = {}
        coins.sort(reverse=True)
        usable_coins = []
        for c in coins:
            if c < amount:
                usable_coins.append(c)
            elif c == amount:
                return 1            
        self.change(usable_coins, amount, memo)
        # print(memo)
        return -1 if amount not in memo else memo[amount]

    def change(self, coins, amount, memo):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        elif amount >= 0 and amount in memo: 
            return memo[amount]

        min_coin_used = -1
        for c in coins:
            # max_coin = amount // c
            # for i in range(1, max_coin+1):
            #     print('used coin: {} by {}'.format(c, i))
            coin_used = self.change(coins, amount - (c), memo)
            if coin_used >= 0 and \
                (min_coin_used == -1 or (coin_used + 1) < min_coin_used):
                min_coin_used = (coin_used + 1)
        
        memo[amount] = min_coin_used
        # print('min_coin_used', min_coin_used)
        return min_coin_used

if __name__ == '__main__':
    s = Solution()
    # assert s.coinChange([1,2], 3) == 2
    # assert s.coinChange([1], 0) == 0
    # assert s.coinChange([1,2,5], 11) == 3
    assert s.coinChange([1,3,5], 8) == 2
    assert s.coinChange([186,419,83,408], 6249) == 20
    assert s.coinChange([3,7,405,436], 8839) == 20
    