#sequence파일을 읽어서 string 변수에 저장
#모두 대문자로
#\n 지우기
#첫 문장 지우기( ex) >CHR1)

def main() :
    a = open("c://Users//sk//Desktop//Python_bioinformatics_class//chroms_Human//chr1_GL383518v1_alt.fa")
    b = a.read()    #전체 읽어오기
    print( len(b) )
    a.close()
    b = b.upper()   #모두 대문자로
    b = b.replace("\n", "")     #개행문자 지우기
    print( len(b) )
    b = b.replace(">CHR1_GL383518V1_ALT", "")   #필요없는 첫문장 지우기(모두 대문자)
    print( len(b) )

main()
