wget https://ftp.ncbi.nlm.nih.gov/pub/pmc/PMC-ids.csv.gz
wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/disease_names
mkdir -p taxdump
cd taxdump
wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip
unzip taxdmp.zip
cd ..

# for newer version in the future check http://www.ensembl.org/info/genome/stable_ids/prefixes.html
wget http://Apr2020.archive.ensembl.org/info/genome/stable_ids/prefixes.html -O ensembl_prefixes.html

wget https://raw.githubusercontent.com/mikelove/awesome-multi-omics/master/README.md -O awesome-multi-omics-README.md
