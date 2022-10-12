# cnvkit 추가 분석 파이프라인
## 221004

### <br/><br/><br/> 

## 사용 방법
### 환경 설정은 자동으로 구축되어(따로 설치 필요 없음) project_dir 만 잘 넣어주면 됩니다.
### sample_config 는 아래 설명과 같이 자동 인식되지만, 따로 넣어주려면 -c 옵션을 사용합니다.
### -b 옵션으로 hg19, h38 선택 가능하며 sample_config 에 명시된 reference 와 맞아야 제대로 분석됩니다. default 는 hg19.
### parallel 은 개발 미정입니다. all sample parallel 분석이고 추후 필요시 개발.
![image](https://user-images.githubusercontent.com/62974484/193763462-b912c867-67e8-404d-98ee-0a731c5d9618.png)

### <br/><br/><br/>

## ex)
```
$ python WGS_human_cnvkit_1_0_0.py -p /data02/project/jhshin/TBD220925-15999-WGS-human-20220921
```

### 결과
### 결과는 06-1_cnvkit 에 생성됩니다.
### <br/> 
### 아래와 같이 분석 완료되었는지 체크하며 WGS 프로세스와 동일합니다.
- complete flag 체크
- sh, sh_err, sh_std 생성
- result/06-1_cnvkit 에 결과 생성
#### ![image](https://user-images.githubusercontent.com/62974484/193763350-b841d2dc-30e2-400b-9f2a-b52d1544a789.png)
#### ![image](https://user-images.githubusercontent.com/62974484/193764026-b168c2cd-fefd-4f6f-9575-789f7a5cd268.png)
#### ![image](https://user-images.githubusercontent.com/62974484/193764170-02ef16ee-efa1-4215-bfa9-29de4bed590c.png)
#### ![image](https://user-images.githubusercontent.com/62974484/193765453-9b813198-c2d7-48d0-bd45-5614a8545ada.png)

### <br/><br/><br/>

## 221005
### WGS_human_cnvkit_upload_1_0_0.py
#### upload 경로에 샘플 명으로 변경하여 링크
![image](https://user-images.githubusercontent.com/62974484/193983849-2cc7ff03-02d4-4b2c-b8d2-29fdf102801d.png)

### <br/><br/><br/>

## 221006
### WGS_human_cnvkit_1_1_0.py
#### 1. 연관 파일들을 실행하는 스크립트의 절대경로 가져오도록 수정
#### 2. diagram 모듈 기능 추가 / 개선하고 명령어 실행 추가
- [python 경로]/site_package/[모듈 이름]/ 에 스크립트 수정

### <br/><br/><br/>
