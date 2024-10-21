from CompNeuroPy import run_script_parallel, create_data_raw_folder
import core_parameters as params


if __name__ == "__main__":
    if params.VARYING_INPUTS_SIMULATE:
        ### create the data folder
        create_data_raw_folder(
            folder_name=params.VARYING_INPUTS_SAVE_FOLDER,
            parameter_module=params,
        )
        ### run the simulation (single script call)
        run_script_parallel(
            script_path="varying_inputs.py",
            n_jobs=params.N_JOBS,
        )
    if params.VARYING_INPUTS_ANALYZE:
        ### run the analysis (single script call)
        run_script_parallel(
            script_path="varying_inputs_analyze.py",
            n_jobs=params.N_JOBS,
        )
