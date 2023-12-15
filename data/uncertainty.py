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
