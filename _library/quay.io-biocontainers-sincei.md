---
layout: container
name:  "quay.io/biocontainers/sincei"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sincei/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sincei/container.yaml"
updated_at: "2024-12-31 03:26:44.574128"
latest: "0.4--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/sincei"
aliases:
 - "bigwigAverage"
 - "loompy"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "scBulkCoverage"
 - "scClusterCells"
 - "scCombineCounts"
 - "scCountQC"
 - "scCountReads"
 - "scFilterBarcodes"
 - "scFilterStats"
 - "scJSD"
 - "sincei"
 - "validate-docstrings"
 - "alignmentSieve"
 - "bamCompare"
 - "bamCoverage"
 - "bamPEFragmentSize"
 - "bigwigCompare"
 - "computeGCBias"
 - "computeMatrix"
 - "computeMatrixOperations"
 - "correctGCBias"
 - "deeptools"
 - "estimateReadFiltering"
 - "estimateScaleFactor"
 - "multiBamSummary"
 - "multiBigwigSummary"
 - "plotCorrelation"
 - "plotCoverage"
 - "plotEnrichment"
 - "plotFingerprint"
 - "plotHeatmap"
 - "plotPCA"
 - "plotProfile"
 - "h5tools_test_utils"
 - "igraph"
 - "sphinx-apidoc"
 - "sphinx-autogen"
versions:
 - "0.3.1--pyhdfd78af_0"
 - "0.4--pyhdfd78af_0"
 - "0.4--pyhdfd78af_1"
description: "singularity registry hpc automated addition for sincei"
config: {"url": "https://biocontainers.pro/tools/sincei", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sincei", "latest": {"0.4--pyhdfd78af_1": "sha256:acafa2ed0c2515d3201451015c501cb35ef8dcc800f6059b324ed4b0e7dd549d"}, "tags": {"0.3.1--pyhdfd78af_0": "sha256:2cd635a92b2878ffa5b2d706a9005120729a298f16dec623d912332ca2c6f688", "0.4--pyhdfd78af_0": "sha256:d142d212df4c1d24606021fd088ad2481c06840709b38147079da4aaf487dbf9", "0.4--pyhdfd78af_1": "sha256:acafa2ed0c2515d3201451015c501cb35ef8dcc800f6059b324ed4b0e7dd549d"}, "docker": "quay.io/biocontainers/sincei", "aliases": {"bigwigAverage": "/usr/local/bin/bigwigAverage", "loompy": "/usr/local/bin/loompy", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "scBulkCoverage": "/usr/local/bin/scBulkCoverage", "scClusterCells": "/usr/local/bin/scClusterCells", "scCombineCounts": "/usr/local/bin/scCombineCounts", "scCountQC": "/usr/local/bin/scCountQC", "scCountReads": "/usr/local/bin/scCountReads", "scFilterBarcodes": "/usr/local/bin/scFilterBarcodes", "scFilterStats": "/usr/local/bin/scFilterStats", "scJSD": "/usr/local/bin/scJSD", "sincei": "/usr/local/bin/sincei", "validate-docstrings": "/usr/local/bin/validate-docstrings", "alignmentSieve": "/usr/local/bin/alignmentSieve", "bamCompare": "/usr/local/bin/bamCompare", "bamCoverage": "/usr/local/bin/bamCoverage", "bamPEFragmentSize": "/usr/local/bin/bamPEFragmentSize", "bigwigCompare": "/usr/local/bin/bigwigCompare", "computeGCBias": "/usr/local/bin/computeGCBias", "computeMatrix": "/usr/local/bin/computeMatrix", "computeMatrixOperations": "/usr/local/bin/computeMatrixOperations", "correctGCBias": "/usr/local/bin/correctGCBias", "deeptools": "/usr/local/bin/deeptools", "estimateReadFiltering": "/usr/local/bin/estimateReadFiltering", "estimateScaleFactor": "/usr/local/bin/estimateScaleFactor", "multiBamSummary": "/usr/local/bin/multiBamSummary", "multiBigwigSummary": "/usr/local/bin/multiBigwigSummary", "plotCorrelation": "/usr/local/bin/plotCorrelation", "plotCoverage": "/usr/local/bin/plotCoverage", "plotEnrichment": "/usr/local/bin/plotEnrichment", "plotFingerprint": "/usr/local/bin/plotFingerprint", "plotHeatmap": "/usr/local/bin/plotHeatmap", "plotPCA": "/usr/local/bin/plotPCA", "plotProfile": "/usr/local/bin/plotProfile", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "igraph": "/usr/local/bin/igraph", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sincei.
singularity registry hpc automated addition for sincei
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sincei
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sincei:0.4--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sincei/0.4--pyhdfd78af_1
$ module help quay.io/biocontainers/sincei/0.4--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sincei-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sincei-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sincei-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sincei-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sincei-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sincei-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigwigAverage

```bash
$ singularity exec <container> /usr/local/bin/bigwigAverage
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigAverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigAverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scBulkCoverage

```bash
$ singularity exec <container> /usr/local/bin/scBulkCoverage
$ podman run --it --rm --entrypoint /usr/local/bin/scBulkCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scBulkCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scClusterCells

```bash
$ singularity exec <container> /usr/local/bin/scClusterCells
$ podman run --it --rm --entrypoint /usr/local/bin/scClusterCells   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scClusterCells   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scCombineCounts

```bash
$ singularity exec <container> /usr/local/bin/scCombineCounts
$ podman run --it --rm --entrypoint /usr/local/bin/scCombineCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scCombineCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scCountQC

```bash
$ singularity exec <container> /usr/local/bin/scCountQC
$ podman run --it --rm --entrypoint /usr/local/bin/scCountQC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scCountQC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scCountReads

```bash
$ singularity exec <container> /usr/local/bin/scCountReads
$ podman run --it --rm --entrypoint /usr/local/bin/scCountReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scCountReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scFilterBarcodes

```bash
$ singularity exec <container> /usr/local/bin/scFilterBarcodes
$ podman run --it --rm --entrypoint /usr/local/bin/scFilterBarcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scFilterBarcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scFilterStats

```bash
$ singularity exec <container> /usr/local/bin/scFilterStats
$ podman run --it --rm --entrypoint /usr/local/bin/scFilterStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scFilterStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scJSD

```bash
$ singularity exec <container> /usr/local/bin/scJSD
$ podman run --it --rm --entrypoint /usr/local/bin/scJSD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scJSD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sincei

```bash
$ singularity exec <container> /usr/local/bin/sincei
$ podman run --it --rm --entrypoint /usr/local/bin/sincei   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sincei   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate-docstrings

```bash
$ singularity exec <container> /usr/local/bin/validate-docstrings
$ podman run --it --rm --entrypoint /usr/local/bin/validate-docstrings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate-docstrings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignmentSieve

```bash
$ singularity exec <container> /usr/local/bin/alignmentSieve
$ podman run --it --rm --entrypoint /usr/local/bin/alignmentSieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignmentSieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamCompare

```bash
$ singularity exec <container> /usr/local/bin/bamCompare
$ podman run --it --rm --entrypoint /usr/local/bin/bamCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamCoverage

```bash
$ singularity exec <container> /usr/local/bin/bamCoverage
$ podman run --it --rm --entrypoint /usr/local/bin/bamCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamPEFragmentSize

```bash
$ singularity exec <container> /usr/local/bin/bamPEFragmentSize
$ podman run --it --rm --entrypoint /usr/local/bin/bamPEFragmentSize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamPEFragmentSize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigCompare

```bash
$ singularity exec <container> /usr/local/bin/bigwigCompare
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeGCBias

```bash
$ singularity exec <container> /usr/local/bin/computeGCBias
$ podman run --it --rm --entrypoint /usr/local/bin/computeGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeMatrix

```bash
$ singularity exec <container> /usr/local/bin/computeMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/computeMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeMatrixOperations

```bash
$ singularity exec <container> /usr/local/bin/computeMatrixOperations
$ podman run --it --rm --entrypoint /usr/local/bin/computeMatrixOperations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeMatrixOperations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correctGCBias

```bash
$ singularity exec <container> /usr/local/bin/correctGCBias
$ podman run --it --rm --entrypoint /usr/local/bin/correctGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correctGCBias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deeptools

```bash
$ singularity exec <container> /usr/local/bin/deeptools
$ podman run --it --rm --entrypoint /usr/local/bin/deeptools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeptools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimateReadFiltering

```bash
$ singularity exec <container> /usr/local/bin/estimateReadFiltering
$ podman run --it --rm --entrypoint /usr/local/bin/estimateReadFiltering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimateReadFiltering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimateScaleFactor

```bash
$ singularity exec <container> /usr/local/bin/estimateScaleFactor
$ podman run --it --rm --entrypoint /usr/local/bin/estimateScaleFactor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimateScaleFactor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiBamSummary

```bash
$ singularity exec <container> /usr/local/bin/multiBamSummary
$ podman run --it --rm --entrypoint /usr/local/bin/multiBamSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiBamSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiBigwigSummary

```bash
$ singularity exec <container> /usr/local/bin/multiBigwigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/multiBigwigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiBigwigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotCorrelation

```bash
$ singularity exec <container> /usr/local/bin/plotCorrelation
$ podman run --it --rm --entrypoint /usr/local/bin/plotCorrelation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotCorrelation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotCoverage

```bash
$ singularity exec <container> /usr/local/bin/plotCoverage
$ podman run --it --rm --entrypoint /usr/local/bin/plotCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotCoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotEnrichment

```bash
$ singularity exec <container> /usr/local/bin/plotEnrichment
$ podman run --it --rm --entrypoint /usr/local/bin/plotEnrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotEnrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotFingerprint

```bash
$ singularity exec <container> /usr/local/bin/plotFingerprint
$ podman run --it --rm --entrypoint /usr/local/bin/plotFingerprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotFingerprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHeatmap

```bash
$ singularity exec <container> /usr/local/bin/plotHeatmap
$ podman run --it --rm --entrypoint /usr/local/bin/plotHeatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHeatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotPCA

```bash
$ singularity exec <container> /usr/local/bin/plotPCA
$ podman run --it --rm --entrypoint /usr/local/bin/plotPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotProfile

```bash
$ singularity exec <container> /usr/local/bin/plotProfile
$ podman run --it --rm --entrypoint /usr/local/bin/plotProfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotProfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)