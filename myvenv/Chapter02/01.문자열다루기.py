#1.replace
# 문자열교체
tired = '오늘 피곤해.'.replace("피곤", "건강")
print(tired)
#2. find
# 문자열 찾기
a = 'Korea wellfare is hell'.find('hell')
    
print(a)

#3. split
#문자열 분리
b = '오늘은 피곤하다 언제 잘까'.split()
print(b)

c = '오늘은 피곤하다 언제 잘까'.split(':')
print(c)

#4. strip
# 문자열 공백 제거
d = '  sleep  '.lstrip() #왼쪽 공백만 제거
print(d)
e = '  sleep  '.rstrip() #오른쪽 공백만 제거
print(e)
f = '  sleep  '.strip() # 양쪽 공백 제거
print(f)

