# Example data store for global glass MFA

The PRObs system has the idea of a "knowlege graph" or "data store" which contains datasets and metadata waiting to be used. The relevant data can then be used for any specific study. For the purposes of this example, this folder sets up a "mini data store" which has only the very limited data needed for the glass MFA in it. But this could be swapped out for the main data store.

## Building the data store RDF file

`doit run build_rdf script_source_dir=<path to Ontologies folder>`

The path to your probs-docs Ontologies folder needs to be given as above.

## Building the documentation

`doit run build_docs`

