import csv
from tweet_parser import Tweet

"""
This module parses CrowdFlower's dataset.
[URL: https://www.crowdflower.com/data-for-everyone (under 'Disasters on social media')]
"""

DATASET_PATH =      'dataset/socialmedia-disaster-tweets-DFE-extended.csv'
POS_TAGGING_PATH =  'dataset/socialmedia-disaster-tweets-DFE-POS-Tagging.txt'
NER_TAGGING_PATH =  'dataset/socialmedia-disaster-tweets-DFE-NER-tags.txt'


class Dataset(object):
    """
    This object contains all the data on our tweets.
    """
    def __init__(self, dataset_path=DATASET_PATH, pos_tagging_path=POS_TAGGING_PATH, ner_tagging_path=NER_TAGGING_PATH):
        self.entries = []

        pos_of_tweets = read_conll_pos_file(pos_tagging_path)
        ne_of_tweets = read_ner_tags_file(ner_tagging_path)

        t = 0
        with open(dataset_path, 'rb') as csvfile:
            for row in csv.DictReader(csvfile):

                POS_tags = ' '.join([tup[1] for tup in pos_of_tweets[t]])
                NEs = ne_of_tweets[t] # list of named-entities in tweet

                # Handle only tweets with confidence > 0.9
                if float(row['choose_one:confidence']) > 0.9:
                    if 'relevance' in row:
                        relevance = row['relevance']
                        relevance_metadata = row['relevance_metadata']
                    else:
                        relevance = 0
                        relevance_metadata = ''
                    self.entries.append(Tweet(row, POS_tags, NEs, relevance=relevance,
                                              relevance_metadata=relevance_metadata))

                t += 1


def read_conll_pos_file(path):
    """
    Takes a path to a file and returns a list of word/tag pairs
    (This code is adopted from the exercises)
    """
    sents = []
    with open(path, 'r') as f:
        curr = []
        for line in f:
            line = line.strip()
            if line == "":
                sents.append(curr)
                curr = []
            else:
                word, tag, acc = line.strip().split("\t")
                curr.append((word,tag))
    return sents

def read_ner_tags_file(path):
    """
    Parse the NER tag file and return a list of named entities for each tweet.
    Example line in NER tag file:
     'On/O the/O freeway/O to/O Africa/B-ENTITY til/O I/O wrecked/O my/O Audi/O'
    """
    ENTITY_BEGIN =          'B-ENTITY'
    ENTITY_INTERMEDIATE =   'I-ENTITY'
    all_entities = []

    with open(path, 'r') as f:
        for tweet in f:
            words = [x[:x.rfind('/')] for x in tweet.split()]
            tags =  [x[x.rfind('/')+1:] for x in tweet.split()]
            curr_entity = None
            ents = []
            for i in xrange(len(words)):
                if tags[i] == ENTITY_BEGIN:
                    if curr_entity:
                        ents.append(curr_entity)
                    curr_entity = words[i]
                    if (i+1 == len(words)) or tags[i+1] != ENTITY_INTERMEDIATE:
                        ents.append(curr_entity)
                        curr_entity = None
                elif tags[i] == ENTITY_INTERMEDIATE:
                    curr_entity += (' ' + words[i])
                    if (i+1 == len(words)) or tags[i+1] != ENTITY_INTERMEDIATE:
                        ents.append(curr_entity)
                        curr_entity = None
            all_entities.append(ents)

    return all_entities