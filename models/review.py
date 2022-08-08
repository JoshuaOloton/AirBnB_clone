#!/usr/bin/python3
"""  class Review inherits from BaseModel """

from .base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""
