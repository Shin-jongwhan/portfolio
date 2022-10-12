# 자주 사용하는 함수를 method 화
# 반복 코드를 줄이는 것이 목적

### <br/><br/><br/> 

## 버전 관리는 다음과 같이 심볼릭 링크를 걸어주어 최신화
### 관리하는 소스 코드가 많아지면 최신 버전으로 자동 업데이트 스크립트 작성해야 함
![image](https://user-images.githubusercontent.com/62974484/193994382-6af4b880-e3e0-4e17-a847-c8ed90597299.png)

### <br/><br/><br/>

## 221012
### general_1_1_0.py
#### 1. ssh_cli_exe return 에러 수정
#### 2. text color 기능 업데이트
```
 def __init__(self) :
        self.dicColor = {"red" : '\033[31m', "green" : '\033[32m', "yellow" : '\033[33m', "blue" : '\033[34m', "purple" : '\033[35m', "cyan" : '\033[36m', "white" : '\033[37m'}
        self.nColor_num = len(self.dicColor.keys())
        
 def text_color(self, sText, nColor_index = 5, blBold = True) :
        if blBold == True :
            sColor_text = "\033[1m{0}{1}\033[0m".format(self.dicColor[list(self.dicColor.keys())[nColor_index]], sText)
        else :
            sColor_text = "{0}{1}\033[0m".format(self.dicColor[list(self.dicColor.keys())[nColor_index]], sText)

        return sColor_text
```
##### ![image](https://user-images.githubusercontent.com/62974484/195221308-aa80b770-c4ce-4b3c-be1f-b922914294f6.png)
