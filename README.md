### Goal:
transform inverse lateral excitation into lateral inhibition in the SNr/GPi.

### Task Scripts:
`simple_resting_run.py` - simple simulation of the SNr/GPi network with inverse lateral excitation. You can vary the input for the two neurons by hand and see the effect on the firing rate.

`varying_inputs_run.py` - multiple inputs for the two neurons are simulated and the firing rates are monitored. For the original inverse lateral excitation and the new lateral inhibition.

### Results:
Found equations to adjust baseline and lateral weight:
- $baseline_{inh} = weights_{exc}*(n-1)+baseline_{exc}$
- $weights_{inh} = (baseline_{inh}-baseline_{exc})/(n-1)$

Where $n$ is the number of neurons in the population.

Because the inverse synapse worked with `w * pos(1.0 - pre.r)`, rates higher than 1 did not lead to further reduction of lateral excitation. Thus the parameter adjustments only work perfect if the rates are below 1.

If necessary, the transition of the new inhibitory laterals could be cut at 1 (`w * clip(pre.r,0.0,1.0)`) to obtain the exact same behavior as before.