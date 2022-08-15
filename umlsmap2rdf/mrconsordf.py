from rdflib import Graph, URIRef
from rdflib.term import Literal
from . import prefix
from tqdm import tqdm
import os



source_conversion = {
    "MSH": "MESH",
    "SNOMEDCT_US": "SNOMED",
    "NCI_NCI-GLOSS": "NCI_NCI_GLOSS"
}

class MRCCONSORDF:
    def __init__(self, fp: str, out_fp: str):
        self.fp = fp
        self.out_fp = out_fp


    
    def _clean_cui(self, cui: str) -> str:
        return cui.split("\t")[0]

    def do(self):
        
        graph = Graph()

        count = 0

        graph.add((URIRef(prefix.UMLS), URIRef(prefix.RDF+"type"), URIRef(prefix.OWL+'Ontology')))
        graph.add((URIRef(prefix.UMLS), URIRef(prefix.RDFS+"comment"), Literal("RDF Version of  UMLS mapping; converted with the UMLSMAPS2RDF tool (https://github.com/KeironO/umlsmap2rdf).")))
        graph.add((URIRef(prefix.UMLS), URIRef(prefix.RDFS+"label"), Literal("UMLS")))
        graph.add((URIRef(prefix.UMLS), URIRef(prefix.OWL+"versionInfo"), Literal("2022AA")))
        
        file_size = round(os.path.getsize(self.fp)/float(1<<20),3)
        with tqdm(total=100) as pbar:
            with open(self.fp, "r") as infile:
                for line in infile:
                    count += 1
                    content = line.split("|")

                    cui = content[0]
                    cui = self._clean_cui(cui)
                    lat = content[1]

                    graph.add((URIRef(prefix.UMLS+cui), URIRef(prefix.RDF+"type"), URIRef(prefix.OWL+'Class') ))
                    prefixes = [x for x in dir(prefix) if x[0] != "_"]

                    for _prefix in prefixes:
                        if _prefix != "UMLS":
                            graph.bind(_prefix, getattr(prefix, _prefix))

                    source = content[11]
                    if source in source_conversion:
                        source = source_conversion[source]

                    try:
                        if content[6] == "Y" and content[2] == "P":
                            source_uri = getattr(prefix, source)
                            graph.add((URIRef(prefix.UMLS+cui), URIRef(prefix.OWL+'sameAs'), URIRef(source_uri+content[13])))

                    except AttributeError:
                        pass
                    line_size = len(line.encode('utf-8'))/float(1<<20)
                    pbar.update((line_size/file_size*100))


        if True in [self.out_fp.endswith(x) for x in ["xml", "rdf"]]:
            format = 'application/rdf+xml'
        elif True in [self.out_fp.endswith(x) for x in ["json", "json-ld"]]:
            format = 'json-ld'
        elif self.out_fp.endswith("ttl"):
            format = "turtle"
        else:
            raise Exception("Filetype has to be one of xml,rdf,json,json-ld,ttl")

        graph.serialize(self.out_fp, format=format)

