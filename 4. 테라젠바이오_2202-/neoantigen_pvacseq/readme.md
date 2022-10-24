## Neoantigen 분석
### WES 분석 이후 mutect2 paired, single 분석, RNA seq (cufflinks 데이터를 뽑기 위해) 진행한 데이터를 받고 neoantigen 분석을 위한 파이프라인
### docker 로 분석을 진행한다.

### <br/><br/><br/>

## 결과
### 102 ~ 103 번 폴더에 결과가 쌓인다.
![image](https://user-images.githubusercontent.com/62974484/195229823-93148704-efd5-46d7-8fb7-08bea13586fa.png)
![image](https://user-images.githubusercontent.com/62974484/195229900-9e723f29-f26b-4f32-ada7-ecfdbfc36d22.png)


### <br/><br/><br/>

## 결과 해석
```
# 결과 파일
{sample_id}.all_epitopes.tsv

# epitopes 후보 선정 기준
['BEST MT Score'] < 500 # 면역원성이 있다고 해석

#'Best MT Score'는 pVACseq 분석에 사용된 모든 tool에서 가장 ic50이 낮은 것을 보여줌
```
