---
layout: container
name:  "quay.io/biocontainers/comparative-annotation-toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/comparative-annotation-toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/comparative-annotation-toolkit/container.yaml"
updated_at: "2022-10-27 00:32:13.260666"
latest: "0.1--py_2"
container_url: "https://biocontainers.pro/tools/comparative-annotation-toolkit"
aliases:
 - "_toil_mesos_executor"
 - "_toil_worker"
 - "autoRun.pathInfo"
 - "axtChain"
 - "bamToPsl"
 - "bamtools-2.4.1"
 - "bedSort"
 - "chainMergeSort"
 - "clusterGenes"
 - "cwltest"
 - "cwltoil"
 - "espoca"
 - "filterGenesIn_mRNAname.pl.patch"
 - "genePredToBed"
 - "genePredToFakePsl"
 - "genePredToGtf"
 - "gff3ToGenePred"
 - "gtf2gff.pl.origexit"
 - "gtfToGenePred"
 - "intron2exex.pl"
 - "luigi"
 - "luigi-deps"
 - "luigi-deps-tree"
 - "luigi-grep"
 - "luigid"
 - "mock-cwl-runner"
 - "pslCDnaFilter"
 - "pslCheck"
 - "pslMap"
 - "pslMapPostChain"
 - "pslPosTarget"
 - "pslRecalcMatch"
 - "pslToBigPsl"
 - "pyfasta"
 - "ratewig.pl"
 - "toil"
 - "toil-cwl-runner"
 - "toil-wdl-runner"
 - "transMapPslToGenePred"
 - "webserver-results.body"
versions:
 - "0.1--py_2"
description: "shpc-registry automated BioContainers addition for comparative-annotation-toolkit"
config: {"url": "https://biocontainers.pro/tools/comparative-annotation-toolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for comparative-annotation-toolkit", "latest": {"0.1--py_2": "sha256:eced8ca5b7bb2dd4ad4bb0d2e1a089944f6b6c95ca6126ba1067a93f8075eb63"}, "tags": {"0.1--py_2": "sha256:eced8ca5b7bb2dd4ad4bb0d2e1a089944f6b6c95ca6126ba1067a93f8075eb63"}, "docker": "quay.io/biocontainers/comparative-annotation-toolkit", "aliases": {"_toil_mesos_executor": "/usr/local/bin/_toil_mesos_executor", "_toil_worker": "/usr/local/bin/_toil_worker", "autoRun.pathInfo": "/usr/local/bin/autoRun.pathInfo", "axtChain": "/usr/local/bin/axtChain", "bamToPsl": "/usr/local/bin/bamToPsl", "bamtools-2.4.1": "/usr/local/bin/bamtools-2.4.1", "bedSort": "/usr/local/bin/bedSort", "chainMergeSort": "/usr/local/bin/chainMergeSort", "clusterGenes": "/usr/local/bin/clusterGenes", "cwltest": "/usr/local/bin/cwltest", "cwltoil": "/usr/local/bin/cwltoil", "espoca": "/usr/local/bin/espoca", "filterGenesIn_mRNAname.pl.patch": "/usr/local/bin/filterGenesIn_mRNAname.pl.patch", "genePredToBed": "/usr/local/bin/genePredToBed", "genePredToFakePsl": "/usr/local/bin/genePredToFakePsl", "genePredToGtf": "/usr/local/bin/genePredToGtf", "gff3ToGenePred": "/usr/local/bin/gff3ToGenePred", "gtf2gff.pl.origexit": "/usr/local/bin/gtf2gff.pl.origexit", "gtfToGenePred": "/usr/local/bin/gtfToGenePred", "intron2exex.pl": "/usr/local/bin/intron2exex.pl", "luigi": "/usr/local/bin/luigi", "luigi-deps": "/usr/local/bin/luigi-deps", "luigi-deps-tree": "/usr/local/bin/luigi-deps-tree", "luigi-grep": "/usr/local/bin/luigi-grep", "luigid": "/usr/local/bin/luigid", "mock-cwl-runner": "/usr/local/bin/mock-cwl-runner", "pslCDnaFilter": "/usr/local/bin/pslCDnaFilter", "pslCheck": "/usr/local/bin/pslCheck", "pslMap": "/usr/local/bin/pslMap", "pslMapPostChain": "/usr/local/bin/pslMapPostChain", "pslPosTarget": "/usr/local/bin/pslPosTarget", "pslRecalcMatch": "/usr/local/bin/pslRecalcMatch", "pslToBigPsl": "/usr/local/bin/pslToBigPsl", "pyfasta": "/usr/local/bin/pyfasta", "ratewig.pl": "/usr/local/bin/ratewig.pl", "toil": "/usr/local/bin/toil", "toil-cwl-runner": "/usr/local/bin/toil-cwl-runner", "toil-wdl-runner": "/usr/local/bin/toil-wdl-runner", "transMapPslToGenePred": "/usr/local/bin/transMapPslToGenePred", "webserver-results.body": "/usr/local/bin/webserver-results.body"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/comparative-annotation-toolkit.
shpc-registry automated BioContainers addition for comparative-annotation-toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/comparative-annotation-toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/comparative-annotation-toolkit:0.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/comparative-annotation-toolkit/0.1--py_2
$ module help quay.io/biocontainers/comparative-annotation-toolkit/0.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### comparative-annotation-toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### comparative-annotation-toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### comparative-annotation-toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### comparative-annotation-toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### comparative-annotation-toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### comparative-annotation-toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _toil_mesos_executor

```bash
$ singularity exec <container> /usr/local/bin/_toil_mesos_executor
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _toil_worker

```bash
$ singularity exec <container> /usr/local/bin/_toil_worker
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoRun.pathInfo

```bash
$ singularity exec <container> /usr/local/bin/autoRun.pathInfo
$ podman run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axtChain

```bash
$ singularity exec <container> /usr/local/bin/axtChain
$ podman run --it --rm --entrypoint /usr/local/bin/axtChain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axtChain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToPsl

```bash
$ singularity exec <container> /usr/local/bin/bamToPsl
$ podman run --it --rm --entrypoint /usr/local/bin/bamToPsl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToPsl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.1

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedSort

```bash
$ singularity exec <container> /usr/local/bin/bedSort
$ podman run --it --rm --entrypoint /usr/local/bin/bedSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chainMergeSort

```bash
$ singularity exec <container> /usr/local/bin/chainMergeSort
$ podman run --it --rm --entrypoint /usr/local/bin/chainMergeSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chainMergeSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterGenes

```bash
$ singularity exec <container> /usr/local/bin/clusterGenes
$ podman run --it --rm --entrypoint /usr/local/bin/clusterGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltest

```bash
$ singularity exec <container> /usr/local/bin/cwltest
$ podman run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltoil

```bash
$ singularity exec <container> /usr/local/bin/cwltoil
$ podman run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### espoca

```bash
$ singularity exec <container> /usr/local/bin/espoca
$ podman run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterGenesIn_mRNAname.pl.patch

```bash
$ singularity exec <container> /usr/local/bin/filterGenesIn_mRNAname.pl.patch
$ podman run --it --rm --entrypoint /usr/local/bin/filterGenesIn_mRNAname.pl.patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterGenesIn_mRNAname.pl.patch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToBed

```bash
$ singularity exec <container> /usr/local/bin/genePredToBed
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToFakePsl

```bash
$ singularity exec <container> /usr/local/bin/genePredToFakePsl
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToFakePsl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToFakePsl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToGtf

```bash
$ singularity exec <container> /usr/local/bin/genePredToGtf
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3ToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gff3ToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2gff.pl.origexit

```bash
$ singularity exec <container> /usr/local/bin/gtf2gff.pl.origexit
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2gff.pl.origexit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2gff.pl.origexit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtfToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gtfToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron2exex.pl

```bash
$ singularity exec <container> /usr/local/bin/intron2exex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi

```bash
$ singularity exec <container> /usr/local/bin/luigi
$ podman run --it --rm --entrypoint /usr/local/bin/luigi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-deps

```bash
$ singularity exec <container> /usr/local/bin/luigi-deps
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-deps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-deps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-deps-tree

```bash
$ singularity exec <container> /usr/local/bin/luigi-deps-tree
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-deps-tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-deps-tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-grep

```bash
$ singularity exec <container> /usr/local/bin/luigi-grep
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigid

```bash
$ singularity exec <container> /usr/local/bin/luigid
$ podman run --it --rm --entrypoint /usr/local/bin/luigid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mock-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/mock-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/mock-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mock-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslCDnaFilter

```bash
$ singularity exec <container> /usr/local/bin/pslCDnaFilter
$ podman run --it --rm --entrypoint /usr/local/bin/pslCDnaFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslCDnaFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslCheck

```bash
$ singularity exec <container> /usr/local/bin/pslCheck
$ podman run --it --rm --entrypoint /usr/local/bin/pslCheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslCheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslMap

```bash
$ singularity exec <container> /usr/local/bin/pslMap
$ podman run --it --rm --entrypoint /usr/local/bin/pslMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslMapPostChain

```bash
$ singularity exec <container> /usr/local/bin/pslMapPostChain
$ podman run --it --rm --entrypoint /usr/local/bin/pslMapPostChain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslMapPostChain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPosTarget

```bash
$ singularity exec <container> /usr/local/bin/pslPosTarget
$ podman run --it --rm --entrypoint /usr/local/bin/pslPosTarget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPosTarget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslRecalcMatch

```bash
$ singularity exec <container> /usr/local/bin/pslRecalcMatch
$ podman run --it --rm --entrypoint /usr/local/bin/pslRecalcMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslRecalcMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslToBigPsl

```bash
$ singularity exec <container> /usr/local/bin/pslToBigPsl
$ podman run --it --rm --entrypoint /usr/local/bin/pslToBigPsl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslToBigPsl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfasta

```bash
$ singularity exec <container> /usr/local/bin/pyfasta
$ podman run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ratewig.pl

```bash
$ singularity exec <container> /usr/local/bin/ratewig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil

```bash
$ singularity exec <container> /usr/local/bin/toil
$ podman run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/toil-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil-wdl-runner

```bash
$ singularity exec <container> /usr/local/bin/toil-wdl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/toil-wdl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil-wdl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transMapPslToGenePred

```bash
$ singularity exec <container> /usr/local/bin/transMapPslToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/transMapPslToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transMapPslToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webserver-results.body

```bash
$ singularity exec <container> /usr/local/bin/webserver-results.body
$ podman run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
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