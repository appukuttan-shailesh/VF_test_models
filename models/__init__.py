import os
import sciunit
from neuron import h
from hbp_validation_framework.versioning import Versioned

#==============================================================================

class testColumn(sciunit.Model, Versioned):
    id = "9ade6831-a758-42be-a50e-d5cb65859c34"

    def __init__(self, name="testColumn", layer_info={}):
        self.layer_info = layer_info
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy model for testing layer heights"
        self.set_layer_info_default()

    def set_layer_info(self, layer_info):
        self.layer_info = layer_info

    def set_layer_info_default(self):
        self.layer_info = { "Layer 1": {'height': {'value':'165 um'}},
                            "Layer 2": {'height': {'value':'149 um'}},
                            "Layer 3": {'height': {'value':'353 um'}},
                            "Layer 4": {'height': {'value':'190 um'}},
                            "Layer 5": {'height': {'value':'525 um'}},
                            "Layer 6": {'height': {'value':'700 um'}} }

    def get_layer_info(self):
        return self.layer_info

#==============================================================================

class hippoCircuit(sciunit.Model, Versioned):
        #id = "f25d05b2-2358-418b-8914-fe02a412ac74"
        #id = "f32776c7-658f-462f-a944-1daf8765ec97" #New VF v1.0
        instance_id = "c9db962f-53e7-4c05-b817-c7bced1a9108" #New VF v2.0

        def __init__(self, name="hippoCircuit", density_info={}):
            self.density_info = density_info
            sciunit.Model.__init__(self, name=name)
            self.name = name
            self.description = "Dummy model for testing cell densities"
            self.set_density_info_default()

        def set_density_info_default(self):
            self.density_info = { "density" : {"value" : "275 1000/mm3"}}

        def get_density_info(self):
            return self.density_info

#==============================================================================

#class neuroM_loader(sciunit.Model, cap.HandlesNeuroM, Versioned):
class neuroM_loader(sciunit.Model, Versioned):
        id = "3957bc1c-4a22-40ca-9ad6-879f75403219"

        def __init__(self, name="neuroM_loader", model_path=None, soma_diameter={}):
            self.soma_diameter = soma_diameter
            sciunit.Model.__init__(self, name=name)
            self.name = name
            self.description = "Model for loading morphologies via NeuroM"
            if model_path == None:
                print "Please specify the path to the morphology file or the directory as the last parameter!"
                print "Example Syntax1: python run_tests.py neuroM_loader https://validation.brainsimulation.eu/tests/7 ./files/1-1-DE-rep-ax-cor.swc"
                print "Example Syntax2: python run_tests.py neuroM_loader https://validation.brainsimulation.eu/tests/7 ./files"
                quit()
            if os.path.isdir(model_path):
                print "Directory"
                quit()
            self.morph_path = model_path
            self.set_soma_diameter_info()

        def set_soma_diameter_info(self):
            import neurom as nm
            nrn = nm.load_neuron(self.morph_path)
            soma_radius = nm.get('soma_radii', nrn, neurite_type=nm.SOMA)
            value = str(soma_radius[0]*2) + " um"
            self.soma_diameter = { "diameter" : {"value" : value}}

        def get_soma_diameter_info(self):
            return self.soma_diameter

#==============================================================================

class NeuroM_NeuriteLength(sciunit.Model, Versioned):

    id = "afc85429-0db2-4414-8fc7-3ed5781a5019"

    def __init__(self, name='NeuriteLength', NeuriteLength_info={}):
        self.NeuriteLength_info = NeuriteLength_info
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy model for testing neurite length"
        self.set_NeuriteLength_info_default()

    def set_NeuriteLength_info_default(self):
        self.NeuriteLength_info = {'NeuriteLength': {'value': '60 um'}}

    def get_NeuriteLength_info(self):
        return self.NeuriteLength_info

#==============================================================================

class CA1Layers_NeuritePathDistance(sciunit.Model, Versioned):

    id = "bb06ab0a-685c-4f0f-b078-195cd947639f"

    def __init__(self, name='CA1Layers_NeuritePathDistance', CA1LayersNeuritePathDistance_info={}):
        self.CA1LayersNeuritePathDistance_info = CA1LayersNeuritePathDistance_info
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy model to test neurite path-distances across CA1 layers"
        self.set_CA1LayersNeuritePathDistance_info_default()

    def set_CA1LayersNeuritePathDistance_info_default(self):
        self.CA1LayersNeuritePathDistance_info = { "SLM": {'PathDistance': {'value':'120 um'}},
						    "SR": {'PathDistance': {'value':'280 um'}},
						    "SP": {'PathDistance': {'value':'40 um'}},
						    "SO": {'PathDistance': {'value':'100 um'}}
						  }

    def get_CA1LayersNeuritePathDistance_info(self):
        return self.CA1LayersNeuritePathDistance_info

#==============================================================================

class IV_Curve_Generator(sciunit.Model, Versioned):
    id = ""

    def __init__(self, name="IV_Curve_Generator", iv_data={}):
        self.iv_data = iv_data
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy model for comparing IV curves of channels"
        self.set_iv_data_default()

    def set_iv_data_default(self):
        self.iv_data = {"IV":
                            {
                                "V":["-100 mV","-80 mV","-60 mV","-40 mV","-20 mV","0 mV","20 mV","40 mV","60 mV","80 mV","100 mV"],
                                "I":["5 mA/cm2","4 mA/cm2","3 mA/cm2","2 mA/cm2","1 mA/cm2","0 mA/cm2","1 mA/cm2","2 mA/cm2","3 mA/cm2","4 mA/cm2","5 mA/cm2"]
                            }
                       }

    def get_iv_data(self):
        return self.iv_data

#==============================================================================

class IV_Model():

    def __init__(self, name="IV_Model"):
        """ Constructor. """
        h.load_file("./hoc_models/IV_Model/iv_model.hoc")
        h('get_IVdata(0)')
        self.i_data = h.rec_ina.to_python()
        self.v_data = h.rec_v.to_python()

    def get_iv_data(self):
        return self.i_data, self.v_data

#model = IV_Model()
#print model.get_iv_data()
#==============================================================================
