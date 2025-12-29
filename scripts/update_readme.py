import os
import re
import pandas as pd

def parse_report(report_path):
    """
    Parses a markdown report to extract metadata for the dashboard.
    """
    if not os.path.exists(report_path):
        return None
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Topic (from Title)
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    topic = title_match.group(1).strip() if title_match else "Untitled Analysis"
    
    # Extract Data Source (from 6W1H section)
    # Looking for "- **Where (출처)**: ..."
    source_match = re.search(r'-\s*\*\*Where \(출처\)\*\*:\s*(.+)', content)
    source = source_match.group(1).strip() if source_match else "Unknown"
    
    # Extract Key Insight (Looking for the blockquote in Executive Summary)
    # > **"Insight text"**
    insight_match = re.search(r'>\s*\*\*"(.*?)"\*\*', content)
    if insight_match:
        insight = insight_match.group(1).strip()
    else:
        # Fallback: Try to find the first bullet in Key Insights
        fallback_match = re.search(r'1\.\s*\*\*(.*?)\*\*:', content)
        insight = fallback_match.group(1).strip() if fallback_match else "See Report for details"
        
    return {
        "topic": topic,
        "source": source,
        "insight": insight
    }

def update_readme():
    projects_dir = "projects"
    archive_data = []
    
    # Scan projects directory
    if os.path.exists(projects_dir):
        for folder_name in sorted(os.listdir(projects_dir), reverse=True):
            project_path = os.path.join(projects_dir, folder_name)
            if not os.path.isdir(project_path):
                continue
            
            # Extract date from folder name (YYYYMMDD_Topic)
            date_match = re.match(r'^(\d{8})_', folder_name)
            date_str = date_match.group(1) if date_match else "Unknown"
            if date_str != "Unknown":
                date_formatted = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
            else:
                date_formatted = "Unknown"

            report_path = os.path.join(project_path, "reports", "insight_report.md")
            metadata = parse_report(report_path)
            
            if metadata:
                # Create relative link (fixing backward slashes for markdown)
                relative_link = f"projects/{folder_name}/reports/insight_report.md"
                
                archive_data.append({
                    "날짜": date_formatted,
                    "분석 주제": metadata['topic'],
                    "데이터 소스": metadata['source'],
                    "핵심 인사이트 (One-Sentence)": metadata['insight'],
                    "리포트 연결": f"[바로가기]({relative_link})"
                })
    
    # Create DataFrame and Markdown Table
    if not archive_data:
        print("No analysis reports found.")
        return

    df = pd.DataFrame(archive_data)
    markdown_table = df.to_markdown(index=False)
    
    # Read existing README
    readme_path = "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Define markers
    start_marker = "<!-- ARCHIVE_START -->"
    end_marker = "<!-- ARCHIVE_END -->"
    
    # Construct new section
    new_section = f"{start_marker}\n\n## 📚 Analysis Archive (데이터 분석 기록)\n\n" \
                  f"에이전트가 수행한 역대 분석 프로젝트의 요약입니다.\n\n{markdown_table}\n\n{end_marker}"
    
    # Replace or Append
    if start_marker in readme_content and end_marker in readme_content:
        # Regex update
        pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
        new_readme_content = pattern.sub(new_section, readme_content)
    else:
        # Append before the footer
        new_readme_content = readme_content.replace("---", f"---\n\n{new_section}", 1) 
        # If no --- found, just append
        if new_readme_content == readme_content:
             new_readme_content += f"\n\n{new_section}"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
    
    print("✅ README.md updated with Analysis Archive.")

if __name__ == "__main__":
    update_readme()
