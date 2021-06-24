# Language Models

_Work in progress_

This project explores applying different language models to automatically identify the language of the text. By using the frequency distribution of character n-grams across different languages.

This program implements three different types of character language models:

1. Unsmoothed
2. Smoothed with add one (Laplace) smoothing
3. Smoothed with linear interpolation smoothing

## Data

The assignment's training data can be found in [data/train](data/train) and the development data can be found in [data/dev](data/dev).

## 1. Members

- Scott Kavalinas
- Fraser Redford

## 2. Listed Resources

- Chapter 3 https://web.stanford.edu/~jurafsky/slp3/3.pdf
- https://towardsdatascience.com/perplexity-intuition-and-derivation-105dd481c8f3
- https://sookocheff.com/post/nlp/n-gram-modeling/

## 3. Installation

- Python3
- Pandas
- NLTK

The program can be run directly from the project directory if the user has Pandas and NLTK installed using:

```
$ python3 code/langid.py [model] [model] [model]
```

The user can choose a `[model]` using either:

```
--unsmoothed
--laplace
--interpolation
```

Which will run either an unsmoothed, laplace or interpolation model on the data provided. The user can run all three at once or choosing one individually to test.

If the user does not have `pandas` or `nltk`, then they can run the program by first installing:

```
$ pip install pandas
$ pip install nltk
```

The program will effectively operate within the confines of `langid.py` and the provided inputs in directory `data`. A `csv` file will be generated for each model that you select and output into `output`.
