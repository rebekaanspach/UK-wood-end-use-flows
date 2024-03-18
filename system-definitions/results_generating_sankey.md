---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Results

```{code-cell} ipython3
from rdflib import Namespace
from sankey_helpers import show_skeleton
from sankey_helpers import guess_elements, guess_and_show, resolve_and_show_elements, elements_to_code, show_elements, show_skeleton, resolve_elements, elements_to_code
SYS = Namespace("http://ukfires.org/analyses/UK-wood/system/")
```

```{code-cell} ipython3
from semantic_sankeys import SankeyProcess, SankeyObject, SankeyElements
```

```{code-cell} ipython3
from semantic_sankeys.build_sdd import build_sdd
import pandas as pd
from semantic_sankeys.graphviz_graph import sdd_ordering
from floweaver import weave, CategoricalScale
```

```{code-cell} ipython3
%load_ext autoreload
%autoreload 2
import final_sdd
```

```{code-cell} ipython3
flows_mean = pd.read_excel(r"..\..\UK-wood-end-use-flows\data_for_sankey_figure_3_manuscript\data_sankey_Figure_3_mean.xlsx")
```

```{code-cell} ipython3
flows_mean_reset_index = flows_mean.reset_index()
```

```{code-cell} ipython3
flows_mean_reset_index
```

```{code-cell} ipython3
flows_mean_reset_index['is_trade'] = flows_mean_reset_index['is_trade'].map({0.0: False, 1.0: True})
```

```{code-cell} ipython3
flows_mean_reset_index.to_clipboard()
```

```{code-cell} ipython3
palette_names = {
    "Particleboard": "#d7bde2",
    "Fibreboard": "#d7bde2",
    "Veneer sheets": "#d7bde2",
    "Plywood": "#d7bde2",
    "Pulp": "#8ebfdd",
    "Recycled pulp": "lightgrey",
    "Other paper products": "#529dcb",
    "Graphic papers": "#529dcb",
    "Sanitary papers": "#529dcb",
    "Packaging": "#529dcb",
    "Commercial products": "#a957cd",
    "Softwood": "#228b22",
    "_": "#a6d89c",
    "Roundwood to energy production": "#228b22",
    "Hardwood": "#228b22",
    "Softwood Sawnwood": "#be93d1",
    "Hardwood Sawnwood": "#be93d1",
    "Furniture": "#a957cd", 
    "Fencing & outdoors": "#a957cd",
    "Pallets": "#a957cd",
    "Other products": "#a957cd",
    "Sawnwood to construction": "#8745a4",
    "Particleboard to construction": "#8745a4",
    "Other engineered products to construction": "#8745a4",
    "Joinery": "#8745a4",
    "Fibreboard to construction": "#8745a4",
    "Plywood to construction": "#8745a4",
    "New structures": "#8745a4",
    "Pre Consumer Waste Products":"lightgrey",
    "Industrial residues":"lightgrey",
    "Recycled fibres":"lightgrey",
    "Refurbished pallets": "#a957cd",
    "Other containers": "#a957cd",
    SYS["RecycledWoodFibres"]: "lightgrey",
    "Fibres to recycling": "lightgrey",
    "Recycled fibres to pallets": "lightgrey",
    SYS["EnergyIndustry"]: "#ff2727",
    "Recycled paper": "lightgrey",
    "By-products": "#74c365",
    SYS["FuelsForEnergy"]: "#ff2727",
    "Wood fibres for energy": "#ff7676",
    "Wood pellets": "#ff2727",
    "Other feedstocks": "#ff2727",
    SYS["OtherEnergyFeedstocksWoodFibres"]: "#ff7676",
        }
link_color = CategoricalScale(
    "type",
    palette_names,
    default="#888"
)
```

```{code-cell} ipython3
weave(final_sdd.sdd, flows_mean_reset_index, link_color=link_color).to_widget(width=1800, height=1800, debugging=True)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
