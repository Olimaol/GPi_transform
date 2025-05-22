from CompNeuroPy import load_variables, CompNeuroExp, create_dir
import core_parameters as params
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # load the results
    loaded_variables = load_variables(
        name_list=["results_exc", "results_inh"],
        path=params.VARYING_INPUTS_SAVE_FOLDER,
    )
    results_exc: CompNeuroExp._ResultsCl = loaded_variables["results_exc"]
    results_inh: CompNeuroExp._ResultsCl = loaded_variables["results_inh"]

    # get the coordinates / inputs
    x1 = results_exc.data["x1"]
    x2 = results_exc.data["x2"]

    # get the firing rates
    r1_exc = []
    r2_exc = []
    r1_inh = []
    r2_inh = []
    for chunk in range(len(x1)):
        r1_exc.append(np.mean(results_exc.recordings[chunk]["gpi;r"][:, 0]))
        r2_exc.append(np.mean(results_exc.recordings[chunk]["gpi;r"][:, 1]))
        r1_inh.append(np.mean(results_inh.recordings[chunk]["gpi;r"][:, 0]))
        r2_inh.append(np.mean(results_inh.recordings[chunk]["gpi;r"][:, 1]))

    # plot the results
    min_r = min(min(r1_exc), min(r2_exc), min(r1_inh), min(r2_inh))
    max_r = max(max(r1_exc), max(r2_exc), max(r1_inh), max(r2_inh))
    min_diff = min(
        min(np.array(r1_inh) - np.array(r1_exc)),
        min(np.array(r2_inh) - np.array(r2_exc)),
    )
    max_diff = max(
        max(np.array(r1_inh) - np.array(r1_exc)),
        max(np.array(r2_inh) - np.array(r2_exc)),
    )
    fig, ax = plt.subplots(3, 2, figsize=(12, 8))
    ax[0, 0].scatter(x1, x2, c=r1_exc, vmin=min_r, vmax=max_r, cmap="viridis")
    ax[0, 0].set_title("Rate of Neuron 1")

    ax[0, 1].scatter(x1, x2, c=r2_exc, vmin=min_r, vmax=max_r, cmap="viridis")
    ax[0, 1].set_title("Rate of Neuron 2")

    ax[1, 0].scatter(x1, x2, c=r1_inh, vmin=min_r, vmax=max_r, cmap="viridis")

    ax[1, 1].scatter(x1, x2, c=r2_inh, vmin=min_r, vmax=max_r, cmap="viridis")

    ax[2, 0].scatter(
        x1,
        x2,
        c=np.array(r1_inh) - np.array(r1_exc),
        vmin=min_diff,
        vmax=max_diff,
        cmap="viridis",
    )

    ax[2, 1].scatter(
        x1,
        x2,
        c=np.array(r2_inh) - np.array(r2_exc),
        vmin=min_diff,
        vmax=max_diff,
        cmap="viridis",
    )

    for ax_i in ax.flatten():
        ax_i.set_xlabel("Input Neuron 1")
        ax_i.set_ylabel("Input Neuron 2")
        ax_i.set_xlim(params.VARYING_INPUTS_INPUTS[0], params.VARYING_INPUTS_INPUTS[1])
        ax_i.set_ylim(params.VARYING_INPUTS_INPUTS[0], params.VARYING_INPUTS_INPUTS[1])
        ax_i.set_aspect("equal")
        ax_i.grid()

    plt.tight_layout()
    # add vertical row labels
    fig.text(0.02, 0.82, "Excitatory Laterals", va="center", rotation="horizontal")
    fig.text(0.02, 0.54, "Inhibitory Laterals", va="center", rotation="horizontal")
    fig.text(0.02, 0.26, "Difference", va="center", rotation="horizontal")

    cbar_r = fig.colorbar(
        ax[1, 1].collections[0], ax=[ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1]]
    )
    cbar_r.set_label("Firing rate")
    cbar_diff = fig.colorbar(ax[2, 1].collections[0], ax=[ax[2, 0], ax[2, 1]])
    cbar_diff.set_label("Difference in firing rate")

    create_dir(params.VARYING_INPUTS_SAVE_FOLDER + "/plots")
    plt.savefig(
        params.VARYING_INPUTS_SAVE_FOLDER + "/plots/varying_inputs.png", dpi=300
    )
