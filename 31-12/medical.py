import xml.etree.ElementTree as ET

def fetch_medical_issues(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    issues = [issue.text for issue in root.findall("Issue")]

    return sorted(issues)

medical_issues = fetch_medical_issues("medical_data.xml")

print("Medical Issues in Alphabitical Order:")
for issue in medical_issues:
        print(issue)