# https://leetcode.com/problems/greatest-common-divisor-of-strings/?source=submission-ac
# greatest-common-divisor-of-strings
# 문자열과 최대공약수의 조합, 유클리드 호제법을 통해 최대공약수를 구하던 이전 스킬 적용

class Solution(object):

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if str1+str2 != str2+str1:
            return ""
        
        def gcd(n, m):
            while m > 0:
                n, m = m, n % m
            return n

        count = gcd(len(str1), len(str2))
        return str1[:count]