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
%load_ext autoreload
```

```{code-cell} ipython3
%autoreload 2
```

```{code-cell} ipython3
#element=guess_elements(SYS.Wood, resolve=False)
#elements_to_code(element, SYS, True )
```

```{code-cell} ipython3
from semantic_sankeys import SankeyProcess, SankeyObject, SankeyElements
```

```{code-cell} ipython3
palette = {
    SYS["WBPproducts"]: "#d7bde2",
    SYS["Pulp"]: "#8ebfdd",
     SYS["RecycledPulp"]: "lightgrey",
    SYS["PaperProducts"]: "#529dcb",
    SYS["NewStructures"]: "#935eaa",
    SYS["Roundwood"]: "#228b22",
    SYS["Sawnwood"]: "#be93d1",
    #SYS["ConstructionProducts"]: "#78508a",      
    SYS["IndustrialResidues"]: "lightgrey",
    SYS["RecycledWoodFibres"]: "lightgrey",
    SYS["EnergyIndustry"]: "#ff2727",
   SYS["RecycledPaper"]: "lightgrey",
    SYS["RecycledWoodFibreToPallets"]: "lightgrey",
    SYS["ByProducts"]: "#6fbcf2",
    SYS["FuelsForEnergy"]: "#ff2727",
    SYS["WoodPelletsWoodFibres"]: "#ff7676",
    SYS["OtherEnergyFeedstocksWoodFibres"]: "#ff7676",
        }

elements = SankeyElements(
    processes=[
        SankeyProcess(SYS.Sawmills),
        SankeyProcess(SYS.Pulpmills),
       # SankeyProcess(SYS.NewPulpMaking), 
       # SankeyProcess(SYS.PulpmillsRecycledPaper),
       # SankeyProcess(SYS.PulpmillsByProducts),
      #  SankeyProcess(SYS.WBPBoardsProduction),
        SankeyProcess(SYS.WoodFibresForEnergyProduction),
       # SankeyProcess(SYS.RoundwoodToFencingAndOutdoorManufacturing),
        SankeyProcess(SYS.RecycledWoodFibreProcessingForPallets),      
         SankeyProcess(SYS.FurnitureManufacturing),
         SankeyProcess(SYS.JoineryManufacturing),
         SankeyProcess(SYS.WoodenContainersManufacturing),
         SankeyProcess(SYS.FencingAndOutdoorManufacturing, include_objects = ([SYS.SawnwoodToFencingAndOutdoor, SYS.RoundwoodToFencingAndOutdoor])),
         SankeyProcess(SYS.OtherProductsManufacturing),
         SankeyProcess(SYS.EnergyIndustry),
         
         SankeyProcess(SYS.PaperProductsConsumption, include_objects = ([SYS.InUse])),
        SankeyProcess(SYS.EnergyConsumption),
         SankeyProcess(SYS.SawnConstructionProductsManufacturing, include_objects = ([SYS.WoodFramesForNewStructures ,
                                                                                      SYS.WoodFloorFramingForNewStructures,
                                                                                      SYS.WoodRoofsForNewStructures,
                                                                                     SYS.EndTerracedHouses,
                                                                                      SYS.MidTerracedHouses,
                                                                                      SYS.SemiDetachedHouses,
                                                                                      SYS.DetachedHouses,
                                                                                      SYS.Bungalows,
                                                                                      SYS.FlatLowRise,
                                                                                      SYS.ConvertedFlats ])),
      
     
        SankeyProcess(SYS.WoodFibresProductionForRMI),
         SankeyProcess(SYS.WBPmanufacturing, include_objects = ([SYS.WBPFibres])),
        # SankeyProcess(SYS.FibreProductionForWBP),
        
        SankeyProcess(SYS.PreConsumerWasteProducts),
        SankeyProcess(SYS.WoodFibresForEnergy),
        SankeyProcess(SYS.Fibreboard),
        SankeyProcess(SYS.Particleboard),
        SankeyProcess(SYS.OtherEngineeredWoodProducts),
        SankeyProcess(SYS.SoftwoodSawnwood),
        SankeyProcess(SYS.HardwoodSawnwood),
        SankeyProcess(SYS.Plywood),
        SankeyProcess(SYS.VeneerSheets),
        SankeyProcess(SYS.Pulp),
        SankeyProcess(SYS.RecycledPulp),
        SankeyProcess(SYS.ByProducts),
     #   SankeyProcess(SYS.RoundwoodToOther),
        
        SankeyProcess(SYS.RecycledWoodFibreToPallets),
        #  SankeyProcess(SYS.InUseLeave),
       #    SankeyProcess(SYS.InUseProductsLeave),

        
        SankeyProcess(SYS.PreConsumerWasteProductsConsumption),
        SankeyProcess(SYS.Papermills),
        SankeyProcess(SYS.SoftwoodRoundwood),
        SankeyProcess(SYS.ForestResidues),
        SankeyProcess(SYS.HardwoodRoundwood),
        SankeyProcess(SYS.RecycledWoodFibre),
        SankeyProcess(SYS.RecycledPaper),
        SankeyProcess(SYS.WoodContainers),
         SankeyProcess(SYS.Furniture),
        SankeyProcess(SYS.FencingAndOutdoor),
     #   SankeyProcess(SYS.Joinery),
        SankeyProcess(SYS.WoodPellets),
        SankeyProcess(SYS.OtherProducts),
        SankeyProcess(SYS.OtherEnergyFeedstocks),
        SankeyProcess(SYS.GraphicPapers),
        SankeyProcess(SYS.SanitaryPapers),
        SankeyProcess(SYS.Packaging),
        SankeyProcess(SYS.OtherPaperProducts),
        SankeyProcess(SYS.Joinery),
        SankeyProcess(SYS.NewBuilds),

         SankeyProcess(SYS.SawnwoodToOther),
        SankeyProcess(SYS.WBPProductsToCst),
       
        SankeyProcess(SYS.ParticleboardToRMIAndOther),
        SankeyProcess(SYS.PlywoodToRMIAndOther),
        SankeyProcess(SYS.FibreboardToRMIAndOther),
         SankeyProcess(SYS.OtherEngineeredWoodProductsToCst),
  

       
                       
            ],
    
    
    objects=[
        SankeyObject(SYS.Fibreboard),
        SankeyObject(SYS.Particleboard),
        SankeyObject(SYS.SoftwoodSawnwood),
        SankeyObject(SYS.HardwoodSawnwood),
        SankeyObject(SYS.Plywood),
        SankeyObject(SYS.OtherEngineeredWoodProducts),
        SankeyObject(SYS.Pulp),
        SankeyObject(SYS.RecycledPulp),
        SankeyObject(SYS.RecycledWoodFibreToPallets),
        SankeyObject(SYS.ByProducts),
        SankeyObject(SYS.WBPFibres),
       # SankeyObject(SYS.SawnProductsToCst),
      #  SankeyObject(SYS.InUse),
      #  SankeyObject(SYS.InUseProducts),
        SankeyObject(SYS.PreConsumerWasteProducts),
        SankeyObject(SYS.ForestResidues, input_port='Roundwood and recycled fibres'),
    


        SankeyObject(SYS.RefurbishedPallets),
        SankeyObject(SYS.Pallets),
        SankeyObject(SYS.OtherWoodContainers),
        SankeyObject(SYS.Furniture),
        SankeyObject(SYS.FencingAndOutdoor),
        SankeyObject(SYS.Joinery),
        SankeyObject(SYS.WoodPellets),
        SankeyObject(SYS.OtherEnergyFeedstocks),
        SankeyObject(SYS.OtherProducts),
        SankeyObject(SYS.GraphicPapers),
        SankeyObject(SYS.SanitaryPapers),
        SankeyObject(SYS.Packaging),
        SankeyObject(SYS.OtherPaperProducts),
        SankeyObject(SYS.ParticleboardToRMIAndOther),
        SankeyObject(SYS.PlywoodToRMIAndOther),
        SankeyObject(SYS.NewBuilds),
        SankeyObject(SYS.SawnwoodToOther),
        SankeyObject(SYS.FibreboardToRMIAndOther),
         SankeyObject(SYS.OtherEngineeredWoodProductsToCst),
        
        
        SankeyObject(SYS.RecycledWoodFibre, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.RecycledPaper, input_port='Roundwood and recycled fibres'),

        SankeyObject(SYS.WoodFibresForEnergy),
        SankeyObject(SYS.VeneerSheets),

        SankeyObject(SYS.SoftwoodRoundwood, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.HardwoodRoundwood, input_port='Roundwood and recycled fibres'),
       
        

    ],
)

resolve_and_show_elements(elements, solution = 'Push s_FlatLowRiseConstruction x 0',object_type_palette=palette, height=1100, width=1400)
```

```{code-cell} ipython3
guess_and_show(SYS.BuildingElementsManufacturing)
```

```{code-cell} ipython3
from semantic_sankeys.build_sdd import build_sdd
from semantic_sankeys.graphviz_graph import sdd_ordering
```

```{code-cell} ipython3
resolve_elements(elements)
sdd = build_sdd(elements)
sdd = sdd_ordering(sdd)
```

```{code-cell} ipython3
SankeyDefinition(nodes={'http://ukfires.org/analyses/UK-wood/system/Sawmills': ProcessGroupExtra(selection=['Sawmills Hardwood', 'Sawmills Softwood', 'http://ukfires.org/analyses/UK-wood/system/SawmillsHardwood', 'http://ukfires.org/analyses/UK-wood/system/SawmillsSoftwood'], partition=None, direction='R', title='Sawmills', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/Pulpmills': ProcessGroupExtra(selection=['New pulp making', 'Pulpmills by products', 'Pulpmills recycled paper', 'http://ukfires.org/analyses/UK-wood/system/NewPulpMaking', 'http://ukfires.org/analyses/UK-wood/system/PulpmillsByProducts', 'http://ukfires.org/analyses/UK-wood/system/PulpmillsRecycledPaper'], partition=None, direction='R', title='Pulpmills', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction': ProcessGroupExtra(selection=['By products to other energy feedstocks', 'By-products to wood pellets manufacturing', 'Hardwood roundwood to other energy feedstocks', 'Post consumer wood to other energy feedstocks', 'Softwood roundwood to other energy feedstocks', 'Softwood roundwood to wood pellets manufacturing', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksByProducts', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksHardwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksPostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksSoftwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturingByProducts', 'http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturingSoftwoodRoundwood'], partition=None, direction='R', title='Energy', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets': ProcessGroupExtra(selection=['Recycled fibres processing to pallets', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets'], partition=None, direction='R', title='Recycled fibres processing to pallets', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing': ProcessGroupExtra(selection=['Wooden bedroom furniture manufacturing', 'Wooden kitchen furniture manufacturing', 'Wooden office furniture manufacturing', 'Wooden other furniture manufacturing', 'Wooden seats manufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurnitureManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurnitureManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurnitureManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurnitureManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeatsManufacturing'], partition=None, direction='R', title='Furniture manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing': ProcessGroupExtra(selection=['Doors manufacturing', 'Flooring manufacturing', 'Windows manufacturing', 'http://ukfires.org/analyses/UK-wood/system/DoorsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/FlooringManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WindowsManufacturing'], partition=None, direction='R', title='Joinery manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing': ProcessGroupExtra(selection=['Other wood containers manufacturing', 'Pallets manufacturing', 'Refurbished pallets manufacturing', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainersManufacturing', 'http://ukfires.org/analyses/UK-wood/system/PalletsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPalletsManufacturing'], partition=None, direction='R', title='Packaging manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing': ProcessGroupExtra(selection=['Fencing posts manufacturing', 'Fencing rails and boards manufacturing', 'Railway sleepers manufacturing', 'Roundwood to fencing and outdoor', 'Roundwood to fencing manufacturing', 'Sawnwood to fencing and outdoor', 'Sawnwood to fencing manufacturing', 'http://ukfires.org/analyses/UK-wood/system/FencingPostsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoardsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepersManufacturing', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoorManufacturing', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoorManufacturing'], partition=None, direction='R', title='Fencing manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing': ProcessGroupExtra(selection=['Oth. objects manufacturing', 'http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing'], partition=None, direction='R', title='Oth. objects manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/EnergyIndustry': ProcessGroupExtra(selection=['Other energy feedstocks production', 'Wood pellets manufacturing', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksProduction', 'http://ukfires.org/analyses/UK-wood/system/WoodPelletsManufacturing'], partition=None, direction='R', title='Energy industry', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing': ProcessGroupExtra(selection=['Fibreboard to RMI', 'FormworkScaffolding manufacturing', 'Particleboard to RMI', 'Plywood to RMI', 'Sawnwood to RMI', 'Upper floors manufacturing', 'WoodFramesForNewStructures manufacturing', 'WoodRoofsForNewStructures manufacturing', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRepairMaintenanceImprovement', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffoldingManufacturing', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRepairMaintenanceImprovement', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRepairMaintenanceImprovement', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRepairMaintenanceImprovement', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructuresManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructuresManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructuresManufacturing'], partition=None, direction='R', title='Construction products manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing': ProcessGroupExtra(selection=['By-products to WBP fibres', 'Fibreboard manufacturing', 'Particleboard manufacturing', 'Plywood manufacturing', 'Recycled fibres to WBP fibres', 'Roundwood to WBP fibres', 'Veneer sheets manufacturing', 'WBP Fibres', 'http://ukfires.org/analyses/UK-wood/system/FibreboardManufacturing', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardManufacturing', 'http://ukfires.org/analyses/UK-wood/system/PlywoodManufacturing', 'http://ukfires.org/analyses/UK-wood/system/VeneerSheetsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/WBPFibres', 'http://ukfires.org/analyses/UK-wood/system/WBPFibresByProducts', 'http://ukfires.org/analyses/UK-wood/system/WBPFibresRecycledWoodFibre', 'http://ukfires.org/analyses/UK-wood/system/WBPFibresSoftwoodRoundwood'], partition=None, direction='R', title='WBP manufacturing', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy': ProcessGroupExtra(selection=['Other energy feedstocks wood fibres', 'Wood pellets wood fibres', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres', 'http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres'], partition=None, direction='R', title='Wood fibres for energy', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Fibreboard': ProcessGroupExtra(selection=['Fibreboard', 'http://ukfires.org/analyses/UK-wood/system/Fibreboard'], partition=None, direction='R', title='Fibreboard', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Particleboard': ProcessGroupExtra(selection=['Particleboard', 'http://ukfires.org/analyses/UK-wood/system/Particleboard'], partition=None, direction='R', title='Particleboard', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood': ProcessGroupExtra(selection=['Softwood Sawnwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood'], partition=None, direction='R', title='Softwood Sawnwood', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood': ProcessGroupExtra(selection=['Hardwood Sawnwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood'], partition=None, direction='R', title='Hardwood Sawnwood', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Plywood': ProcessGroupExtra(selection=['Plywood', 'http://ukfires.org/analyses/UK-wood/system/Plywood'], partition=None, direction='R', title='Plywood', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/VeneerSheets': ProcessGroupExtra(selection=['Veneer sheets', 'http://ukfires.org/analyses/UK-wood/system/VeneerSheets'], partition=None, direction='R', title='Veneer sheets', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Pulp': ProcessGroupExtra(selection=['Pulp', 'http://ukfires.org/analyses/UK-wood/system/Pulp'], partition=None, direction='R', title='Pulp', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/RecycledPulp': ProcessGroupExtra(selection=['Recycled pulp', 'http://ukfires.org/analyses/UK-wood/system/RecycledPulp'], partition=None, direction='R', title='Recycled pulp', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/ByProducts': ProcessGroupExtra(selection=['By-products', 'http://ukfires.org/analyses/UK-wood/system/ByProducts'], partition=None, direction='R', title='By-products', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets': ProcessGroupExtra(selection=['Recycled fibres to pallets', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets'], partition=None, direction='R', title='Recycled fibres to pallets', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Papermills': ProcessGroupExtra(selection=['Graphic papers manufacturing', 'Other paper products manufacturing', 'Packaging manufacturing', 'Sanitary papers manufacturing', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapersManufacturing', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProductsManufacturing', 'http://ukfires.org/analyses/UK-wood/system/PackagingManufacturing', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapersManufacturing'], partition=None, direction='R', title='Papermills', node_type='process'), 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood': ProcessGroupExtra(selection=['Softwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood'], partition=None, direction='R', title='Softwood', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood': ProcessGroupExtra(selection=['Hardwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood'], partition=None, direction='R', title='Hardwood', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres': ProcessGroupExtra(selection=['PostConsumerWood', 'Recycled wood fibre', 'http://ukfires.org/analyses/UK-wood/system/PostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre'], partition=None, direction='R', title='Recycled fibres', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper': ProcessGroupExtra(selection=['Recycled paper', 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper'], partition=None, direction='R', title='Recycled paper', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/WoodContainers': ProcessGroupExtra(selection=['Other containers', 'Pallets', 'Refurbished pallets', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers', 'http://ukfires.org/analyses/UK-wood/system/Pallets', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets'], partition=None, direction='R', title='Industrial packaging', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Furniture': ProcessGroupExtra(selection=['Wooden bedroom furniture', 'Wooden kitchen furniture', 'Wooden office furniture', 'Wooden other furniture', 'Wooden seats', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeats'], partition=None, direction='R', title='Furniture', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Joinery': ProcessGroupExtra(selection=['Doors', 'Flooring', 'Windows', 'http://ukfires.org/analyses/UK-wood/system/Doors', 'http://ukfires.org/analyses/UK-wood/system/Flooring', 'http://ukfires.org/analyses/UK-wood/system/Windows'], partition=None, direction='R', title='Joinery', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/WoodPellets': ProcessGroupExtra(selection=['Wood pellets', 'http://ukfires.org/analyses/UK-wood/system/WoodPellets'], partition=None, direction='R', title='Wood pellets', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/OtherObjects': ProcessGroupExtra(selection=['Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects'], partition=None, direction='R', title='Other objects', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks': ProcessGroupExtra(selection=['Other feedstocks', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks'], partition=None, direction='R', title='Other feedstocks', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers': ProcessGroupExtra(selection=['Graphic papers', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers'], partition=None, direction='R', title='Graphic papers', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers': ProcessGroupExtra(selection=['Sanitary papers', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers'], partition=None, direction='R', title='Sanitary papers', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/Packaging': ProcessGroupExtra(selection=['Packaging', 'http://ukfires.org/analyses/UK-wood/system/Packaging'], partition=None, direction='R', title='Packaging', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts': ProcessGroupExtra(selection=['Other paper products', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts'], partition=None, direction='R', title='Other paper products', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/ConstructionProducts': ProcessGroupExtra(selection=['Fibreboard to construction', 'Formwork Scaffolding', 'Particleboard to construction', 'Plywood to construction', 'Sawnwood to construction', 'Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures'], partition=None, direction='R', title='Construction products', node_type='object'), 'http://ukfires.org/analyses/UK-wood/system/IndustrialResidues': ProcessGroupExtra(selection=['Pre Consumer Waste Construction', 'Pre Consumer Waste Products', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts'], partition=None, direction='R', title='Industrial residues', node_type='object'), '__output_Products': Waypoint(partition=Partition(groups=(Group(label='Fibreboard to construction', query=(('material', ('Fibreboard to construction', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther')),)), Group(label='Joinery', query=(('material', ('Doors', 'Flooring', 'Windows', 'http://ukfires.org/analyses/UK-wood/system/Doors', 'http://ukfires.org/analyses/UK-wood/system/Flooring', 'http://ukfires.org/analyses/UK-wood/system/Windows')),)), Group(label='Furniture', query=(('material', ('Wooden bedroom furniture', 'Wooden kitchen furniture', 'Wooden office furniture', 'Wooden other furniture', 'Wooden seats', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeats')),)), Group(label='Industrial residues', query=(('material', ('Pre Consumer Waste Construction', 'Pre Consumer Waste Products', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts')),)), Group(label='Pallets', query=(('material', ('Pallets', 'http://ukfires.org/analyses/UK-wood/system/Pallets')),)), Group(label='Other containers', query=(('material', ('Other containers', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers')),)), Group(label='Refurbished pallets', query=(('material', ('Refurbished pallets', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets')),)), Group(label='Other objects', query=(('material', ('Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects')),)), Group(label='Fencing & outdoors', query=(('material', ('Fencing posts', 'Fencing rails and boards', 'Railway sleepers', 'Roundwood to fencing and outdoor', 'Sawnwood to fencing and outdoor', 'http://ukfires.org/analyses/UK-wood/system/FencingPosts', 'http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepers', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor')),)))), title='Products'), '__output_Construction': Waypoint(partition=Partition(groups=(Group(label='Other paper products', query=(('material', ('Other paper products', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts')),)), Group(label='Graphic papers', query=(('material', ('Graphic papers', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers')),)), Group(label='Sanitary papers', query=(('material', ('Sanitary papers', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers')),)), Group(label='Packaging', query=(('material', ('Packaging', 'http://ukfires.org/analyses/UK-wood/system/Packaging')),)), Group(label='Wood pellets', query=(('material', ('Wood pellets', 'http://ukfires.org/analyses/UK-wood/system/WoodPellets')),)), Group(label='Other feedstocks', query=(('material', ('Other feedstocks', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks')),)), Group(label='New structures', query=(('material', ('Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures')),)), Group(label='Sawnwood to construction', query=(('material', ('Formwork Scaffolding', 'Sawnwood to construction', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther')),)), Group(label='Particleboard to construction', query=(('material', ('Particleboard to construction', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther')),)), Group(label='Plywood to construction', query=(('material', ('Plywood to construction', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther')),)))), title='Construction'), '__input_Roundwood and recycled fibres': Waypoint(partition=Partition(groups=(Group(label='Recycled paper', query=(('material', ('Recycled paper', 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper')),)), Group(label='Softwood', query=(('material', ('Softwood', 'SoftwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood')),)), Group(label='Hardwood', query=(('material', ('Hardwood', 'HardwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood')),)), Group(label='Recycled fibres', query=(('material', ('PostConsumerWood', 'Recycled wood fibre', 'http://ukfires.org/analyses/UK-wood/system/PostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre')),)))), title='Roundwood and recycled fibres')}, bundles={0: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing'), 1: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing'), 2: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Particleboard', target=Elsewhere, flow_selection='is_trade'), 3: Bundle(source='http://ukfires.org/analyses/UK-wood/system/VeneerSheets', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 4: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Sawmills', target='http://ukfires.org/analyses/UK-wood/system/ByProducts'), 5: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Pulp', target='http://ukfires.org/analyses/UK-wood/system/Papermills'), 6: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing', target=Elsewhere, flow_selection='is_trade'), 7: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing', flow_selection='is_trade'), 8: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SanitaryPapers', target=Elsewhere, flow_selection='is_trade'), 9: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Plywood', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 10: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues', flow_selection='is_trade'), 11: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target=Elsewhere, flow_selection='is_trade'), 12: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Plywood', target='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing'), 13: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Pulp', flow_selection='is_trade'), 14: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets', flow_selection='is_trade'), 15: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', waypoints=('__input_Roundwood and recycled fibres',), flow_selection="material in ['Softwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood'] and not is_trade"), 16: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/WoodPellets', flow_selection='is_trade'), 17: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledPaper', waypoints=('__input_Roundwood and recycled fibres',), flow_selection="material in ['Recycled paper', 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper'] and not is_trade"), 18: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledPulp', target='http://ukfires.org/analyses/UK-wood/system/Papermills'), 19: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Plywood', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing'), 20: Bundle(source='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 21: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Roundwood to fencing and outdoor', 'Sawnwood to fencing and outdoor', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor'] and not is_trade"), 22: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Sawmills', target='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood'), 23: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/VeneerSheets', flow_selection='is_trade'), 24: Bundle(source='http://ukfires.org/analyses/UK-wood/system/VeneerSheets', target=Elsewhere, flow_selection='is_trade'), 25: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Papermills', target='http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts'), 26: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Pulpmills', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 27: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing'), 28: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing'), 29: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledPaper', flow_selection='is_trade'), 30: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Fibreboard to construction', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther'] and not is_trade"), 31: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing'), 32: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Fibreboard', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 33: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing', target=Elsewhere, flow_selection='is_trade'), 34: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction'), 35: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', flow_selection='is_trade'), 36: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', waypoints=('__input_Roundwood and recycled fibres',), flow_selection="material in ['PostConsumerWood', 'Recycled wood fibre', 'http://ukfires.org/analyses/UK-wood/system/PostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre'] and not is_trade"), 37: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing', flow_selection='is_trade'), 38: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Particleboard', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing'), 39: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts', flow_selection='is_trade'), 40: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks', target=Elsewhere, flow_selection='is_trade'), 41: Bundle(source='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues', target=Elsewhere, flow_selection='is_trade'), 42: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Fibreboard', target=Elsewhere, flow_selection='is_trade'), 43: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing'), 44: Bundle(source='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Pre Consumer Waste Construction', 'Pre Consumer Waste Products', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts'] and not is_trade"), 45: Bundle(source='http://ukfires.org/analyses/UK-wood/system/GraphicPapers', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Graphic papers', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers'] and not is_trade"), 46: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/Sawmills'), 47: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodContainers', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Refurbished pallets', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets'] and not is_trade"), 48: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 49: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodContainers', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Other containers', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers'] and not is_trade"), 50: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Pulpmills', target='http://ukfires.org/analyses/UK-wood/system/RecycledPulp'), 51: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Pulp', target=Elsewhere, flow_selection='is_trade'), 52: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ByProducts', target=Elsewhere, flow_selection='is_trade'), 53: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Sawmills', target='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood'), 54: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 55: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/ByProducts', flow_selection='is_trade'), 56: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Particleboard', target='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing'), 57: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets', target='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets'), 58: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Pulpmills', target='http://ukfires.org/analyses/UK-wood/system/Pulp'), 59: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing', flow_selection='is_trade'), 60: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Fibreboard', flow_selection='is_trade'), 61: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Papermills', target='http://ukfires.org/analyses/UK-wood/system/Packaging'), 62: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SanitaryPapers', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Sanitary papers', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers'] and not is_trade"), 63: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target='http://ukfires.org/analyses/UK-wood/system/Plywood'), 64: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood', waypoints=('__input_Roundwood and recycled fibres',), flow_selection="material in ['Hardwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood'] and not is_trade"), 65: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', target=Elsewhere, flow_selection='is_trade'), 66: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Joinery', flow_selection='is_trade'), 67: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodContainers', target=Elsewhere, flow_selection='is_trade'), 68: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks', flow_selection='is_trade'), 69: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing', target='http://ukfires.org/analyses/UK-wood/system/Furniture'), 70: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 71: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Fibreboard', target='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing'), 72: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', flow_selection='is_trade'), 73: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Other paper products', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts'] and not is_trade"), 74: Bundle(source='http://ukfires.org/analyses/UK-wood/system/EnergyIndustry', target='http://ukfires.org/analyses/UK-wood/system/WoodPellets'), 75: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target='http://ukfires.org/analyses/UK-wood/system/Particleboard'), 76: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 77: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing'), 78: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood', flow_selection='is_trade'), 79: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledPulp', target=Elsewhere, flow_selection='is_trade'), 80: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Joinery', target=Elsewhere, flow_selection='is_trade'), 81: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Formwork Scaffolding', 'Sawnwood to construction', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther'] and not is_trade"), 82: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 83: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodContainers', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Pallets', 'http://ukfires.org/analyses/UK-wood/system/Pallets'] and not is_trade"), 84: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/Sawmills'), 85: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Furniture', target=Elsewhere, flow_selection='is_trade'), 86: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy', flow_selection='is_trade'), 87: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Papermills', target='http://ukfires.org/analyses/UK-wood/system/SanitaryPapers'), 88: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target=Elsewhere, flow_selection='is_trade'), 89: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing', target='http://ukfires.org/analyses/UK-wood/system/OtherObjects'), 90: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', target='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets'), 91: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing'), 92: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing', target=Elsewhere, flow_selection='is_trade'), 93: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherObjects', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects'] and not is_trade"), 94: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 95: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Plywood', flow_selection='is_trade'), 96: Bundle(source='http://ukfires.org/analyses/UK-wood/system/EnergyIndustry', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 97: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodPellets', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Wood pellets', 'http://ukfires.org/analyses/UK-wood/system/WoodPellets'] and not is_trade"), 98: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Particleboard', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 99: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing', target='http://ukfires.org/analyses/UK-wood/system/WoodContainers'), 100: Bundle(source='http://ukfires.org/analyses/UK-wood/system/VeneerSheets', target='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing'), 101: Bundle(source='http://ukfires.org/analyses/UK-wood/system/VeneerSheets', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing'), 102: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Joinery', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Doors', 'Flooring', 'Windows', 'http://ukfires.org/analyses/UK-wood/system/Doors', 'http://ukfires.org/analyses/UK-wood/system/Flooring', 'http://ukfires.org/analyses/UK-wood/system/Windows'] and not is_trade"), 103: Bundle(source='http://ukfires.org/analyses/UK-wood/system/EnergyIndustry', target='http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks'), 104: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/GraphicPapers', flow_selection='is_trade'), 105: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing', target='http://ukfires.org/analyses/UK-wood/system/Joinery'), 106: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Particleboard', target='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing'), 107: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', flow_selection='is_trade'), 108: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ByProducts', target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction'), 109: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledPaper', target='http://ukfires.org/analyses/UK-wood/system/Pulpmills'), 110: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', flow_selection='is_trade'), 111: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledPulp', flow_selection='is_trade'), 112: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction'), 113: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', flow_selection='is_trade'), 114: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction'), 115: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Fibreboard', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing'), 116: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing', target=Elsewhere, flow_selection='is_trade'), 117: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres', target='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing'), 118: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Particleboard', flow_selection='is_trade'), 119: Bundle(source='http://ukfires.org/analyses/UK-wood/system/GraphicPapers', target=Elsewhere, flow_selection='is_trade'), 120: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Plywood', target=Elsewhere, flow_selection='is_trade'), 121: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledPaper', target=Elsewhere, flow_selection='is_trade'), 122: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Packaging', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Packaging', 'http://ukfires.org/analyses/UK-wood/system/Packaging'] and not is_trade"), 123: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodPellets', target=Elsewhere, flow_selection='is_trade'), 124: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, flow_selection='is_trade'), 125: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts'), 126: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target=Elsewhere, flow_selection='is_trade'), 127: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/OtherObjects', flow_selection='is_trade'), 128: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing', flow_selection='is_trade'), 129: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Papermills', target='http://ukfires.org/analyses/UK-wood/system/GraphicPapers'), 130: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets', target=Elsewhere, flow_selection='is_trade'), 131: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Plywood to construction', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther'] and not is_trade"), 132: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ByProducts', target='http://ukfires.org/analyses/UK-wood/system/Pulpmills'), 133: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherObjects', target=Elsewhere, flow_selection='is_trade'), 134: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing'), 135: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Fencing posts', 'Fencing rails and boards', 'Railway sleepers', 'http://ukfires.org/analyses/UK-wood/system/FencingPosts', 'http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepers'] and not is_trade"), 136: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood', flow_selection='is_trade'), 137: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target='http://ukfires.org/analyses/UK-wood/system/Fibreboard'), 138: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ByProducts', target='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing'), 139: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Packaging', target=Elsewhere, flow_selection='is_trade'), 140: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood', target=Elsewhere, flow_selection='is_trade'), 141: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy', target=Elsewhere, flow_selection='is_trade'), 142: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures'] and not is_trade"), 143: Bundle(source='http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing', target='http://ukfires.org/analyses/UK-wood/system/Joinery'), 144: Bundle(source='http://ukfires.org/analyses/UK-wood/system/ConstructionProducts', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Particleboard to construction', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther'] and not is_trade"), 145: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/WoodContainers', flow_selection='is_trade'), 146: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Packaging', flow_selection='is_trade'), 147: Bundle(source='http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing', target='http://ukfires.org/analyses/UK-wood/system/IndustrialResidues'), 148: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood', target='http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing'), 149: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks', target=Elsewhere, waypoints=('__output_Construction',), flow_selection="material in ['Other feedstocks', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks'] and not is_trade"), 150: Bundle(source='http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood', target='http://ukfires.org/analyses/UK-wood/system/Pulpmills'), 151: Bundle(source='http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets', target='http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing'), 152: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction', target='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy'), 153: Bundle(source='http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood', target=Elsewhere, flow_selection='is_trade'), 154: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy', target='http://ukfires.org/analyses/UK-wood/system/EnergyIndustry'), 155: Bundle(source='http://ukfires.org/analyses/UK-wood/system/Furniture', target=Elsewhere, waypoints=('__output_Products',), flow_selection="material in ['Wooden bedroom furniture', 'Wooden kitchen furniture', 'Wooden office furniture', 'Wooden other furniture', 'Wooden seats', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeats'] and not is_trade"), 156: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/SanitaryPapers', flow_selection='is_trade'), 157: Bundle(source=Elsewhere, target='http://ukfires.org/analyses/UK-wood/system/Furniture', flow_selection='is_trade'), 158: Bundle(source='http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing', target='http://ukfires.org/analyses/UK-wood/system/VeneerSheets'), 159: Bundle(source='http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts', target=Elsewhere, flow_selection='is_trade')}, ordering=Ordering( ; __input_Roundwood and recycled fibres;  | ; http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood, http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood;  | ; http://ukfires.org/analyses/UK-wood/system/RecycledPaper, http://ukfires.org/analyses/UK-wood/system/Sawmills;  | ; http://ukfires.org/analyses/UK-wood/system/ByProducts, http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibres;  | ; http://ukfires.org/analyses/UK-wood/system/Pulpmills, http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergyProduction, http://ukfires.org/analyses/UK-wood/system/WBPmanufacturing, http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreProcessingForPallets;  | ; http://ukfires.org/analyses/UK-wood/system/Pulp, http://ukfires.org/analyses/UK-wood/system/RecycledPulp, http://ukfires.org/analyses/UK-wood/system/WoodFibresForEnergy, http://ukfires.org/analyses/UK-wood/system/Fibreboard, http://ukfires.org/analyses/UK-wood/system/VeneerSheets, http://ukfires.org/analyses/UK-wood/system/Particleboard, http://ukfires.org/analyses/UK-wood/system/Plywood, http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood, http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets, http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood;  | ; http://ukfires.org/analyses/UK-wood/system/Papermills, http://ukfires.org/analyses/UK-wood/system/EnergyIndustry, http://ukfires.org/analyses/UK-wood/system/JoineryManufacturing, http://ukfires.org/analyses/UK-wood/system/ConstructionProductsManufacturing, http://ukfires.org/analyses/UK-wood/system/FurnitureManufacturing, http://ukfires.org/analyses/UK-wood/system/WoodenContainersManufacturing, http://ukfires.org/analyses/UK-wood/system/OtherObjectsManufacturing, http://ukfires.org/analyses/UK-wood/system/FencingAndOutdoorManufacturing;  | ; http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts, http://ukfires.org/analyses/UK-wood/system/GraphicPapers, http://ukfires.org/analyses/UK-wood/system/SanitaryPapers, http://ukfires.org/analyses/UK-wood/system/Packaging, http://ukfires.org/analyses/UK-wood/system/WoodPellets, http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks, http://ukfires.org/analyses/UK-wood/system/ConstructionProducts, http://ukfires.org/analyses/UK-wood/system/Joinery, http://ukfires.org/analyses/UK-wood/system/Furniture, http://ukfires.org/analyses/UK-wood/system/IndustrialResidues, http://ukfires.org/analyses/UK-wood/system/WoodContainers, http://ukfires.org/analyses/UK-wood/system/OtherObjects;  | ; __output_Construction, __output_Products;  ), flow_selection=None, flow_partition=Partition(groups=(Group(label='Fibreboard', query=(('material', ('Fibreboard', 'http://ukfires.org/analyses/UK-wood/system/Fibreboard')),)), Group(label='Particleboard', query=(('material', ('Particleboard', 'http://ukfires.org/analyses/UK-wood/system/Particleboard')),)), Group(label='Softwood Sawnwood', query=(('material', ('Softwood Sawnwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodSawnwood')),)), Group(label='Hardwood Sawnwood', query=(('material', ('Hardwood Sawnwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodSawnwood')),)), Group(label='Plywood', query=(('material', ('Plywood', 'http://ukfires.org/analyses/UK-wood/system/Plywood')),)), Group(label='Pulp', query=(('material', ('Pulp', 'http://ukfires.org/analyses/UK-wood/system/Pulp')),)), Group(label='Recycled pulp', query=(('material', ('Recycled pulp', 'http://ukfires.org/analyses/UK-wood/system/RecycledPulp')),)), Group(label='Recycled fibres to pallets', query=(('material', ('Recycled fibres to pallets', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibreToPallets')),)), Group(label='By-products', query=(('material', ('By-products', 'ByProducts', 'http://ukfires.org/analyses/UK-wood/system/ByProducts')),)), Group(label='WBP Fibres', query=(('material', ('WBP Fibres', 'http://ukfires.org/analyses/UK-wood/system/WBPFibres')),)), Group(label='Refurbished pallets', query=(('material', ('Refurbished pallets', 'http://ukfires.org/analyses/UK-wood/system/RefurbishedPallets')),)), Group(label='Pallets', query=(('material', ('Pallets', 'http://ukfires.org/analyses/UK-wood/system/Pallets')),)), Group(label='Other containers', query=(('material', ('Other containers', 'http://ukfires.org/analyses/UK-wood/system/OtherWoodContainers')),)), Group(label='Furniture', query=(('material', ('Wooden bedroom furniture', 'Wooden kitchen furniture', 'Wooden office furniture', 'Wooden other furniture', 'Wooden seats', 'http://ukfires.org/analyses/UK-wood/system/WoodenBedroomFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenKitchenFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOfficeFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenOtherFurniture', 'http://ukfires.org/analyses/UK-wood/system/WoodenSeats')),)), Group(label='Fencing & outdoors', query=(('material', ('Fencing posts', 'Fencing rails and boards', 'Railway sleepers', 'Roundwood to fencing and outdoor', 'Sawnwood to fencing and outdoor', 'http://ukfires.org/analyses/UK-wood/system/FencingPosts', 'http://ukfires.org/analyses/UK-wood/system/FencingRailsAndBoards', 'http://ukfires.org/analyses/UK-wood/system/RailwaySleepers', 'http://ukfires.org/analyses/UK-wood/system/RoundwoodToFencingAndOutdoor', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToFencingAndOutdoor')),)), Group(label='Joinery', query=(('material', ('Doors', 'Flooring', 'Windows', 'http://ukfires.org/analyses/UK-wood/system/Doors', 'http://ukfires.org/analyses/UK-wood/system/Flooring', 'http://ukfires.org/analyses/UK-wood/system/Windows')),)), Group(label='Wood pellets', query=(('material', ('Wood pellets', 'http://ukfires.org/analyses/UK-wood/system/WoodPellets')),)), Group(label='Other feedstocks', query=(('material', ('Other feedstocks', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocks')),)), Group(label='Other objects', query=(('material', ('Other objects', 'http://ukfires.org/analyses/UK-wood/system/OtherObjects')),)), Group(label='Graphic papers', query=(('material', ('Graphic papers', 'http://ukfires.org/analyses/UK-wood/system/GraphicPapers')),)), Group(label='Sanitary papers', query=(('material', ('Sanitary papers', 'http://ukfires.org/analyses/UK-wood/system/SanitaryPapers')),)), Group(label='Packaging', query=(('material', ('Packaging', 'http://ukfires.org/analyses/UK-wood/system/Packaging')),)), Group(label='Other paper products', query=(('material', ('Other paper products', 'http://ukfires.org/analyses/UK-wood/system/OtherPaperProducts')),)), Group(label='Particleboard to construction', query=(('material', ('Particleboard to construction', 'http://ukfires.org/analyses/UK-wood/system/ParticleboardToRMIAndOther')),)), Group(label='Plywood to construction', query=(('material', ('Plywood to construction', 'http://ukfires.org/analyses/UK-wood/system/PlywoodToRMIAndOther')),)), Group(label='New structures', query=(('material', ('Wood floor framing for new structures', 'Wood frames for new structures', 'Wood roof for new structures', 'http://ukfires.org/analyses/UK-wood/system/WoodFloorFramingForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodFramesForNewStructures', 'http://ukfires.org/analyses/UK-wood/system/WoodRoofsForNewStructures')),)), Group(label='Fibreboard to construction', query=(('material', ('Fibreboard to construction', 'http://ukfires.org/analyses/UK-wood/system/FibreboardToRMIAndOther')),)), Group(label='Sawnwood to construction', query=(('material', ('Formwork Scaffolding', 'Sawnwood to construction', 'http://ukfires.org/analyses/UK-wood/system/FormworkScaffolding', 'http://ukfires.org/analyses/UK-wood/system/SawnwoodToRMIAndOther')),)), Group(label='Recycled fibres', query=(('material', ('PostConsumerWood', 'Recycled wood fibre', 'http://ukfires.org/analyses/UK-wood/system/PostConsumerWood', 'http://ukfires.org/analyses/UK-wood/system/RecycledWoodFibre')),)), Group(label='Recycled paper', query=(('material', ('Recycled paper', 'http://ukfires.org/analyses/UK-wood/system/RecycledPaper')),)), Group(label='Wood fibres for energy', query=(('material', ('Other energy feedstocks wood fibres', 'Wood pellets wood fibres', 'http://ukfires.org/analyses/UK-wood/system/OtherEnergyFeedstocksWoodFibres', 'http://ukfires.org/analyses/UK-wood/system/WoodPelletsWoodFibres')),)), Group(label='Veneer sheets', query=(('material', ('Veneer sheets', 'http://ukfires.org/analyses/UK-wood/system/VeneerSheets')),)), Group(label='Softwood', query=(('material', ('Softwood', 'SoftwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/SoftwoodRoundwood')),)), Group(label='Hardwood', query=(('material', ('Hardwood', 'HardwoodRoundwood', 'http://ukfires.org/analyses/UK-wood/system/HardwoodRoundwood')),)), Group(label='Industrial residues', query=(('material', ('Pre Consumer Waste Construction', 'Pre Consumer Waste Products', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteConstruction', 'http://ukfires.org/analyses/UK-wood/system/PreConsumerWasteProducts')),)))), time_partition=None)
```

```{code-cell} ipython3
print("flow_partition = Partition.Simple(\"material\", [")
for g in sdd.flow_partition.groups:
    print("    (%r, %r)," % (g.label, g.query[0][1]))
print("])")
```

```{code-cell} ipython3
with open("temp_sdd.py", "wt") as f:
    f.write("nodes = " + repr(sdd.nodes) + "\n")
    f.write("bundles = " + repr(list(sdd.bundles.values())) + "\n")
    f.write("ordering = " + repr(sdd.ordering.layers) + "\n")
```

```{code-cell} ipython3
%load_ext autoreload
%autoreload 2
import final_sdd
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
flows_mean=flows.groupby(["source", "target", "material"]).mean()
```

```{code-cell} ipython3
flows_mean.to_excel(r"..\..\UK-wood-mfa\data_from_sankey_figure_3_manuscript\data_sankey_Figure_3_mean.xlsx")
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
%load_ext autoreload
%autoreload 2
import final_sdd
```

```{code-cell} ipython3
weave(final_sdd.sdd, flows_mean_reset_index, link_color=link_color).to_widget(width=1800, height=1800, debugging=True)
```

```{code-cell} ipython3
%load_ext autoreload
%autoreload 2
import final_sdd
```

```{code-cell} ipython3
palette = {
    SYS["WBPproducts"]: "#d7bde2",
    SYS["Pulp"]: "#8ebfdd",
     SYS["RecycledPulp"]: "lightgrey",
    SYS["Furniture"]: "#a957cd",
    SYS["NewStructures"]: "#935eaa",
    SYS["Roundwood"]: "#228b22",
    SYS["Sawnwood"]: "#be93d1",
    #SYS["ConstructionProducts"]: "#78508a",      
    SYS["IndustrialResidues"]: "lightgrey",
    SYS["RecycledWoodFibres"]: "lightgrey",
    SYS["EnergyIndustry"]: "#ff2727",
   SYS["RecycledPaper"]: "lightgrey",
    SYS["RecycledWoodFibreToPallets"]: "lightgrey",
    SYS["ByProducts"]: "#6fbcf2",
    SYS["FuelsForEnergy"]: "#ff2727",
    SYS["WoodPelletsWoodFibres"]: "#ff7676",
    SYS["OtherEnergyFeedstocksWoodFibres"]: "#ff7676",
        }



elements = SankeyElements(
   processes=[
    
       
         SankeyProcess(SYS.FurnitureManufacturing),
         SankeyProcess(SYS.JoineryManufacturing),
         SankeyProcess(SYS.WoodenContainersManufacturing),
         SankeyProcess(SYS.FencingAndOutdoorManufacturing, include_objects = ([SYS.SawnwoodToFencingAndOutdoor, SYS.RoundwoodToFencingAndOutdoor])),
         SankeyProcess(SYS.OtherProductsManufacturing),

         SankeyProcess(SYS.SawnConstructionProductsManufacturing, include_objects = ([SYS.WoodFramesForNewStructures ,
                                                                                       SYS.WoodFloorFramingForNewStructures,
                                                                                       SYS.WoodRoofsForNewStructures,
                                                                                      SYS.EndTerracedHouses,
                                                                                       SYS.MidTerracedHouses,
                                                                                       SYS.SemiDetachedHouses,
                                                                                        SYS.DetachedHouses,
                                                                                       SYS.Bungalows,
                                                                                       SYS.FlatLowRise,
                                                                                       SYS.ConvertedFlats ])),
      
     
         SankeyProcess(SYS.WoodFibresProductionForRMI),

 

      #  SankeyProcess(SYS.Fibreboard),
      #  SankeyProcess(SYS.Particleboard),
       #   SankeyProcess(SYS.OtherEngineeredWoodProducts),
      #  SankeyProcess(SYS.SoftwoodSawnwood),
      #  SankeyProcess(SYS.SoftwoodRoundwood),
      ##  SankeyProcess(SYS.HardwoodSawnwood),
       # SankeyProcess(SYS.Plywood),
      #  SankeyProcess(SYS.VeneerSheets),

   
        
     #   SankeyProcess(SYS.RecycledWoodFibreToPallets),
 
   ],
 
    
    
    objects=[
        SankeyObject(SYS.Fibreboard, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.Particleboard, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.SoftwoodSawnwood, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.HardwoodSawnwood, input_port='Roundwood and recycled fibres'),
        SankeyObject(SYS.Plywood, input_port='Roundwood and recycled fibres'),
          SankeyObject(SYS.OtherEngineeredWoodProducts, input_port='Roundwood and recycled fibres'),
    
        SankeyObject(SYS.RecycledWoodFibreToPallets, input_port='Roundwood and recycled fibres'),
      
      #  SankeyObject(SYS.WBPFibres),
       # SankeyObject(SYS.SawnProductsToCst),
      #  SankeyObject(SYS.InUse),
      #  SankeyObject(SYS.InUseProducts),
        SankeyObject(SYS.PreConsumerWasteProducts, output_port='Residues'),
       SankeyObject(SYS.SoftwoodRoundwood, input_port='Roundwood'),
    
    


        SankeyObject(SYS.RefurbishedPallets, output_port='Products'),
        SankeyObject(SYS.Pallets, output_port='Products'),
        SankeyObject(SYS.OtherWoodContainers, output_port='Products'),
        SankeyObject(SYS.Furniture, output_port='Products'),
        SankeyObject(SYS.FencingAndOutdoor, output_port='Products'),
        SankeyObject(SYS.Joinery, output_port='Products'),
 
        SankeyObject(SYS.OtherProducts, output_port='Products'),
   
          SankeyObject(SYS.ParticleboardToRMIAndOther, output_port='Products'),
           SankeyObject(SYS.PlywoodToRMIAndOther, output_port='Products'),
          SankeyObject(SYS.NewBuilds, output_port='Products'),
         SankeyObject(SYS.SawnwoodToOther, output_port='Products'),
          SankeyObject(SYS.FibreboardToRMIAndOther, output_port='Products'),
           SankeyObject(SYS.OtherEngineeredWoodProductsToCst, output_port='Products'),
        

        SankeyObject(SYS.VeneerSheets, input_port='Roundwood and recycled fibres'),

       
        

    ],
)

resolve_and_show_elements(elements, solution = 'Push s_FlatLowRiseConstruction x 0',object_type_palette=palette, height=1100, width=1400)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
