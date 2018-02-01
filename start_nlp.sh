#!/usr/bin/env bash

cd data/stanford-corenlp-full/

for file in `find . -name "*.jar"`;
do
    export CLASSPATH="$CLASSPATH:`realpath $file`";
done

nohup java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer &
# after this, you will find stanfordCoreNLP server at http://localhost:9000/
