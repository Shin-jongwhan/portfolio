# HLA class I 분석을 하기 위해 optitype 이라는 tool을 사용한다.

## 설치 방법

### 1. 파이썬 환경 : 2.7

### 2. conda py27 환경 install 
```
$ conda create -n py27 python=2.7
```

### 3. optitype/wes_optitype.sh 에 conda init 자신의 경로에 맞게 부분 수정

```
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh" ]; then    # 자신의 conda 환경에 맞게 수정
        . "/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh"    # 자신의 conda 환경에 맞게 수정
    else
        export PATH="/TBI/People/tbi/jhshin/miniconda3/bin:$PATH"   # 자신의 conda 환경에 맞게 수정
    fi
fi
unset __conda_setup
```


### 4. wes_run_optitype.py 수정

```
# sh 경로 수정
sOptitype_sh = "/TBI/People/tbi/jhshin/pipeline/optitype/wes_optitype.sh"
```

## 5. 파이썬 모듈 에러시 설치

$ python -m pip install [모듈 이름]


## 실행

### 1. -p 옵션은 WES를 수행한 후 result, report가 나오는 상위 폴더를 넣으면 됩니다.

### 2. -c 옵션은 *.sample_config.txt (configmaker 호환)를 인식하며 따로 다른 config 파일이라면 절대 경로로 넣어줍니다.

### 3. -n 옵션으로 몇 개 샘플이 parallel 로 돌아갈지 결정합니다.
![image](https://user-images.githubusercontent.com/62974484/170603444-eb42e1fc-ca03-4ae7-9e2d-0b7f2384f086.png)


## 실행 결과

### result/101_optitype 폴더에 쌓입니다.
![image](https://user-images.githubusercontent.com/62974484/170603469-bf39ceab-5c90-4266-acdd-5b095301cb56.png)


### * 만약 fastq부터 시작하고 싶다면, 다음을 사용하여 fastq 필터링을 한 후 optitype을 실행한다.

### manual ex)
```
# 1. razers3 필터링
razers3 -i 95 -m 1 -dr 0 -o ${path}/optitype_tmp/${sample}_R1.fished.bam /TBI/People/tbi/jhshin/pipeline/optitype/hla_reference_dna.fasta ${path}/rawdata/${sample}_R1_001.fastq.gz

# 2. optitype 실행
python /TBI/People/tbi/jhshin/pipeline/optitype/OptiTypePipeline.py -i ${path}/result/02_trimmomatic_filt/${sample}/${sample}_1.fastq.gz ${path}/result/02_trimmomatic_filt/${sample}/${sample}_2.fastq.gz --dna --beta 0.009 --enumerate 1 --outdir ${path}/result/101_optitype/${sample}/ -p ${sample} --verboseㄱㄷ
```
