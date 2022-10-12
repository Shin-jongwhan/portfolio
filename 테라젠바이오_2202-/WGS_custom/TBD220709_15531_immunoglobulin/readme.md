## 220802
### Immunoglobulin 분석

### <br/><br/><br/>

#### 고객이 RNA 를 PCR product 로 시퀀싱을 의뢰, 분석을 요청 (light chain / heavy chain 을 한 샘플에 같이 pooling 하였고, heavy chain 도 light chain 과 동일한 PCR product 구조임), 특징은 벡터 서열이 붙어 있다.
![image](https://user-images.githubusercontent.com/62974484/182296452-24c6e8c9-9bd9-4519-a852-0e49fb2ec5ea.png)
![image](https://user-images.githubusercontent.com/62974484/182296487-57bdb111-cddb-4cfc-949d-e400a541eb60.png)
### <br/>

#### cutadapt 로 벡터 서열 trimming 후 분석 진행하였음.
![image](https://user-images.githubusercontent.com/62974484/182296816-0ad80504-2b6f-42be-a0e5-0d604af84b58.png)
#### <br/>
#### cutadapt 서열
![image](https://user-images.githubusercontent.com/62974484/182297107-b3169d62-b6b0-4e35-b70c-f15de0cf65c7.png)
#### <br/>
#### cudapt command
```
python -m cutadapt --pair-filter=any --minimum-length 30 -j 12 -q 30 -a file:../trim_seq.fasta -A file:../trim_seq.fasta -o sample_pSBL9b-TD02_cDNA_20_cycle_cutadapt_1.fq.gz -p sample_pSBL9b-TD02_cDNA_20_cycle_cutadapt_2.fq.gz sample_pSBL9b-TD02_cDNA_20_cycle_1.fq.gz sample_pSBL9b-TD02_cDNA_20_cycle_2.fq.gz
```

### <br/>

#### 항체 분석 파이프라인이 없어 cDNA fasta 로 bwa, star mapping 진행
#### 결과가 어느 정도 나온 것은 bwa
- bwa stat : reads mapped / (reads mapped + reads unmapped) = 약 60%
![image](https://user-images.githubusercontent.com/62974484/182296767-0e91634f-d859-4446-ac2c-fd6351a3d947.png)

#### fasta header 에 description 이 되어 있어 annotation 개발 및 진행.
#### fasta header 는 다음과 같이 써져 있다.
```
>ENST00000396075 ENST00000396075.5 cdna chromosome:GRCh38:12:21638368:21657362:-1 gene:ENSG00000111716.14 gene_biotype:polymorphic_pseudogene transcript_biotype:protein_coding gene_symbol:LDHB description:lactate dehydrogenase B [Source:HGNC Symbol;Acc:HGNC:6541]
```
#### annotation_result.tsv
![image](https://user-images.githubusercontent.com/62974484/184080467-9ecafe2a-75d4-41a8-a55b-6fb4b0cc6e65.png)


### <br/><br/><br/>

## 220811
### vcf_to_result_tsv_1_1_0.py
#### vcf 에서 annotation 된 tsv 결과 만들고, 엑셀 파일까지 생성해준다. 개별 샘플을 실행할 수 있다.
### <br/>

### vcf_to_result_tsv_2_0_0.py
#### 한 샘플씩이 아니라 RINE bwa 경로를 파라미터로 주면 모든 샘플의 *.sort.vcf.gz 를 가져와서 annot tsv, 엑셀 파일을 만들어 준다.

### <br/><br/><br/>

## 220817
### vcf_to_result_tsv_1_3_0.py
#### plot 그리기 업데이트
- vcf 에서 chr2, 14, 22번만 있게 하고 나머지 필터링, 유전자 앞 글자에 IG 없으면 필터링
- vcf 에서 각 chr start, end 구해서 plot 에 그려질 maximum bar plot 개수 지정 (20000개로 지정, plot 그리는 것은 무겁기 때문에 줄여줘야 함)
- 막대 width 지정
- 변이 중간에 interval append
#### plot 결과
![image](https://user-images.githubusercontent.com/62974484/184926781-827c4fcd-baac-4395-94fd-68552c4bb1f1.png) <br/>
#### 폰트 변경 : Consolas
![image](https://user-images.githubusercontent.com/62974484/185053832-88fd9844-b5e9-42f7-b059-d213368114b2.png) <br/> 

### <br/><br/><br/>

## 220818
### vcf_to_result_tsv_1_4_0.py
#### 마무리 작업
#### gene annotation
##### * 그래프는 많이 안 그려봤는데.. 진짜 힘들다.
![image](https://user-images.githubusercontent.com/62974484/185264682-53af3350-ad35-4ee4-b662-169992a23a5f.png) <br/>

### <br/><br/><br/>

## 220824
### BamToBaseCount.ver1.1.py
#### human team script
#### 사용 방법
```
 /usr/bin/python2.7 /TBI/Share/NonHumanTeam/Script/WGRS/script/BamToBaseCount.ver1.1.py /TBI/People/tbi/jhshin/reference/TBD220709_15531/pSBL9b-TD02_primer_marked_BIONEER.fa pSBL9b_TD02_cDNA_20_cycle.sort.bam pSBL9b_TD02_cDNA_20_cycle.sort.xls
```
#### 결과
![image](https://user-images.githubusercontent.com/62974484/186429611-dfe7eb49-2c11-423b-b8d0-1d82693eea37.png)

### <br/><br/><br/>

## 220825
### 바이오니아의 김신애 팀장이라는 악성 고객이다. 계속 요구 사항을 바꾸며 추가 요청을 한다.
### basecount_multisample.py
#### basecount 이후 결과 xls 넣어주어 합쳐주고, frequency 컬럼 추가. frequency plot 을 그려준다.
#### result 결과
![image](https://user-images.githubusercontent.com/62974484/186468023-245d530d-eb30-4fc8-a0b5-cb2e59dcbe07.png)
#### plot 결과
![image](https://user-images.githubusercontent.com/62974484/186468089-a2efb206-651a-40e9-aa91-6b51e385b11f.png)

### <br/><br/><br/>

## 220913
### BamToBaseCount.ver1.1.py
#### samtools (또는 bcftools) mpileup 을 사용하여 variant call 을 한 후 basecount 를 해주는 스크립트
![image](https://user-images.githubusercontent.com/62974484/189842220-d0d31b55-ad30-4d46-93bc-cf897507d2ee.png)
#### 사용법
```
python2 [this_script] [.fa] [.bam] [.result]
```

### <br/><br/>

### basecount_multisample_1_1_0.py
#### BamToBaseCount 스크립트 결과 xls 파일을 input 으로 한다.
#### plot 을 그려주고 xls 파일들을 합쳐준다.
#### DP threshold 파라미터를 추가하였다.
![image](https://user-images.githubusercontent.com/62974484/189841848-7d5fc2fd-7e4d-470b-9119-292e7d9e6df2.png)

### <br/><br/><br/>
