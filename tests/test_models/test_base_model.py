#!/usr/bin/python3
""" unnitests for base_model.py"""

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import os
import models


class TestBaseModel_instantiation(unittest.TestCase):
    """Testing instance of base model class"""

    def test_id_is_public_str(self):
        # if id is string
        self.assertEqual(str, type(BaseModel().id))

    def test_new_instance_stored_in_objects(self):
        # if obj is in storage.all
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_no_args_instances(self):
        # if ame type as basemodel instance
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_created_at_public_datetime(self):
        # checks if the type of the created_at att is datetime.
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public_datetime(self):
        # checks if  type of the updated_at attr is datetime.
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_2_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_2_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_instances_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())


class TestBaseModelTo_dict(unittest.TestCase):
    """Testing dict method in the base model"""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_has_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


if __name__ == "__main__":
    unittest.main()
