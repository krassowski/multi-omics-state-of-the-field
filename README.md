# Multi-omics: state of the field

[![Build Status](https://travis-ci.com/krassowski/multi-omics-state-of-the-art.svg?token=JhArfvq99eozHLbsktv8&branch=master)](https://travis-ci.com/krassowski/multi-omics-state-of-the-art)

Literature analyses for "State of the Field in Multi-Omics Research: From Computational Needs to Data Mining and Sharing"

## Overiew

![image](https://user-images.githubusercontent.com/5832902/89242343-3f12ef80-d5f9-11ea-96b3-5fe06dfd0e4d.png)

**Figure X**. Characterisation of multi-omics literature based on a systematic screen of PubMed indexed articles (up to July 2020). The details of the methods with reproducible code are available at [github.com/krassowski/multi-omics-state-of-the-field](https://github.com/krassowski/multi-omics-state-of-the-field). The comprehensive search terms (see the online repository for details) were collapsed into four categories; _integrated omics_ (*) 
includes _integromics_ and _integrative_ omics, _multi-view_ (\*\*) includes multi-view|block|source|modal omics, _other terms_ (\*\*\*) include pan-, trans-, poly-, cross-omics.

The subpanels present: A) Combinations of omics (grouped by the characterised entities) commonly discussed occurring together in multi-omics articles (intersections with degree > 2 and at least 50 papers). The proteins group (1) also includes peptides, the metabolites group (2) includes other endogenous molecules, the epigenetic group (3) encompasses all epigenetic modifications. B) The number of multi-omics articles indexed in PubMed is rapidly increasing (also after adjusting for the number of articles published in matched journals - data not shown); the dip in 2020 can be attributed to indexing delay which was not accounted for. C) Articles of various types mention different numbers of omics; while it is understandable that multi-omics reviews discuss many omics, the computational method articles appear to lag behind all other article types. The detected number of omics may underestimate the actual numbers (due to the automated search strategy) but should put useful lower bound on the number of omics discussed. D) The number of articles mentioning the most popular clinical findings, disease terms (screening based on ClinVar diseases list) and species (based upon NCBI Taxonomy database). Both databases were manually filtered down to remove ambiguous terms and merge plural/singular forms. Only the abstracts were screened. E) The detected references to code and data versioning and distribution platforms and systems (links to repositories with deposited code/data); both the abstracts and full-texts (open-access subset, 77% of all articles) were screened. No manual curation to classify intend of the link inclusion (i.e. to share authors code/data vs to report the use of a datset/tool) was undertaken.


### Setup and requirements

Developed with:

- Ubuntu: 20.04 (x64)
- Python: 3.8.3
- R: 3.6.3

To install minimal requirements:

```bash
pip install -r requirements.txt
```

Additional requirements fro development and testing:

```bash
pip install -r requirements-dev.txt
```

Execute tests with:

```bash
python3 -m pytest
```
