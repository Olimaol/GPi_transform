from CompNeuroPy import load_variables, CompNeuroExp
import core_parameters as params

if __name__ == "__main__":
    # load the results
    loaded_variables = load_variables(
        name_list=["results"],
        path=params.VARYING_INPUTS_SAVE_FOLDER,
    )
    results: CompNeuroExp._ResultsCl = loaded_variables["results"]
    # TODO
