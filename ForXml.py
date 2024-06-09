import xmltodict

def load_xml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = xmltodict.parse(file.read())
        except Exception as e:
            print(f"Error decoding XML from {file_path}: {e}")
            sys.exit(1)
    return data
