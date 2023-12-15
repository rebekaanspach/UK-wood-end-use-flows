from semantic_sankeys.build_sdd import ProcessGroupExtra
from floweaver import (
    Waypoint,
    ProcessGroup,
    Bundle,
    Partition,
    Group,
    Elsewhere,
    SankeyDefinition,
)

nodes = {
    "http://ukfires.org/analyses/UK-wood/system/Sawmills": ProcessGroupExtra(
        selection=[
            "Sawmills Hardwood",
            "Sawmills Softwood",
            "http://ukfires.org/analyses/UK-wood/system/SawmillsHardwood",
            "http://ukfires.org/analyses/UK-wood/system/SawmillsSoftwood",
        ],
        partition=None,
        direction="R",
        title="Sawmills",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Pulpmills": ProcessGroupExtra(
        selection=[
            "New pulp making",
            "Pulpmills by products",
            "http://ukfires.org/analyses/UK-wood/system/NewPulpMaking",
            "http://ukfires.org/analyses/UK-wood/system/PulpmillsByProducts",
        ],
        partition=None,
        direction="R",
        title="Pulpmills",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled": ProcessGroupExtra(
        selection=[
            "Pulpmills recycled paper",
            "http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycledPaper",
        ],
        partition=None,
        direction="R",
        title="Pulpmills (recycled)",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction": ProcessGroupExtra(
        selection=[
            "Hardwood roundwood to other energy feedstocks",
            "Softwood roundwood to other energy feedstocks",
            "Softwood roundwood to wood pellets manufacturing",
            "Wood charcoal production",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksHardwoodRoundwood",
            "http://ukfires.org/analyses/UK-wood/system/WoodCharcoalProduction",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksSoftwoodRoundwood",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturingSoftwoodRoundwood",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction": ProcessGroupExtra(
        selection=[
            "By products to other energy feedstocks",
            "By-products to wood pellets manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksByProducts",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturingByProducts",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction": ProcessGroupExtra(
        selection=[
            "Post consumer wood to other energy feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksPostConsumerWood",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/ForestResiduesToEnergyProduction": ProcessGroupExtra(
        selection=[
            "Forest residues to other energy feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksForestResidues",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets": ProcessGroupExtra(
        selection=[
            "Recycled fibres processing to pallets",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing": ProcessGroupExtra(
        selection=[
            "Wooden bedroom furniture manufacturing",
            "Wooden kitchen furniture manufacturing",
            "Wooden office furniture manufacturing",
            "Wooden other furniture manufacturing",
            "Wooden seats manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodenSeatsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Furniture mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing": ProcessGroupExtra(
        selection=[
            "Doors manufacturing",
            "Flooring manufacturing",
            "Windows manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/DoorsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FlooringManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WindowsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Joinery mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing": ProcessGroupExtra(
        selection=[
            "Other wood containers manufacturing",
            "Pallets manufacturing",
            "Refurbished pallets manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherWoodContainersManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/PalletsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/RefurbishedPalletsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Packaging mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing": ProcessGroupExtra(
        selection=[
            "Fencing posts manufacturing",
            "Fencing rails and boards manufacturing",
            "Roundwood to fencing and outdoor",
            "Roundwood to fencing manufacturing",
            "Sawnwood to fencing and outdoor",
            "Sawnwood to fencing manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FencingPostsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoardsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor",
            "http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoorManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoorManufacturing",
        ],
        partition=None,
        direction="R",
        title="Fencing mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing": ProcessGroupExtra(
        selection=[
            "Oth. objects manufacturing",
            "Wood wool and flour  manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodWoolAndFlourManufacturing",
        ],
        partition=None,
        direction="R",
        title="Oth prod mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction": ProcessGroupExtra(
        selection=[
            "Other energy feedstocks production",
            "Wood charcoal to other energy feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
            "http://ukfires.org/analyses/UK-wood/system/WoodCharcoalToOtherEnergyFeedstocks",
        ],
        partition=None,
        direction="R",
        title="",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing": ProcessGroupExtra(
        selection=[
            "Wood pellets manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Wood pellets mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing": ProcessGroupExtra(
        selection=[
            "Fibreboard to RMI",
            "Particleboard to RMI",
            "Plywood to RMI",
            "Other engineered products to construction",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToConstruction",
        ],
        partition=None,
        direction="R",
        title="Eng cst prod mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing": ProcessGroupExtra(
        selection=[
            "FormworkScaffolding manufacturing",
            "Sawnwood to RMI",
            "Railway sleepers manufacturing",
            "Upper floors manufacturing",
            "WoodFramesForNewStructures manufacturing",
            "WoodRoofsForNewStructures manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/RailwaySleepersManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffoldingManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructuresManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructuresManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructuresManufacturing",
        ],
        partition=None,
        direction="R",
        title="Sawn cst prod mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts": ProcessGroupExtra(
        selection=[
            "Formwork Scaffolding",
            "Sawnwood to construction",
            "Railway sleepers",
            "Wood floor framing for new structures",
            "Wood frames for new structures",
            "Wood roof for new structures",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
            "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures",
            "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures",
            "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures",
        ],
        partition=None,
        direction="R",
        title="Sawn cst prod",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts": ProcessGroupExtra(
        selection=[
            "Fibreboard to construction",
            "Particleboard to construction",
            "Plywood to construction",
            "Other engineered products to construction",
            "Other engineered wood products to cst",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
        ],
        partition=None,
        direction="R",
        title="Eng cst prod",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts": ProcessGroupExtra(
        selection=[
            "OtherEngineeredWoodProducts",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        ],
        partition=None,
        direction="R",
        title="Oth eng prod",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing": ProcessGroupExtra(
        selection=[
            "By-products to WBP fibres",
            "Fibreboard manufacturing",
            "Particleboard manufacturing",
            "Other engineered wood products manufacturing",
            "Plywood manufacturing",
            "Recycled fibres to WBP fibres",
            "Roundwood to WBP fibres",
            "Veneer sheets manufacturing",
            "WBP Fibres",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/VeneerSheetsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WBPFibres",
            "http://ukfires.org/analyses/UK-wood/system/WBPFibresByProducts",
            "http://ukfires.org/analyses/UK-wood/system/WBPFibresRecycledWoodFibre",
            "http://ukfires.org/analyses/UK-wood/system/WBPFibresSoftwoodRoundwood",
        ],
        partition=None,
        direction="R",
        title="WBP mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets": ProcessGroupExtra(
        selection=[
            "Wood pellets wood fibres",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres",
        ],
        partition=None,
        direction="R",
        title="to wood pellets",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks": ProcessGroupExtra(
        selection=[
            "Other energy feedstocks wood fibres",
            "Wood pellets wood fibres",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres",
            "http://ukfires.org/analyses/UK-wood/system/WoodCharcoal",
        ],
        partition=None,
        direction="R",
        title="to oth energy",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Fibreboard": ProcessGroupExtra(
        selection=[
            "Fibreboard",
            "http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        ],
        partition=None,
        direction="R",
        title="Fibreboard",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Particleboard": ProcessGroupExtra(
        selection=[
            "Particleboard",
            "http://ukfires.org/analyses/UK-wood/system/Particleboard",
        ],
        partition=None,
        direction="R",
        title="Particleboard",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood": ProcessGroupExtra(
        selection=[
            "Softwood Sawnwood",
            "http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        ],
        partition=None,
        direction="R",
        title="Sawnwood (Soft)",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood": ProcessGroupExtra(
        selection=[
            "Sawnwood (Hard)",
            "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        ],
        partition=None,
        direction="R",
        title="Sawnwood (Hard)",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Plywood": ProcessGroupExtra(
        selection=["Plywood", "http://ukfires.org/analyses/UK-wood/system/Plywood"],
        partition=None,
        direction="R",
        title="Plywood",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/VeneerSheets": ProcessGroupExtra(
        selection=[
            "Veneer sheets",
            "http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        ],
        partition=None,
        direction="R",
        title="Veneer sheets",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Pulp": ProcessGroupExtra(
        selection=["Pulp", "http://ukfires.org/analyses/UK-wood/system/Pulp"],
        partition=None,
        direction="R",
        title="Pulp",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledPulp": ProcessGroupExtra(
        selection=[
            "Recycled pulp",
            "http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        ],
        partition=None,
        direction="R",
        title="Recycled pulp",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/ByProducts": ProcessGroupExtra(
        selection=[
            "By-products",
            "http://ukfires.org/analyses/UK-wood/system/ByProducts",
        ],
        partition=None,
        direction="R",
        title="By-products",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets": ProcessGroupExtra(
        selection=[
            "Recycled fibres to pallets",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
        ],
        partition=None,
        direction="R",
        title="to pallets",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing": ProcessGroupExtra(
        selection=[
            "Graphic papers manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing",
        ],
        partition=None,
        direction="R",
        title="Graphic papers mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing": ProcessGroupExtra(
        selection=[
            "Other paper products manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Oth paper mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing": ProcessGroupExtra(
        selection=[
            "Packaging manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing",
        ],
        partition=None,
        direction="R",
        title="Packaging mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing": ProcessGroupExtra(
        selection=[
            "Sanitary papers manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing",
        ],
        partition=None,
        direction="R",
        title="Sanitary papers mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood": ProcessGroupExtra(
        selection=[
            "Softwood",
            "http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        ],
        partition=None,
        direction="R",
        title="Softwood",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/ForestResidues": ProcessGroupExtra(
        selection=[
            "Forest residues",
            "http://ukfires.org/analyses/UK-wood/system/ForestResidues",
        ],
        partition=None,
        direction="R",
        title="Forest residues",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood": ProcessGroupExtra(
        selection=[
            "Hardwood",
            "http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        ],
        partition=None,
        direction="R",
        title="Hardwood",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres": ProcessGroupExtra(
        selection=[
            "PostConsumerWood",
            "Recycled wood fibre",
            "http://ukfires.org/analyses/UK-wood/system/PostConsumerWood",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        ],
        partition=None,
        direction="R",
        title="Recycled fibres",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledPaper": ProcessGroupExtra(
        selection=[
            "Recycled paper",
            "http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        ],
        partition=None,
        direction="R",
        title="Recycled paper",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodContainers": ProcessGroupExtra(
        selection=[
            "Other containers",
            "Pallets",
            "Refurbished pallets",
            "http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers",
            "http://ukfires.org/analyses/UK-wood/system/Pallets",
            "http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets",
        ],
        partition=None,
        direction="R",
        title="Industrial packaging",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor": ProcessGroupExtra(
        selection=[
            "Fencing posts",
            "Fencing rails",
            "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
            "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
        ],
        partition=None,
        direction="R",
        title="Fencing",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Furniture": ProcessGroupExtra(
        selection=[
            "Wooden bedroom furniture",
            "Wooden kitchen furniture",
            "Wooden office furniture",
            "Wooden other furniture",
            "Wooden seats",
            "http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture",
            "http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture",
            "http://ukfires.org/analyses/UK-wood/system/WoodenSeats",
        ],
        partition=None,
        direction="R",
        title="Furniture",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Joinery": ProcessGroupExtra(
        selection=[
            "Doors",
            "Flooring",
            "Windows",
            "http://ukfires.org/analyses/UK-wood/system/Doors",
            "http://ukfires.org/analyses/UK-wood/system/Flooring",
            "http://ukfires.org/analyses/UK-wood/system/Windows",
        ],
        partition=None,
        direction="R",
        title="Joinery",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodPellets": ProcessGroupExtra(
        selection=[
            "Wood pellets",
            "http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        ],
        partition=None,
        direction="R",
        title="Wood pellets",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherProducts": ProcessGroupExtra(
        selection=[
            "Other objects",
            "Wood wool and flour",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
            "http://ukfires.org/analyses/UK-wood/system/WoodWoolAndFlour",
        ],
        partition=None,
        direction="R",
        title="Oth prod",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks": ProcessGroupExtra(
        selection=[
            "Other feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        ],
        partition=None,
        direction="R",
        title="Oth feedstocks",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/GraphicPapers": ProcessGroupExtra(
        selection=[
            "Graphic papers",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
        ],
        partition=None,
        direction="R",
        title="Graphic papers",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers": ProcessGroupExtra(
        selection=[
            "Sanitary papers",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
        ],
        partition=None,
        direction="R",
        title="Sanitary papers",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/Packaging": ProcessGroupExtra(
        selection=["Packaging", "http://ukfires.org/analyses/UK-wood/system/Packaging"],
        partition=None,
        direction="R",
        title="Packaging",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts": ProcessGroupExtra(
        selection=[
            "Other paper products",
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
        ],
        partition=None,
        direction="R",
        title="Oth paper prod",
        node_type="object",
    ),
    # "http://ukfires.org/analyses/UK-wood/system/IndustrialResidues": ProcessGroupExtra(
    #     selection=[
    #         "Pre Consumer Waste Construction",
    #         "Pre Consumer Waste Products",
    #         "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction",
    #         "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    #     ],
    #     partition=None,
    #     direction="R",
    #     title="Industrial residues",
    #     node_type="object",
    # ),
    "__output_Products": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Pallets",
                    query=(
                        (
                            "material",
                            (
                                "Pallets",
                                "http://ukfires.org/analyses/UK-wood/system/Pallets",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Other containers",
                    query=(
                        (
                            "material",
                            (
                                "Other containers",
                                "http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Refurbished pallets",
                    query=(
                        (
                            "material",
                            (
                                "Refurbished pallets",
                                "http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Products",
    ),
    "__output_Products_1": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Fencing",
                    query=(
                        (
                            "material",
                            (
                                "Fencing posts",
                                "Fencing rails and boards",
                                "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
                                "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Furniture",
                    query=(
                        (
                            "material",
                            (
                                "Wooden bedroom furniture",
                                "Wooden kitchen furniture",
                                "Wooden office furniture",
                                "Wooden other furniture",
                                "Wooden seats",
                                "http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture",
                                "http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture",
                                "http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture",
                                "http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture",
                                "http://ukfires.org/analyses/UK-wood/system/WoodenSeats",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Other products",
                    query=(
                        (
                            "material",
                            (
                                "Other objects",
                                "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
                                "Wood wool and flour",
                                "http://ukfires.org/analyses/UK-wood/system/WoodWoolAndFlour",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Products_1",
    ),
    "__output_Construction": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Plywood to construction",
                    query=(
                        (
                            "material",
                            (
                                "Plywood to construction",
                                "http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Fibreboard to construction",
                    query=(
                        (
                            "material",
                            (
                                "Fibreboard to construction",
                                "http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Other engineered products to construction",
                    query=(
                        (
                            "material",
                            (
                                "Other engineered wood products to cst",
                                "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Particleboard to construction",
                    query=(
                        (
                            "material",
                            (
                                "Particleboard to construction",
                                "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="New structures",
                    query=(
                        (
                            "material",
                            (
                                "Wood floor framing for new structures",
                                "Wood frames for new structures",
                                "Wood roof for new structures",
                                "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures",
                                "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures",
                                "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Sawnwood to construction",
                    query=(
                        (
                            "material",
                            (
                                "Formwork Scaffolding",
                                "Sawnwood to construction",
                                "RailwaySleepers",
                                "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
                                "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
                                "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Joinery",
                    query=(
                        (
                            "material",
                            (
                                "Doors",
                                "Flooring",
                                "Windows",
                                "http://ukfires.org/analyses/UK-wood/system/Doors",
                                "http://ukfires.org/analyses/UK-wood/system/Flooring",
                                "http://ukfires.org/analyses/UK-wood/system/Windows",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Construction",
    ),
    "__output_Energy": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Other feedstocks",
                    query=(
                        (
                            "material",
                            (
                                "Other feedstocks",
                                "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Wood pellets",
                    query=(
                        (
                            "material",
                            (
                                "Wood pellets",
                                "http://ukfires.org/analyses/UK-wood/system/WoodPellets",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Energy",
    ),
    "__output_Residues": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Industrial residues",
                    query=(
                        (
                            "material",
                            (
                                "Pre Consumer Waste Construction",
                                "Pre Consumer Waste Products",
                                "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction",
                                "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Industrial residues",
    ),
    "__output_Paper": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Other paper products",
                    query=(
                        (
                            "material",
                            (
                                "Other paper products",
                                "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Graphic papers",
                    query=(
                        (
                            "material",
                            (
                                "Graphic papers",
                                "http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Sanitary papers",
                    query=(
                        (
                            "material",
                            (
                                "Sanitary papers",
                                "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
                            ),
                        ),
                    ),
                ),
                Group(
                    label="Packaging",
                    query=(
                        (
                            "material",
                            (
                                "Packaging",
                                "http://ukfires.org/analyses/UK-wood/system/Packaging",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Paper",
    ),
    "__input_Recycled paper": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Recycled paper",
                    query=(
                        (
                            "material",
                            (
                                "Recycled paper",
                                "http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Recycled paper",
    ),
    "__input_Forest_residues": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Forest residues",
                    query=(
                        (
                            "material",
                            (
                                "Forest residues",
                                "http://ukfires.org/analyses/UK-wood/system/ForestResidues",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Forest residues",
    ),
    "__input_Recycled fibres": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Recycled fibres",
                    query=(
                        (
                            "material",
                            (
                                "PostConsumerWood",
                                "Recycled wood fibre",
                                "http://ukfires.org/analyses/UK-wood/system/PostConsumerWood",
                                "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Recycled fibres",
    ),
    "__input_Soft_Roundwood": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Softwood",
                    query=(
                        (
                            "material",
                            (
                                "Softwood",
                                "SoftwoodRoundwood",
                                "http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Soft Roundwood",
    ),
    "__input_Hard_Roundwood": Waypoint(
        partition=Partition(
            groups=(
                Group(
                    label="Hardwood",
                    query=(
                        (
                            "material",
                            (
                                "Hardwood",
                                "HardwoodRoundwood",
                                "http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Hard Roundwood",
    ),
    "_wpt_recycled_fibres_1": Waypoint(title=""),
    "_wpt_recycled_fibres_2": Waypoint(title=""),
    "_wpt_forest_residues_1": Waypoint(title=""),
    "_wpt_forest_residues_2": Waypoint(title=""),
    "_wpt_softwood_1": Waypoint(title=""),
    "_wpt_softwood_2": Waypoint(title=""),
    "_wpt_softwood_3": Waypoint(title=""),
    "_wpt_softwood_4": Waypoint(title=""),
    "_wpt_softsawn_1": Waypoint(title=""),
    "_wpt_softsawn_2": Waypoint(title=""),
    "_wpt_hardsawn_1": Waypoint(title=""),
    "_wpt_hardsawn_2": Waypoint(title=""),
    "Residues_1": Waypoint(title=""),
    "Residues_2": Waypoint(title="Industrial residues"),
    "Residues_3": Waypoint(title=""),
    "Residues_4": Waypoint(title=""),
    # "Residues_sf_products": Waypoint(title="Residues"),
}
bundles = [
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        waypoints=[
            "_wpt_softwood_1",
            "_wpt_softwood_2",
            "_wpt_softwood_3",
            "_wpt_softwood_4",
        ],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        waypoints=["_wpt_softwood_1", "_wpt_softwood_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Sawmills",
        target="http://ukfires.org/analyses/UK-wood/system/ByProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulp",
        target="http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulp",
        target="http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulp",
        target="http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulp",
        target="http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Fibreboard to construction', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Other engineered products to construction', 'http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst', ] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Particleboard to construction', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Plywood to construction', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Formwork Scaffolding', 'RailwaySleepers', 'Sawnwood to construction',  'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepers','http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Plywood",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Plywood",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
    ),
    # Bundle(
    #     source=Elsewhere,
    #     target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
    #     flow_selection="is_trade",
    # ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Plywood",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Pulp",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        waypoints=("__input_Soft_Roundwood",),
        flow_selection="material in ['Softwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood'] and not is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        waypoints=("__input_Recycled paper",),
        flow_selection="material in ['Recycled paper', 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        target="http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        target="http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        target="http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        target="http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target=Elsewhere,
        waypoints=("__output_Products_1",),
        flow_selection="material in ['Roundwood to fencing and outdoor', 'Sawnwood to fencing and outdoor', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Sawmills",
        target="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_3", "Residues_4", "Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_3", "Residues_4", "Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        waypoints=["_wpt_hardsawn_1", "_wpt_hardsawn_2"],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        waypoints=(
            "__input_Recycled fibres",
            "_wpt_recycled_fibres_1",
            "_wpt_recycled_fibres_2",
        ),
        flow_selection="material in ['PostConsumerWood', 'Recycled wood fibre', 'http://ukfires.org/analyses/UK-wood/system/PostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre'] and not is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/ForestResidues",
        waypoints=(
            "__input_Forest_residues",
            "_wpt_forest_residues_1",
            "_wpt_forest_residues_2",
        ),
        flow_selection="material in ['ForestResidues',  'http://ukfires.org/analyses/UK-wood/system/ForestResidues'] and not is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    # Bundle(
    #     source="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
    #     target=Elsewhere,
    #     flow_selection="is_trade",
    # ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        waypoints=["_wpt_hardsawn_1", "_wpt_hardsawn_2"],
    ),
    # Bundle(
    #     source="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
    #     target=Elsewhere,
    #     waypoints=("__output_Residues",),
    #     flow_selection="material in ['Pre Consumer Waste Construction', 'Pre Consumer Waste Products', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts'] and not is_trade",
    # ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
        target=Elsewhere,
        waypoints=("__output_Paper",),
        flow_selection="material in ['Graphic papers', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/Sawmills",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        target=Elsewhere,
        waypoints=("__output_Products",),
        flow_selection="material in ['Refurbished pallets', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        target=Elsewhere,
        waypoints=("__output_Products",),
        flow_selection="material in ['Other containers', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulp",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Sawmills",
        target="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=[
            "Residues_3",
            "Residues_4",
            "Residues_1",
            "Residues_2",
        ],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
        target="http://ukfires.org/analyses/UK-wood/system/Pulp",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Packaging",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
        target=Elsewhere,
        waypoints=("__output_Paper",),
        flow_selection="material in ['Sanitary papers', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Plywood",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        waypoints=("__input_Hard_Roundwood",),
        flow_selection="material in ['Hardwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ForestResidues",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Joinery",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Furniture",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        target="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
        target=Elsewhere,
        waypoints=("__output_Paper",),
        flow_selection="material in ['Other paper products', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Particleboard",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        waypoints=[
            "_wpt_softwood_1",
            "_wpt_softwood_2",
            "_wpt_softwood_3",
            "_wpt_softwood_4",
        ],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Joinery",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        target=Elsewhere,
        waypoints=("__output_Products",),
        flow_selection="material in ['Pallets', 'http://ukfires.org/analyses/UK-wood/system/Pallets'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/Sawmills",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Furniture",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherProducts",
        target=Elsewhere,
        waypoints=("__output_Products_1",),
        flow_selection="material in ['Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects','Wood wool and flour', 'http://ukfires.org/analyses/UK-wood/system/WoodWoolAndFlour'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        waypoints=["_wpt_hardsawn_1", "_wpt_hardsawn_2"],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Plywood",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        target=Elsewhere,
        waypoints=("__output_Energy",),
        flow_selection="material in ['Wood pellets', 'http://ukfires.org/analyses/UK-wood/system/WoodPellets'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        target="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Joinery",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Doors', 'Flooring', 'Windows', 'http://ukfires.org/analyses/UK-wood/system/Doors', 'http://ukfires.org/analyses/UK-wood/system/Flooring', 'http://ukfires.org/analyses/UK-wood/system/Windows'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
        target="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        target="http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        target="http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
        waypoints=[
            "_wpt_softwood_1",
            "_wpt_softwood_2",
        ],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/ForestResidues",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        target="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Plywood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Packaging",
        target=Elsewhere,
        waypoints=("__output_Paper",),
        flow_selection="material in ['Packaging', 'http://ukfires.org/analyses/UK-wood/system/Packaging'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        target="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
        target=Elsewhere,
        waypoints=("__output_Products_1",),
        flow_selection="material in ['Fencing posts', 'Fencing rails and boards', 'Railway sleepers', 'http://ukfires.org/analyses/UK-wood/system/FencingPosts', 'http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepers'] and not is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        target="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Packaging",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Joinery",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Packaging",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_1", "Residues_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        target=Elsewhere,
        waypoints=("__output_Energy",),
        flow_selection="material in ['Other feedstocks', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
        waypoints=[
            "_wpt_softwood_1",
            "_wpt_softwood_2",
        ],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ForestResiduesToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ForestResidues",
        target="http://ukfires.org/analyses/UK-wood/system/ForestResiduesToEnergyProduction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
        target="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
        target="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
        target="http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Furniture",
        target=Elsewhere,
        waypoints=("__output_Products_1",),
        flow_selection="material in ['Wooden bedroom furniture', 'Wooden kitchen furniture', 'Wooden office furniture', 'Wooden other furniture', 'Wooden seats', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeats'] and not is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/Furniture",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
]
ordering = (
    (
        (
            "__input_Forest_residues",
            "__input_Recycled fibres",
        ),
        ("__input_Hard_Roundwood",),
        (),
        ("__input_Soft_Roundwood",),
        (),
        ("__input_Recycled paper",),
    ),
    (
        (
            "_wpt_forest_residues_1",
            "_wpt_recycled_fibres_1",
        ),
        ("http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",),
        (),
        ("http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",),
        (),
        (),
    ),
    (
        (
            "_wpt_forest_residues_2",
            "_wpt_recycled_fibres_2",
        ),
        (),
        (),
        (
            "_wpt_softwood_1",
            "http://ukfires.org/analyses/UK-wood/system/Sawmills",
        ),
        (),
        ("http://ukfires.org/analyses/UK-wood/system/RecycledPaper",),
    ),
    (
        (
            "http://ukfires.org/analyses/UK-wood/system/ForestResidues",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres",
        ),
        (),
        ("_wpt_softwood_2",),
        (
            "http://ukfires.org/analyses/UK-wood/system/ByProducts",
            "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
            "http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        ),
        (),
        (),
    ),
    (
        (
            "http://ukfires.org/analyses/UK-wood/system/ForestResiduesToEnergyProduction",
            "http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
            "http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
            "http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
            "_wpt_softwood_3",
        ),
         ("http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",),
        (
            
            "_wpt_hardsawn_1",
            "_wpt_softsawn_1",
        ),
        (),
        (
            "http://ukfires.org/analyses/UK-wood/system/Pulpmills",
            "http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled",
        ),
    ),
    (
        (
            "http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks",
            "http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
            "_wpt_softwood_4",
            "http://ukfires.org/analyses/UK-wood/system/Fibreboard",
           
            
           
        ),
         (   "http://ukfires.org/analyses/UK-wood/system/Particleboard",
            
            
            ),
        ( 
            "http://ukfires.org/analyses/UK-wood/system/Plywood",
          "http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
            "_wpt_hardsawn_2",
            "_wpt_softsawn_2",
        ),
        ("Residues_3",),
        (
            "http://ukfires.org/analyses/UK-wood/system/Pulp",
            "http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        ),
    ),
    (
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
          
        ),
         (  "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherProductsManufacturing",),
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        ),
        ("Residues_4",),
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing",
        ),
    ),
    (
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
            "Residues_1",
            "http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/WoodContainers",
            
            #  "http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        ),
         ("http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
            "http://ukfires.org/analyses/UK-wood/system/Furniture",
            "http://ukfires.org/analyses/UK-wood/system/OtherProducts",),
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
            "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
            "http://ukfires.org/analyses/UK-wood/system/Joinery",
        ),
        ("Residues_1",),
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
            "http://ukfires.org/analyses/UK-wood/system/Packaging",
        ),
    ),
    (
        ("__output_Energy",),
        (
            "__output_Products",
           
        ),
         ( "__output_Products_1",),
        ("__output_Construction",),
        ("Residues_2",),
        ("__output_Paper",),
    ),
)

flow_partition = Partition.Simple(
    "material",
    [
        (
            "Fibreboard",
            ("Fibreboard", "http://ukfires.org/analyses/UK-wood/system/Fibreboard"),
        ),
        (
            "Particleboard",
            (
                "Particleboard",
                "http://ukfires.org/analyses/UK-wood/system/Particleboard",
            ),
        ),
        (
            "Softwood Sawnwood",
            (
                "Softwood Sawnwood",
                "http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
            ),
        ),
        (
            "Hardwood Sawnwood",
            (
                "Hardwood Sawnwood",
                "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
            ),
        ),
        ("Plywood", ("Plywood", "http://ukfires.org/analyses/UK-wood/system/Plywood")),
        ("Pulp", ("Pulp", "http://ukfires.org/analyses/UK-wood/system/Pulp")),
        (
            "Recycled pulp",
            (
                "Recycled pulp",
                "http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
            ),
        ),
        (
            "Recycled fibres to pallets",
            (
                "Recycled fibres to pallets",
                "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets",
            ),
        ),
        (
            "By-products",
            (
                "By-products",
                "ByProducts",
                "http://ukfires.org/analyses/UK-wood/system/ByProducts",
            ),
        ),
        (
            "WBP Fibres",
            ("WBP Fibres", "http://ukfires.org/analyses/UK-wood/system/WBPFibres"),
        ),
        (
            "Refurbished pallets",
            (
                "Refurbished pallets",
                "http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets",
            ),
        ),
        ("Pallets", ("Pallets", "http://ukfires.org/analyses/UK-wood/system/Pallets")),
        (
            "Other containers",
            (
                "Other containers",
                "http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers",
            ),
        ),
        (
            "Furniture",
            (
                "Wooden bedroom furniture",
                "Wooden kitchen furniture",
                "Wooden office furniture",
                "Wooden other furniture",
                "Wooden seats",
                "http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture",
                "http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture",
                "http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture",
                "http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture",
                "http://ukfires.org/analyses/UK-wood/system/WoodenSeats",
            ),
        ),
        (
            "Fencing & outdoors",
            (
                "Fencing posts",
                "Fencing rails and boards",
                "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
                "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
            ),
        ),
        (
            "Joinery",
            (
                "Doors",
                "Flooring",
                "Windows",
                "http://ukfires.org/analyses/UK-wood/system/Doors",
                "http://ukfires.org/analyses/UK-wood/system/Flooring",
                "http://ukfires.org/analyses/UK-wood/system/Windows",
            ),
        ),
        (
            "Wood pellets",
            ("Wood pellets", "http://ukfires.org/analyses/UK-wood/system/WoodPellets"),
        ),
        (
            "Other feedstocks",
            (
                "Other feedstocks",
                "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
            ),
        ),
        (
            "Other products",
            (
                "Other objects",
                "Wood wool and flour",
                "http://ukfires.org/analyses/UK-wood/system/WoodWoolAndFloor",
                "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
            ),
        ),
        (
            "Graphic papers",
            (
                "Graphic papers",
                "http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
            ),
        ),
        (
            "Sanitary papers",
            (
                "Sanitary papers",
                "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
            ),
        ),
        (
            "Packaging",
            ("Packaging", "http://ukfires.org/analyses/UK-wood/system/Packaging"),
        ),
        (
            "Other paper products",
            (
                "Other paper products",
                "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
            ),
        ),
        (
            "Particleboard to construction",
            (
                "Particleboard to construction",
                "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther",
            ),
        ),
        (
            "Other engineered products to construction",
            (
                "Other engineered products to construction",
                "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
            ),
        ),
        (
            "Plywood to construction",
            (
                "Plywood to construction",
                "http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther",
            ),
        ),
        (
            "New structures",
            (
                "Wood floor framing for new structures",
                "Wood frames for new structures",
                "Wood roof for new structures",
                "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures",
                "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures",
                "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures",
            ),
        ),
        (
            "Fibreboard to construction",
            (
                "Fibreboard to construction",
                "http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther",
            ),
        ),
        (
            "Sawnwood to construction",
            (
                "Formwork Scaffolding",
                "RailwaySleepers",
                "Sawnwood to construction",
                "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
                "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
                "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
            ),
        ),
        (
            "Recycled fibres",
            (
                "PostConsumerWood",
                "Recycled wood fibre",
                "http://ukfires.org/analyses/UK-wood/system/PostConsumerWood",
                "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
            ),
        ),
        (
            "Recycled paper",
            (
                "Recycled paper",
                "http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
            ),
        ),
        (
            "Wood fibres for energy",
            (
                "Other energy feedstocks wood fibres",
                "Wood pellets wood fibres",
                "WoodCharcoal",
                "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres",
                "http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres",
                "http://ukfires.org/analyses/UK-wood/system/WoodCharcoal",
            ),
        ),
        (
            "Veneer sheets",
            (
                "Veneer sheets",
                "http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
            ),
        ),
        (
            "Softwood",
            (
                "Softwood",
                "SoftwoodRoundwood",
                "http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",
            ),
        ),
        (
            "Hardwood",
            (
                "Hardwood",
                "HardwoodRoundwood",
                "http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
            ),
        ),
        (
            "Industrial residues",
            (
                "Pre Consumer Waste Construction",
                "Pre Consumer Waste Products",
                "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction",
                "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
            ),
        ),
    ],
)

sdd = SankeyDefinition(nodes, bundles, ordering, flow_partition=flow_partition)
