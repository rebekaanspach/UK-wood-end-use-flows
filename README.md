# UK wood end-use flows 

This repository is linked to the project ''**Robust modelling of material flows to end-uses under uncertainty: UK wood flows and material efficiency opportunities**'' which:
- provides a material flow map of wood for the UK in 2019 all the way to end-uses
- introduces a systematic method to handle mixed units during the reconciliation of material flows and uncertainty in data observations, conversion factors and process recipes.

## Contents

## Data and model's structure

Data that are graphically represented in Figure 3 of the paper are stored in:
- The excel file ''*data_for_sankey_figure_3_manuscript\data_sankey_Figure_3.xlsx*'' which contains the data used to draw the sankey diagram of Figure 3.
- The excel file ''*data_for_violin_plot_uncertainty_Figure_3_manuscript\data_violin_plot_Figure_3.xlsx*'' which contains the data used to plot the violin plots of Figure 3.

Data that are presented in Table 2 are stored in:
- The excel file ''*data_analysis\Data_for_Table_2_manuscript.xlsx*''

The model's structure (describing how the data fit together), known data observations and conversion factors are stored in the following locations:

1. **Model's structure (recipes)** and their uncertainty characterisation:

 - are stored in the ''*system-definitions\structure.md*'' file
 - are referenced in Table S3 of the supporting information (SI) (containing references to secondary data)
 - are described in Section S2.2 of the SI and in the ''*system-definitions\structure.md*'' file

2. **Data observations** and their uncertainty characterisation: 

 - are stored in the ''*example_data_store\datasources\UK_wood_data\UK_wood_observations.csv*'' file and Table S1 and S2 of the SI
 - are referenced in Table S1 and S2 of the SI (containing references to secondary data)
 - are described in Section S1 of the SI, in the ''*system-definitions\definitions.md*'' file and by the commodity codes given in Table S1 and S2 of the SI

3. **Conversion factors** and their uncertainty characterisation:

 - are stored in ''*data\uncertainty.py*'' file 
 - are referenced in Table S5-S7 of the SI
 - are described in Section S3 of the SI 

## Generating results
Data reconciliation generates the ''*\build\flows.csv*'' and ''*\build\flows_obs.csv*'' files.
There are three main jupyter notebook that use the ''*flows.csv*'' and ''*flows_obs.csv*'' files to produce the table and sankey diagram of the paper:
- the violin plot in Figure 3 showing uncertainty in finished product consumption is generated by running:

''*data_analysis\1_Data_for_Figure_3_violin_plot_finished_products_consumption.ipynb*''
- the data for Table 2 comparing observed and reconciled values is generated by running:

''*data_analysis\1_Data_for_Table_2_reconciled_observed_values_comparison.ipynb*''
- the mean values for each flow which is used to draw the sankey diagram is generated by running:

''*system-definitions\results_generating_data_for_sankey.ipynb*'' 
-  the sankey diagram in Figure 3 is generated by running:

''*system-definitions\results_generating_sankey.ipynb*''

## Installation

Using `conda`: run `conda env create` to create an environment called `UK-wood-end-use-flows` with the required packages (listed in `environment.yml`)

Activate this environment with `conda activate UK-wood-end-use-flows` before running the commands below.

## Building documentation pages

Run `doit`. Tasks that need to run RDFox need an extra argument `script_source_dir` to the Ontologies folder, for example:

```
doit run enhance_data script_source_dir=<...>
```

## License

Robust modelling of material flows to end-uses under uncertainty: UK wood flows and material efficiency opportunities. © 2023 by R. L. Anspach, S. R. Allen and R. C. Lupton is licensed under CC BY 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/