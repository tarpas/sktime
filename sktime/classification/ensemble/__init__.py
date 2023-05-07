# -*- coding: utf-8 -*-
"""Compositions for classifiers."""
# copyright: sktime developers, BSD-3-Clause License (see LICENSE file)

__all__ = [
    "ComposableTimeSeriesForestClassifier",
    "WeightedEnsembleClassifier",
]

from sktime.classification.ensemble._ctsf import ComposableTimeSeriesForestClassifier
from sktime.classification.ensemble._weighted import WeightedEnsembleClassifier