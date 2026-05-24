import xml.etree.ElementTree as ET

def read_data(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            data[key] = value
    return data

def create_xml(data, output_file):
    root = ET.Element("Vehicle")

    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = value
        

    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)

def main():
    data = read_data("data.txt")
    create_xml(data, "vehicle_data.xml")
    print("XML file created successfully.")

if __name__ == "__main__":
    main()

