## 프로그램 설명
### 다양한 분석 pipeline에 필요한 분석 툴 경로, 파라미터, 샘플, DB 정보를 구성해주는 프로그램.
### 궁극적인 목표는 여기서 파이프라인의 필요한 정보들을 모두 취합하고, 분석 명령어 하나만 치게 하게 만드는 것이다.
### 기능
1. nipton db 에서 sql 문 사용하여 정보 취합
2. 분석 파이프라인에 들어가는 config 정보 작성
3. rawdata 경로 인식
4. 분석 파이프라인 명령어 cmd.sh 파일로 저장
5. 분석 폴더 생성
6. ready to analysis !

## <br/><br/><br/>

## 220315
### 코드 정리, 최적화 및 프로그램 개선
### 샘플 fastq 파일 한글명 -> 영문명 지원
#### 기존에 만들어진 json 파일을 활용하였다. 해당 json 파일은 림스 DB에서 가져온 것이고, 특정 작업번호의 정보다. 시스템의 통합이 안 되어 있어 이러한 문제점이 생긴다.
![image](https://user-images.githubusercontent.com/62974484/158285041-eec80c30-f21b-4660-a188-74e7bd28dfa1.png)
## <br/><br/><br/>

## 220317
### WES 분석 파이프라인 돌린 후 exon_coverage 추가 분석 지원
## <br/><br/><br/>

## 220427
### json 파일이 없을 경우(자동납품을 하지 않았을 경우) DB에서 가져오도록 수정
### Autodelivery가 아닌 Rawreaddeliver에서 실행 후 나온 trimmed rawdata 폴더 및 파일 인식
## <br/><br/><br/>

## 220531
### copy_data.py 수정
#### qc 서버 업글레이드하면서 경로들을 다 파괴(?)해놨다. 그래서 일부 작업들을 다시 해야했고 sql문 써서 한글로 된 fastq 명을 trimming 경로에서 잘 가져올 수 있도록 업데이트해주었다.

### <br/><br/><br/>

## 220614
### make_config.py 수정
#### qc 서버 업글레이드하면서 config에서 한글이 써지는 것 -> 영문으로 써지도록 DB에서 값 가져와서 

### <br/><br/><br/>

## 220622
### WGS human 파이프라인 추가 지원

### <br/><br/><br/>

## 220704
### DB에서 fastq 경로 잘못 가져오는 것 쿼리 수정
### WES 분석 완료 후 분석 데이터 경로 chmod -R 777 로 권한 풀어주기

### <br/><br/><br/>

## 220921
### rawdata 경로 가져올 때 특수문자 있으면 경로를 제대로 못 가져온다. 특수문자는 '\_'으로 치환하여 가져오게 기능 업데이트.
#### copy_data.py
![image](https://user-images.githubusercontent.com/62974484/191387132-1e6209bd-c386-4c61-a7c1-b1d64c270b3d.png) <br/> 
![image](https://user-images.githubusercontent.com/62974484/191387180-8837afcf-d26a-4b75-b1ad-eaef6214cb80.png) <br/> 
#### 다음과 같이 특수문자가 있는 경우 제대로 가져올 수 있도록 수정
![image](https://user-images.githubusercontent.com/62974484/191387380-22383c67-df37-4e4c-aa4b-f72f3f2e8009.png) <br/> 
![image](https://user-images.githubusercontent.com/62974484/191387433-cfcbdffd-5edd-454c-b90e-950146555c52.png) <br/> 

### <br/><br/><br/>

## 220922
### 220921 과 같은 이유로 sample_config.txt 에 샘플명 특수문자는 '\_'으로 치환하여 가져오게 기능 업데이트.

### <br/><br/><br/>

