class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n % 2 != 0:
            return pow(x, (n-1)/2) * pow(x, (n-1)/2) * x
        else:
            return pow(x, n/2) * pow(x, n/2)