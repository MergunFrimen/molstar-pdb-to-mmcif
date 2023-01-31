import os
import gemmi_convert as gemmi
import biopython_convert as biopython

root = os.path.dirname(os.path.abspath(__file__))
input_dir = f"{root}/../input"
output_dir = f"{root}/../output"

for file in os.listdir(input_dir):
    print(f"Converting {file}...")
    biopython.convert(input_dir, output_dir, file)
    gemmi.convert(input_dir, output_dir, file)