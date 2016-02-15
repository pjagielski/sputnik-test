#!/usr/bin/python

import os, sys, traceback


def check_env():
    print "1 - check env variables"
    try:
        assert (os.environ["CI"])
        assert (os.environ["TRAVIS"])
        assert (os.environ["TRAVIS_PULL_REQUEST"])
        assert (os.environ["TRAVIS_REPO_SLUG"])
    except Exception as e:
        print "Problem while reading env variable", e
        print traceback.format_exception(*sys.exc_info())


def check_travis_ci():
    if (os.environ["CI"] == 'true' and os.environ["TRAVIS"] == 'true'):
        print "Running on Travis CI"
    else:
        print "Not running on Travis CI"


def sputnik_ci():
    check_env()
    check_travis_ci()

sputnik_ci()



# #!/bin/bash
#
# if [ "$CI" = "true" ] && [ "$TRAVIS" = "true" ];
# then
#   echo "Running on Travis CI"
#   PR="$TRAVIS_PULL_REQUEST"
# fi
#
# if [ "$PR" != "false" ];
# then
#   echo "Running on pull request $PR"
#   if [ ! -z "$api_key" ];
#   then
#     echo "Downloading sputnik.properties"
#     wget -q "http://sputnik.touk.pl/conf/$TRAVIS_REPO_SLUG/sputnik-properties?key=$api_key" -O sputnik.properties
#   fi
#   wget "https://philanthropist.touk.pl/nexus/service/local/artifact/maven/redirect?r=snapshots&g=pl.touk&a=sputnik&c=all&v=LATEST" -O sputnik.jar && java -jar sputnik.jar --conf sputnik.properties --pullRequestId $PR
# fi
#
