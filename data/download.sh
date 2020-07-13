wget https://ftp.ncbi.nlm.nih.gov/pub/pmc/PMC-ids.csv.gz
wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/disease_names
mkdir -p taxdump
cd taxdump
wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip
unzip taxdmp.zip
cd ..

# 812 MB for spacy 2.0, the most accurate model (https://spacy.io/usage/facts-figures#benchmarks-models-english)
python -m spacy download en_core_web_lg
