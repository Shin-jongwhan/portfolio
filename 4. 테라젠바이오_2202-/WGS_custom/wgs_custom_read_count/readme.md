## 프로그램 설명
### 이 파이프라인은 fastq에서 forward와 reverse primer의 중간에 있는 insert를 찾아서 해당 read를 count하는 프로그램입니다.
### fastq R1, R2, merged (R1, R2에서 겹치는 부분을 찾아 merge하며, flash라는 툴을 사용) 3개에서 찾습니다.

### 실행 명령어
```
snakemake \
    --cores 10 \
    --snakefile /TBI/People/tbi/jhshin/pipeline/wgs_custom_read_count/workflow/Snakefile \
    --configfile /TBI/People/tbi/jhshin/pipeline/wgs_custom_read_count/config/config.yaml \
    --config 'script_home="/TBI/People/tbi/jhshin/pipeline/wgs_custom_read_count/workflow/scripts"'
```

### 결과 파일
![image](https://user-images.githubusercontent.com/62974484/174946470-0c376f34-5884-475c-a970-7739f5c5ed41.png)
### <br/>
![image](https://user-images.githubusercontent.com/62974484/174946495-dc4d2471-af62-46e6-bd24-4bcd4626a042.png)
### <br/>
![image](https://user-images.githubusercontent.com/62974484/174946552-99fc988b-4a00-4973-aedc-4ecf27ef6681.png)
### <br/>
![image](https://user-images.githubusercontent.com/62974484/174946594-716ce06b-d3fa-4d18-a04d-bed4249c6e30.png)

### <br/><br/><br/>

## 221007
### count 내림차순으로 정렬 후 length, ratio, rank 추가
![image](https://user-images.githubusercontent.com/62974484/194468260-e5d314c5-b20c-4949-aa3b-c3e11b602282.png)

### <br/><br/><br/>
