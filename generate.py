import json
import random
import string
import csv

def generate_string(offset):
    length = random.randint(1, offset)
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return rand_str.ljust(offset)[:offset]

def generate(spec, outfile = "fixed.txt", n=5):
    names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    
    with open(outfile, "w", encoding=spec["FixedWidthEncoding"]) as data:
        # Evaluate Header
        if spec["IncludeHeader"].lower() == "true":
            header = ""
            for name, offset in zip(names, offsets):
                header += name.ljust(offset)[:offset]
            data.write(header + "\n")
        

        for _ in range(n):
            line = "".join(generate_string(offset) for offset in offsets)
            data.write(line + "\n")
    
    print(f"\n-- Prob 1 File Generation Complete. --\n\n")

def parse(spec, source="fixed.txt", destination="parsed.csv"):
    names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    
    # Parse fixed width to generate delimited file
    with open(source, "r") as infile, open(destination, "w", encoding=spec["DelimitedEncoding"]) as outfile:
        
        writer = csv.DictWriter(outfile, names)
        
        for line in infile:
            i = 0
            row = {}
            
            for name, offset in zip(names, offsets):
                row[name] = line[i:i+offset].rstrip()
                i += offset
            
            # map folumn nam,es to values for row
            
            writer.writerow(row)
        
             
    print(f'-- Prob 1 Complete: {destination} generated successfully --\n\n')
        
def read(filename, encoding_type):
    with open(filename, "r", encoding=encoding_type) as f:
        print(f.read())

if __name__ == "__main__":
    try:
        with open("spec.json", "r") as file:
            spec = json.load(file)
    
        generate(spec, "fixed.txt")
        read("fixed.txt", encoding_type=spec["FixedWidthEncoding"])
        
        parse(spec, "fixed.txt" , "parsed.csv")
        read("parsed.csv", encoding_type=spec["DelimitedEncoding"])
        
    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)
    