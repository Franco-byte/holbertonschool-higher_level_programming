#!/usr/bin/env python3
import pickle

class CustomObject:
    
    def __init__(self, name: str = "", age: str = "", is_student: bool = False):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as pickle_file:
            pickle.dump(self, pickle_file)
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as py_data_struct:
                return pickle.load(py_data_struct)
        except Exception:
            return None
