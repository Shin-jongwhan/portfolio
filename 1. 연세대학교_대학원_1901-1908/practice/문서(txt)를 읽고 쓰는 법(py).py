def main_1() :
    fTest = open("C:\\Users\\sk\\Desktop\\test.txt", 'w')   # 파일을 특정 위치에 만들고 쓰는 법 (w)
    for i in range(1, 11) :
	data = "%d번째 줄입니다.\n" % i
	fTest.write(data)
	# %d는 i를 받아 입력됨. 1~10까지 반복
    f.close()   #파일 닫기


main_1()
##############################################################

f = open("C:\\Uesrs\\sk\\Desktop\\test.txt", 'r')   # 파일 읽기 (r)
line = f.readline() # .readline()은 한 줄을 읽고 읽은 줄을 날린다.
line = f.readline() # 다음 줄 읽어옴
f.close()   #파일 닫기
##############################################################

f = open("C:\\Uesrs\\sk\\Desktop\\test.txt", 'r')   # 파일 읽기 (r)
for i in f :
    print(i)    #f를 통해 한 줄씩 읽어올 수도 있다.
##############################################################

f = open("C:\\Uesrs\\sk\\Desktop\\test.txt", 'r')
f.read()    #파일의 전체 text를 읽어온다.
sFile = f.read()    #파일의 text를 변수에 저장할 수 있다.
while True :
    line = f.readline()
    if not line : break
    print(line) #line이 f.readline()을 읽어서 더 이상 읽어올 내용이 없을 때까지 읽어온다.
f.close()
##############################################################

f = open("C:\\Users\\sk\\Desktop\\test.txt", 'r')
lines = f.readlines()   #.readlines는 각 줄을 리스트로 불러온다.
for i in lines :
    print(i)    #리스트 [0]부터 lines[ len(lines) ] 까지 읽어온다.
#똑같이 읽어오는 다른 방법
for i in range(0, len(lines)) : #len은 리스트에서는 리스트가 몇개인지 알려준다(int형)
                                #string에서는 string 글자 개수가 몇개인지 알려준다.
    print( liens[i] )
##############################################################\


