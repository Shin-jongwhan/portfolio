## 문제점
### 수학적 계산이 있고 대용량(몇십억줄~몇천억줄 또는 그 이상)의 파일을 읽기 때문에 굉장히 오래 걸리는 작업이다.
### 따라서 성능 개선이 필요하여 프로그램을 개발하였다.
### <br/> 

## 220315
### 파이프라인에서 가장 오래 걸리는 프로그램 개선(4.82배)
### Cython
#### 10만 line (25000 read) test
![image](https://user-images.githubusercontent.com/62974484/158284286-062a9f3b-b9e6-4f3e-ac03-f3aa8c114dce.png)
### <br/> 

## 220319
### 파이프라인에서 가장 오래 걸리는 프로그램 개선(21.11배)
### C언어로 개발
#### 1M line (25만 read) test
![image](https://user-images.githubusercontent.com/62974484/159109564-94ef30b1-533d-4e3d-86e4-519de3e1f0ac.png)
### <br/> 

## 220321
### c 파일
### FastqStatExtractFastqGZ.pairedend.cal.c
#### fq.gz 압축파일을 그대로 읽는 방식
### FastqStatExtractFastqGZ.pairedend.cal2.c
#### .fq 로 읽는 방식. cal.c보다 10~12% 속도 향상이 있지만 파이프라인이 기본적으로 fq.gz로 되어 있어 불필요하다고 판단하여 cal.c를 쓰고 있음.
### <br/> 

## 220424
### FastqStatExtractFastqGZ.pairedend.cal.1.2.0.o
#### 1000만 read를 읽을 때마다 출력(진행 상황 확인)
#### 아래와 같이 문자열의 메모리 할당을 받을만큼만 설정해줬더니 파일이 클 때(100기가 베이스 이상) 에러와 속도를 개선할 수 있었다. 4096으로 임의로 설정해줬을 때 넘어가는 경우도 있나보다.
![image](https://user-images.githubusercontent.com/62974484/164956459-1c04c9e7-d1cf-4c02-9cc4-6f32d41023cb.png)
#### 속도는 25.5배 향상
![image](https://user-images.githubusercontent.com/62974484/164956377-f59c1fd1-1a8c-4ec4-b3f0-3e0a8ca35666.png)
### <br/> 

## 220424
### FastqStatExtractFastqGZ.pairedend.cal.1.3.0.o
#### 최적화 작업 : read의 seq과 quality의 length는 같기 때문에 for loop의 반복을 줄임
#### 속도는 35.8배 향상
![image](https://user-images.githubusercontent.com/62974484/166092844-a586772c-a306-4261-b516-a91769d0aab0.png)
### <br/> 

## 220608
### FastqStatExtractFastqGZ.singleend.cal.1.3.0.c
#### single end 버전. input으로 fastq 하나만 들어간다.
### <br/>
### single end cython 으로 개발한 테스트 결과
![image](https://user-images.githubusercontent.com/62974484/172551360-2aa9df46-5165-403e-9367-a43932c89d5a.png)
### <br/> 

## 220609
### cython final
### paired, single 테스트 결과(최종)
```
paired, single 테스트 완료하였습니다. 적용시켜도 될 것 같습니다.
수정된 사항은 깃랩에 반영하겠습니다.
paired end에서는 FasterFastqStat에서는 약 1.51배, original에서는 약 4.34배 속도 향상 되었습니다.
single end에서는 이전에 공유드린 것과 거의 비슷합니다(4.53배).통계 계산이 1시간 걸린다면 10~15분으로 단축하는 효과가 있습니다.
```
![100Gb paired, single 테스트 결과_220609](https://user-images.githubusercontent.com/62974484/172740313-00ea79bf-f429-4029-b8a1-d3e75e8fbc0c.png)
### <br/> 
