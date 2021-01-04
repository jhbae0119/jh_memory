# 11-1. 모듈
# 필요한 것들이 부품처럼 만들어져있는것
# 모듈 사용시, 같은 경로에 있거나, 파이썬 라이브러리 폴더에 있어야 함

import python_module
python_module.price(3)
python_module.price_morning(3)
python_module.price_soldier(3)

# 별명 사용
import python_module as pm
pm.price(3)
pm.price_morning(3)
pm.price_soldier(3)

# from import
from python_module import * 
price(3)
price_soldier(3)
price_morning(3)

# 원하는 def만 import할 수 있음
from python_module import price_soldier, price_morning
price_soldier(3)
price_morning(3)

# 함수에 별명 붙일 수 있음
from python_module import price_soldier as sd
sd(3)

# 11-2. 패키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import *
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()