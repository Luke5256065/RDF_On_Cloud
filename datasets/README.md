## Datasets, Queries And File Formats Conversion Tools

# Datasets

The table below lists the datasets used during the experiments along with relevant statistics such as the number of triples, entities, literals, subjects, predicates, and the dataset size.

<table>
    <tr>
        <td></td>
        <td>Triple</td>
        <td>Entity</td>
        <td>Literal</td>
        <td>Subject</td>
        <td>Predicate</td>
        <td>Size</td>
    </tr>
    <tr>
        <td>Dbpedia</td>
        <td>113704605</td>
        <td>7404319</td>
        <td>19353142</td>
        <td>4796027</td>
        <td>53383</td>
        <td>14.4GB</td>
    </tr>
    <tr>
        <td>Watdiv</td>
        <td>108997714</td>
        <td>5212745</td>
        <td>5038202</td>
        <td>5212385</td>
        <td>86</td>
        <td>14.5GB</td>
    </tr>
    <tr>
        <td>LDBC SNB sf10</td>
        <td>478201036</td>
        <td>78088024</td>
        <td>121231019</td>
        <td>78080384</td>
        <td>40</td>
        <td>77.6GB</td>
    </tr>
    <tr>
        <td>LUBM10240</td>
        <td>1366712443</td>
        <td>222213905</td>
        <td>114292492</td>
        <td>222213889</td>
        <td>18</td>
        <td>223.2GB</td>
    </tr>
</table>

- Datasets links

Dbpedia: https://databus.dbpedia.org/dbpedia#data 

Watdiv 100M: https://github.com/dsg-uwaterloo/watdiv

LDBC SNB sf10: https://repository.surfsara.nl/datasets/cwi/snb

LUBM10240: https://www.dropbox.com/s/4ifouv5n5pa4vdk/10240_new_str.tar.gz?e=1&dl=0

# Queries

The experiment used a set of queries that are provided for median and large dataset. The snb_queries file includes multiple queries separated by the // delimiter.

# File Formats Conversion Tools

The following tools can be used to convert file formats, particularly RDF-based formats, during the experimentation process:

https://github.com/knakk/rdf2rdf