# convert IDoft to Flakify/FlakeFlagger format

ultimate goal: csv file -> csv file
sample input: sample_input.csv
sample output: sample_output.csv

The IDoFT is from the dataset provided by Flakify.

## step1
Use script for batch downloading
python download_sha.py --csv_path `$your_csv_path$'

## step2
Use parse_data.py to generate the converted output.csv