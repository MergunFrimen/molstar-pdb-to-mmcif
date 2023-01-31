from os import path
from gemmi import read_pdb

def convert(input_dir, output_dir, file):
    filename, _ = path.splitext(file)
    outfile = f"{filename}.gemmi.cif"
    inpath = f"{input_dir}/{file}"
    outpath = f"{output_dir}/{outfile}"

    structure = read_pdb(inpath)
    structure.setup_entities()
    structure.assign_label_seq_id()
    block = structure.make_mmcif_block()
    block.write_file(outpath)