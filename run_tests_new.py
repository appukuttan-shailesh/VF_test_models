"""
Main script for running vaidation tests of testCell

Author: Andrew P. Davison and Shailesh Appukuttan, CNRS
Date: February 2017
"""

import argparse
from datetime import datetime
from hbp_validation_framework import TestLibrary
from hbp_validation_framework.datastores import CollabDataStore
import models

parser = argparse.ArgumentParser()
parser.add_argument("model",
                    help="name of the model to test, e.g. Bianchi, Golding, KaliFreund or Migliore"),
parser.add_argument("test",
                    help="test configuration file (local path or URL)")
parser.add_argument("instance_id",
                    help="test instance ID")
parser.add_argument("model_path", nargs='?',
                    help="currently used to load morphologies. Specifies path to morphology file. ")

config = parser.parse_args()

# Load the model
if config.model_path is not None:
    model = getattr(models, config.model)(model_path=config.model_path)
else:
    model = getattr(models, config.model)()
print "----------------------------------------------"
print "Model name: ", model
print "Model type: ", type(model)
if config.model_path is not None:
    print "Model path: ", config.model_path
print "----------------------------------------------"

# Load the test
# checks the test is registered with the Validation framework,
# if it is not, fail with instructions for registering,
# or offer to register it
# test_library = TestLibrary() # default url for HBP service
test_library = TestLibrary(username="shailesh") # default url for HBP service
# test = test_library.get_test(alias=config.test, instance_id=config.instance_id)
test = test_library.get_validation_test(alias=config.test, version=config.instance_id)
print "----------------------------------------------"
print "Test name: ", test
print "Test type: ", type(test)
print "----------------------------------------------"

# Run the test
score = test.judge(model, deep_error=True)
print "----------------------------------------------"
print "Score: ", score
if "figures" in score.related_data:
    print "Output files: "
    for item in score.related_data["figures"]:
        print item
print "----------------------------------------------"

# Register the result with the HBP Validation service
# This could be integrated into test.judge() if we extend sciunit appropriately
print "=============================================="
print "Enter Collab ID for Data Storage (if applicable)
print "(Leave empty for Model's host collab, i.e. ", model.content, ")"
score.related_data["project"] = raw_input('Collab ID: ')

collab_folder = "{}_{}".format(config.model, datetime.now().strftime("%Y%m%d-%H%M%S"))
# TODO: have collab_id automatically entered
collab_storage = CollabDataStore(collab_id=score.related_data["project"],
                                 base_folder=collab_folder,
                                 auth=test_library.auth)

test_library.register_result(test_result=score, data_store=collab_storage)
# test_library.register_result(test_result=score)
