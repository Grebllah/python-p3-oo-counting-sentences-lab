#!/usr/bin/env python3
# For this lab, you will be creating the `MyString` class and several methods on
# the class. You will need to use the `self` keyword in the body of these methods
# to refer to the instance of `MyString` on which the method is being called.


class MyString:
  def __init__(self, value = ""):
    self.value = value
    pass
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  def is_sentence(self):
    sentence_list = [*self._value]
    if sentence_list[-1] == ".":
      return True
    else: return False
  def is_question(self):
    sentence_list = [*self._value]
    if sentence_list[-1] == "?":
      return True
    else: return False
  def is_exclamation(self):
    sentence_list = [*self._value]
    if sentence_list[-1] == "!":
      return True
    else: return False
  def count_sentences(self):
    splitable_string = self.value
    splitable_string = splitable_string.replace("!", ".")
    splitable_string = splitable_string.replace("?", ".")
    splitable_string = splitable_string.replace(",", "")
    split_string = splitable_string.split(".")
    sentence_count = len([sentence for sentence in split_string if sentence])
    return sentence_count
