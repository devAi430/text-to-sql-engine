"""
Module: Text to SQL Engine
Author: devAi430

This module is part of a natural language to SQL
translation system designed for clarity and extensibility.
"""

import re

import pandas as pd
import torch
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
)
from peft import PeftModel


from .cypherquery import CypherQuery
from .kustoquery import KustoQuery
from .mongoquery import MongoQuery
from .pandasquery import PandasQuery
