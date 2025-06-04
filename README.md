# 2025 부경대 자바개발자과정 MiniProject(1) - 편의점 재고확인 및 발주 시스템

---

## 🔍 프로젝트 개요

> **편의점 재고 및 발주 시스템**은 Oracle DB와 Python(PyQt5)을 기반으로,  
> 사용자 로그인부터 재고 관리, 발주, 판매까지 가능한 **GUI 기반 데스크탑 애플리케이션**입니다.

- 🗓 **진행 기간**: 2025.03.25 ~ 2025.03.31 (5일간)
- 👨‍👩‍👧‍👦 **팀 구성**: 박수민, 이동호, 박세찬, 이경주
- 🛠 **기술 스택**: Python, Oracle, PyQt5, pandas

---

## 💻 사용 기술

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=flat&logo=oracle&logoColor=white) ![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=flat&logo=qt&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

---

## ✅ 주요 기능 요약

### 👤 사용자 기능

- 로그인 / 로그아웃 (비밀번호 5회 실패 시 차단)
- 제품 재고 확인 (키워드 검색 포함)

### 📦 발주 및 판매

- 제품 발주 등록 / 수정 / 취소
- 판매 제품 배송일 기준 조회

### 📊 데이터 분석

- pandas 기반 판매량 분석 및 예측
- 차트 시각화로 발주/판매 전략 보조

---

<img src="./image/UI 디자인.jpg" width="800" alt="UI 디자인">

---

<img src="./image/설계도.jpg" width="800" alt="시스템 설계도">

---

## 🗓 개발일정

### 1일차

- 아이디어 구상 및 일정 체크
- 요구사항서 작성  
  <img src="./image/요구사항서.jpg" width="500" alt="요구사항서">
- DB 구조 설계  
  <img src="./image/DB 구조.jpg" width="500" alt="DB 명세">
- 요구사항 정의  
  (상세 내용은 기존과 동일)

### 2일차

- oracle 계정 생성과 Ui 디자인 설계
  - DBeaver, QT Designer 사용
  - [BRAND](./mini_project/DB/BRAND%20테이블%20생성%20쿼리.sql) / [CMEMBERLIST](./mini_project/DB/CMEMBERLIST%20테이블%20생성%20쿼리.sql.sql) / [DELIVERY](./mini_project/DB/DELIVERY%20테이블%20생성%20쿼리.sql) / [HISTORY](./mini_project/DB/HISTORY%20테이블%20생성%20쿼리.sql) / [TEAMPROD](./mini_project/DB/TEAMPROD%20테이블%20생성%20쿼리.sql)
- oracle과 Python 연동 및 이해

### 3일차

- DB 및 CRUD 기능 개발
- 활용 코드 개발
- 코딩 테스트

### 4일차

- 디버깅
- 코드 간소화 및 에러 해결

### 5일차

- 추가 테스트 및 마무리
- 코드 배포
- 발표용 PPT 제작

---

#### 📊 데이터 시각화

- Python pandas 사용하여 판매량 분석 차트 및 예측 차트 생성
- [분석/예측](./mini_project/mini_pro1/미니프로젝트.ipynb)

<img src="./image/데이터시각화.jpg" width="500" alt="데이터시각화">

#### 📈 판매 예측 시각화

<img src="./image/판매예측.jpg" width="500" alt="판매예측">

---

## 🌟 프로젝트 특징

- GUI 기반의 직관적 인터페이스 (PyQt5)
- Oracle 연동 통한 실시간 DB 조작
- 데이터 시각화를 통한 의사결정 보조

---

## 📌 앞으로의 확장 방향

### 🔄 사용자 기능 개선

- [ ] 판매 페이지에서 **제품 전체 삭제가 아닌 수량 지정 취소 기능** 추가
- [ ] 배송 상태에 따른 색상/필터 기능 개선

### 🛵 배달기사 전용 기능

- [ ] 배달기사 전용 창에서 **배송 완료 직접 체크 기능** 구현

### 🔔 자동화 및 알림 시스템

- [ ] 실시간 재고 부족 알림
- [ ] 판매량 기반 **자동 발주 추천 기능**
