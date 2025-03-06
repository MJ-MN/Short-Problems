class Solution(object):
    def findFibonacci(self, n1, n2, seqStr, base, arr):
        seqStrLen = len(seqStr) - base
        if seqStrLen == 0:
            return True
        if seqStr[base] == "0" and n1 + n2 != 0:
            return False
        n3 = n1 + n2
        n3Str = str(n3)
        if len(n3Str) <= seqStrLen and n3Str == seqStr[base:base + len(n3Str)] and n3 < 2147483648:
            arr.append(n3)
            return self.findFibonacci(n2, n3, seqStr, base + len(n3Str), arr)
        else:
            return False

    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        numLen = len(num)
        for i in range(1, (numLen + 1) // 2):
            n1 = int(num[:i])
            for j in range(1, (numLen - i) // 2 + 1):
                n2 = int(num[i:i + j])
                arr = [n1, n2]
                if self.findFibonacci(n1, n2, num, i + j, arr):
                    return arr
        return []
