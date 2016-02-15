#!/usr/bin/python

import os, subprocess, sys, traceback, urllib


def check_env():
    print "check required env variables"
    get_env("CI")
    get_env("TRAVIS")
    get_env("TRAVIS_PULL_REQUEST")
    get_env("TRAVIS_REPO_SLUG")


def get_env(single_env):
    try:
        assert (os.environ[single_env])
        return os.environ[single_env]
    except Exception as e:
        print "Problem while reading env variable " + single_env
        return None


def is_travis_ci():
    if os.environ["CI"] == 'true' and os.environ["TRAVIS"] == 'true':
        return True


def download_sputnik_files():
    if is_travis_ci():
        if get_env("api_key"):
            print "Downloading sputnik.properties"
            properties_url = "http://sputnik.touk.pl/conf/" + os.environ["TRAVIS_REPO_SLUG"] + "/sputnik-properties?key=" + os.environ["api_key"]
            urllib.urlretrieve(properties_url, filename="sputnik.properties")

            print "Downloading checkstyle.xml"
            checkstyle_url = "http://sputnik.touk.pl/conf/rafalnowak/sputnik-test/checkstyle?key=" + os.environ["api_key"]
            urllib.urlretrieve(checkstyle_url, file_name="checkstyle.xml")

        print "Downloading sputnik.jar"
        sputnik_jar_url = "https://philanthropist.touk.pl/nexus/service/local/artifact/maven/redirect?r=snapshots&g=pl.touk&a=sputnik&c=all&v=LATEST"
        urllib.urlretrieve(sputnik_jar_url, filename="sputnik.jar")

        subprocess.call(['java', '-jar', 'sputnik.jar', '--conf', 'sputnik.properties', '--pullRequestId', get_env("TRAVIS_PULL_REQUEST")])


def sputnik_ci():
    print "start"
    check_env()
    download_sputnik_files()
    print "end"


sputnik_ci()
