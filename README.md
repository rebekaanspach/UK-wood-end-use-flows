# UK wood end use flows


## Contents

Data that are graphically represented in Figure 3 are stored in the "data_for_violin_plot_uncertainty_Figure_3_manuscript" and "data_from_sankey_figure_3_manuscript" folders.
- The excel file "data_from_sankey_figure_3_manuscript" contains the data that was used to draw the sankey diagram in Figure 3.
- The excel file "data_box_plot_Figure_3" contains the data which was used to plot the violin plots in Figure 3.


1. in system-definitions the structure.md file describes process recipes. 
2. data observations are stored in the data folder in the flows.csv file
3. conversion factors and their uncertainty characterisation and the uncertainty characterisation of recipe mixes is stored in the data folder and the uncertainty-py file. 


## Installation

Using `conda`: run `conda env create` to create an environment called `UK-wood-end-use-flows` with the required packages (listed in `environment.yml`)

Activate this environment with `conda activate UK-wood-end-use-flows` before running the commands below.

## Structure

1. Data sources / knowledge graph

   It's very simple in this case -- but the data is first assembled into an RDF "knowledge graph".
   
   This is then loaded and enhanced with the PRObs RDFox algorithm and made available for querying.
   .
   
2. Model structure

   This is defined in the `system-definitions` files and extracted to RDF.

## Building documentation pages

Run `doit`. Tasks that need to run RDFox need an extra argument `script_source_dir` to the Ontologies folder, for example:

```
doit run enhance_data script_source_dir=<...>
```

## License

Robust modelling of material flows to end-uses under uncertainty: UK wood flows and material efficiency opportunities. © 2023 by R. L. Anspach, S. R. Allen and R. C. Lupton is licensed under CC BY 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/