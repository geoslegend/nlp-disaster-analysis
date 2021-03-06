# Detection and Analysis of Disaster-Related Tweets
### Final Project // Advanced Methods in Natural Language Processing @TAU // Spring 2017

### 1. Usage

The project may be used for completing one of the three following tasks:
- Classifying tweets as `disaster-related` or `not disaster-related`.
- Classifying `disaster-related` tweets as `objective` or `subjective`.
- Extract `named-entities` from `disaster-related` tweets.
    
Usage summary:
```
$ python __main__.py --help

usage: __main__.py [-h] [-v] [-d] [-s] [-n] [-o OUTPUT] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -d, --disaster-classification
                        will train and classify tweets dataset as disaster or
                        not
  -s, --sentiment-analysis
                        will train and classify disaster related tweets
                        dataset as objective or subjective
  -n, --named-entity-recognition
                        will classify named entities in disaster related
                        tweets dataset
  -o OUTPUT, --output OUTPUT
                        output directory for graphs
  -a, --all             equivalent to -d -s -n
```

#### 1.1 Disaster Classification

The `--disaster-related` flag trains `disaster-related` classifiers and test their prediction accuracy while tuning parameters using *grid search* method (penalty constant in *SVM* and number of estimators in *Random Forest*). We split the dataset into train and test sets.
After the *fitting* phase on the train set, the *predicting* phase will output the following:
- Best accuracies in the format of a table.
- Plot comparable graphs of the classifiers (*SVM*, *Random Forest*, *Naive Bayes*).
Output example:
_______________
```
$ python __main__.py --disaster-classification

Measure times for function: test_disaster_classification (2017-09-09 17:12:58)
===============================
Test unigrams:
Fitting 1...
.
.
.
Fitting 1024...
===============================
Test unigrams and bigrams:
Fitting 1...
.
.
.
Fitting 1024...
Forest uni: Max acc: 7: 0.91124260355, Max ppv: 7: 0.945355191257, Max npv: 7: 0.891975308642
Forest bi: Max acc: 9: 0.905325443787, Max ppv: 6: 0.934065934066, Max npv: 9: 0.88379204893
Saving graph into: Projects\nlp-disaster-analysis\graphs\DisasterClassification\random_forest_unigram_vs_bigram_features.png
===============================
Test SVM unigrams and bigrams:
C=10
.
.
.
C=10000000
SVM uni: Max acc: 3: 0.934911242604, Max ppv: 2: 0.961325966851, Max npv: 3: 0.934640522876
SVM uni pos: Max acc: 3: 0.936883629191, Max ppv: 2: 0.94623655914, Max npv: 3: 0.937704918033
SVM bi: Max acc: 3: 0.932938856016, Max ppv: 2: 0.952127659574, Max npv: 3: 0.926045016077
SVM bi pos: Max acc: 3: 0.944773175542, Max ppv: 3: 0.954545454545, Max npv: 3: 0.938511326861
Saving graph into: Projects\nlp-disaster-analysis\graphs\DisasterClassification\svm_uni_features.png
Saving graph into: Projects\nlp-disaster-analysis\graphs\DisasterClassification\svm_bi_features.png
          Uni NB  Bi NB  Uni RF  Bi RF  Uni SVM  Uni POS SVM  Bi SVM  \
accuracy   0.921  0.864   0.911  0.890    0.935        0.937   0.933
ppv        0.977  1.000   0.945  0.969    0.961        0.946   0.952
npv        0.891  0.813   0.892  0.856    0.935        0.938   0.926

          Bi POS SVM
accuracy       0.945
ppv            0.955
npv            0.939
Saving table into: Projects\nlp-disaster-analysis\graphs\DisasterClassification\best_result_table.png
Total running time of test_disaster_classification in seconds: 383
```

#### 1.2 Sentiment Analysis Classification

The `--sentiment-analysis` flag trains `objective/subjective` classifiers and test their prediction accuracy while tuning number of features using feature selection methods. We split the dataset into train and test sets.
After the *fitting* phase on the train set, the *predicting* phase will output the following:
- Best accuracies in the format of a table.
- The selected features which each classifier used when it achieved its best accuracy.
- Plot comparable graphs of the classifiers (*SVM*, *Random Forest*).
Output example:
_______________
```
$ python __main__.py --disaster-classification

===============================
Test sentiment analysis:
Measure times for function: test_sentiment_analysis (2017-09-09 17:31:22)
#features: 1
.
.
.
#features: 18
Total running time of test_sentiment_analysis in seconds: 24
Random Forest: Max acc: 12: 0.871428571429, Max ppv: 0: 0.905063291139, Max npv: 12: 0.75
Random Forest Best 13 features: exclamation_count, exclamation_presence, question_mark_presence, url_presence, emoticon_presence, digits_count, cap_letters_count, punctuation_marks_and_symbols_count, length
SVM: Max acc: 3: 0.847619047619, Max ppv: 0: 0.905063291139, Max npv: 3: 0.666666666667
SVM Best 4 features: exclamation_count, url_presence, emoticon_presence, punctuation_marks_and_symbols_count
Saving graph into: Projects\nlp-disaster-analysis\graphs\SentimentAnalysis\random_forest.png
Saving graph into: Projects\nlp-disaster-analysis\graphs\SentimentAnalysis\SVM.png
          RF (1)  RF (13)  SVM (1)  SVM (4)
accuracy   0.805    0.871    0.805    0.848
ppv        0.905    0.890    0.905    0.874
npv        0.500    0.750    0.500    0.667
Saving table into: Projects\nlp-disaster-analysis\graphs\SentimentAnalysis\best_result_table.png

```

#### 1.3 Named Entity Recognition

The `--named-entity-recognition` flag performs named entity classification and recognition on the dataset, by using the GMB database as a training input, and NLTK as the POS-tagger.
After training on the GMB database, the recognition phase would print entities in the following categories, sorted from the most common to the least common, along with their number of appearances:
- Geographical Entities
- Organization Entities
- Person Entities
- Geopolitical Entities
- Time Indicator Entities
- Artifact Entities
- Event Entities
- Natural Phenomenon Entities

After, the top 10 entities are printed.

In order to use this option, one needs to extract the GMB zip, located at ner/gbm-2.2.0.zip, to the same directory.
After, as the reader is saved in .pkl format for time saving reasons, delete the gmb_reader.pkl file from the base
directory, if exists.

Output example:
_______________
```
$ python __main__.py --named-entity-recognition

Measure times for function: test_named_entity_recognition (2017-09-09 21:14:08)
===============================

Test named entity recognition:
Geographical Entities - hiroshima-48, northern-36, california-29, the-26, japan-16, mediterranean-14, reunion-12, myanmar-10, india-10, fukushima-10, colorado-10, ...
Organization Entities - abc-57, abc news-32, california-21, -abc news-21, bbc-19, pic of-16, reunion-11, washington-11, devastation wrought-11, india-10, japan-10, ...
Person Entities - obama-25, i-6, food-5, calgary-5, userref-4, runion debris-3, rainstorm-3, news bin-2, warne-2, tornado-2, bin laden-2, insane-1, hermancranston-1, ...
Geopolitical Entities - userref-79, california-50, turkey-48, refugio-35, legionnaires-27, wreckage-27, severe-25, disea-23, mh370-22, indian-17, giant-17, old-16, ...
Time Indicator Entities - twitter ``-86, 15-30, edinburgh - bbc-29, minute-28, typhoon-devastated saipan obama-24, --23, mh370 malaysia pm-22, wildfire - abc-19, ...
Artifact Entities - on-46, redirect-6, ok seek-3, reports-3, live noaa tracking looping-3, fresno-2, penny sized-2, deputy jessica-2, collapses demolishes houses-2, ...
Event Entities - etc kenneth-4, maj muzzamil-2, severe-2, heavy-1, stubborn forest-1, fortitudevalley unit-1, green line-1, cree torch-1, nc till-1, cta green-1, ...
Natural Phenomenon Entities - 6igm-4, dvc bjp-3, allah gv-2, woman teen-2, rt-2, dont-2, virgin-2, ebola virus-2, account-2, hiroshima-2, seattle cheyenne-2, worry-2, ...
Top 10 Entities - california, twitter ``, hiroshima, abc, turkey, northern, severe, refugio, japan, obama
Total running time of test_named_entity_recognition in seconds: 171

```

#### 1.4 Other

For more *verbosed* output, `--verbose` flag can be passed. It will result more debugging prints as well as printing *false positive* and *false negative* tweets.
Example:
```
$ python __main__.py --sentiment-analysis --verbose
.
.
.    
Real: 0, Prediction: 1
Tweet is: Hiroshima: 70 years since the worst mass murder in human history. Never forget. http://www.aljazeera.com/ Atomic bomb in 1945: A look back at the destruction - Al Jazeera English
.
.
.
```
The `--output` flag may be used in order to change plots directory, if not given the default directory is *graphs* inside the project package.

### 2. Project Structure

The project consists of the following files and libraries:
- `__main__.py`: *script*.
    - The main script, the client interface for running the project.
- `classifer.py`: *script*
    - Wraps *Naive Bayes*, *Random Forest* and *SVM* classifiers.
- `classify_recent_tweets`: *script*
    - Can be used to test trained classifiers against new data.
- `common.py`: *script*
    - Bunch of useful utilities.
- `feature.py`: *script*
    - Small framework that allows easy assigns and dissociate features to specific classifiers.
- `preprocess_dataset.py`: *script*
    - Tweets preprocessor that follows tiny urls, expands them and extracts titles from the page itself.
- `ark-tweet-nlp-0.3.2`: *library*
    - See *References* section.
- `dataset`: *directory*
    - Contains all dataset we used.
- `dataset_parser`: *directory*
    - Contains bunch of scripts for parsing and preprocessing our dataset and tweets.
- `graphs`: *directory*
    - Output graphs of `__main__.py` script.
- `ner`: *directory*
    - Contains GMB parsing tools, and a named entity classifier.
- `sentiment_analysis`: *directory*
    - Contains features for sentiment analysis section and the `emoticon.py` script (see *References* section).
- `ttp`: *library*
    - See *References* section.
- `twitter_api`: *directory*
    - Bunch of scripts that were used in order to test classifiers on real time data using Twitter API.
- `twokenizer`: *library*
    - See *References* section.

### 3. Prerequisites

- [Python Twitter Tools](https://pypi.python.org/pypi/twitter) library (```pip install twitter```)

### 4. References

For convenience, we copied some code from outer sorces to this project. Here are some references to the packages we used:
- [ark-tweet-nlp](https://github.com/brendano/ark-tweet-nlp/) library (*POS tagging*)
    - Note: This project is written in Java and should be run from a Linux machine. For further instrutions please see 'Part-of-Speech Tagging' section at [Tweet NLP @ CMU](http://www.cs.cmu.edu/~ark/TweetNLP/)
- [emoticon](https://github.com/aritter/twitter_nlp/blob/master/python/emoticons.py) script (*Emoticons extraction*)
- [twitter-text-python](https://pypi.python.org/pypi/twitter-text-python/) library (*Tweets parsing*)
- [Twitter-API](https://dev.twitter.com/rest/public/search) API (*API for tweets extraction*)
- [twokenizer](https://github.com/ataipale/geotagged_tweet_exploration/blob/master/twokenizer.py) script (*Separating tweets into tokens*)
- [GMB](http://gmb.let.rug.nl/) dataset
