from neuron import h

class IV_Model():

    def __init__(self, name="IV_Model"):
        """ Constructor. """
        print "__init__"

    def initialise(self):
        # load cell
        print "initialise"
        h.load_file("./IV_Model/iv_model.hoc")

model = IV_Model()
model.initialise()

h('get_IVdata(0)')
