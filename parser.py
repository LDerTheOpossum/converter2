
### Task1: Parsowanie argumentów przekazywanych przy uruchomieniu programu

#### Plik `main.py`
```python
import sys

def parse_args(args):
    if len(args) != 3:
        print("Usage: python main.py pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = args[1]
    output_file = args[2]

    return input_file, output_file

if __name__ == "__main__":
    input_file, output_file = parse_args(sys.argv)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

