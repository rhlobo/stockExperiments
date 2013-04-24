#!/bin/bash
CURRDIR="$(pwd)"
TESTTYPE=${1:-full}
export TESTTYPE
cd "${PROJECT_HOME}/stockExperiments"
nosetests -v --with-coverage --cover-erase --cover-inclusive --cover-branches --cover-package=stockExperiments --cover-html --cover-html-dir="../coverage/" -w stockExperiments
find . -type f -name "*.pyc" -exec rm -f {} \;
cd "${CURRDIR}"
