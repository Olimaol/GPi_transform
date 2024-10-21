from CompNeuroPy import CompNeuroExp
from ANNarchy import simulate, get_population, Projection, get_projection
import core_parameters as params
from core_model import LinearPopulation
import numpy as np


class SimpleTrialGPi(CompNeuroExp):
    """
    Just a simple trial with the GPi population. You can set the input, the
    baseline, and the lateral weights of the GPi population.
    """

    def run(self, input: float = None, baseline: float = None, weights: float = None):
        # reset GPi population and lateral weights
        self.reset(projections=True)
        # set parameters
        gpi: LinearPopulation = get_population("gpi")
        gpi__gpi: Projection = get_projection("gpi__gpi")
        if input is not None:
            gpi.input = input
        if baseline is not None:
            gpi.B = baseline
        if weights is not None:
            gpi__gpi.w = weights
        # start monitoring
        self.monitors.start()
        # simulate
        simulate(params.SIMPLE_TRIAL_DURATION)
        # store optional data
        self.data["input"] = input
        self.data["baseline"] = baseline
        self.data["weights"] = weights
        # return results
        return self.results()


class VaryingInputGPi(CompNeuroExp):
    """
    Simulate multiple trials (recording chunks) with varying inputs for two GPi neurons.
    """

    def run(self, baseline: float = None, weights: float = None):
        # reset GPi population and lateral weights (using projections=True and stored
        # model state)
        self.reset(projections=True)
        # set parameters
        gpi: LinearPopulation = get_population("gpi")
        gpi__gpi: Projection = get_projection("gpi__gpi")
        if baseline is not None:
            gpi.B = baseline
        if weights is not None:
            gpi__gpi.w = weights
        # create combinations of increasing input for two GPi neurons
        # unique input values
        x1 = np.linspace(0.0, 1.0, 5)
        x2 = np.linspace(0.0, 1.0, 5)
        # create meshgrid for all combinations
        x1, x2 = np.meshgrid(x1, x2)
        # flatten
        x1 = x1.ravel()
        x2 = x2.ravel()
        nr_trials = len(x1)
        # start monitoring
        self.monitors.start()
        # simulate trials
        for trial in range(nr_trials):
            # reset GPi population without resetting the parameters (baseline)
            self.reset(parameters=False)
            # set input
            gpi.input = [x1[trial], x2[trial]]
            # simulate
            simulate(params.SIMPLE_TRIAL_DURATION)
        # store optional data
        self.data["baseline"] = baseline
        self.data["weights"] = weights
        self.data["nr_trials"] = nr_trials
        self.data["x1"] = x1
        self.data["x2"] = x2
        # return results
        return self.results()
