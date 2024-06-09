import sys
import json

def parse_args(args):
    if len(args) != 3:
        print("Usage: python main.py pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = args[1]
    output_file = args[2]

    return input_file, output_file

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("JSON data loaded successfully")
        return data
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_args(sys.argv)
    if input_file.endswith('.json'):
        data = load_json(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
