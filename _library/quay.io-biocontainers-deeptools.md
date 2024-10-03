---
layout: container
name:  "quay.io/biocontainers/deeptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeptools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deeptools/container.yaml"
updated_at: "2024-10-03 03:13:37.015559"
latest: "3.5.5--pyhdfd78af_0"
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
 - "g-ir-doc-tool"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
versions:
 - "3.1.3--py37h14c3975_1"
 - "3.5.5--pyhdfd78af_0"
 - "3.4.3--py_0"
 - "3.3.2--py_1"
 - "3.2.1--py_0"
 - "3.1.3--py36h14c3975_1"
description: "shpc-registry automated BioContainers addition for deeptools"
config: {"url": "https://biocontainers.pro/tools/deeptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeptools", "latest": {"3.5.5--pyhdfd78af_0": "sha256:fab4182e0f1338745d9fe8315477e05a6484e717aac1430403dbc8d7e789ecf9"}, "tags": {"3.1.3--py37h14c3975_1": "sha256:ef1e36188b42d2dc4307ef27bb6232c8de9f9329be68a7d9c12f5304579cacee", "3.5.5--pyhdfd78af_0": "sha256:fab4182e0f1338745d9fe8315477e05a6484e717aac1430403dbc8d7e789ecf9", "3.4.3--py_0": "sha256:fa9360a860cba2e0f455ef501a6c208713caf110fd8bee2dd973105f16facb23", "3.3.2--py_1": "sha256:54e8e1984a109d5f2e31ad775aae6804979785b4670f07e08d23087d31f47a36", "3.2.1--py_0": "sha256:74bd8ac1811a084485e71464405ab46f0b95d5f7c77271cf3d21ba39b8b75966", "3.1.3--py36h14c3975_1": "sha256:1a70e1cfbfcfd4307188d2d39b0fb70f3f548b021ea1ae72ea5f86b0a06ccb6f"}, "docker": "quay.io/biocontainers/deeptools", "aliases": {"alignmentSieve": "/usr/local/bin/alignmentSieve", "bamCompare": "/usr/local/bin/bamCompare", "bamCoverage": "/usr/local/bin/bamCoverage", "bamPEFragmentSize": "/usr/local/bin/bamPEFragmentSize", "bigwigCompare": "/usr/local/bin/bigwigCompare", "computeGCBias": "/usr/local/bin/computeGCBias", "computeMatrix": "/usr/local/bin/computeMatrix", "computeMatrixOperations": "/usr/local/bin/computeMatrixOperations", "correctGCBias": "/usr/local/bin/correctGCBias", "deeptools": "/usr/local/bin/deeptools", "estimateReadFiltering": "/usr/local/bin/estimateReadFiltering", "estimateScaleFactor": "/usr/local/bin/estimateScaleFactor", "multiBamSummary": "/usr/local/bin/multiBamSummary", "multiBigwigSummary": "/usr/local/bin/multiBigwigSummary", "plotCorrelation": "/usr/local/bin/plotCorrelation", "plotCoverage": "/usr/local/bin/plotCoverage", "plotEnrichment": "/usr/local/bin/plotEnrichment", "plotFingerprint": "/usr/local/bin/plotFingerprint", "plotHeatmap": "/usr/local/bin/plotHeatmap", "plotPCA": "/usr/local/bin/plotPCA", "plotProfile": "/usr/local/bin/plotProfile", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeptools.
shpc-registry automated BioContainers addition for deeptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeptools:3.5.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeptools/3.5.5--pyhdfd78af_0
$ module help quay.io/biocontainers/deeptools/3.5.5--pyhdfd78af_0
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


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
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