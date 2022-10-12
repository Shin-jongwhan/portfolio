## WGS non-human 파이프라인을 위한 스크립트
### <br/><br/><br/> 

### WGS_nonhuman_ftp_upload.py
#### WGS 파이프라인 실행 후 고객 ftp 서버의 폴더로 scp 하는 기능
- -w, -p, -r, -f 파라미터를 전달할 수 있다.
- -w 파라미터는 필수로 써야 한다.
- -w만 쓸 경우 ftp에 대한 정보만을 출력한다.
- -w와 -p만 쓸 경우 ftp에 대한 정보 + 고객 ftp 서버에 있는 -w에 준 작업번호 dir와 tree 구조를 출력한다.
- -r은 autodelivery, rawreaddeliver dir를 선택할 수 있다. 1이면 ftp 서버에서 autodelivery 폴더 구조만을 바꾸고, autodelivery와 rawreaddeliver 둘 다 재업로드 가능하다.
- -f 1을 주면 ftp 업로드한다. default는 0이다.

![image](https://user-images.githubusercontent.com/62974484/166344035-869eca17-586d-4704-89cc-6efdc4c89f1f.png)

### <br/><br/><br/>

## cnvkit_scatter.1.0.0.py
### cnvkit scatter에서 크모로좀 별로 나눠서 scatter plot을 그릴 수 있게 함
### 사용법은 python [script] 입력 시 출력

### <br/><br/><br/> 

## cnvkit.annot.snakefile
### cnvkit를 돌릴 수 있는 snakefile
### scatter 및 diagram까지 돌릴 수 있다.

### <br/><br/><br/> 

## AnnotatSV.sh
### cnvkit.vcf 파일을 annotation 해주는 AnnotSV 명령어가 저장된 쉘 스크립트이다.

### <br/><br/><br/>

## 220630
### wgs_nonhuman_report.1.0.0.py
#### wgs nonhuman report에 들어갈 정보를 정리해주는 script
#### 현재 nonhuman은 정보가 일정하지 않고 다양하기 때문에 지금까지(?) report를 준비된 ppt 양식으로 작성 -> pdf로 변환하여 납품한다.
1. 슬라이드 각각에 들어갈 정보를 ppt 양식 포맷에 맞춰서 input 파일을 정리하는 기능
2. 필요한 plot을 추가로 그려주는 기능

### <br/> 
### 다음과 같이 정보를 출력해준다.
![image](https://user-images.githubusercontent.com/62974484/195231808-fbde7a00-c1b3-4390-90b8-54466a4ed361.png)

### <br/><br/><br/>

## 220721
### wgs_nonhuman_prep_running.1.0.0.py
#### WGS nonhuman 파이프라인을 실행하기 위해 rawdata 를 qc1 서버에서 복사하고 분석 폴더를 만든 후 config, cmd.sh 를 만들어주는 프로그램이다.
#### nonhuman 의 경우 종마다 / 의뢰마다 reference (fasta, gff3)를 다운로드 링크를 통해 항상 다시 받아야 하므로 reference 까지 자동화하는 것은 만들지 못 하였으나 나중에 규칙이 생겼을 때 만드는 걸로
![image](https://user-images.githubusercontent.com/62974484/180109294-c259609e-433a-4193-b146-9fffbc44c532.png)


### <br/><br/><br/>
