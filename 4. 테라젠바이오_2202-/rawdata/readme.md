## rawdata_get_ftp_report
### 1. 작업 번호를 통해 DB에서 여러가지 정보를 가져온다(ftp 접속 정보, 프로젝트 번호 등)
### 2-1. autodelivery를 통해 생산한 데이터가 ftp 서버로 잘 전송되었는지 체크, 납품 정보 출력(tree 구조), report pdf 파일 가져오기
### 2-2. rawreaddeliver를 통해 생산한 데이터에서 report pdf 가져오기, 고객 ftp 서버로 데이터 전송, 납품 정보 출력(tree 구조)
#### * autodelivery는 LIMS에서 자동납품이라는 기능을 담당한다. fastq, fastqc, fastq의 stat, report pdf 등이 output으로 나오고, 고객 ftp 계정으로 데이터를 자동으로 전송한다.
#### * rawreaddeliver는 autodelivery의 수동 버전. ftp 파일 전송 기능도 있으나 실제로는 ftp 접속 정보(아이디, 비밀번호, 접속 ip)를 출력하지 못 해 잘 안 쓰는 기능이고 autodelivery를 위한 기능.
### <br/><br/>

### UPDATE
### 1.3.0
#### rawreaddeliver로 파일 전송 시 전송 체크 기능 추가
### <br/> 

### 1.4.0
#### 파라미터 안 줬을 경우 help 출력
#### rawreaddeliver 경로 주고 ftp 업로드는 안 할 경우, ftp 서버에 workid 폴더 있는지 검사
### <br/><br/>

### 사용 방법
![image](https://user-images.githubusercontent.com/62974484/164180375-0b03df5c-d8aa-4ede-a965-446fec26d1d5.png)

### <br/><br/><br/>

## rawdata_demulti_with_no_sample_idx
### 작업번호만을 가지고 rawreaddeliver 프로그램을 실행시킬 수 있게 만들어주는 프로그램이다.
### <br/>

### UPDATE
### 3.0.0
#### data_list 작성 - 첫 번째 컬럼 --[idx1]-[idx2] 제외하고 TNID만 써지게 수정(인덱스까지 있으면 다른 걸로 간주해서 merge를 못 함)
#### qc server 폴더에 프로젝트 폴더 생성, 해당 폴더 안에 data_list 생성
#### rawreaddeliver 실행 os.system 명령어에 cd [프로젝트 폴더] && 추가
### <br/>

### 3.2.0
#### 인덱스로 분리할지 안 할지 파라미터 지정(0 false, 1 true)
### <br/> 

### 3.2.1
#### trimming 같은 TNID 별로는 같은 수치가 나오고, 2배로 나오게 수정(2배가 맞는 수치)
### <br/> 

### 3.3.0
#### 파라미터 전달 오류시 사용법 출력
![image](https://user-images.githubusercontent.com/62974484/165347037-101cb4d4-adcd-4182-af33-cc803ac21d57.png)
#### merge할 workid가 없을 때는 해당 workid에만 해당하는 rawdata만 가져오도록 기능 추가(파라미터 전달하여 사용)

### <br/><br/> 

### 사용 방법 
### 3.3.0
![image](https://user-images.githubusercontent.com/62974484/165351009-04dcd2c2-aaf3-4145-b5e8-c413de11bd45.png)

### <br/><br/><br/>

## preprocess_rawreaddeliver
### 아직 lims에 요청이 없는 상태, 디멀티는 끝난 상태에서 rawdata 선납품 요청이 들어왔을 때 rawreaddeliver를 돌릴 수 있게 해주는 프로그램
### 1.0.0
#### 기능
- trimming length in Gb
- trimming read length
- /data02~07 하드 연동 및 관리
- data_list 만들기
- 샘플 수 모두 잘 들어갔는지 검사
- rawreaddeliver 명령어 출력
![image](https://user-images.githubusercontent.com/62974484/166719572-ad0d6e6c-fd00-4a03-9085-e718ad167515.png)
### <br/>

### 사용 방법
#### 먼저 sample_list.txt를 작성한 후 프로그램을 돌린다.
#### samplt_list.txt : 탭으로 구분됨. [TNID]\t[sample_name]
![image](https://user-images.githubusercontent.com/62974484/166722209-1520ebbf-5ceb-4915-aca4-857587648173.png)

### <br/><br/><br/>

## upload_riken_rawdata
### riken_maker.v1.3.py로 riken genesis에서 요구하는 폴더 구조로 바꾼 후 고객 FTP 서버로 업로드
### riken genesis 건의 백엔드 전자동화 스텝임
- ssh 접속
- root 계정으로 업로드하기 위한 중간 프로세스 생성
  - 고객 FTP 서버에 upload_tmp.sh 생성하여 sudo 실행
- FTP 서버에서 sh 스크립트가 끝났는지 체크 -> 끝나면 폴더 체크하고 tree 구조 출력

### <br/><br/><br/>

## link_rawdata_dir_to_home.1.0.0.py
### 나의 홈 디렉토리에 /data02 ~ 07 에서 작업한 rawdata, 분석 데이터 경로를 통합 관리할 수 있게 심볼릭 링크를 걸어준다.

### <br/><br/><br/>

## 220621
### cp_rawdata_from_qc1.1.0.0.py
#### qc 서버 업그레이드로 qc1 서버에서(qc2도 추가 예정) 분석 서버로 copy data

### <br/><br/><br/>

## 220622
### cp_rawdata_from_qc1.1.1.0.py
#### 분석 서버에서 이미 복사된 rawdata가 있다면 해당 경로를 출력한 후 스킵한다.

### <br/><br/><br/>

## 220628
### rawdata_get_ftp_report.1.5.0.py
#### qc서버에서 rawdata 복사 후 분석 서버에서도 복사한 rawdata 폴더에서 report pdf 복사할 수 있도록 업데이트

### <br/><br/><br/>

## 220629
### rawdata_demulti_with_no_sample_idx_4.0.2.py (분석 서버 전용)
#### DB에서 fastq 경로, TNID, sample name 정보 가져올 때 중복된 정보는 fastq 경로로 정렬하여 삭제 기능 업데이트
### rawdata_demulti_with_no_sample_idx_3.3.2.py (qc 서버 전용)
#### DB 쿼리 추가
1. 쿼리 1
- TNID
- fastq file
- fastq file dir
- read length
- fastq file full path

2. 쿼리 2
- 작업번호 입력시 트리밍일괄입력 / 리드길이일괄입력 정보

### <br/><br/><br/>

## 220706
### rawdata_demulti_with_no_sample_idx_3.4.0.py
#### 1. 다른 TNID, 같은 sample name 체크 기능 추가 및 잘 보이도록 로그 색깔 입히기
#### 다른 TNID 인데 같은 sample name 이 있을 경우 rawreaddeliver 과정에서 에러가 난다. 마지막에 실행된 샘플명만 데이터가 저장되고 다른 건 삭제된다(덮어쓰게 된다).
#### 이러한 문제를 체크하기 위해 해당 기능을 넣었고, 고객이나 림스에 작업을 넘기는 컨설팅팀 / 실험팀 측의 검수를 확인하기 위함이다.
#### 2. DB에서 readlength를 -1로 잘못 가져오는 경우(151이 default) 해결
![image](https://user-images.githubusercontent.com/62974484/177448468-a4ed9b85-9677-48f8-98be-6c86233115d7.png)

### <br/><br/><br/>

## 220727
### rawdata_demulti_with_no_sample_idx_3.4.1.py
#### trim_throughput 잘못 계산되는 것 수정(지금까지 잘 계산되고 있었는데.. 뭔지 모르겠음)
- 기존 : 2 * ( 10억 * trim_len( Gb 수) ) / ( 샘플 개수 * (read 길이 - read_trimming_length) ) 
- 변경 : ( 10억 * trim_len( Gb 수) ) / (read 길이 - read_trimming_length)

### <br/><br/><br/>

## 220808
### rawdata_demulti_with_no_sample_idx_3.4.2.py
#### 한글 -> 영문 표기명 변환 업데이트
#### 자동납품을 누르지 않으면 delivery_file_name 은 none 으로 나오기 때문에 자동납품을 이용하지 않을 때에는 필히 delivery_name 에서 값을 가져와야 하지만, 한글명으로 되어 있는 경우가 많다...
![image](https://user-images.githubusercontent.com/62974484/183446649-92d02b97-ef99-4e3a-b6dd-2cd7917b0bd7.png)

### <br/><br/><br/>

## 220809
### preprocess_rawreaddeliver_2_1_0.py
#### rawdata_demulti_with_no_sample_idx_3.4.1.py 과 같은 이유로 수정

### <br/><br/><br/>

## 220829
### rawdata_demulti_with_no_sample_idx_3.5.0.py
#### taxonomy 분석 flag 추가

### <br/><br/><br/>

## 220905
### rawdata_demulti_with_no_sample_idx_3.6.0.py
#### sMerge_workid_flag 가 1 이면 merge 할 workid 같이 추가할 수 있도록 업데이트
- nipton db \- analysis_group 에 is_merge 가 'Y' 인지 체크, merge workid 불러와서 각 workid 별로 lsFastq_file 에 append

### <br/><br/><br/>

## 220919
### rawdata_demulti_with_no_sample_idx_3.6.2.py
#### merge workid 업데이트
#### merge workid 가 없을 때 data_list 가 안 만들어지는 현상 수정

### <br/><br/><br/>

## 221004
### preprocess_rawreaddeliver_2_2_0.py
#### -i 옵션에 run id 가 같은 것이 여러 개 들어갈 경우 sys.exit()
