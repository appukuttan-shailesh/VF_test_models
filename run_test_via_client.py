import models
from hbp_validation_framework import utils

mymodel = models.hippoCircuit()
utils.run_test(hbp_username="shailesh", model=mymodel, test_alias="CDT-5", test_version="6.0")
