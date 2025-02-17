import json
import random
import string

def generate_string(offset):
    length = random.randint(1, offset)
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return rand_str.ljust(offset)[:offset]

def generate(outfile = "fixed.txt", n=15):
    
    with open("spec.json", "r") as file:
        spec = json.load(file)
    
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

if __name__ == "__main__":
    generate()