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
from floweaver import weave, CategoricalScale
```

```{code-cell} ipython3
from sankey_helpers import load_flows, FLOWS_FILENAME
dataset = load_flows(FLOWS_FILENAME)
flows = dataset.query("solution == 'Only solution found'") 
```

```{code-cell} ipython3
flows_mean=flows.groupby(["source", "target", "material"], as_index=False).mean()
```

```{code-cell} ipython3
flows_mean.to_excel(r"..\..\UK-wood-end-use-flows\data_for_sankey_figure_3_manuscript\data_sankey_Figure_3_mean.xlsx")
```

```{code-cell} ipython3
flows_mean
```

```{code-cell} ipython3

```
