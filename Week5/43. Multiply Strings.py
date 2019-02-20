
class Solution(object):
    def multiply(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        carry=0
        sum=''
        arr=[0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j]=arr[i+j]+int(num1[i])*int(num2[j])
        for i in range(len(arr)):
            number=(arr[i]+carry)%10
            carry=(arr[i]+carry)/10
            sum=str(number)+sum
        while sum[0]=='0'and len(sum)>=2:
            sum=sum[1:]
        return sum
