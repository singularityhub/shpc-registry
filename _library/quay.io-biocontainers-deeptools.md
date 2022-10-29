---
layout: container
name:  "quay.io/biocontainers/deeptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeptools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deeptools/container.yaml"
updated_at: "2022-10-29 05:55:50.472988"
latest: "3.1.3--py37h14c3975_1"
container_url: "https://biocontainers.pro/tools/deeptools"
aliases:
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
 - "2to3-3.7"
 - "ace2sam"
 - "assistant"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "chardetect"
 - "color-chrs.pl"
 - "dbus-cleanup-sockets"
versions:
 - "3.1.3--py37h14c3975_1"
description: "shpc-registry automated BioContainers addition for deeptools"
config: {"url": "https://biocontainers.pro/tools/deeptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeptools", "latest": {"3.1.3--py37h14c3975_1": "sha256:2bf9fbdd82da72ae0a1e4b0fe8e634215b9bbc02bfa510c175e2f15ee3a2a1a8"}, "tags": {"3.1.3--py37h14c3975_1": "sha256:2bf9fbdd82da72ae0a1e4b0fe8e634215b9bbc02bfa510c175e2f15ee3a2a1a8"}, "docker": "quay.io/biocontainers/deeptools", "aliases": {"alignmentSieve": "/usr/local/bin/alignmentSieve", "bamCompare": "/usr/local/bin/bamCompare", "bamCoverage": "/usr/local/bin/bamCoverage", "bamPEFragmentSize": "/usr/local/bin/bamPEFragmentSize", "bigwigCompare": "/usr/local/bin/bigwigCompare", "computeGCBias": "/usr/local/bin/computeGCBias", "computeMatrix": "/usr/local/bin/computeMatrix", "computeMatrixOperations": "/usr/local/bin/computeMatrixOperations", "correctGCBias": "/usr/local/bin/correctGCBias", "deeptools": "/usr/local/bin/deeptools", "estimateReadFiltering": "/usr/local/bin/estimateReadFiltering", "estimateScaleFactor": "/usr/local/bin/estimateScaleFactor", "multiBamSummary": "/usr/local/bin/multiBamSummary", "multiBigwigSummary": "/usr/local/bin/multiBigwigSummary", "plotCorrelation": "/usr/local/bin/plotCorrelation", "plotCoverage": "/usr/local/bin/plotCoverage", "plotEnrichment": "/usr/local/bin/plotEnrichment", "plotFingerprint": "/usr/local/bin/plotFingerprint", "plotHeatmap": "/usr/local/bin/plotHeatmap", "plotPCA": "/usr/local/bin/plotPCA", "plotProfile": "/usr/local/bin/plotProfile", "2to3-3.7": "/usr/local/bin/2to3-3.7", "ace2sam": "/usr/local/bin/ace2sam", "assistant": "/usr/local/bin/assistant", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "chardetect": "/usr/local/bin/chardetect", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeptools.
shpc-registry automated BioContainers addition for deeptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeptools:3.1.3--py37h14c3975_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeptools/3.1.3--py37h14c3975_1
$ module help quay.io/biocontainers/deeptools/3.1.3--py37h14c3975_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeptools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeptools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeptools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeptools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeptools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeptools-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
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