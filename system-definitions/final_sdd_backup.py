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
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksHardwoodRoundwood",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksSoftwoodRoundwood",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturingSoftwoodRoundwood",
        ],
        partition=None,
        direction="R",
        title="Fuelwood",
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
        title="By-products",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction": ProcessGroupExtra(
        selection=[
            "Post consumer wood to other energy feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksPostConsumerWood",
        ],
        partition=None,
        direction="R",
        title="Wood fibre waste",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets": ProcessGroupExtra(
        selection=[
            "Recycled fibres processing to pallets",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
        ],
        partition=None,
        direction="R",
        title="Recycled fibres",
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
    "http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption": ProcessGroupExtra(
        selection=[
            "Graphic papers consumption",
            "In use",
            "In use leave",
            "Other paper products consumption",
            "Packaging consumption",
            "Sanitary papers consumption",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapersConsumption",
            "http://ukfires.org/analyses/UK-wood/system/InUse",
            "http://ukfires.org/analyses/UK-wood/system/InUseLeave",
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/PackagingConsumption",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapersConsumption",
        ],
        partition=None,
        direction="R",
        title="Paper products consumption",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption": ProcessGroupExtra(
        selection=[
            "Doors consumption",
            "Fencing posts consumption",
            "Fencing rails and boards consumption",
            "FibreboardToRMIAndOther consumption",
            "Flat and Box Pallets consumption",
            "Flooring consumption",
            "Formwork scaffolding consumption",
            "In use products",
            "In use products leave",
            "Other objects consumption",
            "Other wood containers consumption",
            "OtherEngineeredWoodProducts consumption",
            "ParticleboardToRMIAndOther consumption",
            "PlywoodToRMIAndOther consumption",
            "Railway sleepers consumption",
            "Refurbished pallets consumption",
            "SawnwoodToRMIAndOther consumption",
            "Windows consumption",
            "Wooden Bedroom Furniture consumption",
            "Wooden Kitchen Furniture consumption",
            "Wooden Office Furniture consumption",
            "Wooden Other Furniture consumption",
            "Wooden Seats consumption",
            "http://ukfires.org/analyses/UK-wood/system/DoorsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/FencingPostsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoardsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOtherConsumption",
            "http://ukfires.org/analyses/UK-wood/system/FlooringConsumption",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffoldingConsumption",
            "http://ukfires.org/analyses/UK-wood/system/InUseProducts",
            "http://ukfires.org/analyses/UK-wood/system/InUseProductsLeave",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjectsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/OtherWoodContainersConsumption",
            "http://ukfires.org/analyses/UK-wood/system/PalletsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOtherConsumption",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOtherConsumption",
            "http://ukfires.org/analyses/UK-wood/system/RailwaySleepersConsumption",
            "http://ukfires.org/analyses/UK-wood/system/RefurbishedPalletsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOtherConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WindowsConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurnitureConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurnitureConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurnitureConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurnitureConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodenSeatsConsumption",
        ],
        partition=None,
        direction="R",
        title="Commercial products consumption",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/EnergyConsumption": ProcessGroupExtra(
        selection=[
            "Other energy feedstocks consumption",
            "Wood pellets consumption",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksConsumption",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsConsumption",
        ],
        partition=None,
        direction="R",
        title="Energy consumption",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst": ProcessGroupExtra(
        selection=[
            "Other engineered wood products to cst",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
        ],
        partition=None,
        direction="R",
        title="Other engineered wood products to cst",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing": ProcessGroupExtra(
        selection=[
            "Fencing posts manufacturing",
            "Fencing rails and boards manufacturing",
            "Railway sleepers manufacturing",
            "Roundwood to fencing and outdoor",
            "Roundwood to fencing manufacturing",
            "Sawnwood to fencing and outdoor",
            "Sawnwood to fencing manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FencingPostsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoardsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/RailwaySleepersManufacturing",
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
    "http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing": ProcessGroupExtra(
        selection=[
            "Oth. objects manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        ],
        partition=None,
        direction="R",
        title="Oth. objects mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction": ProcessGroupExtra(
        selection=[
            "Other energy feedstocks production",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
        ],
        partition=None,
        direction="R",
        title="Feedstocks prod",
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
    "http://ukfires.org/analyses/UK-wood/system/SawnwoodToConstruction": ProcessGroupExtra(
        selection=[
            "Sawnwood to construction",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToConstruction",
        ],
        partition=None,
        direction="R",
        title="Sawnwood to construction",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing": ProcessGroupExtra(
        selection=[
            "Fibreboard to RMI",
            "Particleboard to RMI",
            "Plywood to RMI",
            "Other engineered product to construction",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToConstruction",
        ],
        partition=None,
        direction="R",
        title="Other construction products mfg",
        node_type="process",
    ),
        "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing": ProcessGroupExtra(
        selection=[
            "FormworkScaffolding manufacturing",
            "Sawnwood to RMI",
            "Upper floors manufacturing",
            "WoodFramesForNewStructures manufacturing",
            "WoodRoofsForNewStructures manufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffoldingManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructuresManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructuresManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructuresManufacturing",
        ],
        partition=None,
        direction="R",
        title="Sawn construction products mfg",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing": ProcessGroupExtra(
        selection=[
            "By-products to WBP fibres",
            "Fibreboard manufacturing",
            "Particleboard manufacturing",
            "Plywood manufacturing",
            "Other engineered product manufacturing",
            "Recycled fibres to WBP fibres",
            "Roundwood to WBP fibres",
            "Veneer sheets manufacturing",
            "WBP Fibres",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodManufacturing",
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
    "http://ukfires.org/analyses/UK-wood/system/WoodFibresProductionForRMI": ProcessGroupExtra(
        selection=[
            "Fibreboard to RMI",
            "Other engineered wood products to construction",
            "Particleboard to RMI",
            "Plywood to RMI",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToConstruction",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRepairMaintenanceImprovement",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRepairMaintenanceImprovement",
        ],
        partition=None,
        direction="R",
        title="Wood fibres production for RMI",
        node_type="process",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodFibresToWoodPellets": ProcessGroupExtra(
        selection=[
            "Wood pellets wood fibres",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres",
        ],
        partition=None,
        direction="R",
        title="to pellets",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/WoodFibresToOtherEnergyFeedstocks": ProcessGroupExtra(
        selection=[
            "Other energy feedstocks wood fibres",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres",
        ],
        partition=None,
        direction="R",
        title="to other energy",
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
    "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts": ProcessGroupExtra(
        selection=[
            "OtherEngineeredWoodProducts",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        ],
        partition=None,
        direction="R",
        title="Other engineered products",
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
        title="Sof Sawnwood",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood": ProcessGroupExtra(
        selection=[
            "Hard Sawnwood",
            "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        ],
        partition=None,
        direction="R",
        title="Hard Sawnwood",
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
        title="Recycled fibres",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst": ProcessGroupExtra(
        selection=[
            "Sawn products to construction",
            "http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
        ],
        partition=None,
        direction="R",
        title="Sawn products to construction",
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
        title="Other paper mfg",
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
            "Railway sleepers",
            "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
            "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
            "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
        ],
        partition=None,
        direction="R",
        title="Fencing & outdoor",
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
    "http://ukfires.org/analyses/UK-wood/system/OtherObjects": ProcessGroupExtra(
        selection=[
            "Other objects",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
        ],
        partition=None,
        direction="R",
        title="Other objects",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks": ProcessGroupExtra(
        selection=[
            "Other feedstocks",
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        ],
        partition=None,
        direction="R",
        title="Other feedstocks",
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
    "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts": ProcessGroupExtra(
        selection=[
            "Pre Consumer Waste Products",
            "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
        ],
        partition=None,
        direction="R",
        title="Pre Consumer Waste Products",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre": ProcessGroupExtra(
        selection=[
            "Recycled wood fibre",
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        ],
        partition=None,
        direction="R",
        title="Recycled wood fibre",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProductsConsumption": ProcessGroupExtra(
        selection=[
            "Pre consumer waste products consumption",
            "http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProductsConsumption",
        ],
        partition=None,
        direction="R",
        title="Pre consumer waste products consumption",
        node_type="process",
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
        title="Other paper products",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts": ProcessGroupExtra(
        selection=[
            "Fibreboard to construction",
            "Particleboard to construction",
            "Plywood to construction",
            "Other engineered products to construction",
            "http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
    
        ],
        partition=None,
        direction="R",
        title="Other construction products",
        node_type="object",
    ),
    "http://ukfires.org/analyses/UK-wood/system/SawnwoodToOther": ProcessGroupExtra(
        selection=[
            "Formwork Scaffolding",
            "Sawnwood to rmi and other",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
        ],
        partition=None,
        direction="R",
        title="Sawnwood to other",
        node_type="object",
    ),

    "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts": ProcessGroupExtra(
        selection=[
            "Formwork Scaffolding",
            "Sawnwood to construction",
            "Wood floor framing for new structures",
            "Wood frames for new structures",
            "Wood roof for new structures",
            "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
            "http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures",
            "http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures",
            "http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures",
        ],
        partition=None,
        direction="R",
        title="Sawn construction products",
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
                Group(
                    label="Fencing & outdoor",
                    query=(
                        (
                            "material",
                            (
                                "Fencing posts",
                                "Fencing rails and boards",
                                "Railway sleepers",
                                "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
                                "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
                                "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
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
                    label="Other objects",
                    query=(
                        (
                            "material",
                            (
                                "Other objects",
                                "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
                            ),
                        ),
                    ),
                ),
            )
        ),
        title="Products",
    ),
    "__output_Construction": Waypoint(
        partition=Partition(
            groups=(
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
                    label="Other engineered products to construction",
                    query=(
                        (
                            "material",
                            (
                                "Other engineered products to construction",
                                "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
                            ),
                        ),
                    ),
                ),
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
                                "http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding",
                                "http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther",
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
        title="Residues",
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
    "__input_Roundwood": Waypoint(
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
        title="Roundwood",
    ),
    "_wpt_recycled_fibres_1": Waypoint(title=""),
    "_wpt_recycled_fibres_2": Waypoint(title=""),
    "_wpt_softwood_1": Waypoint(title=""),
    "_wpt_softwood_2": Waypoint(title=""),
    "_wpt_softwood_3": Waypoint(title=""),
    "_wpt_softwood_4": Waypoint(title=""),
    "_wpt_softsawn_1": Waypoint(title=""),
    "_wpt_softsawn_2": Waypoint(title=""),
    "_wpt_hardsawn_1": Waypoint(title=""),
    "_wpt_hardsawn_2": Waypoint(title=""),
    "Residues pulpmills": Waypoint(title="Residues"),
    "Residues_products": Waypoint(title="Residues"),
    "Residues_sf_products": Waypoint(title="Residues"),
    "Residues_products": Waypoint(title="Residues"),
}
bundles = [
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
        target="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
        flow_selection="is_trade",
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
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/SawnwoodToConstruction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnwoodToConstruction",
        target="http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
    ),
    
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Sawmills",
        target="http://ukfires.org/analyses/UK-wood/system/ByProducts",
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
        waypoints=("__input_Roundwood",),
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
        source="http://ukfires.org/analyses/UK-wood/system/Plywood",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_products"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target=Elsewhere,
        waypoints=("__output_Products",),
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
        source="http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues pulpmills"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycled",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues pulpmills"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        waypoints=["_wpt_hardsawn_1", "_wpt_hardsawn_2"],
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Fibreboard to construction', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther'] and not is_trade",
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
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Particleboard",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
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
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnwoodToOther",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodContainers",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Packaging",
        target="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledPaper",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        target=Elsewhere,
        flow_selection="is_trade",
    ),

    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
        target="http://ukfires.org/analyses/UK-wood/system/EnergyConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/EnergyConsumption",
        target="http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/EnergyConsumption",
        target="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjects",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodFibresProductionForRMI",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),

    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Furniture",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        target="http://ukfires.org/analyses/UK-wood/system/EnergyConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
        target="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts",
        target="http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProductsConsumption",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
        target="http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",
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
        waypoints=["Residues_products"],
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
        waypoints=["Residues_sf_products"],
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
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        flow_selection="is_trade",
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
        source="http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        waypoints=("__input_Roundwood",),
        flow_selection="material in ['Hardwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood'] and not is_trade",
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
        waypoints=["Residues_products"],
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
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        # target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_products"],
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
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Formwork Scaffolding', 'Sawnwood to construction', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_products"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        #  target="http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
        target=Elsewhere,
        waypoints=["Residues_products"],
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
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherObjects",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
        target="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjects",
        target=Elsewhere,
        waypoints=("__output_Products",),
        flow_selection="material in ['Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects'] and not is_trade",
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
        waypoints=["Residues_products"],
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
        source="http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
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
        source="http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
        target="http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/Fibreboard",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",
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
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target=Elsewhere,
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherObjects",
        flow_selection="is_trade",
    ),
    Bundle(
        source=Elsewhere,
        target="http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
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
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Plywood to construction', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/ByProducts",
        target="http://ukfires.org/analyses/UK-wood/system/Pulpmills",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherObjects",
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
        waypoints=("__output_Products",),
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
        source="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
        target="http://ukfires.org/analyses/UK-wood/system/Joinery",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Particleboard to construction', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther'] and not is_trade",
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
        target=Elsewhere,
        waypoints=("__output_Construction",),
        flow_selection="material in ['Other engineered products to construction', 'http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProductsToCst'] and not is_trade",
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
        waypoints=["Residues_products"],
    ),
    Bundle(
        source="http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        target="http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        waypoints=["_wpt_softsawn_1", "_wpt_softsawn_2"],
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
        waypoints=("__output_Products",),
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
    ((), ("__input_Roundwood",), ()),

    (   (),
        
        (   "http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood",
            "http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood",),
        
        (),
    ),


    (
        (),
        (
            "_wpt_softwood_1",
            "http://ukfires.org/analyses/UK-wood/system/Sawmills",
        ),
        ("http://ukfires.org/analyses/UK-wood/system/RecycledPaper",),
        
       
    ),


    (
        ("http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre",),
        (
            "_wpt_softwood_2",
            "http://ukfires.org/analyses/UK-wood/system/ByProducts",
            "http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood",
            "http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood",
        ),
        (),
        
        
    ),
    (   (
            "http://ukfires.org/analyses/UK-wood/system/RecycledFibresToEnergyProduction",
            "http://ukfires.org/analyses/UK-wood/system/RoundwoodToEnergyProduction",
            "http://ukfires.org/analyses/UK-wood/system/ByProductsToEnergyProduction",
        ),
        
        (
            "http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets",
            "http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing",
            "_wpt_softwood_3",
            "_wpt_hardsawn_1",
            "_wpt_softsawn_1",
            "http://ukfires.org/analyses/UK-wood/system/SawnwoodToConstruction",
        ),
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
            "http://ukfires.org/analyses/UK-wood/system/Fibreboard",
            "http://ukfires.org/analyses/UK-wood/system/VeneerSheets",
            "_wpt_softwood_4",
            "http://ukfires.org/analyses/UK-wood/system/Particleboard",
            "http://ukfires.org/analyses/UK-wood/system/Plywood",
            "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
            "Residues_sf_products",
            "_wpt_hardsawn_2",
            "_wpt_softsawn_2",
            "http://ukfires.org/analyses/UK-wood/system/SawnProductsToCst",
        ),
        (
            "Residues pulpmills",
            "http://ukfires.org/analyses/UK-wood/system/Pulp",
            "http://ukfires.org/analyses/UK-wood/system/RecycledPulp",
        ),
        
        
    ),
    (    (
            "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction",
            "http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing",
        ),
        
        (
            "http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProductsManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing",
            "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProductsManufacturing",
        ),
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
            "Residues_products",
            "http://ukfires.org/analyses/UK-wood/system/WoodPellets",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/WoodContainers",
            "http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoor",
            "http://ukfires.org/analyses/UK-wood/system/Furniture",
            "http://ukfires.org/analyses/UK-wood/system/OtherObjects",
            "http://ukfires.org/analyses/UK-wood/system/OtherConstructionProducts",
            "http://ukfires.org/analyses/UK-wood/system/Joinery",
            "http://ukfires.org/analyses/UK-wood/system/SawnConstructionProducts",
            #  "http://ukfires.org/analyses/UK-wood/system/IndustrialResidues",
            "Residues_products",
        ),
        (
            "http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts",
            "http://ukfires.org/analyses/UK-wood/system/GraphicPapers",
            "http://ukfires.org/analyses/UK-wood/system/SanitaryPapers",
            "http://ukfires.org/analyses/UK-wood/system/Packaging",
        ),
        
        
    ),
    (
        
        ("http://ukfires.org/analyses/UK-wood/system/EnergyConsumption",),
        (
        "http://ukfires.org/analyses/UK-wood/system/CommercialProductsConsumption",
        ),
        ( "http://ukfires.org/analyses/UK-wood/system/PaperProductsConsumption",),
        
        
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
                "Railway sleepers",
                "http://ukfires.org/analyses/UK-wood/system/FencingPosts",
                "http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards",
                "http://ukfires.org/analyses/UK-wood/system/RailwaySleepers",
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
            "Other objects",
            (
                "Other objects",
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
                "Sawnwood to construction",
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
                "http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres",
                "http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres",
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
            "Other engineered products",
            (
                "Other engineered produts",
                "http://ukfires.org/analyses/UK-wood/system/OtherEngineeredWoodProducts",
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
    ],
)

sdd = SankeyDefinition(nodes, bundles, ordering, flow_partition=flow_partition)
