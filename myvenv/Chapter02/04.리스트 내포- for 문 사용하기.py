#리스트 내포
#for if 문 간편하게 사용
#[표현식 for 변수 in 순회 가능한 데이터]
from random import randrange


nums = [i for i in range (5)] #0~4
print(nums)

nums2 = [100,200,300]
double_nums = [i * 2 for i in nums2 ] # 200,400,600
print(double_nums)

nums3 = [ i for i in range(10) if i% 2 == 0]  
# for i in range(10) #i = 0~9
#   if i % 2 == 0 # 02468
print(nums3)

nums4 = [ 100,200,300,400,500]
double_nums2 = [ i * 2 for i in nums4 if i >= 300]
# for i in nums 
# if i >= 300 
# 600 800 1000
print(nums)

