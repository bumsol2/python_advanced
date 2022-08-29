# 실습문제 2.4.1
# word_list 에 들어 있는 문자열 중 첫글자가
# a 인 것만 뽑아서 리스트로 만드세요.

word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

a = []

for word in word_list:
    if word[0] == 'a':
        a.append(word)
print(a) 



