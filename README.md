# UK wood end use flows

This repository is linked to the project "Robust modelling of material flows to end-uses under uncertainty: UK wood flows and material efficiency opportunities." which:
- provides a material flow map of wood for the UK in 2019 all the way to end-uses
- introduces a systematic method to handle mixed units during the reconciliation of material flows and uncertainty in data observations, conversion factors and process recipes.

## Contents

Data that are graphically represented in Figure 3 of the manuscript are stored in the "data_for_violin_plot_uncertainty_Figure_3_manuscript" and "data_from_sankey_figure_3_manuscript" folders:
- The excel file "data_from_sankey_figure_3_manuscript" contains the data that was used to draw the sankey diagram of Figure 3.
- The excel file "data_violin_plot_Figure_3" contains the data which was used to plot the violin plots of Figure 3.

The model's structure, observations, conversion factors and process recipes are stored in the following locations:
1. process recipes are described in the system-definitions\structure.md file. 
2. data observations are stored in the example_data_store\build\flows.csv file
3. conversion factors and their uncertainty characterisation and the uncertainty characterisation of recipe mixes are stored in data\uncertainty.py file.

The jupyter notebooks used to generate the data for:
- the violin plot showing uncertainty in finished product consumption in Figure 3 can be found in the data analysis folder "1- Data_for_Figure_3_violin_plot_finished_products_consumption" file.
- Table 2 showing discrepancies between observed and reconciled values can be found in the data analysis folder "1_Data_for_Table_2_reconciled_observed_values_comparison" file.

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