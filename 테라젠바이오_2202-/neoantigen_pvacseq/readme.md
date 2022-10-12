## Neoantigen 분석
### WES 분석 이후 mutect2 paired, single 분석, RNA seq (cufflinks 데이터를 뽑기 위해) 진행한 데이터를 받고 neoantigen 분석을 위한 파이프라인
### docker 로 분석을 진행한다.

### <br/><br/><br/>

### optitype 실행 파이프라인 - script_optitype.sh
```
#!/bin/bash

path=${1}
sample=${2}

# 1. RUN1
#echo "RUN1 START"
conda activate py27
#date
#mkdir ${path}/optitype_tmp

# input bam file if analysis is paired : normal.fastq
#razers3 -i 95 -m 1 -dr 0 -o ${path}/optitype_tmp/${sample}_R1.fished.bam /TBI/People/tbi/jhshin/pipeline/optitype/hla_reference_dna.fasta ${path}/rawdata/${sample}_R1_001.fastq.gz && \
#razers3 -i 95 -m 1 -dr 0 -o ${path}/optitype_tmp/${sample}_R2.fished.bam /TBI/People/tbi/jhshin/pipeline/optitype/hla_reference_dna.fasta ${path}/rawdata/${sample}_R2_001.fastq.gz && \
#samtools bam2fq ${path}/optitype_tmp/${sample}_R1.fished.bam > ${path}/optitype_tmp/${sample}_R1.fished.fastq && \
#samtools bam2fq ${path}/optitype_tmp/${sample}_R2.fished.bam > ${path}/optitype_tmp/${sample}_R2.fished.fastq

#echo "RUN1 END."
#date

# 2. RUN2
echo "RUN2 START"
date
mkdir ${path}/result/101_optitype
echo ${path}/result/02_trimmomatic_filt/${sample}/${sample}_1.fastq
mkdir ${path}/result/101_optitype/${sample}

rm -rf ${path}/result/101_optitype/${sample}/*
python /TBI/People/tbi/jhshin/pipeline/optitype/OptiTypePipeline.py -i ${path}/result/02_trimmomatic_filt/${sample}/${sample}_1.fastq.gz ${path}/result/02_trimmomatic_filt/${sample}/${sample}_2.fastq.gz --dna --beta 0.009 --enumerate 1 --outdir ${path}/result/101_optitype/${sample}/ -p ${sample} --verbose

#conda deactivate
echo "RUN2 END."
date

```

### <br/><br/><br/>

### pvacseq 파이프라인 - my-script.sh
```
#!/bin/bash

path=${1}
sample=${2}
assem=${3} # [hg19, hg38]

#echo 'PARAM:' $0
RELATIVE_DIR=`dirname "$0"`
#echo 'Dir:' $RELATIVE_DIR
cd $RELATIVE_DIR
SHELL_PATH=`pwd -P`
#echo $SHELL_PATH

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/TBI/People/tbi/jhshin/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/TBI/People/tbi/jhshin/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


if [ ${assem} == "hg19" ] || [ ${assem} == "GRCh37" ]; then
    ref="/TBI/Share/BioPeople/shsong/BioResources/References/homo_sapiens/hg19/fasta/hg19.fa"
    assembly="GRCh37"
elif [ ${assem} == "hg38" ] || [ ${assem} == "GRCh38" ]; then
    ref="/TBI/Share/BioPeople/siyoo/BioResources/References/Homo_sapiens/H_sapiens_ENS_99/H_sapiens_ENS_99.genome.fa"
    assembly="GRCh38"
else
    # default
    ref="/TBI/Share/BioPeople/shsong/BioResources/References/homo_sapiens/hg19/fasta/hg19.fa"
    assembly="GRCh37"
fi

## 1. paired_mutect2_tumor_pass_filter
echo "1. paired_mutect2_tumor_pass_filter"
#conda activate fgbio
date

python ${SHELL_PATH}/mutect2_tumor_pass_filter.py ${path} ${sample}

#conda deactivate
echo "DONE."
## END::1

## 2. vep_annotation_paired   ##conda activate vep
echo "2. vep_annotation_paired"
#conda activate vep
date

input_vcf=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vcf
output_vcf=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vcf

pvacseq_cache_path="/TBI/Share/BioPeople/shsong/BioTools/vep/VEP_Cache/"
vep -q --input_file ${input_vcf} --output_file ${output_vcf} --format vcf --vcf --symbol --terms SO --tsl --hgvs --species homo_sapiens --assembly ${assembly} --offline --cache --dir_cache ${pvacseq_cache_path} --cache_version 99 --plugin Downstream --plugin Frameshift --plugin Wildtype 
# --fasta /TBI/Share/HumanTeam/BioResource/hg19/hg19.fa
#conda deactivate
echo "DONE."
## END::2

## 3. bamreadcount_paired
echo "3. bamreadcount_paired"
#conda activate fgbio
conda activate py27
date

sample_tmp=${sample%_paired}
bam_file=${path}/result/RNAseq-result/${sample_tmp}-R/Aligned.sortedByCoord.out.bam
snv_list=${path}/result/102_pvacseq_pre/${sample}/${sample}.snv.txt
indel_list=${path}/result/102_pvacseq_pre/${sample}/${sample}.indel.txt
tmp_snv_trna_depth=${path}/result/102_pvacseq_pre/${sample}/${sample}.trna.snv.depth.tmp.txt
tmp_indel_trna_depth=${path}/result/102_pvacseq_pre/${sample}/${sample}.trna.indel.depth.tmp.txt
bam-readcount -f ${ref} -l ${snv_list} -b 20 ${bam_file} >${tmp_snv_trna_depth}
bam-readcount -f ${ref} -l ${indel_list} -b 20 ${bam_file} >${tmp_indel_trna_depth}

python ${SHELL_PATH}/bamreadcount.py ${tmp_snv_trna_depth} ${tmp_indel_trna_depth}
echo "DONE."
## END::3

## 4. paired_run_vt
echo "4. paired_run_vt"
conda activate base
date

final_vcf=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vt.vcf
vt decompose -s ${output_vcf} -o ${final_vcf}
echo "DONE."
## END::4

## 5. run_add_coverage
echo "5. run_add_coverage"
date

snv_trna_depth=${path}/result/102_pvacseq_pre/${sample}/${sample}.trna.snv.depth.txt
tmp_vcf=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vt.pvacseq_input.tmp.vcf
indel_trna_depth=${path}/result/102_pvacseq_pre/${sample}/${sample}.trna.indel.depth.txt
output_vcf=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vt.pvacseq_input.tmp1.vcf
vcf_gx=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vt.pvacseq_input.exp.tmp.vcf
genes=${path}/result/RNAseq-result/${sample_tmp}-R/genes.fpkm_tracking
vcf_tx=${path}/result/102_pvacseq_pre/${sample}/${sample}.pass.vep.vt.pvacseq_input.vcf
isoforms=${path}/result/RNAseq-result/${sample_tmp}-R/isoforms.fpkm_tracking

vcf-readcount-annotator ${final_vcf} ${snv_trna_depth} RNA -s ${sample_tmp} -t snv -o ${tmp_vcf}
vcf-readcount-annotator ${tmp_vcf} ${indel_trna_depth} RNA -s ${sample_tmp} -t indel -o ${output_vcf}
vcf-expression-annotator -s ${sample_tmp} -o ${vcf_gx} ${output_vcf} ${genes} cufflinks gene
vcf-expression-annotator -s ${sample_tmp} -o ${vcf_tx} ${vcf_gx} ${isoforms} cufflinks transcript

echo "DONE."
## END::5

#conda deactivate
```

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
