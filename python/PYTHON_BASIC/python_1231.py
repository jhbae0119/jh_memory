#자동으로 여러명에게 편지 쓰기

import pickle

#name = input("편지 보낼 친구 이름: ")
lst = ["지영","혜진","호은"]
last_thank = "2021년엔 좋은 일들만 가득하길 싸랑해"

for i in lst:
    with open("{0}에게 보내는 2020년 마지막 편지.txt".format(i), "w", encoding="utf8") as letter_2020:
        letter_2020.write("{0}아 안녕 2020년이 벌써 지나갔네 올 해는 정말 순식간에 지나간거 같아".format(i))
        letter_2020.write("\n어쩌다보니 올 해는 살아남은것에 감사하는 해가 됐어. \n우리 정말 고생 많았다.")
        letter_2020.write("\n내년은 코로나도 종식되는 좋은 소식이 있었으면 좋겠어.")
        letter_2020.write("\n내 곁에서 함께 해줘서 고마워 앞으로도 더 잘 지내쟈 우리")
        letter_2020.write("\n{0}".format(last_thank))