#!/usr/bin/python

import datetime, logging, os, subprocess, sys, traceback, urllib

def configure_logger():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def check_env():
    logging.info("Check required env variables")
    get_env("CI")
    get_env("TRAVIS")
    get_env("TRAVIS_PULL_REQUEST")
    get_env("TRAVIS_REPO_SLUG")

    required_vars = ["CI", "TRAVIS", "TRAVIS_PULL_REQUEST", "TRAVIS_REPO_SLUG"]
    for env_var in required_vars:
        get_env(env_var)


def get_env(single_env):
    try:
        logging.info("Check single var: " + single_env)
        assert (os.environ[single_env])
        return os.environ[single_env]
    except Exception as e:
        logging.warn("Problem while reading env variable: " + single_env)
        return None


def is_travis_ci():
    if os.environ["CI"] == 'true' and os.environ["TRAVIS"] == 'true':
        return True


def download_sputnik_files():
    if is_travis_ci():
        if get_env("api_key"):
            logging.info("Downloading sputnik.properties")
            properties_url = "http://sputnik.touk.pl/conf/" + os.environ["TRAVIS_REPO_SLUG"] + "/sputnik-properties?key=" + os.environ["api_key"]
            urllib.urlretrieve(properties_url, filename="sputnik.properties")

            logging.info("Downloading checkstyle.xml")
            checkstyle_url = "http://sputnik.touk.pl/conf/rafalnowak/sputnik-test/checkstyle?key=" + os.environ["api_key"]
            urllib.urlretrieve(checkstyle_url, file_name="checkstyle.xml")

        logging.info("Downloading sputnik.jar")
        sputnik_jar_url = "https://philanthropist.touk.pl/nexus/service/local/artifact/maven/redirect?r=snapshots&g=pl.touk&a=sputnik&c=all&v=LATEST"
        urllib.urlretrieve(sputnik_jar_url, filename="sputnik.jar")

        subprocess.call(['java', '-jar', 'sputnik.jar', '--conf', 'sputnik.properties', '--pullRequestId', get_env("TRAVIS_PULL_REQUEST")])


def sputnik_ci():
    configure_logger()
    check_env()
    download_sputnik_files()


sputnik_ci()
