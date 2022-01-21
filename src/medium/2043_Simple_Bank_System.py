"""
https://leetcode.com/problems/simple-bank-system
Runtime: 696 ms, faster than 85.65% of Python3 online submissions for Simple Bank System.
Memory Usage: 43.6 MB, less than 96.41% of Python3 online submissions for Simple Bank System.
"""

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 < account1 <= self.n and 0 < account2 <= self.n and self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 < account <= self.n:
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 < account <= self.n and self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)