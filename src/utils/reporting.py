import json
from datetime import datetime

def save_json_report(results, filename='report.json'):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

def save_html_report(results, filename='report.html'):
    html = '<html><head><title>Accessibility Test Report</title></head><body>'
    html += f'<h1>Accessibility Test Report - {datetime.now()}</h1>'
    html += '<ul>'
    for result in results:
        html += f"<li>{result['test']}: {'PASS' if result['passed'] else 'FAIL'} - {result.get('details', '')}</li>"
    html += '</ul></body></html>'
    with open(filename, 'w') as f:
        f.write(html) 