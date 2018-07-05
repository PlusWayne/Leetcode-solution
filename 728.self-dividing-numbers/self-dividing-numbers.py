class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left,right+1):
            list_num = [int(ele) for ele in str(num)]
            if 0 in list_num:
                continue
            flag = 0
            for i in list_num:
                if num % i != 0:
                    flag = 1
            if flag == 0:    
                res.append(num)
        return res
