# corpus-generate #
Genreate a corpus of text used for training a text classifier. `corpus-generate`
will search the net for text on a topic or list of topics and output a file that
can be used in training.


## installation ##
Requires `Python >= 3.6`. Use `pip` to install directly from github:
```bash
$ python -m pip install git+https://github.com/AnikaSystems/corpus_generate.git 
```
This will expose the command `corpus-generate.exe`. See below for usage.

### from source ###
To install from source, simply `clone` the repo, `cd` into it, and run the 
`setup.py` install script.
```bash
```


## usage ##
```
```

## running locally ##
To test the module locally without installing, `cd` into the project root and
type `python -m corpus_generate`. This will run the modules entry point, which 
happens to be a CLI.


## TODO ##
* Train a classifier for a set number of topics

* How to generate training data for a term or phrase
    * Input:  {"topic": "Products/Checking and Savings", "Explanation": "Everything about deposit accounts"}
        * Generate a corpus (Or manually train classifier)
            * Google search topic
            * Extract 2-3 pages
            * Use 'newspaper' to extract main article of page  
        * Train classifier with SpaCy or Tensorflow

* Courpus example: https://www.kaggle.com/ritresearch/happydb

* Find articles online
* Create Courpus (.csv file), 2 columns (text, and topic)
* Train classifier
* Test classifier