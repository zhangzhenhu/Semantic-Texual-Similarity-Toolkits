#!/usr/bin/env bash
mkdir data
cd data

#wget -O 'glove.840B.300d.zip'  'http://nlp.stanford.edu/data/glove.840B.300d.zip'
#wget -O 'glove.6B.zip' 'http://nlp.stanford.edu/data/glove.6B.zip'
#wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

# download the STSBenchmark Dataset
wget http://ixa2.si.ehu.es/stswiki/images/4/48/Stsbenchmark.tar.gz
tar zxvf Stsbenchmark.tar.gz
rm -rf Stsbenchmark.tar.gz

# download the stanford CoreNLP 3.6.0
#wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
#unzip stanford-corenlp-full-2015-12-09.zip
wegt -O 'stanford-corenlp-full.zip' 'http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip'
unzip stanford-corenlp-full.zip
cd stanford-corenlp-full/
wget -O 'stanford-chinese-corenlp-models.jar' 'http://nlp.stanford.edu/software/stanford-chinese-corenlp-2017-06-09-models.jar'

# lanch the stanford CoreNLP
#cd stanford-corenlp-full-2015-12-09/
#java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
# after this, you will find stanfordCoreNLP server at http://localhost:9000/

# install requirements
cd ..
pip install -r requirements.txt

# install nltk stopwords
python -m nltk.downloader stopwords