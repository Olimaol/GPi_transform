from CompNeuroPy import run_script_parallel, create_data_raw_folder
import core_parameters as params


if __name__ == "__main__":
    if params.SIMPLE_RESTING_SIMULATE:
        ### create the data folder
        create_data_raw_folder(
            folder_name=params.SIMPLE_RESTING_SAVE_FOLDER,
            parameter_module=params,
        )
        ### run the simulation (single script call)
        run_script_parallel(
            script_path="simple_resting.py",
            n_jobs=params.N_JOBS,
        )
    if params.SIMPLE_RESTING_ANALYZE:
        ### run the analysis (single script call)
        run_script_parallel(
            script_path="simple_resting_analyze.py",
            n_jobs=params.N_JOBS,
        )
