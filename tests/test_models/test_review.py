#!/usr/bin/python3
"""Unittests for the TestReviewDocs Classes"""

from datetime import datetime
import inspect
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review


class TestReview(unittest.TestCase):
    """Tests that check the documentation and style of Review class"""
    @classmethod
    """Sets up for the doc tests"""
    cls.
