import sciunit
import quantities as pq
from neuronunit.capabilities import ProvidesLayerInfo
from hbp_validation_framework.versioning import Versioned

class testCell(sciunit.Model, ProvidesLayerInfo, Versioned):
    id = "9ade6831-a758-42be-a50e-d5cb65859c34"

    def __init__(self, name="testCell", layer_info={}):
        self.layer_info = layer_info
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy cell for testing layer heights"
        self.set_layer_info_default()

    def set_layer_info(self, layer_info):
        self.layer_info = layer_info

    def set_layer_info_default(self):
        self.layer_info = { "Layer 1": {'height': {'value':'150 um'}},
                            "Layer 2/3": {'height': {'value':'300 um'}},
                            "Layer 4": {'height': {'value':'250 um'}},
                            "Layer 5": {'height': {'value':'425 um'}},
                            "Layer 6": {'height': {'value':'675 um'}} }

    def get_layer_info(self):
        return self.layer_info
