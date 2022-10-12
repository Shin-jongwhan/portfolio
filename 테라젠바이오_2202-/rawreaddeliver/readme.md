## 프로그램 설명
### demulti 후 fastq 데이터 read 개수 조절, read length 길이 조절, 통계 프로그램(read 개수, Q20, Q30, GC content, Nbase 개수 등을 계산), fastqc, ftp 서버 납품(sshpass, scp를 통해서)의 기능이 있다.

# 개선점
## 1. rawreaddeliver 명령어 실행 개선
### 수연 사원님에게 rawreaddeliver 실행하는 방법에 대해 교육을 받던 도중 개선할 수 있을 것 같아서 만들었습니다.
### 기존 방식은 엑셀에서 sample.idx.txt를 만든 다음 -> 3개의 스크립트를 실행하는데 중간중간에 텍스트 수정이 필요한 작업이 있고 -> rawreaddeliver를 실행합니다.
### * 엑셀 파일은 운영팀에서 메일로 전달 받는 엑셀파일입니다.
### 엑셀파일 예시 - 분석의뢰 (작업번호: 13972, 프로젝트: TBD211642, 서비스: 12946: Sequencing).
<div align="center"><img src="https://user-images.githubusercontent.com/62974484/155466707-390a6a74-d0fc-4ace-a725-de8bfb8f463d.png" width="50%" height="50%"><br/></div>

### <br/><br/><br/>

## 2. 트리밍일괄입력(Gb), TN ID마다의 생산량 조절 개선
### 2-1. LIMS의 트리밍일괄입력 칸은 Gb (10억 base)로 표현, rawreaddeliver는 순수 개수로 써야 하는 문제점이 있습니다. 그 결과 양식을 통일해줘야 합니다.
<div align="center">
    <img src="https://user-images.githubusercontent.com/62974484/155466773-7171e65a-1495-4ca9-bfc2-336ec0d7af70.png" width="50%" height="40%"><br/>
</div>

### 2-2. TN ID가 여러개 있을 때는 각 TN ID마다 생산량을 계산해줘야 합니다.
### 2-3. TN ID 하나에는 여러 개 샘플이 들어 있습니다. 그래서 한 TN ID의 샘플 개수가 10개 일 때, 총 생산량을 10 Gb로 조절해주고 싶다면 한 개 샘플의 생산량 = 10 / 10 = 1 Gb 로 조정해줘야 합니다. 
### 2-4. 각 샘플마다 여러 요인에 의해 생산량이 다릅니다. 어떤 샘플 데이터는 많이 생성되고, 어떤 것은 적게 생성됩니다. 이 부분은 간단한 방법으로는 max 값을 설정해주어 총 생산량이 넘지 않게 설정할 경우 해결됩니다. 요청된 'TN ID마다의 생산량 / 한 TN ID 샘플 수'만큼 하면 생산량을 넘지 않게 됩니다. 이를 max 값으로 설정합니다. 또한 성준 사원님에게 전달 받은 사항으로는 read 개수가 같을 때 고객이 헤깔리는 경우가 있다고 합니다. 그래서 (nGb ~ nGb + 1) 범위 내 난수를 발생시켜 해결하였습니다.

### <br/><br/><br/>

## 3. NIPTON LIMS 연동, fetch
### LIMS에서 가져오는 데이터는 fastq 파일명, fastq dir, read length입니다. 
### fastq 파일명과 fastq dir는 data_list를 작성할 때, 파일 exist test에 쓰입니다.
### read length는 Gb 생산량 계산시 구해야 하는 값으로 보통 151이지만 림스에서 그대로 가져와 수기로 기입할시 발생하는 휴먼에러 등의 오류를 줄입니다.

### <br/><br/><br/>

# 실행 방법
### 1. 엑셀에서 [라이브러리명]\t[인덱스1]\t[인덱스2]\t[샘플명] 과 같이
### sample.idx.txt를 만든다. (기존 방식과 동일)

<img src="https://user-images.githubusercontent.com/62974484/155466823-ad7f4371-f27a-49aa-8e1d-02731c7f612d.png" width="70%" height="70%"><br/>
### 
### 2. 아래와 같이 다음 스크립트를 실행한다
### python [this script] [트리밍일괄입력(Gb)] [리드 서열의 3' 부터 잘라낼 base 길이] [work_id] 1> log.txt &
#### * 주의 : [리드 서열의 3' 부터 잘라낼 base 길이]는 LIMS의 리드길이일괄입력란을 그대로 입력하시면 안 됩니다. 리드길이일괄입력란이 100이면 151 - 100 = 50 입력하셔야 합니다. 그래야 101개가 됩니다. 1은 Calibration base 입니다. (리드길이일괄입력란을 입력으로 수정할 수는 있지만... 생략...)
![image](https://user-images.githubusercontent.com/62974484/155466865-105d8c80-ccdb-4efd-8b10-7400b12535f8.png)

### ex)
```
$ python ../script/rawdata_demulti_2.1.0.py 10 0 14378 1> log.txt 2> stderr.txt &
```
### 
### 만약 rawreaddeliver.py에 파라미터를 수정하고 싶은 경우 아래 라인을 고치시면 됩니다.
```
os.system("python {0} {1} {2} dna data_list {3} outprefix --server-name qc --cpu 10 --from-to cp".format(sRawReadDeliver, sProject, sWork_id, sCurrent_dir))
```

#### 파라미터는 rawreaddeliver 페이지를 참고
#### https://gitlab.ptbio.kr/bi/rawreaddeliver


### <br/><br/>
##### * rawreaddeliver에서 max 값보다 작은 read가 있는 fastq의 경우 데이터가 그대로 나오는 것을 확인하였습니다.
##### * 샘플마다 균일하게 생산량을 줄이려면 TN ID 마다 있는 모든 샘플의 fastq를 읽어서 합한 다음, 생산량과의 차를 구하고, 그 값 / 샘플 수만큼 나눈 후, 각 fastq read 개수 - 해당 값을 빼주면 균일하게 뺄 수 있으나 생산량이 적은 fastq는 더 줄어드는 문제점이 있을 것 같습니다. 다른 방법으로는 총 생산량 / 샘플 수보다 많은 데이터에서만 정확히 실제 데이터 양에서 요청한 생산량만 남도록 하는 방법이 있을 것 같습니다. 가장 좋은 방법은 퀄리티를 계산해서 퀄리티가 낮은 것 순서로 삭제하는 방식이지만, 퀄리티 기준으로 and 원하는 생산량만큼만 컨트롤한다는 것은 기술적으로 가능은 하지만 이 부분은 이 프로그램에서 개선하는 방향성은 아닐 것 같습니다.
### <br/><br/><br/>

# 220712
## rawreaddeliver_220712.zip
### improved 최종

### <br/><br/><br/>

