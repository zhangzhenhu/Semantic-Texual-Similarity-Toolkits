# coding: utf8

import stst
import sts_tools

# Define Model
# 用sklearn的GBRT作为回归模型
gb = stst.Classifier(stst.GradientBoostingRegression())
model = stst.Model('S1-gb', gb)

# avg = stst.Classifier(stst.AverageEnsemble())
# model = stst.Model('S1-avg', avg)

# 各种特征抽取
# Add features to the Model
# model.add(stst.WeightednGramOverlapFeature(type='lemma'))

'''several nGramOverlapFeatures'''
# 两个句子共同的'元素' 数量拟合成一个分数，作为特征
# 这里的元素 是 char word lemma
model.add(stst.nGramOverlapFeature(type='word'))
# lemma 原型词
model.add(stst.nGramOverlapFeature(type='lemma'))
model.add(stst.nCharGramOverlapFeature(stopwords=False))
model.add(stst.nCharGramOverlapFeature(stopwords=True))
model.add(stst.nGramOverlapBeforeStopwordsFeature(type='word'))
model.add(stst.nGramOverlapBeforeStopwordsFeature(type='lemma'))
# 带有idf权重
model.add(stst.WeightednGramOverlapFeature(type='word'))
model.add(stst.WeightednGramOverlapFeature(type='lemma'))

'''several BOWFeatures'''
# 先对每个句子用bow生成向量，然后计算这两个向量的各种距离，作为特征
# 目前有11个距离算法，也就是生成11维特征
model.add(stst.BOWFeature(stopwords=False))
model.add(stst.BOWFeature(stopwords=True))

'''several AlignmentFeatures'''
model.add(stst.AlignmentFeature())
model.add(stst.IdfAlignmentFeature())
model.add(stst.PosAlignmentFeature())





'''several WordEmbeddingFeatures'''
# 利用词向量生成句子向量，然后计算这两个句子向量的各种距离，作为特征
# 目前有11个距离算法，也就是生成11维特征
word2vec_file = 'data/GoogleNews-vectors-negative300.txt'
paragram_file = 'data/paragram_300_sl999.txt'
glove100_file = 'data/glove.6B.100d.txt'
glove300_file = 'data/glove.840B.300d.txt'

# from gensim.models.keyedvectors import KeyedVectors
# from gensim.models import word2vec
#
# model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
# model.save_word2vec_format('GoogleNews-vectors-negative300.txt', binary=False)

# model.add(stst.MinAvgMaxEmbeddingFeature('word2vec', 300, word2vec_file, 'word'))
# model.add(stst.MinAvgMaxEmbeddingFeature('paragram', 300, paragram_file, 'word'))
model.add(stst.MinAvgMaxEmbeddingFeature('glove100', 100, glove100_file, 'word'))
model.add(stst.MinAvgMaxEmbeddingFeature('glove300', 300, glove300_file, 'word'))
#
# model.add(stst.MinAvgMaxEmbeddingFeature('word2vec', 300, word2vec_file, 'lemma'))
# model.add(stst.MinAvgMaxEmbeddingFeature('paragram', 300, paragram_file, 'lemma'))
model.add(stst.MinAvgMaxEmbeddingFeature('glove100', 100, glove100_file, 'lemma'))
model.add(stst.MinAvgMaxEmbeddingFeature('glove300', 300, glove300_file, 'lemma'))

'''several DependencyFeatures'''
model.add(stst.DependencyGramFeature(convey='count'))
model.add(stst.DependencyGramFeature(convey='idf'))
model.add(stst.DependencyRelationFeature(convey='count'))
model.add(stst.DependencyRelationFeature(convey='idf'))

model.add(stst.POSLemmaMatchFeature(stopwords=True))
model.add(stst.POSLemmaMatchFeature(stopwords=False))
# model.add(stst.POSNounEmbeddingFeature('word2vec', 300, word2vec_file))
model.add(stst.POSNounEditFeature())
# 有异常
# model.add(stst.POSTreeKernelFeature())
# 有异常
# model.add(stst.Doc2VecGlobalFeature())

'''several NegativeFeature'''
model.add(stst.NegativeFeature())
# 有异常
# model.add(stst.AsiyaMTFeature())

model.add(stst.SequenceFeature())
model.add(stst.SentenceFeature())
# 有异常
#model.add(stst.ShortSentenceFeature())

# sts_tools.feature_importance(model)
sts_tools.train_sts(model)
# sts_tools.dev_sts(model)
sts_tools.test_sts(model)

# sts_tools.hill_climbing(model)
# sts_tools.hill_climbing(model, [0])
