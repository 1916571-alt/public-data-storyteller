import os
import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class GoogleSearchTool:
    def search(self, query):
        trends = ["Global EV Sales 2025", "AI Adoption in Finance", "Renewable Energy Growth", "Gaming Industry Revenue"]
        return random.choice(trends)

def run_mission():
    print("🤖 Agent Activated: Starting Weekly Trend Analysis...")
    
    # 1. Trend Discovery
    search_tool = GoogleSearchTool()
    topic = search_tool.search("latest global trends data")
    print(f"🔍 Trend Identified: {topic}")
    
    # 2. Directory Setup
    today = datetime.datetime.now().strftime("%Y%m%d")
    sanitized_topic = topic.replace(" ", "_")
    base_dir = f"projects/{today}_{sanitized_topic}"
    
    os.makedirs(f"{base_dir}/data", exist_ok=True)
    os.makedirs(f"{base_dir}/plots", exist_ok=True)
    os.makedirs(f"{base_dir}/reports", exist_ok=True)
    os.makedirs(f"{base_dir}/scripts", exist_ok=True)
    
    print(f"📂 Created Workspace: {base_dir}")

    # 3. Data Simulation
    print("⬇️  Fetching/Generating Data...")
    data = {
        'Category': ['Segment A', 'Segment B', 'Segment C', 'Segment D', 'Segment E'],
        'Value': [random.randint(20, 150) for _ in range(5)],
        'Growth_Rate': [random.uniform(-0.1, 0.3) for _ in range(5)]
    }
    df = pd.DataFrame(data)
    df.to_csv(f"{base_dir}/data/dataset.csv", index=False)

    # 4. Analysis & Visualization
    print("📊 Generating Visualizations...")
    sns.set_theme(style="whitegrid")
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Value', data=df, palette='viridis')
    plt.title(f"Market Analysis: {topic}")
    plt.savefig(f"{base_dir}/plots/trend_analysis.png")
    plt.close()

    # 5. Report Generation (Multi-Faceted)
    print("📝 Writing Insight Report...")
    
    top_segment = df.loc[df['Value'].idxmax()]['Category']
    
    report_content = f"""# 📊 {topic} (2025 Analysis)

## 📌 6W1H 분석 개요
- **Who (대상)**: Global Market Segments
- **When (시기)**: {datetime.datetime.now().strftime("%Y-%m-%d")}
- **Where (출처)**: Simulated Global Data Repository / Kaggle
- **What (주제)**: Market dynamics and growth patterns in **{topic}**
- **Why (목적)**: To identify high-growth opportunities and mitigate domain-specific risks.
- **How (방법)**: Automated Data Collection, Descriptive Statistics, Trend Visualization
- **Results (경로)**: 
  - Report: `{base_dir}/reports/insight_report.md`
  - Data: `{base_dir}/data/dataset.csv`

---

## 1. Executive Summary
> **"{topic} appears to be driven significantly by {top_segment}, suggesting a strong shift in market priorities toward efficiency."**

---

## 2. Analysis & Visualization
Significant variance was observed across categories.

![Trend Chart](../plots/trend_analysis.png)

---

## 3. Multi-perspective Insight (다각적 도메인 분석)

데이터 분석가로서 이 현상을 세 가지 관점에서 입체적으로 해석합니다.

### ① 🏢 비즈니스 관점 (Business Impact)
- **Cost & Efficiency**: `{top_segment}`의 성장은 자본 투자 수익률(ROI)이 해당 세그먼트에서 가장 높음을 시사합니다.
- **Strategic Move**: 경쟁사들보다 먼저 `{top_segment}` 관련 공급망을 선점하는 것이 핵심 성공 요인(KSF)입니다.

### ② 🧠 사회/심리적 관점 (Socio-psychological)
- **Consumer Behavior**: 소비자들이 이 트렌드를 선택하는 이유는 단순한 기능성이 아니라, '사회적 가치'나 '트렌드 편승 심리(FOMO)'가 작용했을 가능성이 큽니다.
- **Quality of Life**: 이 기술/트렌드의 확산은 장기적으로 사용자들의 생활 편의성을 `15%` 이상 증대시킬 잠재력이 있습니다.

### ③ ⚙️ 기술적 관점 (Technological)
- **Data Limitations**: 현재 데이터는 거시적 지표에 의존하고 있어, 미시적인 소비자 불만 사항(VOC)을 포착하지 못하는 한계가 있습니다.
- **AI Solution**: 향후 NLP(자연어 처리) 기술을 도입하여 소셜 미디어의 감성 분석을 병행한다면 예측 정확도를 높일 수 있습니다.

---

<p align="right">Authorized by Autonomous Agent</p>
"""
    with open(f"{base_dir}/reports/insight_report.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print("✅ Mission Complete!")

if __name__ == "__main__":
    run_mission()
