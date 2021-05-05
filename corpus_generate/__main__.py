"""Tool to generate a corpus of text, or a training data file for a text
classifier, given a list of topics to classify."""

import sys
import argparse

from termcolor import colored

from corpus_generate.CorpusGenerate import CorpusGenerate


def main():
    """Run CLI for corpus_generate. Wrapper to use in setup[entry_points]"""

    parser = argparse.ArgumentParser(
        prog="corpus-generate",
        description="Tool to generate a corpus of text, or a training data "
        +"file for a text classifier, given a list of topics to classify."
    )

    parser.add_argument(
        "-t",
        "--topic",
        type=str,
        required=True,
        help="The topic to research, which will be used as the name of the "+
             "class for the texts outputed."
    )

    parser.add_argument(
        "-o",
        "--outfile",
        type=str,
        required=False,
        help="Optionally supply a .csv file path to output the texts to."
    )

    parser.add_argument(
        "-n",
        "--num-articles",
        type=int,
        required=False,
        default=10,
        help="Supply the number of articles found on the net that the bot "+
             "should search through for text."
    )

    args = parser.parse_args()

    # Run generator.
    try:
        generator = CorpusGenerate()
        generator.generate([args.topic], args.num_articles, args.outfile)

    except KeyboardInterrupt:
        print("[* corpus-generate] Exiting. Goodbye!")
        sys.exit(1)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # Use this entry point to test package locally.
    main()