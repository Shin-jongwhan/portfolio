# snpeff tsv 결과 필터링

## 220930
### 기능
#### FILTERING, AF 계산하여 컬럼 추가 및 필터링
#### WES config 인식
#### WES 파이프라인에서 mutect2, 19_snpeff 폴더에 있는 tsv 파일들을 모두 인식하여 한 번에 필터링
#### AF (allele frequency) 컬럼 추가

### <br/><br/><br/> 

## 221006
### run_wes_snpeff_filter_1_1_0.py
#### method import 하여 코드 간소화
### snpeff_tsv_filter_upload_1_0_0.py
#### haplotypecaller / mutect2 single / mutect2 paired filtering 결과 upload 폴더에 심볼릭 링크 
##### * run_wes_snpeff_filter_1_1_0 는 아직 mutect2 single 이 없긴 하다...

### <br/>
### 결과 : snpeff 폴더에 샘플 별로, 분석 별로 각각 tsv 파일로 생성된다.
#### ![image](https://user-images.githubusercontent.com/62974484/195233267-a519bc9f-2699-4a0a-baa8-1353c68d0bb0.png)
#### ![image](https://user-images.githubusercontent.com/62974484/195233479-2a9156dc-e8db-4e7d-b102-73b654c9e0a2.png)

### <br/><br/><br/>  
