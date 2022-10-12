## run_wes_mutect2_1.0.0.py (모든 샘플 자동분석)
### WES 분석에서 sample_config.txt를 인식하여 mutect2 single / paired 분석을 가능하게 함

### run_wes_mutect2_1.0.0.py 사용법
![image](https://user-images.githubusercontent.com/62974484/170191686-70a96cb9-fb9f-4438-aa5e-cc085d484d85.png)

1. sample_config.txt 에 다음 항목을 추가한다. <br/>
single의 경우에는 paired_analysis를 추가 안 하면 된다. delivery_tbi_id 줄을 인식하여 single analysis가 실행된다.
```
paired_analysis                =     22017-Tumor:22017-Tumor:22017-Normal:22017-Normal,22018-Tumor:22018-Tumor:22018-Normal:22018-Normal,22020-Tumor:22020-Tumor:22020-Normal:22020-Normal
mutect2_bed                    =     All_Exon_V8
```
2. 실행 <br/>
만약 sample_config를 특정한 것을 넣고 싶다면 -c 옵션으로 절대경로로 넣어준다. <br/>
sureselect 라이브러리 키트 지원 목록 : All_Exon_V8,All_Exon_V5,All_Exon_V5_UTR,All_Exon_V6,All_Exon_V6_UTR,All_Exon_V7
```
python run_wes_mutect2_1.0.0.py -p /data05/project/jhshin/TBD220510-14975-WES-human-20220516
```

### <br/><br/><br/> 
## WES_mutect2_1.1.0.py (한 샘플씩 수동 분석)
![image](https://user-images.githubusercontent.com/62974484/170191979-221682ff-54c2-4b6d-8173-0b849bc20087.png)

### ex) (nohup, 1>, 2>, 마지막 &은 안 적어도 된다)
```
nohup python /TBI/People/tbi/jhshin/script/WES/wes_mutect2/WES_mutect2_1.1.0.py \
-p /data05/project/jhshin/TBD220510-14975-WES-human-20220516/result/08_gatk4_applybqsr/22017-Tumor/22017-Tumor.bam,/data05/project/jhshin/TBD220510-14975-WES-human-20220516/result/08_gatk4_applybqsr/22017-Normal/22017-Normal.bam \
-i All_Exon_V8 \
-o /data05/project/jhshin/TBD220510-14975-WES-human-20220516 \
1> /data05/project/jhshin/TBD220510-14975-WES-human-20220516/result/sh_log_file/09-1_gatk4_mutect2/22017-Tumor_paired/22017-Tumor_paired_cmd.txt \
2> /data05/project/jhshin/TBD220510-14975-WES-human-20220516/result/sh_log_file/09-1_gatk4_mutect2/22017-Tumor_paired/22017-Tumor_paired_cmd.txt \
&
```

### <br/><br/><br/> 

## 220528
### snpeff 기능 추가(WES pipeline snpeff)

### <br/><br/><br/> 

## 220530
### run_wes_mutect2_1.2.0.py
#### parallel 기능 추가. -n 옵션으로 한 번에 돌릴 샘플 수를 정해준다.

### <br/><br/><br/> 

## 220531
### mutect2_link_to_upload_dir.1.1.0.py
#### 고객 FTP 서버에 데이터 납품을 위해 테라젠 샘플 아이디 -> 고객 샘플 아이디로 변경, 복사
![image](https://user-images.githubusercontent.com/62974484/171125321-c7301cb5-3ce3-4a1b-a6c8-50265bc3599b.png)

### <br/><br/><br/> 

## 220929
### mutect2_link_to_upload_dir.1.1.1.py
#### 파일명 TNID -> sample name 으로 써지게 변경

### <br/><br/><br/> 

