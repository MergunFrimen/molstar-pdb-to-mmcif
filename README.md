# Molstar PDB to mmCIF conversion

Testing out different Python packages for converting PDB files to mmCIF in order to determine which one is the most suitable for Molstar.

> Short answer: so far none

## How to run

Add the PDB files to the `./input` folder and run the script.

```bash
# Install dependencies
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 

# Run the script
# by default it will convert all files in the ./input folder
$ python src/main.py 
# or you can specify the files you want to convert
$ python src/main.py 3BJ1.pdb ...
```

## How to view in Molstar

Go to the [Molstar viewer](https://molstar.org/viewer) and upload all `./output/*.cif` files.