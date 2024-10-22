from core_model import gpi_model
from core_simulations import VaryingInputGPi
from ANNarchy import simulate
from CompNeuroPy import CompNeuroMonitors, save_variables
import core_parameters as params
import sys

if __name__ == "__main__":
    # create and compile the model
    # raise error if sys.argv[1] is not "exc" or "inh"
    if sys.argv[1] == "exc":
        # use default parameters, just pass
        pass
    elif sys.argv[1] == "inh":
        # switch to inhibitory laterals and therefore change the weights and baseline
        gpi_model.model_kwargs = {
            "baseline": params.GPI__GPI_WEIGHTS * (params.GPI_GEOMETRY - 1)
            + params.GPI_BASELINE,
            "weights": (
                (
                    params.GPI__GPI_WEIGHTS * (params.GPI_GEOMETRY - 1)
                    + params.GPI_BASELINE
                )
                - params.GPI_BASELINE
            )
            / (params.GPI_GEOMETRY - 1),
            "laterals": "inh",
        }
        # change compile folder name
        gpi_model.compile_folder_name = gpi_model.compile_folder_name + "_inh"
    else:
        raise ValueError(
            f"Invalid value for first script argument: {sys.argv[1]}. Must be 'exc' or 'inh'."
        )
    gpi_model.create()
    # create monitors recording the firing rate of the GPi population
    monitors = CompNeuroMonitors(mon_dict={"gpi": ["r"]})
    # create the experiment
    simple_trial = VaryingInputGPi(monitors=monitors)
    # run 1000 ms resting period and store this state (of all populations and
    # projections) for the experiment
    simulate(1000)
    simple_trial.store_model_state(
        compartment_list=gpi_model.populations + gpi_model.projections
    )
    # run the experiment
    results = simple_trial.run()
    # save the results
    save_variables(
        variable_list=[results],
        name_list=[f"results_{sys.argv[1]}"],
        path=params.VARYING_INPUTS_SAVE_FOLDER,
    )
