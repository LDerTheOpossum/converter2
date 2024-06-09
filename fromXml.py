import xmltodict

def save_xml(data, file_path):
    with open(file_path, 'w') as file:
        xmltodict.unparse(data, output=file, pretty=True)
