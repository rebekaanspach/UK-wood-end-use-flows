# Derivations of equations in the paper's spreadsheet

The global glass MFA paper's supporting information contains a spreadsheet with all the calculations used to produce the MFA model and Sankey diagram flows. However, these are the "final" versions of the equations and it's not easy to see how they have been derived or why they are correct. In this section we will start with the expanded model structure defined previously here, and show how the spreadsheet equations can be derived.

## Our model structure

The structure of this model is based on simple linear descriptions of each process. That is, the material inputs and outputs associated with a "unit" level of operation of the process are:

\begin{align}
u_{ij} &= \text{use of material $i$ in process $j$} \\
s_{ij} &= \text{supply of material $i$ from process $j$}
\end{align}

If the process is operating at a level $X_j$ then the actual flow of material $i$ into the process is scaled up as $X_j u_{ij}$.

## Differences between processes between the two models

The melting processes `FGM` and `CGM` have been split into 2 or 3 separate sub-processes, compared to the spreadsheet model. This is because the model is based on linear recipes for each process, which scale up and down in proportion. In contrast, the melting process in the spreadsheet calculates the flows based on this logic:
- Assume that the recycled cullet input produces molten glass directly
- Emissions are proportional to production from raw materials
- The shares of different raw materials are fixed fractions of the total *raw material* input, not of the total process throughput.

These assumptions can be modelled by splitting the single melting process into 2 or 3 separate sub-processes, each with a linear recipe, as shown below.

## Approach and terminology

We will relate the variables of our model ($X_j$, $u_{ij}$ and $s_{ij}$ to the variables and parameters used in the spreadsheet, and show that the flows can be described equivalently using either set of variables.

The quantities used in the spreadsheet are:

| Symbol        | Meaning                                    | Spreadsheet cell (in flows sheet unless specified) |
|---------------+--------------------------------------------+----------------------------------------------------|
| $G_1$         | Global production of container glass       | `Container glass ! D13`                            |
| $G_2$         | Global production of flat glass            | `Flat glass ! D18`                                 |
| $\alpha_1$    | Share of primary production from soda      | `J1`                                               |
| $\alpha_2$    | Share of primary production from limestone | `J2`                                               |
| $\alpha_3$    | Share of primary production from silica    | `J3`                                               |
| $\beta$       | Batch-to-melt yield                        | `J4`                                               |
| $\gamma_1$    | Container glass fabrication yield loss     | `J5`                                               |
| $\gamma_2$    | Flat glass fabrication yield loss          | `J6`                                               |
| $\delta_{11}$ | Share of CG to beverages                   | `J7`                                               |
| $\delta_{12}$ | Share of CG to food                        | `J8`                                               |
| $\delta_{13}$ | Share of CG to other                       | `J9`                                               |
| $\delta_{21}$ | Share of FG to buildings                   | `J10`                                              |
| $\delta_{22}$ | Share of FG to automotive                  | `J11`                                              |
| $\delta_{23}$ | Share of FG to other                       | `J12`                                              |

## Flat glass

This diagram shows the flat glass processes and their inputs and outputs. The numbering is equivalent to the naming used here, for example $X_{\mathrm{FGF}}$ below is the same thing as $X_{2}$ in the diagram.
![diagram of flat glass processes and objects](images/glass_model_FG_diagram.png)

### Flat glass forming

Let's start with the input of molten glass to the forming process `FGF`. In our system notation this flow is

$$ X_{\mathrm{FGF}} u_{\mathrm{MoltenFG},\mathrm{FGF}} $$

Since the process has only one input, we know that $u_{\mathrm{MoltenFG},\mathrm{FGF}} = 1$ and this can immediately be simplified. In the spreadsheet, the equation for this flow is in cell `D10`: `'Flat glass'!$D$18/(1-$J$6)`, or in other words,

$$ \frac{G_{2}}{1 - \gamma_2} $$

Equating these we can discover that:

$$ X_{\mathrm{FGF}} = \frac{G_{2}}{1 - \gamma_2} $$

Now consider the output of flat glass `FG` from the forming process `FGF`. This is simply equal to $G_{2}$ (in the spreadsheet it's split into 3 flows in cells `D17:D19`). Equating this to the output flow in our notation,

$$ X_{\mathrm{FGF}} s_{\mathrm{FG},\mathrm{FGF}} = G_{2} $$

Comparing this to the equation above, we can deduce that

$$ s_{\mathrm{FG},\mathrm{FGF}} = 1 - \gamma_2 $$

This makes sense, since $\gamma_{2}$ is the fabrication yield *loss*, so $1 - \gamma_2$ should indeed be the fraction of the process which is useful output. Since the process has only the two outputs, and we know that for mass to be conserved between the inputs and the outputs of the process we need

$$ \sum_{i} u_{i, \mathrm{FG}} = \sum_{i} s_{i, \mathrm{FG}} $$

we can conclude that

$$ s_{\mathrm{FGCullet},\mathrm{FGF}} = \gamma_2 $$

You can verify that using this coefficient to calculate the flow of forming cullet out of the `FGF` process gives the same result as the spreadsheet equation in cell `D13`.

### Flat glass melting

By applying the principle of conservation of mass for each object type, we can relate the variables for the `FGF` process across to the `FGM` process on the left-hand side.

First, we can say that production and consumption of `FGCullet` must balance each other. In general, this could be written as:

$$ \sum_{j} X_{j} s_{\mathrm{FGCullet},j} - \sum_{j} X_{j} u_{\mathrm{FGCullet},j} + v_{\mathrm{FGCullet}} - w_{\mathrm{FGCullet}} = \Delta S_{\mathrm{FGCullet}} $$

Our model is global, so there can be no imports $v$ or exports $w$. We also assume that there is no stock accumulation $\Delta S$. So this simplifies to:

$$ \sum_{j} X_{j} s_{\mathrm{FGCullet},j} = \sum_{j} X_{j} u_{\mathrm{FGCullet},j} $$

Since there is only one process that produces the material, and only one process which consumes it, specifically this general conservation equation becomes simply

$$
\begin{align}
X_{\mathrm{FGF}} s_{\mathrm{FGCullet},\mathrm{FGF}} &= X_{\mathrm{SecondaryFGM}} u_{\mathrm{FGCullet},\mathrm{SecondaryFGM}} \\
X_{\mathrm{FGF}} \gamma_{2} &= X_{\mathrm{SecondaryFGM}} \\
\end{align}
$$

Next, by comparing the raw material inputs to `PrimaryFGM` against the spreadsheet formula (cells `D2` to `D4`), we can relate the process scale parameter $X_{\mathrm{PrimaryFGM}}$ to the other parameters:

$$ 
\sum_{i} X_{\mathrm{PrimaryFGM}} u_{i,\mathrm{PrimaryFGM}} = \sum_k \left[ G_{2} + G_{2} \frac{1 - \beta}{\beta} \right] \alpha_{k}
$$

By convention we normalise the use coefficients to sum to 1, and the $\alpha_{k}$ coefficients also sum to 1, so this simplifies to

$$ 
X_{\mathrm{PrimaryFGM}} = G_{2} + G_{2} \frac{1 - \beta}{\beta} = \frac{G_{2}}{\beta}
$$ (eq:X_PrimaryFGM)

Next, by comparing the emissions from process `FGM` against the spreadsheet formula (cell `D11`), we can work out the meaning of the parameter $\beta$:

$$ 
X_{\mathrm{PrimaryFGM}} s_{\mathrm{Emissions},\mathrm{PrimaryFGM}} = G_{2} \frac{1 - \beta}{\beta}
$$

Substituting in from {eq}`eq:X_PrimaryFGM` shows that

$$ 
s_{\mathrm{Emissions},\mathrm{PrimaryFGM}} = 1 - \beta
$$

As before, since the sum of the supply coefficients for the process should sum to 1 for conservation of mass across the process, we find that

$$ 
s_{\mathrm{MoltenFG},\mathrm{PrimaryFGM}} = \beta
$$

This makes sense since $\beta$ is described as a yield factor.

As a final check for consistency, let us derive the flow from `FGM` to `FGF` (cell `D10`) from two directions. 
We expect that the material `MoltenFG` is conserved, that is production and consumption are equal. The total consumption of `MoltenFG` has already been described above.

$$
\begin{align}
X_{\mathrm{PrimaryFGM}} s_{\mathrm{MoltenFG},\mathrm{PrimaryFGM}} +
X_{\mathrm{SecondaryFGM}} s_{\mathrm{MoltenFG},\mathrm{SecondaryFGM}}
&= X_{\mathrm{FGF}} u_{\mathrm{MoltenFG},\mathrm{FGF}} \\
\frac{G_{2}}{\beta} \times \beta +
\frac{G_{2} \gamma_{2}}{1 - \gamma_{2}} \times 1 
&= \frac{G_{2}}{1 - \gamma_2} \times 1
\end{align}
$$

which does indeed balance.

## Container glass

This is similar to flat glass. The main difference is that there are two recycling loops. The spreadsheet model treats these both like the recycled flat glass cullet, i.e. they are ignored for the purposes of defining the share of raw materials and the emissions. Hence we model "container glass melting" with three separate processes.

## Summary

We have started with a definition of an [expanded] set of processes using the "PACTOT" model structure: a process activity level $X_{j}$ and linear recipes $u_{ij}$ and $s_{ij}$. By equating this model structure to the known starting flows from the spreadsheet model ($G_{1}$ and $G_{2}$) and the coefficients used there ($\beta$, $\gamma$ and $\delta$), we have shown that the two models are equivalent.

In other words, we start with a set of simpler but redundant equations for the process inputs and outputs. By adding the conservation of mass constraints, we can eliminate some of the original unknown variables and reach a set of expressions for each flow value in terms of the original input values. But in the process, the physical structure and interpretation of the expressions becomes harder to follow.
