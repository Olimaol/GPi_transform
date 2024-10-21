from CompNeuroPy import CompNeuroExp
from ANNarchy import simulate, get_population, Projection, get_projection
import core_parameters as params
from core_model import LinearPopulation


class SimpleTrialGPi(CompNeuroExp):
    def run(self, input: float = None, baseline: float = None, weights: float = None):
        # reset and start monitoring
        self.reset()
        self.monitors.start()
        # set parameters
        gpi: LinearPopulation = get_population("gpi")
        gpi__gpi: Projection = get_projection("gpi__gpi")
        if input is not None:
            gpi.input = input
        if baseline is not None:
            gpi.B = baseline
        if weights is not None:
            gpi__gpi.w = weights
        # simulate
        simulate(params.SIMPLE_TRIAL_DURATION)
        # store optional data
        self.data["input"] = input
        self.data["baseline"] = baseline
        self.data["weights"] = weights
        # return results
        return self.results()
