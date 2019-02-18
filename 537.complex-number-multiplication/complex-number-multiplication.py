class Solution:
    def complexNumberMultiply(self, a: 'str', b: 'str') -> 'str':
        a_split = a.split('+')
        a_real, a_imag = int(a_split[0]), int(a_split[1].strip('i'))
        b_split = b.split('+')
        b_real, b_imag = int(b_split[0]), int(b_split[1].strip('i'))
        res_real = a_real * b_real - a_imag * b_imag
        res_imag = a_real * b_imag + a_imag * b_real
        return str(res_real) + '+' + str(res_imag) + 'i'
