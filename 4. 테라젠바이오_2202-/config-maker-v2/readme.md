# configmaker v2
## for WINE (새로운 WES 파이프라인), RINE (RNA seq 파이프라인(STAR mapping, cufflinks...))

### <br/><br/><br/> 

## config-maker-v2_220715.zip
### 기본적인 골격이 만들어졌음
### 업데이트 사항
- qc1 서버 업그레이드, WINE 파이프라인에서 요구하는 config 에 맞춰서 작성되도록 수정.
- qc1 서버에 rawdata 가 있으면 분석 폴더로 복사 : fastq, fastqc, report pdf, 통계 엑셀 파일
- WINE 파이프라인에서 인식하는 fastq 명으로 심볼릭링크
- WINE config 작성 수정
- 분석 서버에 이미 rawdata 경로가 있다면 해당 폴더를 인식하여 config 등을 작성
- 현재까지 WINE - germline 분석만 테스트가 되었음

### <br/><br/><br/> 
