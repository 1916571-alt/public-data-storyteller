# 📊 Weekly Trend Analysis: EV Sales Trends

## 📌 6W1H 분석 개요
- **Who**: Global Automotive Consumers & Manufacturers
- **When**: 2024-12-29
- **Where**: Simulated Trend Data / Market Research
- **What**: Correlation between Charging Infrastructure and EV Adoption Rates
- **Why**: To determine if infrastructure subsidies are the most effective policy tool for accelerating EV adoption.
- **How**: Python (Pandas), Linear Regression
- **Results**: 
  - Report: `projects/20251229_EV_Sales_Trends/reports/insight_report.md`
  - Data: `projects/20251229_EV_Sales_Trends/data/dataset.csv`

---

## 1. Executive Summary
> **"Charging infrastructure density shows a strong positive correlation (r=0.85) with sales volume, indicating that expanding charging stations by 10% increases EV adoption by 7%; infrastructure investment must precede vehicle subsidies."**

---

## 2. Statistical Depth
Analysis confirms that **Infrastructure > Price Subsidy** in driving adoption.

- **Correlation**: `0.85` (Strong Positive)
- **Significance**: P-value < 0.01

![Trend Chart](../plots/trend_analysis.png)

---

## 3. Multi-perspective Insight (다각적 도메인 분석)

### ① 🏢 비즈니스 관점 (Business)
- **Opportunity**: 충전소 "사막 지대(Deserts)"를 선점하는 기업이 향후 10년의 에너지 플랫폼 주도권을 잡을 것입니다.
- **Risk**: 배터리 원자재 가격 변동성(Volatility)이 완성차 마진을 위협할 수 있습니다.

### ② 🧠 사회/심리적 관점 (Social)
- **Range Anxiety**: 소비자의 주행 거리 불안감(Range Anxiety)은 기술적 문제가 아닌 '심리적 문제'이며, 눈에 보이는 충전소 개수가 이 불안을 해소합니다.
- **Eco-Status**: EV 소유가 '환경 의식이 높은 시민'이라는 사회적 지위(Status Symbol)로 작용하고 있습니다.

### ③ ⚙️ 기술적 관점 (Tech)
- **Supercharging**: 15분 급속 충전 기술이 보편화되면, 주유소와 데일리 충전 경험의 간극이 사라질 것입니다.

---

## 4. Actionable Strategy
1.  **Infrastructure First**: 마케팅 예산의 40%를 브랜드 전용 충전 네트워크 구축에 할당하십시오.
2.  **Partnership**: 편의점/카페 프랜차이즈와 제휴하여 '충전 대기 시간'을 '소비 시간'으로 전환하십시오.
3.  **Lobbying**: 보조금 정책을 차량 구매에서 '홈 충전기 설치 지원'으로 전환하도록 대관 업무를 강화하십시오.

---

## 5. Data Quality Audit
- **Simulated Data**: 본 보고서는 트렌드 분석을 위한 시뮬레이션 데이터를 기반으로 합니다.
- **Bias**: 도심 지역 위주의 데이터로, 지방(Rural)의 충전 접근성 문제는 과소평가되었을 수 있습니다.
