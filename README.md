# umlsmap2rdf

These python scripts take the Unified Medical Language System (UMLS) `MRCONSO.RRF` file and translates them into into RDF/OWL files for mapping.

## Installation

You can install the development version directly from this repository with:

```
pip install git+https://github.com/KeironO/umlsmap2rdf --no-cache-dir
```

## Usage

```
umlsmap2rdf --input_fp /path/to/MRCONSO.RRF --output_fp /path/to/output.xml
```

Which will give you the following output:

```
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
   xmlns:OWL="http://www.w3.org/2002/07/owl#"
   xmlns:RDF="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:RDFS="http://www.w3.org/2000/01/rdf-schema#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
  <rdf:Description rdf:about="https://identifiers.org/umls:C0000511">
    <RDF:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <OWL:sameAs rdf:resource="http://purl.bioontology.org/ontology/MESH/D015112"/>
    <OWL:sameAs rdf:resource="https://www.cancer.gov/publications/dictionaries/cancer-terms/def/CDR0000367450"/>
    <OWL:sameAs rdf:resource="https://bioportal.bioontology.org/ontologies/NCI/C194"/>
  </rdf:Description>
  <rdf:Description rdf:about="https://identifiers.org/umls:C0000246">
    <RDF:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
```


## Currently supported mappings

```
MESH = "http://purl.bioontology.org/ontology/MESH/"
SNOMED = "http://bioportal.bioontology.org/ontologies/SNOMEDCT/"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
OWL = "http://www.w3.org/2002/07/owl#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
UMLS = "https://identifiers.org/umls:"
UMLS_STY = "http://purl.bioontology.org/ontology/STY/"
ICD10CM = "http://purl.bioontology.org/ontology/ICD10CM/"
RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
ICD9CM = "https://bioportal.bioontology.org/ontologies/ICD9CM/"
ICD10 = "https://identifiers.org/icd10:"
SKOS = "http://www.w3.org/2004/02/skos/core#"
RXNORM = "http://purl.bioontology.org/ontology/RXNORM/"
NCBI = "http://purl.bioontology.org/ontology/NCBITAXON/"
GO = "http://purl.obolibrary.org/obo/GO_"
WHO = "http://purl.bioontology.org/ontology/WHO-ART/"
NCI = "https://bioportal.bioontology.org/ontologies/NCI/"
DRUGBANK = "http://www.drugbank.ca/drugs/"
HPO = "http://purl.bioontology.org/ontology/HPO/"
NCI_NCI_GLOSS = "https://www.cancer.gov/publications/dictionaries/cancer-terms/def/"
```
