#!/usr/bin/env bash

cd data/stanford-corenlp-full-2015-12-09/
nohup java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer &
# after this, you will find stanfordCoreNLP server at http://localhost:9000/
