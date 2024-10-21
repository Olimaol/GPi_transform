from CompNeuroPy import CompNeuroModel
from ANNarchy import Synapse, Population, Neuron, Projection
import core_parameters as params
import numpy as np

reversed_synapse = Synapse(
    psp="""
        w * pos(1.0 - pre.r)
    """,
    name="Reversed Synapse",
    description="Higher pre-synaptic activity lowers the synaptic transmission and vice versa.",
)


class LinearPopulation(Population):
    """
    Population which uses the linear neuron as neuron model.
    """

    linear_neuron = Neuron(
        parameters="""
        tau = 'tau' : population
        phi = 'phi' : population
        B = 'B'
        input = 'input'
        """,
        equations="""
        net_input = sum(exc) - sum(inh) + B + input + phi * Uniform(-1.0,1.0)
        tau * dmp/dt = -mp + net_input
        r = pos(mp)
        """,
        name="Linear Neuron",
        description="Regular rate-coded neuron with excitatory and inhibitory inputs plus baseline and noise.",
        extra_values=params.LINEAR_NEURON_DEFAULT_PARAMETERS,
    )

    def __init__(
        self,
        geometry: tuple | int,
        name: str = None,
        stop_condition: str = None,
        storage_order: str = "post_to_pre",
        copied=False,
    ):

        ### annotate types for automatically added attributes

        ### parameters
        self.tau: float
        self.phi: float
        self.B: np.ndarray
        self.input: np.ndarray

        ### variables
        self.mp: np.ndarray
        self.r: np.ndarray

        ### call parent constructor
        super().__init__(
            geometry, self.linear_neuron, name, stop_condition, storage_order, copied
        )


def create_model(
    baseline=params.GPI_BASELINE, weights=params.GPI__GPI_WEIGHTS, laterals="exc"
):
    """
    Create a GPi population and lateral connections. The default is how it is
    implemented in the original model, with excitatory laterals.

    Args:
        baseline (float, optional):
            Baseline input of the GPi population.
        weights (float, optional):
            Weight of the lateral connections.
        laterals (str, optional):
            Type of lateral connections. Must be either 'exc' or 'inh'.
    """
    ### create GPi population
    gpi = LinearPopulation(geometry=params.GPI_GEOMETRY, name="gpi")
    gpi.phi = params.GPI_PHI
    gpi.B = baseline
    ### create lateral connections
    if laterals == "exc":
        gpi__gpi = Projection(
            pre=gpi, post=gpi, target="exc", synapse=reversed_synapse, name="gpi__gpi"
        )
        gpi__gpi.connect_all_to_all(weights=weights)
    elif laterals == "inh":
        gpi__gpi = Projection(pre=gpi, post=gpi, target="inh", name="gpi__gpi")
        gpi__gpi.connect_all_to_all(weights=weights)
    else:
        raise ValueError(
            f"Invalid value for laterals: {laterals}. Must be 'exc' or 'inh'."
        )


gpi_model = CompNeuroModel(
    model_creation_function=create_model,
    name="GPi model",
    description="GPi neurons either with inversed excitatory or 'normal' inhibitory laterals",
    do_create=False,
    do_compile=False,
    compile_folder_name="gpi_model",
)
