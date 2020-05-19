# pythonTestsCI
A simple implementation of Continuous Integrations (CI)

## What is
In this example is implemented the OpsNumber package, which have a sum function, given a number list, the function return a sum of all numbers of the list

## CI Pipeline
The implemented continuous integration have two stages in pipeline:

* Test stage: using [unittest](https://docs.python.org/3/library/unittest.html)
* Code Formatting : using [flake8](https://flake8.pycqa.org/en/latest/)

In each commit in master branch, the pipeline run analysing the source code, validating each stage, case success, the pipipeline return sucess, in case of error, the pipeline show broken message in commit.
