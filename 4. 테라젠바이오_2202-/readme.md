# 테라젠바이오
## 입사 : 2202~
## 재직 중
## 기간 : 재직 중
### 모든 프로젝트는 90% 이상 직접 프로그래밍하였습니다.

### <br/><br/><br/>

# 프로젝트

### <br/><br/><br/>

## rawreaddeliver
### rawreaddeliver index pooling 건 처리 방법 개선
#### lims 에서 자동으로 처리할 수 없는 건 중의 한 케이스로, 이를 어느 정도 간소화해주는 프로그램입니다.
#### [rawreaddeliver](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/rawreaddeliver)
### rawreaddeliver 속도 개선
### fastq 전처리, merge, stat 을 계산해주는 파이프라인
### cython (파이썬 코드 c 컴파일할 수 있는 언어) 로 개발 후 C 로 개발
#### [rawreaddeliver 속도 개선](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/rawreaddeliver/improved)

### <br/><br/><br/>

## rawdata
### rawreaddeliver 와 연계된 프로그램, rawreaddeliver 이후 처리해야하는 것에 대한 프로그램들이다.
#### [rawdata](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/rawdata)

### <br/><br/><br/>

## neoantigen 분석 파이프라인 구축
### WES 기반이며 HLA I (optitype 결과), cufflinks (FPKM 결과), GATK mutect2 결과를 input 으로 하여 pvacseq 이라는 tool 을 사용하여 신항원 예측을 해주는 파이프라인이다.
#### [neoantigen](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/neoantigen_pvacseq)

### <br/><br/><br/>

## igblast
### igblast 이론 및 실습 교육 자료 작성, 발표
#### [igblast](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/igblast)

### <br/><br/><br/>

## configmaker
### 다양한 파이프라인에서 필요한 config, 파이프라인을 실행하기 위한 (ready to execute) 전처리기
#### [configmaker](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/configmaker)
#### [configmaker-v2](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/config-maker-v2)

### <br/><br/><br/>

## class
### 개인적으로 관리하는 파이썬 class 모듈이다.
### 경로는 .bashrc 에 등록, import 하여 사용한다.
#### [class 모듈](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/class)

### <br/><br/><br/>

## WGS_nonhuman
### WGS_nonhuman 파이프라인을 위한 스크립트
#### [WGS_nonhuman](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_nonhuman)

### <br/><br/><br/>

## WGS_human
### WGS_nonhuman 파이프라인을 위한 스크립트
### WGS_human 분석 이후 CNV 분석 (cnvkit) 파이프라인
#### [WGS_human - cnvkit](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_human/cnvkit)
### 한국화학융합시험연구원 전용 WGS human 분석 파이프라인 개발
#### [KTR_WGS_pipeline](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_human/KTR_WGS)

### <br/><br/><br/>

## WGS_custom
### 고객의 요청으로 사내 분석 파이프라인이 없는 것은 별도 개발
### 항체 분석 건. 데이터 시각화 plot 자료 제공
#### [항체 분석](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_custom/TBD220709_15531_immunoglobulin)
### fastq readcount 분석 - 일정한 길이일 때(특정 read 길이만 분석), 각 포지션, base ratio plot 제공
#### [readcount - 일정 길이 분석](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_custom/wgs_custom_anlbio)
### fastq readcount 분석 - 길이가 일정하지 않을 때(모든 길이 분석)
#### [readcount - general](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WGS_custom/wgs_custom_read_count)

### <br/><br/><br/>

## WES
### WES 파이프라인을 위한 스크립트
#### [WES](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES)
### optitype (HLA class I) 분석을 위한 파이프라인
#### [HLA class I 분석](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/optitype)
### hisatgenotype (HLA class II) 분석을 위한 파이프라인
#### [HLA class I 분석](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/hisat_genotype)
### configmaker 에서 지원하지 않고 manual 로 config 를 만들어야 할 때 사용하는 스크립트
#### [manual config 작성](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/manual_anal_config)
### 기존 WES 파이프라인에서 지원하지 않는 annotation 을 추가
#### [annotation addon 프로그램](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/snpeff_addon_db)
### WES 파이프라인 이후 나온 vcf 를 snpeff annotated vcf 필터링해주는 기능
#### [snpeff annot result filtering](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/snpeff_tsv_filter)
### somatic mutation 추가 분석 (mutect2) 파이프라인
#### [somatic mutation 분석](https://github.com/Shin-jongwhan/portfolio/tree/main/%ED%85%8C%EB%9D%BC%EC%A0%A0%EB%B0%94%EC%9D%B4%EC%98%A4_2202-/WES/wes_mutect2)

### <br/><br/><br/>
