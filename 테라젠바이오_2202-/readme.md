# 테라젠바이오
## 입사 : 2202~
## 재직 중
## 기간 : 재직 중

### <br/><br/><br/>

# 프로젝트

### <br/><br/><br/>

## rawreaddeliver
### rawreaddeliver 속도 개선
### fastq 전처리, merge, stat 을 계산해주는 파이프라인
### cython (파이썬 코드 c 컴파일할 수 있는 언어) 로 개발 후 C 로 개발
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/rawreaddeliver/improved

### <br/><br/><br/>

## rawdata
### rawreaddeliver 와 연계된 프로그램, rawreaddeliver 이후 처리해야하는 것에 대한 프로그램들이다.
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/rawdata

### <br/><br/><br/>

## neoantigen 분석 파이프라인 구축
### WES 기반이며 HLA I (optitype 결과), cufflinks (FPKM 결과), GATK mutect2 결과를 input 으로 하여 pvacseq 이라는 tool 을 사용하여 신항원 예측을 해주는 파이프라인이다.
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/neoantigen_pvacseq

### <br/><br/><br/>

## igblast
### igblast 이론 및 실습 교육 자료 작성, 발표
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/igblast

### <br/><br/><br/>

## configmaker
### 다양한 파이프라인에서 필요한 config, 파이프라인을 실행하기 위한 (ready to execute) 전처리기
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/configmaker
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/config-maker-v2

### <br/><br/><br/>

## class
### 개인적으로 관리하는 파이썬 class 모듈이다.
### 경로는 .bashrc 에 등록, import 하여 사용한다.
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/class

### <br/><br/><br/>

## WGS_nonhuman
### WGS_nonhuman 파이프라인을 위한 스크립트
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_nonhuman

### <br/><br/><br/>

## WGS_human
### WGS_nonhuman 파이프라인을 위한 스크립트
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_human
### WGS_human 분석 이후 CNV 분석 (cnvkit) 파이프라인
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_human/cnvkit
### 한국화학융합시험연구원 전용 WGS human 분석 파이프라인 개발
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_human/KTR_WGS

### <br/><br/><br/>

## WGS_custom
### 고객의 요청으로 사내 분석 파이프라인이 없는 것은 별도 개발
### 항체 분석 건
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_custom/TBD220709_15531_immunoglobulin
### fastq readcount 분석 - 일정한 길이일 때(특정 read 길이만 분석), 각 포지션, base ratio plot 제공
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_custom/wgs_custom_anlbio
### fastq readcount 분석 - 길이가 일정하지 않을 때(모든 길이 분석)
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WGS_custom/wgs_custom_read_count

### <br/><br/><br/>

## WES
### WES 파이프라인을 위한 스크립트
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES
### optitype (HLA class I) 분석을 위한 파이프라인
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/optitype
### hisatgenotype (HLA class II) 분석을 위한 파이프라인
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/hisat_genotype
### configmaker 에서 지원하지 않고 manual 로 config 를 만들어야 할 때 사용하는 스크립트
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/manual_anal_config
### 기존 WES 파이프라인에서 지원하지 않는 annotation 을 추가
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/snpeff_addon_db
### WES 파이프라인 이후 나온 vcf 를 snpeff annotated vcf 필터링해주는 기능
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/snpeff_tsv_filter
### somatic mutation 추가 분석 (mutect2) 파이프라인
#### https://github.com/Shin-jongwhan/theragenbio_2202/tree/main/WES/wes_mutect2

### <br/><br/><br/>
