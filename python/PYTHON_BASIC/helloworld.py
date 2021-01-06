#Quiz
#사이트별로 비밀번호를 만들어주는 프로그램 작성

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1)+ "!"로 구성
# 최종 생성 비밀번호: nav51!

site ="http://naver.com"
rule1=site[7:]
#print(rule1)
rule2 = rule1[:rule1.index(".")]
#print(rule2)
rule3 = rule2[:3]
#print(rule3) 
password= rule3 + str(len(rule2)) + str(rule2.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(site, password))
