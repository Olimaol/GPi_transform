from core_model import gpi_model
from core_simulations import SimpleTrialGPi
from ANNarchy import simulate
from CompNeuroPy import CompNeuroMonitors, save_variables
import core_parameters as params

if __name__ == "__main__":
    # create and compile the model
    gpi_model.create()
    # create monitors recording the firing rate of the GPi population
    monitors = CompNeuroMonitors(mon_dict={"gpi": ["r"]})
    # create the experiment
    simple_trial = SimpleTrialGPi(monitors=monitors)
    # run 1000 ms resting period and store this state (of all populaitons and
    # projections) for the experiment
    simulate(1000)
    simple_trial.store_model_state(
        compartment_list=gpi_model.populations + gpi_model.projections
    )
    # run the experiment
    results = simple_trial.run(input=[-2.5, -1.2])
    # save the results
    save_variables(
        variable_list=[results],
        name_list=["results"],
        path=params.SIMPLE_RESTING_SAVE_FOLDER,
    )
