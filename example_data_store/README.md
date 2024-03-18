# Example data store for UK wood MFA

The PRObs system has the idea of a "knowlege graph" or "data store" which contains datasets and metadata waiting to be used. The relevant data can then be used for any specific study. 
## Building the data store RDF file

`doit run build_rdf script_source_dir=<path to Ontologies folder>`

The path to your probs-docs Ontologies folder needs to be given as above.

## Building the documentation

`doit run build_docs`

