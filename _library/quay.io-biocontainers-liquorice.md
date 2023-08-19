---
layout: container
name:  "quay.io/biocontainers/liquorice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/liquorice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/liquorice/container.yaml"
updated_at: "2023-08-19 02:46:52.158695"
latest: "0.5.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/liquorice"
aliases:
 - "LIQUORICE"
 - "LIQUORICE_summary"
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
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "multiBamSummary"
 - "multiBigwigSummary"
 - "plotCorrelation"
 - "plotCoverage"
 - "plotEnrichment"
 - "plotFingerprint"
 - "plotHeatmap"
 - "plotPCA"
 - "plotProfile"
 - "send2trash"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-notebook"
 - "jupyter-serverextension"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "jupyter-nbconvert"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
versions:
 - "0.5.5--pyhdfd78af_1"
 - "0.5.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for liquorice"
config: {"url": "https://biocontainers.pro/tools/liquorice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for liquorice", "latest": {"0.5.6--pyhdfd78af_0": "sha256:e1ae2cb7dd019402565f8e24a34e022c49db5817fc5be147289d0a75ad94ebf4"}, "tags": {"0.5.5--pyhdfd78af_1": "sha256:4e2a6292eb7c95b57e2cf4842956e91128067f943d29e93cd7c778153c5f636e", "0.5.6--pyhdfd78af_0": "sha256:e1ae2cb7dd019402565f8e24a34e022c49db5817fc5be147289d0a75ad94ebf4"}, "docker": "quay.io/biocontainers/liquorice", "aliases": {"LIQUORICE": "/usr/local/bin/LIQUORICE", "LIQUORICE_summary": "/usr/local/bin/LIQUORICE_summary", "alignmentSieve": "/usr/local/bin/alignmentSieve", "bamCompare": "/usr/local/bin/bamCompare", "bamCoverage": "/usr/local/bin/bamCoverage", "bamPEFragmentSize": "/usr/local/bin/bamPEFragmentSize", "bigwigCompare": "/usr/local/bin/bigwigCompare", "computeGCBias": "/usr/local/bin/computeGCBias", "computeMatrix": "/usr/local/bin/computeMatrix", "computeMatrixOperations": "/usr/local/bin/computeMatrixOperations", "correctGCBias": "/usr/local/bin/correctGCBias", "deeptools": "/usr/local/bin/deeptools", "estimateReadFiltering": "/usr/local/bin/estimateReadFiltering", "estimateScaleFactor": "/usr/local/bin/estimateScaleFactor", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "multiBamSummary": "/usr/local/bin/multiBamSummary", "multiBigwigSummary": "/usr/local/bin/multiBigwigSummary", "plotCorrelation": "/usr/local/bin/plotCorrelation", "plotCoverage": "/usr/local/bin/plotCoverage", "plotEnrichment": "/usr/local/bin/plotEnrichment", "plotFingerprint": "/usr/local/bin/plotFingerprint", "plotHeatmap": "/usr/local/bin/plotHeatmap", "plotPCA": "/usr/local/bin/plotPCA", "plotProfile": "/usr/local/bin/plotProfile", "send2trash": "/usr/local/bin/send2trash", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/liquorice.
shpc-registry automated BioContainers addition for liquorice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/liquorice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/liquorice:0.5.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/liquorice/0.5.6--pyhdfd78af_0
$ module help quay.io/biocontainers/liquorice/0.5.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### liquorice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### liquorice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### liquorice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### liquorice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### liquorice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### liquorice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LIQUORICE

```bash
$ singularity exec <container> /usr/local/bin/LIQUORICE
$ podman run --it --rm --entrypoint /usr/local/bin/LIQUORICE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LIQUORICE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LIQUORICE_summary

```bash
$ singularity exec <container> /usr/local/bin/LIQUORICE_summary
$ podman run --it --rm --entrypoint /usr/local/bin/LIQUORICE_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LIQUORICE_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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