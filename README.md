# corpus-generate #
Genreate a corpus of text used for training a text classifier. `corpus-generate`
will search the net for text on a topic or list of topics and output a file that
can be used in training.


## Installation ##
Requires `Python >= 3.6`. Use `pip` to install directly from github:
```bash
$ python -m pip install git+https://github.com/AnikaSystems/corpus_generate.git 
```
This will expose the command `corpus-generate.exe`. See below for usage.


### From Source ###
To install from source, simply `clone` the repo, `cd` into it, and run the 
`setup.py` install script.
```bash
$ git clone https://github.com/dan-velez/corpus_generate.git
$ cd corpus_generate
$ python setup.py install
```


## Usage ##
```
usage: corpus-generate [-h] -t TOPIC [-o OUTFILE] [-n NUM_ARTICLES]

Tool to generate a corpus of text, or a training data file for a text
classifier, given a list of topics to classify.

optional arguments:
  -h, --help            show this help message and exit
  -t TOPIC, --topic TOPIC
                        The topic to research, which will be used as the name 
                        of the class for the texts outputed.
  -o OUTFILE, --outfile OUTFILE
                        Optionally supply a .csv file path to output the texts
                        to.
  -n NUM_ARTICLES, --num-articles NUM_ARTICLES
                        Supply the number of articles found on the net that   
                        the bot should search through for text.
```

## Running Locally ##
To test the module locally without installing, `cd` into the project root and
type `python -m corpus_generate`. This will run the modules entry point, which 
happens to be a CLI.


## TODO ##
* Cannot install package `google` on linux: https://pypi.org/project/google/

* Train a classifier for a set number of topics.

* Create a **classifier generator** given a set of topics.

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