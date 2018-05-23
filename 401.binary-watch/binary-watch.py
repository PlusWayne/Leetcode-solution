import itertools
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        '''
        s=list(range(10))
        res=[]
        for ele in itertools.combinations(s,num):
            temp=[0]*10
            hours=0
            mins=0
            temp_hour=8
            temp_min=32
            for i in range(len(ele)):
                temp[ele[i]]=1
            for j in temp[0:4]:
                hours+=temp_hour*j
                temp_hour=temp_hour//2
            if hours>=12:
                continue
            hours=str(hours)
            for j in temp[4:]:
                mins+=temp_min*j
                temp_min=temp_min//2
            if mins>=60:
                continue
            mins=str(mins)
            if len(mins)==1:
                mins='0'+mins
            res.append(hours+':'+mins)
        return res[::-1]
        '''
        return ['%d:%02d' %(h,m) for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1')==num]
