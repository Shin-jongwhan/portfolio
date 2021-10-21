sFile_dir = "C:\\Users\\user\\Desktop\\앙팡_과제\\"
sFile_name = "앙팡_업데이트_200506_decision.txt"
sResult_file_1 = sFile_dir + sFile_name.split(".")[0] + "_modi1." + sFile_name.split(".")[1]
sResult_file_2 = sFile_dir + sFile_name.split(".")[0] + "_modi2." + sFile_name.split(".")[1]

def modi_0() :
        # DB를 CSV로 받으면 한글이 깨지기 때문에 txt로 연 후에 수정
        # txt 파일 안에서 NULL -> "NULL"로 수정한 후 스크립트 실행하기
        # 개행문자로 인한 파싱 오류 수정(문장의 "를 /으로 수정한 상태)
        f = open(sFile_dir + sFile_name, 'r', encoding = "utf-8")
        ls = []
        ls = f.readlines()
        print(len(ls))
        f.close()
        
        for i in range(len(ls) - 1, -1, -1) :
                if ls[i] == "\n" :
                        del ls[i]
        
        for i in range(0, len(ls)) :
                ls[i] = ls[i].strip()

        lsResult = []
        sTmp = ""
        for i in range(0, len(ls)) :
                if ls[i][-1] == "/" and sTmp == "" :
                        lsResult.append(ls[i])
                elif ls[i][-1] != "/" :
                        sTmp += ls[i]
                elif ls[i][-1] == "/" and sTmp != "" :
                        sTmp += ls[i]
                        lsResult.append(sTmp)
                        sTmp = ""
                else :
                        print(ls[i])            # error check
                        
        fResult = open(sResult_file_1, 'w', encoding = "utf-8")
        for i in range(0, len(lsResult)) :
                if lsResult[i][0] == "/" :              # 양쪽 끝 "/" 제거
                        lsResult[i] = lsResult[i][1:]
                if lsResult[i][-1] == "/" :             # 양쪽 끝 "/" 제거
                        lsResult[i] = lsResult[i][:-1]
                fResult.write("\t".join( lsResult[i].split("/,/") ) + "\n")             # "\t" 로 join
        fResult.close()


def modi_1() :
        # 테스트 샘플 제거
        f = open(sResult_file_1, 'r', encoding = "utf-8")
        ls = []
        ls = f.readlines()
        f.close()
        for i in range(0, len(ls)) :
                ls[i] = ls[i].strip()
                
        for i in range(len(ls) - 1, -1, -1) :
                #print(ls[i].split("\t")[1])
                if len(ls[i].split("\t")[1].split("-")[0]) != 13 :              # 샘플 id 규칙(len(sample_id) == 13)이 아니면 제거
                        del ls[i]
                elif "test" in ls[i] or "TEST" in ls[i] or "Test" in ls[i] :              # test 샘플 제거
                        del ls[i]
                elif "Father" in ls[i] or "Mother" in ls[i] :           # 부모 검사 제거
                        del ls[i]

        for i in range(len(ls) - 1, -1, -1) :
                #if ls[i].split("\t")[1][:4] == "2018" or ls[i].split("\t")[1][:4] == "2019" or ls[i].split("\t")[1][:4] == "2020" :
                        #print(ls[i].split("\t")[1][:4])
                        #continue
                if int(ls[i].split("\t")[1][:6]) > 201806 :
                        #print(ls[i].split("\t")[1][:6])
                        continue
                #print(ls[i].split("\t")[1][:4])
                del ls[i]
                        
                        
                        
        fResult = open(sResult_file_2, 'w', encoding = "utf-8")
        for i in range(0, len(ls)) :
                fResult.write(ls[i] + "\n")
        fResult.close()


def sample_count() :            # decision_call 데이터에서 중복된 샘플이름 제거하고 샘플 수 세기
        f = open("C:\\Users\\user\\Desktop\\앙팡_과제\\test\\sample.txt", 'r')
        ls = []
        ls = f.readlines()
        f.close()

        lsResult = []

        for i in range(0, len(ls)) :
                ls[i] = ls[i].strip()
        ls = sorted(ls)

        for i in range(0, len(ls)) :
                if lsResult == [] :
                        lsResult.append(ls[i])
                        continue
                elif lsResult[-1] == ls[i] :
                        continue
                elif lsResult[-1] != ls[i] :
                        lsResult.append(ls[i])
        print(len(lsResult))


def main() :
        sample_count()


main()
