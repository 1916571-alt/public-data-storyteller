import os
import re
import pandas as pd

def parse_report_for_dashboard(report_path):
    """
    Parses a markdown report to extract metadata for the dashboard table.
    """
    if not os.path.exists(report_path):
        return None
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Topic (from Title)
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    topic = title_match.group(1).strip() if title_match else "Untitled Analysis"
    
    # Extract Key Insight (Business/Social)
    # Looking for the blockquote in Executive Summary or specific key insight text
    # Prioritizing the blockquote format: > **"Insight"**
    insight_match = re.search(r'>\s*\*\*"(.*?)"\*\*', content)
    
    if insight_match:
        insight = insight_match.group(1).strip()
    else:
        # Fallback: Try to find a bullet point under "Key Insights"
        fallback_match = re.search(r'\d\.\s*\*\*(.*?)\*\*:', content)
        insight = fallback_match.group(1).strip() if fallback_match else "본문 참조"

    return {
        "topic": topic,
        "insight": insight
    }

def update_dashboard():
    projects_dir = "projects"
    dashboard_data = []
    
    if os.path.exists(projects_dir):
        # Sort folders by date (newest first)
        for folder_name in sorted(os.listdir(projects_dir), reverse=True):
            project_path = os.path.join(projects_dir, folder_name)
            if not os.path.isdir(project_path):
                continue
            
            # Parse Date from folder name
            date_match = re.match(r'^(\d{8})_', folder_name)
            if not date_match:
                continue
                
            date_str = date_match.group(1)
            date_formatted = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
            
            # Find report
            report_path = os.path.join(project_path, "reports", "insight_report.md")
            metadata = parse_report_for_dashboard(report_path)
            
            if metadata:
                # Relative link for GitHub
                report_link = f"projects/{folder_name}/reports/insight_report.md"
                
                dashboard_data.append({
                    "분석 날짜": date_formatted,
                    "도메인/주제": metadata['topic'],
                    "핵심 인사이트 (비즈니스+사회적 관점)": metadata['insight'],
                    "리포트 바로가기": f"[👉 읽기]({report_link})"
                })
    
    if not dashboard_data:
        print("No reports found to update dashboard.")
        return

    # Create Markdown Table
    df = pd.DataFrame(dashboard_data)
    markdown_table = df.to_markdown(index=False)
    
    # Update README
    readme_path = "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = "<!-- DASHBOARD_START -->"
    end_marker = "<!-- DASHBOARD_END -->"
    
    new_section = f"{start_marker}\n\n## 📚 Analysis Archive (프로젝트 대시보드)\n\n" \
                  f"에이전트가 수행한 역대 분석 프로젝트의 요약입니다.\n\n{markdown_table}\n\n{end_marker}"
    
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_section, content)
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README Dashboard updated successfully.")
    else:
        print("❌ Dashboard markers not found in README.md")

if __name__ == "__main__":
    update_dashboard()
