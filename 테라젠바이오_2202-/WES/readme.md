# Whole Exome Sequencing 완전 자동화 프로젝트

## 220317
### 1. 분석 tools들에 대한 정보, 샘플, 분석 정보 등을 만들어주는 configmaker 인식, 프로그램 실행
### 2. WES 분석 파이프라인 실행
#### - WES 분석만 골라서 실행
#### - WES 분석 파이프라인을 실행할 수 있는 계정으로 ssh 접속
#### - conda 환경 자동 바꾸기
#### - nipton DB (LIMS)에서 필요한 정보 fatching (sql)
#### - 프로그램 백그라운드 실행, 타계정에서 실행된 프로그램 접속 끊어도 끝날 때까지 실행
### 3. 분석 완료 모니터링
### 4. 고객 ftp 서버로 자동으로 데이터 복사(납품)
### 5. 분석 완료 후 수주 업무에 대한 기록을 남기는 기록지 자동 작성
#### - 분석 관리 용이성 증대
### 그외 : 기존에는 exon_coverage 분석이 여러 스텝으로 나뉘어져 있었던 것을 한 번의 명령어로 실행되도록 수정

### <br/><br/><br/> 

## 220415
### 이전 버전은 configmaker를 수동으로 작성한 후 wes_auto_run.sh를 실행해줘야 했음
### configmaker - samples.tsv 파라미터를 전달받아 자동 작성, 기존에 있던 samples.tsv는 \[프로젝트 id\]\_\[작업번호\]\_samples.tsv"로 변경
### auto_wes.sh err, std를 프로젝트 id, 작업번호, 현재날짜(YYMMDD)를 같이 써주게 변경
### 작업번호마다 개별 프로세스 관리할 수 있도록 변경(while, time.sleep으로 데몬과 같이 작동하며 24시간 전까지 결과가 안 나오면 죽는다)
![image](https://user-images.githubusercontent.com/62974484/163516794-c5518ed1-b76c-4e39-8868-f45a4c182b13.png)

- wes_get_report_pdf_and_tree_from_ftp.py <br/>
  this script is same as wes_ftp_upload.py and it just turn off scp function
  
### <br/><br/><br/> 

## 220518
### WES_mutect2 파이프라인
### WES 기본 분석 이후 네오안티젠 파이프라인 셋팅에 필요한 paired / single mutect2 pipeline 구축
### WES 분석은 germline (haplotypecaller), single sample 분석만 있는 상태임
#### 빅데이터 팀에 해당 파이프라인이 있었고 이를 생명정보부 팀에 맞게 재구축하는 작업 중 mutect2 paired 또는 single sample 분석이 요구됨
#### 빅데이터 팀 자료
![image](https://user-images.githubusercontent.com/62974484/169056123-7b09af8d-d645-401d-af1e-cf8a9f4cbbd1.png)
### <br/>
### 분석 단계
1. mutect2 <br/>
paired / single bam을 input으로 한 mutect2 분석
2. FilterMutect2Var <br/>
mutect2.vcf filtering. gatk4 FilterMutectCalls을 사용한다.
3. CollectSequencingArtifactMetrics, FilterMutect2Bias <br/>
somatic mutation annotation에서 추가 필터링 과정 (sequence context-dependent artifacts, e.g. OxoG or FFPE deamination) <br/>
gatk4 FilterByOrientationBias 에서 사용되는 -P 옵션에 넣는 input을 생산하기 위해 picard CollectSequencingArtifactMetrics 를 이용
4. final vcf <br/>
germline, panel of normal 변이 필터링 후 output으로 final vcf 생성
![image](https://user-images.githubusercontent.com/62974484/169059636-9cb9af77-1d61-4c7a-af2b-7e93456b85d5.png)

### <br/><br/><br/> 

## 220524
### WES_mutect2 파이프라인 업데이트
1. parallel 분석(CPU 최적화를 위해 한 번에 돌아가는 샘플 개수 제한은 일부 만들어놓고 필요시 업데이트)
2. 샘플마다 complete flag 작성
3. 실행한 명령어 출력 및 저장
4. 각 분석 스텝마다의 err, std 저장
### WES ftp upload 업데이트
#### 샘플 수가 많아서 report pdf가 여러개일 때 여러 개 모두 가져오기

### <br/><br/><br/>

## 220525
### ftp 업로드, get tree 관련 스크립트 wes_get_report_pdf_and_tree_from_ftp_220525.py, wes_ftp_upload_220525.py
#### 자동납품을 안 해서 json 파일이 안 생긴 경우, LIMS DB에서 FTP 정보(아이디, 비밀번호, ftp 서버 등) 가져오기

### <br/><br/><br/>

## 220613
### wes_auto_run_with_configmaker_1.2.0.py
#### qc1 업그레이드로 rawdata /data02 ~ 07 경로로 인식하게 수정
### <br/>
### manual_anal_config 폴더
#### 림스를 통해 넘어오지 않은 fastq 인식 -> WES config 및 cmd.sh 자동 작성

### <br/><br/><br/>

## 220615
### wes_auto_run_with_configmaker_1.3.0.py
#### qc1 서버 업그레이드로 qc1 서버 rawdata 인식, 분석 서버로 복사 -> 분석 진행하도록 업데이트
#### 이미 rawdata가 복사되었다면, 시간 / 리소스 낭비이므로 다시 복사 안 함
#### WES 분석 계정에서 분석이  chmor -R 777 * 하여 권한 풀기

### <br/><br/><br/>

## 220617
### WES_upload_snpeff_vcf.1.1.0.py
#### snpeff vcf 70_ftp_upload_run/04_annotation_file/\[샘플\] 폴더에 샘플별로 snpeff vcf  심볼릭링크를 걸어준다.

### <br/><br/><br/>

## 220707
### wes_ftp_upload.1.1.0.py
#### 파라미터 안 맞을 시 에러메세지 출력 기능 추가
#### 서버 scp 10g, 120g 지원으로, 지원되는 titan 서버일 시 10g / 120g 로 실행 가능하도록 코드 수정

### <br/><br/><br/>

## 220630
### wes_auto_run_with_configmaker_1.4.0.py
#### get_rawdata_from_qc1(cli, lsMax_storage) rawdata dir 체크 기능 강화

### <br/><br/><br/>

## 220720
### wes_auto_run_with_configmaker_1.5.0.py
#### analysis flag 를 추가하여 분석을 진행할지 안 할지 선택하는 기능 추가

### <br/><br/><br/>

## 220721
### wes_auto_run_with_configmaker_1.6.0.py
#### ftp upload flag 를 추가하여 고객 FTP 서버에 업로드를 할지 안 할지 선택하는 기능 추가
#### project id 와 DB 에서 가져오고 species 받는 파라미터도 DB 에서 가져올 수 있으나 'human' 으로 고정되게 수정하여 해당 2개 파라미터는 제거 -> 좀 더 사용하기 간편해짐 :)

### <br/><br/><br/>

## 220725
### wes_auto_run_with_configmaker_1.7.0.py, wes_auto_run.1.2.0.sh
#### 파라미터 수정
- annotated vcf 업로드는 자주 들어오고 범용성 있는 기능으로 uplaod_snpeff_vcf_flag 기능 추가
- FTP_upload_flag, uplaod_snpeff_vcf_flag 체크 기능 추가 : 해당 flag 는 wes_analysis_flag 가 1 이어야만 작동하게 체크. 아니면 programm exit
#### wes_auto_run.1.2.0.sh 는 버전에 맞게 파라미터 주도록 수정


### <br/><br/><br/> 

## 220729
### wes_ftp_upload.1.3.0.py
#### FTP 서버에서 데이터 삭제 후 디렉토리가 비어있는지 체크하는 과정에서 wait 이 제대로 안 되어서 empty check 단계가 오류가 있었음
#### 30초 동안 10번, dir 가 비어있는지 다시 체크하는 스텝을 추가

### <br/>
### folder_structure_munjangsup.1.1.0.py
#### 자주 들어오는 고객으로 폴더 구조 변경을 요청하여 해당 고객에 맞춰 디렉토리 변경과 폴더 이름 변경을 한다.
#### 1.1.0 업데이트 : wes_ftp_upload.1.3.0.py 과 같은 이유

### <br/><br/><br/> 

## 220731
### concordance_cal.py
#### vcf 간 변이 일치율 확인. 샘플이 섞였는지 QC 확인할 수 있다.
#### 90% 이상이면 같은 샘플로 의심할 수 있다.
#### 75~80% 정도면 부모 - 자식 간의 일치율이다.
#### 다른 샘플일경우 아무리 높더라도 75% 미만이다.
#### 사용법 (python2)
```
$ python2 concordance_cal.py -i "*/*.vcf.gz" > concordance.tsv
```
![image](https://user-images.githubusercontent.com/62974484/182012292-73c6cbeb-68be-4ff3-9e80-da05462cbd16.png)


### <br/><br/><br/>

## 220803
### wes_auto_run_with_configmaker_1.7.0.py 다음 부분을 수정
```
def get_rawdata_from_qc1(cli, lsMax_storage) : 
	#stdin, stdout, stderr = cli.exec_command("ls | grep _{0}_".format(sWork_id))
	nDir_count = 0
	sRawdata_dir_qc1 = ""
	for i in range(0, len(lsRawdata_dir_qc1)) : 
		stdin, stdout, stderr = cli.exec_command("ls {0} | grep _{1}_".format(lsRawdata_dir_qc1[i], sWork_id))
		time.sleep(5)
		lsRawdata_dir = stdout.readlines()
		# 수정 : -[workid]- 로 되어 있는 경우 인식가능하게 수정. -가 문자로 인식하지 않고 std 로 인식해서 에러가 나서 \\- 로 문자로 인식하게끔 함
		if lsRawdata_dir == [] : 
			stdin, stdout, stderr = cli.exec_command("ls {0} | grep \"\\-{1}\\-\"".format(lsRawdata_dir_qc1[i], sWork_id))
			time.sleep(5)
			lsRawdata_dir = stdout.readlines()
```
