# 화학연(KTR) WGS 과제를 위한 파이프라인

## 220801

### <br/><br/><br/>

### KTR_WGS_1_1_0.py
#### rawdata 를 qc1 서버에서 분석 서버로 복사, fastq_stat과 data_list 파일 를 인식, sample 명, fastq 파일 경로 인식
#### 파이프라인의 기본 골격을 만들어준다. 
#### 기본 골격에는 complete flag, 샘플 별 log (cmd, err, std), 샘플 별 result, script 크게 4가지로 나뉜다.
#### result 폴더
0. fastqc
1. cutadapt
2. bwa
3. gatk markduplicate
4. samtools stats (for alignment stat)
5. qualimap (for alignment stat)
6. gatk haplotypecaller
7. merge vcf
8. alignment stat
9. merge alignment stat
10. ftp upload

- rawdata qc1 서버에서 분석 서버로 복사 : rawdata, fastqc, data_list, rawdata stat, report pdf 를 가져온다. <br/>
![image](https://user-images.githubusercontent.com/62974484/182197269-7d968370-ed9e-4072-8ac5-a9881a501b60.png)
### <br/>

- 기본 골격 폴더 구조 <br/>
![image](https://user-images.githubusercontent.com/62974484/182425579-a0a36a8f-6bac-42d1-9365-6e6c78add875.png)
### <br/>

- 기본 골격 폴더 구조 log : 각각 분석 폴더에 다시 샘플 폴더가 있고 그 안에 std, err, cmd sh 스크립트가 있다. <br/>
![image](https://user-images.githubusercontent.com/62974484/182201850-68e473ce-c046-4f40-87fd-aca9f376d729.png)
### <br/>

- 기본 골격 폴더 구조 result <br/>
![image](https://user-images.githubusercontent.com/62974484/182425751-67c9ef9f-05d3-47c3-aa60-adddaf74ab17.png)
### <br/>
- script 폴더에는 샘플 별 분석 파이프라인 스크립트가 생성된다. complete flag 파일이 있는지 체크하여 생성되어 있다면 분석 pass 후 다음 분석을 진행한다. 만약 분석이 진행되었는데도 여전히 complete flag 파일이 없다면 에러 메세지와 함께 system exit.
![image](https://user-images.githubusercontent.com/62974484/182426495-3ef54b12-6a13-4cb7-a772-156899ae7194.png) <br/>
![image](https://user-images.githubusercontent.com/62974484/182427469-ee5fb7ab-3328-43f1-8c48-1131cf5a4cb6.png)
### <br/>

### 추후 개발 사항
#### 앞으로 얼마 안 남았다. concordance 분석(완료 -> 9. merge alignment stat 에 포함)과 심볼릭 링크 걸어준 ftp upload 폴더만 만들어주면 기본 골격 만드는 것은 끝난다(완).
#### complete flag 파일 만들기(완)
#### flag 파일 인식하여 분석 pass, complete flag 이 잘 만들어졌는지 체크(완)
#### 분석 실행을 제외하고 cmd 와 기본 골격까지만 실행가능하도록 만들기(220802 현재는 rawdata 복사까지만 가능하도록 하는 기능은 있음)
#### 기본 골격 완성 후 wgs queue 서버 인식(husky, orc, orca, grampus), 해당 4개 서버에서 분석 진행. queue 넣기.

### <br/><br/><br/>

## 220804
### KTR_WGS_1_2_0.py
1. husky, orc, orca, grampus 서버 연동
2. sample parellel 으로 들어가게 함(제한 현재는 한 번에 60 샘플까지)
3. log dir 에 샘플 script log 작성
4. 전 단계가 다 끝났는지 체크 후 merge vcf, merge align stat 실행
5. 개별 샘플의 분석이 끝났다면 그 샘플 analysis done 출력
6. 모든 단계가 끝났다면 analysis done 출력 
7. analysis 는 제외하고 cmd 와 기본 골격까지만 만들어지게 하는 flag (parameter) 추가 <br/>
![image](https://user-images.githubusercontent.com/62974484/182799627-a9fde9b6-e2ab-461b-8eb2-e844517700df.png) <br/>

### <br/><br/><br/>

## 220809
### KTR_WGS_1_2_1.py
#### thread 조절되는 프로그램을 위해 변수 추가

### <br/><br/><br/>

## 220810
### KTR_WGS_1_2_2.py
#### 07 merge vcf, 09 merge alignment stat 검사 기능 오류 수정 및 업데이트 : 분석 끝날 때까지 기다릴 때 출력 수정, 여러 번 프로그램 실행되지 않게 함.
#### 02 bwa 가 상당히 heavy 한 관계로 bwa 와 sort sam (bam file 만듦)의 complete check 을 2단계로 나눠놓았다.
#### run daemon 로그 출력 수정

### <br/><br/><br/>

## 220829
### KTR_WGS_align_stat_1_1_0.py
#### TBI_ID 컬럼 추가

### <br/><br/><br/>

## 220930
### WGS_KTR_ftp_upload.1.0.0.py
#### FTP 서버로 vcf, align stat, align_stat_all 전송

### <br/><br/><br/>

## 221012
### view_and_kill_process_1_0_0.py
#### 색으로 server name, process pid 표시, process kill 할지 선택
##### ![image](https://user-images.githubusercontent.com/62974484/195222312-2fc97a9c-34a5-4753-a8eb-fb14a006cc76.png)
##### ![image](https://user-images.githubusercontent.com/62974484/195222275-6965ea5a-846c-4bab-a02a-2c5de7d51e70.png)

### <br/><br/><br/>
