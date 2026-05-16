class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while temp > 0:
            num = temp%10
            reverse = reverse*10 + num
            temp = temp//10
        return reverse == x

        