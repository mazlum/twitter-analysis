import argparse
import sys
from TwitterAnalysis import TwitterAnalysis


description = """
    This script for your twitter account analysis.. \n
    Example :
    python twitter.py -u username
"""
parser = argparse.ArgumentParser("twitter", description=description)
parser.add_argument("--username", "-u", help="twitter account username")
args = parser.parse_args()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print parser.print_help()
        exit(0)


    t = TwitterAnalysis(consumer_key, consumer_secret, access_token, access_token_secret)
    t.find_not_following(args.username)