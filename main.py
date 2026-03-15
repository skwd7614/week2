import math
number1 = int(input('inch 단위를 입력해주세요:'))
print(number1*2.54,'cm')
number2 = int(input('kg 단위를 입력해주세요:'))
print(number2*2.20462,'lb')
number3 = int(input('원의 지름을 입력해주세요:'))
print('원의 둘레:',number3*math.pi,'원의 넓이:',(number3/2)**2*math.pi)