import db
import nltk

s1 = "CUSTOM 3 Grams of Premium FISHSCALE Cocaine HQ"


words = nltk.word_tokenize(s1)

words2 = nltk.regexp_tokenize(s1, r'(?u)\d+(?:\.\,\d+)?|\w+')


nltk.pos_tag(words)
pos = nltk.pos_tag(words2)

chunkGram = r"""Chunk:{<CD><NNP>}"""
chunkParser = nltk.RegexParser(chunkGram)
chunked = chunkParser.parse()
