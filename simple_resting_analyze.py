from CompNeuroPy import load_variables, PlotRecordings, CompNeuroExp
import core_parameters as params

if __name__ == "__main__":
    # load the results
    loaded_variables = load_variables(
        name_list=["results"],
        path=params.SIMPLE_RESTING_SAVE_FOLDER,
    )
    results: CompNeuroExp._ResultsCl = loaded_variables["results"]
    # plot the firing rates of the GPi population
    PlotRecordings(
        figname=f"{params.SIMPLE_RESTING_SAVE_FOLDER}/plots/gpi_firing_rate.png",
        recordings=results.recordings,
        recording_times=results.recording_times,
        shape=(1, 1),
        plan={
            "position": [1],
            "compartment": ["gpi"],
            "variable": ["r"],
            "format": ["line"],
        },
    )
