#!/usr/bin/env python
# coding: utf-8

import os

import logging

log = logging.getLogger(__name__)

from copy import deepcopy
from pathlib import Path
import numpy as np
from scipy import stats
import pandas as pd
import yaml
from rdflib import Namespace

from probs_runner import probs_endpoint
from probs_models.models import pactot
from probs_models.observations import ConsumptionFractionObs
from query_model import query_model_from_endpoint, SYS
from distributions import make_uniform_distribution

# from data.uncertainty_data import conversion_factor_distributions_1, input_distribution_params, output_distribution_params


def make_normal_distribution_recipe(mean, sd):
    loc = np.array([old_value for (obj, metric, old_value) in mean])
    scale = sd
    rv = stats.norm(loc, scale)

    def _sample_normal():
        return rv.rvs(size=1)

    return _sample_normal


def make_dirichlet_distribution(tuples, concentration):
    alpha = np.array([old_value for (obj, metric, old_value) in tuples])
    rv = stats.dirichlet(alpha * concentration)

    def _sample_dirichlet():
        return rv.rvs(size=1)[0]

    return _sample_dirichlet


# Set up the distributions for sampling conversion factors

SYS = Namespace("http://ukfires.org/analyses/UK-wood/system/")
QUANTITYKIND = Namespace("http://qudt.org/vocab/quantitykind/")

paper_distribution = make_uniform_distribution((1 / 1.06), (1 / 1.04))
pulp_distribution = make_uniform_distribution((1 / 1.06), (1 / 1.04))
no_distribution = make_uniform_distribution(1, 1)

conversion_factor_distributions_1 = {
    # Roundwood
    (QUANTITYKIND.GreenMass, SYS.SoftwoodRoundwood): make_uniform_distribution(
        (1 / 1.018), (1 / 1.018)
    ),
    (QUANTITYKIND.GreenMass, SYS.HardwoodRoundwood): make_uniform_distribution(
        (1 / 1.143), (1 / 1.143)
    ),
    (QUANTITYKIND.Mass, SYS.SoftwoodRoundwood): make_uniform_distribution(
        (1 / 1.018), (1 / 1.018)
    ),
    (QUANTITYKIND.Mass, SYS.RoundwoodToFencingAndOutdoor): make_uniform_distribution(
        (1 / 1.018), (1 / 1.018)
    ),
    # Sawnwood
    (QUANTITYKIND.Volume, SYS.SoftwoodSawnwood): make_uniform_distribution(1.06, 1.1),
    (QUANTITYKIND.Volume, SYS.HardwoodSawnwood): make_uniform_distribution(1.06, 1.1),
    # Wood-based panels
    (QUANTITYKIND.Volume, SYS.Fibreboard): make_uniform_distribution((1.85), (1.85)),
    (QUANTITYKIND.Volume, SYS.Particleboard): make_uniform_distribution(1.54, 1.68),
    (QUANTITYKIND.Volume, SYS.VeneerSheets): make_uniform_distribution(1, 1),
    (QUANTITYKIND.Volume, SYS.Plywood): make_uniform_distribution(0.96, 0.96),
    (QUANTITYKIND.Mass, SYS.OtherEngineeredWoodProducts): make_uniform_distribution(
        1 / 0.595, 1 / 0.464
    ),
    (QUANTITYKIND.Mass, SYS.WBPFibres): no_distribution,
    # By-products, post-consumer wood, waste and recycled wood fibre
    (QUANTITYKIND.GreenMass, SYS.ByProducts): make_uniform_distribution(
        (1 / 1.043), (1 / 1.018)
    ),
    (QUANTITYKIND.Mass, SYS.ByProducts): make_uniform_distribution(0.87, 0.98),
    (QUANTITYKIND.GreenMass, SYS.RecycledWoodFibre): make_uniform_distribution(
        (1 / 1.043), (1 / 1.018)
    ),
    (QUANTITYKIND.Mass, SYS.RecycledWoodFibre): make_uniform_distribution(
        (1 / 0.595), (1 / 0.467)
    ),
    (QUANTITYKIND.Mass, SYS.PreConsumerWasteProducts): no_distribution,
    (QUANTITYKIND.Mass, SYS.PreConsumerWasteConstruction): no_distribution,
    (QUANTITYKIND.Mass, SYS.RecycledWoodFibreToPallets): no_distribution,
    (QUANTITYKIND.Mass, SYS.PostConsumerWood): make_uniform_distribution(
        (1 / 0.595), (1 / 0.467)
    ),
    (QUANTITYKIND.Volume, SYS.PostConsumerWood): no_distribution,
    # Pulp and paper
    (QUANTITYKIND.Mass, SYS.GraphicPapers): make_uniform_distribution(
        ((1 - 0.30) / (0.467 * (1 + 0.06))), ((1 - 0.10) / (0.467 * (1 + 0.04)))
    ),
    (QUANTITYKIND.Mass, SYS.SanitaryPapers): make_uniform_distribution(
        (1 / (0.467 * (1 + 0.06))), (1 / (0.467 * (1 + 0.04)))
    ),
    (QUANTITYKIND.Mass, SYS.Packaging): make_uniform_distribution(
        ((1 - 0.10) / (0.467 * (1 + 0.06))), ((1 - 0.10) / (0.467 * (1 + 0.04)))
    ),
    (QUANTITYKIND.Mass, SYS.OtherPaperProducts): make_uniform_distribution(
        ((1 - 0.23) / (0.467 * (1 + 0.06))), ((1 - 0.23) / (0.467 * (1 + 0.04)))
    ),
    (QUANTITYKIND.Mass, SYS.Pulp): make_uniform_distribution(1 / 0.495, 1 / 0.449),
    (QUANTITYKIND.Mass, SYS.RecycledPulp): no_distribution,
    (QUANTITYKIND.Mass, SYS.NewPulp): no_distribution,
    (QUANTITYKIND.Mass, SYS.RecycledPaper): make_uniform_distribution(
        1 / 0.628, 1 / 0.628
    ),
    # Furniture
    (QUANTITYKIND.Dimensionless, SYS.WoodenOfficeFurniture): make_uniform_distribution(
        ((10 * (1 - 0.09)) / (0.595 * (1 + 0.19))),
        ((25 * (1 - 0.01)) / (0.595 * (1 + 0.06))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.WoodenBedroomFurniture): make_uniform_distribution(
        ((15 * (1 - 0.09)) / (0.595 * (1 + 0.19))),
        ((35 * (1 - 0.01)) / (0.467 * (1 + 0.106))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.WoodenKitchenFurniture): make_uniform_distribution(
        ((10 * (1 - 0.09)) / (0.595 * (1 + 0.19))),
        ((20 * (1 - 0.09)) / (0.464 * (1 + 0.19))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.WoodenOtherFurniture): make_uniform_distribution(
        ((5 * (1 - 0.09)) / (0.595 * (1 + 0.19))),
        ((30 * (1 - 0.09)) / (0.464 * (1 + 0.19))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.WoodenSeats): make_uniform_distribution(
        ((8 * (1 - 0.09)) / (0.595 * (1 + 0.19))),
        ((15 * (1 - 0.09)) / (0.464 * (1 + 0.19))),
    ),
    (QUANTITYKIND.Mass, SYS.WoodenOfficeFurniture): make_uniform_distribution(
        (0.91 / (0.595 * (1 + 0.19))), ((1 - 0.01) / (0.595 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.WoodenBedroomFurniture): make_uniform_distribution(
        ((1 - 0.09) / (0.595 * (1 + 0.19))), ((1 - 0.01) / (0.595 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.WoodenKitchenFurniture): make_uniform_distribution(
        ((1 - 0.09) / (0.595 * (1 + 0.19))), ((1 - 0.01) / (0.595 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.WoodenOtherFurniture): make_uniform_distribution(
        ((1 - 0.09) / (0.595 * (1 + 0.19))), ((1 - 0.01) / (0.595 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.WoodenSeats): make_uniform_distribution(
        ((1 - 0.09) / (0.595 * (1 + 0.19))), ((1 - 0.01) / (0.595 * (1 + 0.06)))
    ),
    # Fencing
    (QUANTITYKIND.Mass, SYS.FencingPosts): make_uniform_distribution(
        (1 / 1.043), (1 / 1.018)
    ),
    (QUANTITYKIND.Mass, SYS.FencingRailsAndBoards): no_distribution,
    (QUANTITYKIND.Dimensionless, SYS.WoodenOutbuildings): make_uniform_distribution(
        (1 / (6 * 0.595)), (1 / (2 * 0.467))
    ),
    (QUANTITYKIND.Mass, SYS.RailwaySleepers): make_uniform_distribution(
        (1 / (1 + 0.08)), (1 / (1 + 0.06))
    ),
    # Building elements
    (QUANTITYKIND.Mass, SYS.Frames): no_distribution,
    (QUANTITYKIND.Mass, SYS.Roof): no_distribution,
    (QUANTITYKIND.Mass, SYS.UpperFloors): no_distribution,
    # RMI
    (QUANTITYKIND.Mass, SYS.PlywoodToRMIAndOther): no_distribution,
    (QUANTITYKIND.Mass, SYS.ParticleboardToRMIAndOther): no_distribution,
    (QUANTITYKIND.Mass, SYS.FibreboardToRMIAndOther): no_distribution,
    (QUANTITYKIND.Mass, SYS.SoftwoodSawnwoodToRMIAndOther): no_distribution,
    # NewBuilds
    (QUANTITYKIND.Mass, SYS.NewBuilds): no_distribution,
    # Other energy feedstocks
    (QUANTITYKIND.Mass, SYS.OtherEnergyFeedstocks): make_uniform_distribution(
        ((11630000 * 0.0036) / (0.595 * (1 + 0.20) * 20.3)),
        ((11630000 * 0.0036) / (0.595 * (1 + 0.1) * 16.3)),
    ),
    (QUANTITYKIND.Volume, SYS.OtherEnergyFeedstocksWoodFibres): no_distribution,
    (QUANTITYKIND.Mass, SYS.WoodCharcoal): make_uniform_distribution(1.65, 1.65),
    # Industrial packaging
    (QUANTITYKIND.Mass, SYS.Pallets): make_uniform_distribution(
        ((1 - 0.02) / (0.467 * (1 + 0.30))), ((1 - 0.02) / (0.467 * (1 + 0.22)))
    ),
    (QUANTITYKIND.Dimensionless, SYS.Pallets): make_uniform_distribution(
        ((15 * (1 - 0.02)) / (0.467 * (1 + 0.30))),
        (25 * (1 - 0.02) / (0.467 * (1 + 0.22))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.RefurbishedPallets): make_uniform_distribution(
        (15 * (1 - 0.02) / (0.467 * (1 + 0.30))),
        (25 * (1 - 0.02) / (0.467 * (1 + 0.22))),
    ),
    (QUANTITYKIND.Mass, SYS.OtherWoodContainers): make_uniform_distribution(
        ((1 - 0.02) / (0.467 * (1 + 0.30))), ((1 - 0.02) / (0.467 * (1 + 0.22)))
    ),
    # Wood pellets
    (QUANTITYKIND.Mass, SYS.WoodPellets): make_uniform_distribution(1.44, 1.53),
    (QUANTITYKIND.Mass, SYS.WoodPelletsWoodFibres): no_distribution,
    (QUANTITYKIND.Volume, SYS.WoodPelletsWoodFibres): no_distribution,
    # Joinery
    (QUANTITYKIND.Mass, SYS.Windows): make_uniform_distribution(
        (1 - 0.19) / (0.467 * (1 + 0.06)), ((1 - 0.02) / (0.467 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Dimensionless, SYS.Windows): make_uniform_distribution(
        ((10 * (1 - 0.19)) / (0.467 * (1 + 0.06))),
        ((35 * (1 - 0.02)) / (0.467 * (1 + 0.06))),
    ),
    (QUANTITYKIND.Mass, SYS.Doors): make_uniform_distribution(
        ((1 - 0.09) / (0.467 * (1 + 0.19))), ((1 - 0.01) / (0.467 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.Flooring): make_uniform_distribution(
        ((1 - 0.09) / (0.467 * (1 + 0.19))), ((1 - 0.01) / (0.467 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Area, SYS.Flooring): make_uniform_distribution(
        ((9.5 * (1 - 0.09)) / (0.467 * (1 + 0.09))),
        ((9.5 * (1 - 0.01)) / (0.467 * (1 + 0.09))),
    ),
    (QUANTITYKIND.Dimensionless, SYS.Doors): make_uniform_distribution(
        ((19 * (1 - 0.09)) / (0.467 * (1 + 0.19))),
        ((25 * (1 - 0.01)) / (0.467 * (1 + 0.06))),
    ),
    # Others
    (QUANTITYKIND.Mass, SYS.FormworkScaffolding): make_uniform_distribution(
        (1 / (0.467 * (1 + 0.14))), (1 / (0.467 * (1 + 0.09)))
    ),
    (QUANTITYKIND.Mass, SYS.OtherObjects): make_uniform_distribution(
        ((1 - 0.09) / (0.467 * (1 + 0.09))), ((1 - 0.01) / (0.467 * (1 + 0.06)))
    ),
    (QUANTITYKIND.Mass, SYS.WoodWoolAndFlour): make_uniform_distribution(
        (1 / 1.018), (1 / 1.018)
    ),
}


# Set up the distributions for sampling different inputs
input_distribution_params = {
    SYS.GraphicPapersManufacturing: 100,
    SYS.SanitaryPapersManufacturing: 100,
    SYS.PackagingManufacturing: 100,
    SYS.OtherPaperProductsManufacturing: 100,
    SYS.PalletsManufacturing: 1000,
    SYS.RefurbishedPalletsManufacturing: 100,
    SYS.DoorsManufacturing: 10,
    SYS.WoodenKitchenFurnitureManufacturing: 100,
    SYS.WoodenOfficeFurnitureManufacturing: 100,
    SYS.WoodenOtherFurnitureManufacturing: 100,
    SYS.WoodenSeatsManufacturing: 100,
    SYS.WoodenBedroomFurnitureManufacturing: 100,
    SYS.OtherWoodContainersManufacturing: 10,
    SYS.OtherWoodContainersManufacturing: 10,
}

output_distribution_params = {
    SYS.FibreboardManufacturing: 1000,
    SYS.ParticleboardManufacturing: 1000,
    SYS.WoodPelletsManufacturing: 100,
    SYS.SawnwoodToRepairMaintenanceImprovement: 1000,
    SYS.ParticleboardToRepairMaintenanceImprovement: 1000,
    SYS.PlywoodToRepairMaintenanceImprovement: 1000,
    SYS.PalletsManufacturing: 100,
    SYS.RefurbishedPalletsManufacturing: 100,
    SYS.OtherWoodContainersManufacturing: 10,
    SYS.OtherObjectsManufacturing: 10,
    SYS.FlooringManufacturing: 10,
    SYS.DoorsManufacturing: 10,
    SYS.WindowsManufacturing: 10,
    SYS.SawmillsSoftwood: 1000,
    SYS.SawmillsHardwood: 1000,
    SYS.NewPulpMaking: 1000,
    SYS.PulpmillsRecycledPaper: 1000,
    SYS.PulpmillsByProducts: 1000,
    SYS.WindowsManufacturing: 1000,
    SYS.WoodenKitchenFurnitureManufacturing: 1000,
    SYS.WoodenOfficeFurnitureManufacturing: 1000,
    SYS.WoodenOtherFurnitureManufacturing: 1000,
    SYS.WoodenSeatsManufacturing: 1000,
    SYS.WoodenBedroomFurnitureManufacturing: 1000,
    SYS.InUseProductsLeave: 100,
    SYS.InUseLeave: 100,
}


input_normal_distributions_params = {
    SYS.WoodFramesForNewStructuresManufacturing: 5,
    SYS.WoodRoofsForNewStructuresManufacturing: 5,
    SYS.WoodFloorFramingForNewStructuresManufacturing: 5,
}


def save_flows_table(flows, output_path):
    # Save flows
    flows = flows.sort_values(["solution", "source", "target", "material"]).reset_index(
        drop=True
    )
    flows.to_csv(output_path, index=False, float_format="%.2f")


MODEL_NS = Namespace("http://ukfires.org/analyses/UK-wood/model/")
model_uri = MODEL_NS["Model"]


def get_flows(result):
    flows = [pactot.build_flows_table(result.model, X) for X in result.solutions]
    for f, label in zip(flows, result.solution_labels):
        # f.loc[f["value"] < 5e-2, "value"] = 0
        f.loc[:, "solution"] = label
        f = f[f["value"] > 1e-4]
    return pd.concat(flows, axis=0, ignore_index=True)


def transform_linked_obs(flows, x):
    x["id"] = str(x["id"])  # Not URIRef
    x["objects"] = [str(y) for y in x["objects"]]  # Not URIRef
    x["processes"] = [str(y) for y in x["processes"]]  # Not URIRef
    x["flows"] = [
        dict(source=str(flows.loc[i, "source"]), target=str(flows.loc[i, "target"]))
        for i in x["flows"]
    ]
    return x


def solve_model(enhanced_data_path, flows_path, script_source_dir):
    flows_path = Path(flows_path)

    # SYS = Namespace("http://ukfires.org/analyses/UK-wood/system/")

    with probs_endpoint(
        enhanced_data_path, script_source_dir=script_source_dir
    ) as rdfox:
        object_types, recipe_builders, obs = query_model_from_endpoint(rdfox, model_uri)

    # XXX for testing, manually add observations here -- we don't currently have
    # a way of describing this more complicated type of observation via RDF.
    # When that is solved, this can be loaded through
    # `query_model_from_endpoint` above.

    #  obs += [

    #   ConsumptionFractionObs(
    #       SYS.SawnwoodToFencingAndOutdoor,
    #       {
    #           SYS.DeckingManufacturing: 0.6,
    #           SYS.FencingRailsAndBoardsManufacturing: 0.4,
    #        },
    #       obs_id = "ConsumptionFractionObs_1",
    #       metric = QUANTITYKIND.Mass,
    #   ),
    # ]

    # Do some Monte Carlo sampling

    log.info("Building model...")
    m = pactot.build_model(recipe_builders, object_types, obs)

    pactot.diagnose(m)
    result = pactot.solve(m, verbose=False, max_solutions=10000)
    print(f"Found {len(result.solutions)} solutions")
    if len(result.solutions) >= 1:
        flows = get_flows(result)
        save_flows_table(flows, flows_path)

        # flows_abbrev = flows.copy()
        # for k in ["source", "target", "material"]:
        #     flows_abbrev[k] = flows_abbrev[k].str.replace("http://ukfires.org/analyses/UK-wood/SYS/", "")

        # Save observations
        obj_dict = {obj.name: obj for obj in object_types}
        linked_obs = pactot.link_obs_to_flows(obs, obj_dict, flows)
        linked_obs = sorted(
            [transform_linked_obs(flows, x) for x in linked_obs], key=lambda x: x["id"]
        )
        with open(
            flows_path.parent / (flows_path.stem + "_observations.yaml"), "wt"
        ) as f:
            yaml.dump(linked_obs, f)


# Do some Monte Carlo sampling

SYS = Namespace("http://ukfires.org/analyses/UK-wood/system/")
QUANTITYKIND = Namespace("http://qudt.org/vocab/quantitykind/")


def solve_model_mc(enhanced_data_path, flows_path, script_source_dir, num_samples):
    flows_path = Path(flows_path)

    with probs_endpoint(
        enhanced_data_path, script_source_dir=script_source_dir
    ) as rdfox:
        object_types, recipe_builders, observations = query_model_from_endpoint(
            rdfox, model_uri
        )

        for r in recipe_builders:
            print(r.output_tuples)
        #
    # print(observations)

    #  observations += [

    #     ConsumptionFractionObs(
    #         SYS.SawnwoodToFencingAndOutdoor,
    #         {
    #             SYS.DeckingManufacturing: 0.6,
    #             SYS.FencingRailsAndBoardsManufacturing: 0.4,
    #         },
    #         obs_id = "ConsumptionFractionObs_1",
    #         metric = QUANTITYKIND.Mass,
    #     ),
    # ]

    # This is an annoying feature of the way the code is set up -- the
    # observation values are pre-scaled, so to get the actual value out again,
    # we need to multiply be the relevant object scale.
    object_scales = {obj.name: obj.scale for obj in object_types}

    input_distributions = {}
    for r in recipe_builders:
        if r.process_uri in input_distribution_params:
            concentration = input_distribution_params[r.process_uri]
            input_distributions[r.process_uri] = make_dirichlet_distribution(
                r.input_tuples, concentration
            )
            print(r.input_tuples)

    output_distributions = {}
    for r in recipe_builders:
        if r.process_uri in output_distribution_params:
            concentration_output = output_distribution_params[r.process_uri]
            output_distributions[r.process_uri] = make_dirichlet_distribution(
                r.output_tuples, concentration_output
            )

    input_normal_distributions = {}
    for r in recipe_builders:
        if r.process_uri in input_normal_distributions_params:
            sd = input_normal_distributions_params[r.process_uri]
            input_normal_distributions[r.process_uri] = make_normal_distribution_recipe(
                r.input_tuples, sd
            )

    # Load the CV for each observation (dictionary of obs ID -> CV)
    filename_of_spreadsheet = pd.read_excel(
        "../UK-wood-mfa/data/observations_with_references.xlsx"
    )
    observation_value_cvs = load_cv_for_observation_ids(filename_of_spreadsheet)

    # Do some Monte Carlo sampling here
    flow_samples = []  # to store the flow results
    obs_samples = []  # to store the sampled observation values
    for i in range(num_samples):
        # Resample the recipes
        for r in recipe_builders:
            if r.process_uri in input_distributions:
                resample_input_recipes(r, input_distributions[r.process_uri])
            if r.process_uri in output_distributions:
                resample_output_recipes(r, output_distributions[r.process_uri])
                print(r.output_tuples)
            if r.process_uri in input_normal_distributions:
                resample_input_recipes(r, input_normal_distributions[r.process_uri])

        # for obs in observations:
        # print(obs.params)

        # Resample the observations (values and uncertain conversion factors)
        resampled_obs = list(
            sample_observation_values(observations, observation_value_cvs)
        )
        # for obs in resampled_obs:
        print(resampled_obs)

        # Do the sampling once first (so all observations sharing the same
        # object type will use the same conversion factor for this iteration)
        conversion_factor_values = {
            k: v() for k, v in conversion_factor_distributions_1.items()
        }
        # print(conversion_factor_values)
        converted_obs = list(
            apply_conversion_factors(resampled_obs, conversion_factor_values)
        )
        # print(converted_obs)

        # Actually build and solve the model
        log.info("Building model...")
        m = pactot.build_model(recipe_builders, object_types, converted_obs)

        pactot.diagnose(m)
        result = pactot.solve(m, verbose=False, max_solutions=1)
        print(f"Found {len(result.solutions)} solutions")

        sampled_flows = get_flows(result)
        print(sampled_flows)

        sampled_flows["sample"] = i
        flow_samples.append(sampled_flows)

        # for obs in converted_obs:
        #     if 'original_value' in list(obs.params.keys()):
        #         print(obs.params)

        # Store a copy of the sampled observations used for this iteration

        obs_samples += [
            (
                i,
                obs.objects[0],
                obs.__class__.__name__,
                getattr(obs, "processes", [None])[0],
                obs.params["metric"],
                #  object_scales[obs.objects[0]] * obs.params["original_value"],
                object_scales[obs.objects[0]] * obs.params["value"],
            )
            for obs in (converted_obs)
            #    if 'original_value' in list(obs.params.keys())
        ]
        # print(type(obs_samples))
        # for obs in converted_obs:
        #    print(obs.params)
        #    print(object_scales[obs.objects[0]])
    # print(obs_samples)

    flows = pd.concat(flow_samples)
    # print(flows)
    save_flows_table(flows, flows_path)

    obs_samples = pd.DataFrame(
        obs_samples,
        columns=["solution", "object", "role", "process", "metric", "sampled_value"],
    )
    obs_samples.to_csv(str(Path(flows_path).with_suffix("")) + "_obs.csv")

    # # flows_abbrev = flows.copy()
    # # for k in ["source", "target", "material"]:
    # #     flows_abbrev[k] = flows_abbrev[k].str.replace("http://ukfires.org/analyses/UK-wood/system/", "")

    # # Save observations
    # obj_dict = {obj.name: obj for obj in object_types}
    # linked_obs = pactot.link_obs_to_flows(obs, obj_dict, flows)
    # linked_obs = sorted([transform_linked_obs(flows, x) for x in linked_obs], key=lambda x: x["id"])
    # with open(flows_path.parent / (flows_path.stem + "_observations.yaml"), "wt") as f:
    #     yaml.dump(linked_obs, f)


# Convert pd dataframe format to a dictionary with the ID as a key/index and the cvs as the value.
def load_cv_for_observation_ids(filename_of_spreadsheet):
    cvs = pd.Series(
        filename_of_spreadsheet.CV.values, index=filename_of_spreadsheet.ID
    ).to_dict()
    return cvs


def resample_input_recipes(r, distribution):
    """Overwrite the input_tuples in `r` with values returned by calling `distribution()`."""
    new_values = distribution()
    r.input_tuples = [
        (obj, metric, new_value)
        for (obj, metric, old_value), new_value in zip(r.input_tuples, new_values)
    ]
    # print(new_values)


def resample_output_recipes(r, distribution):
    """Overwrite the input_tuples in `r` with values returned by calling `distribution()`."""
    new_values = distribution()
    r.output_tuples = [
        (obj, metric, new_value)
        for (obj, metric, old_value), new_value in zip(r.output_tuples, new_values)
    ]


def apply_conversion_factors(observations, conversion_factor_values):
    """Yield new Observations with unit conversion factors applied."""
    for obs in observations:
        assert len(obs.objects) == 1, "assuming for now observation has just one object"
        obj = obs.objects[0]
        metric = obs.params["metric"]
        if metric != QUANTITYKIND.Area:
            if (metric, obj) in conversion_factor_values:
                factor = conversion_factor_values[metric, obj]
                # print(conversion_factor_values[metric, obj])
                log.debug(
                    "Applying conversion factor: (%s, %s) = %s", metric, obj, factor
                )
                new_obs = deepcopy(obs)
                new_obs.params["original_value"] = obs.params["value"]
                # print(obs.params["value"])
                new_obs.params["value"] = factor * obs.params["value"]
                # print(factor)
                yield new_obs
                # print(new_obs)
        else:
            log.warning(
                "No conversion factor defined for object %s measured by %s; skipping observation",
                obj,
                metric,
            )
            yield obs


# def retrieve_id_from_link(string):
#    n = len(string)
#    i = n-1
#    id = ""
#    while string[i] != '-':
#        id = string[i] + id
#        i = i-1
#    return id


def sample_observation_values(observations, cvs):
    """Yield new Observations with values resampled according to variations in `cvs`."""
    for obs in observations:
        # print(observations)
        assert len(obs.objects) == 1, "assuming for now observation has just one object"
        obj = obs.objects[0]
        metric = obs.params["metric"]
        # obs_id = retrieve_id_from_link(str(obs.params["obs_id"]))
        obs_id = str(obs.params["obs_id"])
        # print(obs)
        # last_char = obs_id[-1]
        # if last_char in "0123456789":

        # if ((obs_id[len(obs_id)-1] == '0') or (obs_id[len(obs_id)-1] == '1') or (obs_id[len(obs_id)-1] == '2') or (obs_id[len(obs_id)-1] == '3') or (obs_id[len(obs_id)-1] == '4') or (obs_id[len(obs_id)-1] == '5')
        # or (obs_id[len(obs_id)-1] == '6') or (obs_id[len(obs_id)-1] == '7') or (obs_id[len(obs_id)-1] == '8') or (obs_id[len(obs_id)-1] == '9')):

        if obs_id in cvs:
            cv = cvs[obs_id]
            # may want to provide a default like cvs.get(obs_id, 0.0)

            # sample a value from the distribution
            #
            # In the other functions we prepared this function in advance and stored it, so here we would just have to call it
            #
            distribution_value = stats.norm(loc=0, scale=cv).rvs()
            # print(obs.params)
            # print(distribution_value)

            # log.debug("Applying conversion factor: (%s, %s) = %s",
            #             metric, obj, factor)

            new_obs = deepcopy(obs)
            new_obs.params["original_value"] = obs.params["value"]
            new_obs.params["value"] = (
                distribution_value * obs.params["value"] + obs.params["value"]
            )
            yield new_obs
            # print(new_obs.params)
        else:
            # print("unknown obs", obs_id)
            # return the observation unchanged if we don't have a CV defined for it
            log.warning(
                "No coefficient of variation defined for object %s measured by %s; skipping observation",
                obj,
                metric,
            )
            yield obs
            # print(obs.params)
            # print(obs)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    SCRIPT_SOURCE_DIR = Path(os.environ["SCRIPT_SOURCE_DIR"])
    ENHANCED_DATA_PATH = Path("build/probs_enhanced_data.nt.gz")
    FLOWS_PATH = Path("build/flows.csv")
    # solve_model(ENHANCED_DATA_PATH, FLOWS_PATH, SCRIPT_SOURCE_DIR)
    # log.setLevel(logging.DEBUG)
    # logging.basicConfig()
    solve_model_mc(ENHANCED_DATA_PATH, FLOWS_PATH, SCRIPT_SOURCE_DIR, 10000)
