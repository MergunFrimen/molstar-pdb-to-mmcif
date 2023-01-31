from Bio.PDB import PDBParser, MMCIFIO
from os import path

def convert(input_dir, output_dir, file):
    filename, _ = path.splitext(file)
    outfile = f"{filename}.biopython.cif"
    inpath = f"{input_dir}/{file}"
    outpath = f"{output_dir}/{outfile}"

    parser = PDBParser()
    structure = parser.get_structure("", inpath)
    io = MMCIFIO()
    io.set_structure(structure)
    io.save(outpath)