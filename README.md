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
$ python src/main.py
```