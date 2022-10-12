## snpeff 추가 annotation 분석

### <br/><br/><br/>

## 220616
### wes_snpeff_add_db.1.0.0.py
#### DB vcf를 주어 추가 snpeff annotation 분석을 할 수 있다. 현재는 KRGDB만 지원하며 추후를 위해 multiple DB annotation 기능을 넣어두고 나중에 개발하려고.. 일단 여러 개 DB를 넣으면 에러 메세지와 함께 sys.exit()으로 빠져나오게 만들었다.
1. 기본 snpeff annotation 쉘 스크립트를 읽어서 저장한다.
2. 인덱스로 들어가야할 인풋들을 차례대로 넣는다.
3. err, std, sh 스크립트를 저장하고 annotation 명령어들을 실행한다.
#### 결과 파일의 넘버는 snpeff*.vcf 파일 개수에 따라 정해지며 각 샘플 폴더에 결과 파일이 생성된다.
![image](https://user-images.githubusercontent.com/62974484/174029797-1f56abb8-81d7-4447-8344-c250f360a93c.png)
### <br/> 

#### sh 폴더에 sh 스크립트, std, err 저장
![image](https://user-images.githubusercontent.com/62974484/174029734-3af276b9-c53a-4f29-b1e0-950704caa9b9.png)

### <br/><br/><br/>

### snpeff_addon_link_to_upload_dir.1.0.0.py
#### upload dir에 링크를 걸어준다. snpeff annot 결과는 과도한 용량 차지로 cp를 안 쓰고 ln -s (심볼릭 링크)로 대체하였다.
#### 샘플명은 TNID (내부 아이디)에서 고객 샘플 명으로 전환하여 업로드한다.
![image](https://user-images.githubusercontent.com/62974484/174034080-bffd8a88-ec32-459f-9675-5390b971f2ac.png)

### <br/><br/><br/>
