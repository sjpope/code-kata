import json
import random
import string
import csv

def generate_string(offset):
    length = random.randint(1, offset)
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return rand_str.ljust(offset)[:offset]

def generate(spec, outfile = "fixed.txt", n=15):
    
    names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    
    with open(outfile, "w", encoding=spec["FixedWidthEncoding"]) as data:

        # Evaluate Header
        if spec["IncludeHeader"].lower() == "true":
            header = ""
            for name, offset in zip(names, offsets):
                header += name.ljust(offset)[:offset]
            data.write(header + "\n")
        

        for rec in range(1, n + 1):
            line = ""
            
            for offset in offsets:
                value = generate_string(offset)
                line += value
                
            data.write(line + "\n")
    
    print(f"Prob 1 File Generation Complete")

def parse(spec):
    
    names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    
    # Parse fixed width to generate delimited file
    with open("fixed.txt", "r") as infile, open("parsed.csv", "w", encoding=spec["DelimitedEncoding"]) as outfile:
        
        writer = csv.DictWriter(outfile, names)
        
        for line in infile:
            i = 0
            row = {}
            
            for name, offset in zip(names, offsets):
                row[name] = line[i:offset].rstrip()
                i += offset
            
            # map folumn nam,es to values for row
            
            writer.writerow(row)
        
             
    print('Prob 1 Complete: parsed.csv generated successfully')
        
        


if __name__ == "__main__":
    
    with open("spec.json", "r") as file:
        spec = json.load(file)
    
    generate(spec)
    parse(spec)