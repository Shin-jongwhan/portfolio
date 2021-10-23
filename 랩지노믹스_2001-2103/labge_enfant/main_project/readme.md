# 프로젝트 소개
## 1. decision call (200122_EnfantGuard_analyser.ver3.py.decision)
### 설명
#### 서비스 분석 마지막 단계에서 실행되는 스크립트로 decision call이라고 부릅니다.
#### CNV를 분석해주는 CopywriteR이 실행된 후에 1~22번, X, Y 염색체의 각 window (50000bp)를 분석합니다.
#### 다양한 cutoff를 거쳐 앙팡가드에서 분석하는 질병 목록에 해당하는 이수성이 있는지 분석하여 최종 output을 도출합니다.
### 진행했던 업무
#### 1. check_call 기능 업데이트
#### CNV 관련하여 decision call에서 잡히지 않는 segment들이 발생합니다.
#### significant한 변이는 아닙니다. 다만 확인은 필요한 segment들입니다.
#### 확인이 필요한 segment만 따로 분류하여 최종 output에 check call이라는 데이터가 나오도록 하였습니다.
#### 2. cutoff 조정
#### 앙팡가드 서비스 기간 동안 쌓여온 데이터를 기반으로 하여 여러 번의 테스트를 거쳐 양성 / 음성 분석의 기준을 조정하였습니다.
####
## 2. seg_analysis_jh_210127.py
### 설명
#### decision call까지는 리눅스 상에서 최종 output을 도출하기 위한 분석 시스템입니다.
#### decision call이 끝난 후 변이 위치, 관련 질병, 주요 유전자 등을 파악하는 여러 가지 '검사 업무'가 있습니다.
#### 검사 업무를 자동화한 프로그램입니다.
#### statistics_seg_analysis.py는 양성 / 음성 파악을 실제로 잘 분석했는지 통계를 냅니다(프로그램의 신뢰성을 위한 재분석).
### 진행했던 업무
#### 모든 코드 작성하였습니다.
