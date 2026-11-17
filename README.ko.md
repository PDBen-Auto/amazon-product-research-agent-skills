# Amazon 상품 조사 스위트

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

사용자가 명시한 출력 언어를 따르고, 지정이 없으면 요청 언어를 따릅니다. 명령, 스킬 ID, JSON 키, 열거값, 단위와 원문 인용은 유지합니다. 번역과 원문을 구분하고 언어로 국가, 통화, 관할을 추정하지 않습니다. 전체 명세의 관련 자료를 읽고 기존 검증과 권한 조건을 적용합니다.

## 설치와 사용

저장소를 내려받거나 복제한 뒤 아래 스킬 디렉터리를 기존 references, scripts, assets 등과 함께 호스트의 스킬 디렉터리에 복사합니다. 이름과 SKILL.md는 유지합니다. 문서 언어만 바꾸는 경우 재설치할 필요가 없습니다. 설치 명령은 선택지이며 설치 또는 활성화 완료를 뜻하지 않습니다.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## 근거 기반 상품 차별화

`amazon-product-differentiation-rd`

고객 문제를 제품 원리, 측정 가능한 사양, 저비용 실험과 사전 중단 기준으로 바꿉니다.

스킬 디렉터리: `skills/amazon-product-differentiation-rd`

**구현 근거와 의존성**

추적 가능한 고객 근거, 기준 제품과 핵심 사용자 과제가 필요합니다. 타당성에는 사업 제약, 검증에는 시제품·특허/공급 검토가 조건부로 필요합니다.

**입력**

필수 리뷰/인터뷰/반품 근거, 기준 이미지·사양, 사용자 과제. 조건부 가격·원가·크기·재료·호환·MOQ·규제. 제안한 성공 임계값은 가정으로 표시합니다.

**출력**

근거-원리 대응표, 개념 비교, 수치 사양, 실험 계획, 미해결 위험을 Markdown/JSON/표로 출력합니다. 각 추천에는 근거·원리·요구·시험이 필요합니다.

[실행 절차 · 제약과 중단 조건 · 요청 예시](skills/amazon-product-differentiation-rd/references/i18n/ko.md)

> 다음 스킬을 사용하세요: `$amazon-product-differentiation-rd` — 미끄러지는 거치대라면 자력뿐 아니라 유지·해제 힘, 휴대전화 무게, 진동·온도 시험을 정의합니다. 한국어로 답하고 근거, 미확인 사항과 작업 권한을 유지하세요.

## Amazon 상품 조사 스위트

`amazon-product-research-suite`

두 개 이상의 근거 영역을 다루는 결정을 최소한의 전문 Skill로 연결합니다. 좁은 단일 과제는 해당 전문 절차를 사용합니다.

스킬 디렉터리: `skills/amazon-product-research-suite`

**구현 근거와 의존성**

Agent Skills 호스트와 선택한 전문 스킬이 필요합니다. 제공 자료로 오프라인 작업이 가능하며 실시간 수집은 네트워크·허가가 필요합니다. Python 3.10+는 보조 도구 이용 시 필요합니다.

**입력**

필수 상품 결정; 조건부 ASIN/제품, 시장, 관할, 기간, 작업 권한. 선택 CSV/JSON/XLSX/PDF/이미지, 견적, 사업 제약. 없는 사실은 공백으로 남깁니다.

**출력**

route-plan.json, 공유 근거 계약, 스킬·순서, 부족 입력과 산출 위치. 라우팅 자체는 설치나 서비스 접촉을 하지 않습니다.

[실행 절차 · 제약과 중단 조건 · 요청 예시](skills/amazon-product-research-suite/references/i18n/ko.md)

> 다음 스킬을 사용하세요: `$amazon-product-research-suite` — 차량용 거치대의 시장·리뷰·차별화·공급·경제성을 연결하고 외관 자료가 있으면 디자인권 예비 조사를 추가합니다. 한국어로 답하고 근거, 미확인 사항과 작업 권한을 유지하세요.

## 공급업체 타당성과 샘플 기준

`amazon-supplier-feasibility`

RFQ, 동일 조건 견적 비교, 근거 기반 샘플 합격 기준을 준비합니다. 기본적으로 공장 연락·주문은 하지 않습니다.

스킬 디렉터리: `skills/amazon-supplier-feasibility`

**구현 근거와 의존성**

제품 사양이 필수이며 비교에는 날짜가 있는 비교 가능 견적이 필요합니다. 규제·샘플 접근·통신 권한은 조건부이고 공장 연락은 별도 허가가 필요합니다.

**입력**

단위·공차가 있는 사양/도면, 주문·수요 가정. 조건부 통화·Incoterm·금형 예산·결제 조건. 선택 PDF/XLSX/CSV 견적과 품질 자료.

**출력**

RFQ, 원가·납기 비교, 제조 위험 기록, 샘플 계획. 상태는 READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL, INSUFFICIENT_EVIDENCE.

[실행 절차 · 제약과 중단 조건 · 요청 예시](skills/amazon-supplier-feasibility/references/i18n/ko.md)

> 다음 스킬을 사용하세요: `$amazon-supplier-feasibility` — 거치대 견적 전 자석 등급, 접착제, 토크, 온도 시험, 금형 소유권, 포장을 일치시킵니다. 한국어로 답하고 근거, 미확인 사항과 작업 권한을 유지하세요.

## 단위 경제성과 첫 주문 현금

`amazon-unit-economics-cashflow`

명시적 가정으로 공헌이익, 광고 손익분기점, 반품 민감도와 초기 현금을 계산합니다.

스킬 디렉터리: `skills/amazon-unit-economics-cashflow`

**구현 근거와 의존성**

수치 가격·원가와 근거가 있는 시장 수수료가 필요합니다. 표준 라이브러리 계산기는 Python 3.10+이며 현금 분석에는 주문량·결제 시점이 필요합니다.

**입력**

JSON: 판매가, 판매·물류 수수료, 도착 원가, 반품률·손실, 광고 ACOS, 기타 변동비. 현금에는 수량·금형·준비비·계약금·버퍼. 단일 통화, 비율0~1.

**출력**

이익·이익률, 손익분기 ACOS, 반품 손실, 첫 주문 현금과 시나리오의 JSON/지정 파일. 오류 입력은 비정상 종료이며 네트워크·계정 변경은 없습니다.

[실행 절차 · 제약과 중단 조건 · 요청 예시](skills/amazon-unit-economics-cashflow/references/i18n/ko.md)

> 다음 스킬을 사용하세요: `$amazon-unit-economics-cashflow` — 사용자 거치대 가격·비용으로 반품률과 ACOS를 비교하고 공헌이익과 첫 주문 현금을 함께 제시합니다. 한국어로 답하고 근거, 미확인 사항과 작업 권한을 유지하세요.

## 언어 지원과 검증

이 문서는 목적, 전제, 입출력, 절차, 예시와 제약을 다루는 한국어 운영 가이드이며 모든 참고 문서의 문장별 번역은 아닙니다. 상세 기술 자료, 과거 사례, 스크립트 오류, 예제 화면과 이미지는 원래 언어를 유지합니다. 요청 시 해당 언어로 설명할 수 있습니다. 구조, 링크와 핵심 제약을 확인했으나 각 언어 원어민 교정은 수행하지 않았습니다.

전달 전에 입력, 근거, 결측값, 출력 파일과 원래 완료 기준을 대조합니다. 실행하지 않은 단계는 미검증으로 표시하며 스크립트의 정상 종료를 업무 검증 성공으로 취급하지 않습니다.
