# general
N_JOBS = 1

# "linear neuron" neuron model's default values
LINEAR_NEURON_DEFAULT_PARAMETERS = {
    "tau": 10.0,
    "phi": 0.0,
    "B": 0.0,
    "input": 0.0,
}
# GPi population
GPI_GEOMETRY = 2
GPI_PHI = 0.1
GPI_BASELINE = 1.2
# GPi to GPi connection
GPI__GPI_WEIGHTS = 0.9

# simulations
# SimpleTrialGPi
SIMPLE_TRIAL_DURATION = 500.0

# task scripts
# simple_resting
SIMPLE_RESTING_SIMULATE = True
SIMPLE_RESTING_ANALYZE = True
SIMPLE_RESTING_SAVE_FOLDER = "simple_resting_data"
