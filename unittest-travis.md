---
title: Unit testing with `unittest` and Travis CI
author: Eric Leung
date: December 3rd, 2015
---

## Overview

What are unit tests?

Why are they important?

Can you automate them?

## Unit Tests

"Unit testing refers to the practice of testing certain functions and areas – or
units – of our code"

![Lego bricks](images/lego-bricks-resize.png)

Source: http://www.welovebug.com/wp-content/uploads/2013/11/13UnitTests.png

## Why?

Finds problems early

Facilitates change

Simplifies integration

Documentation

Design

## Python's `unittest`

Terms:

- test fixture: the preparation needed to run tests
- test case: smallest unit of testing
- test suite: collection of test cases
- test runner: runs all tests and reports results

Statements:

- `assertEqual()`
- `assertTrue()`
- `assertFalse()`
- `assertRaise()`

Source: https://docs.python.org/2/library/unittest.html

## Automate Everything!

![Travis CI: FOSS, hosted, distributed continuous integration](images/travis.png)

## Other Automators

[GitLab CI](https://about.gitlab.com/gitlab-ci/)

[Jenkins](http://jenkins-ci.org/)

More: [Comparison of continuous integration
software](https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software)

## Resources

- [The Beginner's Guide to Unit Testing: What is Unit Testing?](http://code.tutsplus.com/articles/the-beginners-guide-to-unit-testing-what-is-unit-testing--wp-25728)
