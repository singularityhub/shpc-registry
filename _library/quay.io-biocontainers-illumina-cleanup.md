---
layout: container
name:  "quay.io/biocontainers/illumina-cleanup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/illumina-cleanup/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/illumina-cleanup/container.yaml"
updated_at: "2022-10-29 05:55:19.562144"
latest: "1.0.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/illumina-cleanup"
aliases:
 - "Xcalcmem.sh"
 - "fastq-scan"
 - "illumina-cleanup"
 - "jq"
 - "lighter"
 - "nextflow.bak"
 - "onig-config"
 - "a_sample_mt.sh"
 - "ace2sam"
 - "addadapters.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "alltoall.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
 - "analyzesketchresults.sh"
 - "applyvariants.sh"
versions:
 - "1.0.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for illumina-cleanup"
config: {"url": "https://biocontainers.pro/tools/illumina-cleanup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for illumina-cleanup", "latest": {"1.0.0--hdfd78af_2": "sha256:55f1683d2fbbd3dd946897e2f301f16670ccb5f2d611882dcfcdbce4b9e3db3c"}, "tags": {"1.0.0--hdfd78af_2": "sha256:55f1683d2fbbd3dd946897e2f301f16670ccb5f2d611882dcfcdbce4b9e3db3c"}, "docker": "quay.io/biocontainers/illumina-cleanup", "aliases": {"Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "fastq-scan": "/usr/local/bin/fastq-scan", "illumina-cleanup": "/usr/local/bin/illumina-cleanup", "jq": "/usr/local/bin/jq", "lighter": "/usr/local/bin/lighter", "nextflow.bak": "/usr/local/bin/nextflow.bak", "onig-config": "/usr/local/bin/onig-config", "a_sample_mt.sh": "/usr/local/bin/a_sample_mt.sh", "ace2sam": "/usr/local/bin/ace2sam", "addadapters.sh": "/usr/local/bin/addadapters.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/illumina-cleanup.
shpc-registry automated BioContainers addition for illumina-cleanup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/illumina-cleanup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/illumina-cleanup:1.0.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/illumina-cleanup/1.0.0--hdfd78af_2
$ module help quay.io/biocontainers/illumina-cleanup/1.0.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### illumina-cleanup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### illumina-cleanup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### illumina-cleanup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### illumina-cleanup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### illumina-cleanup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### illumina-cleanup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-scan

```bash
$ singularity exec <container> /usr/local/bin/fastq-scan
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illumina-cleanup

```bash
$ singularity exec <container> /usr/local/bin/illumina-cleanup
$ podman run --it --rm --entrypoint /usr/local/bin/illumina-cleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illumina-cleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lighter

```bash
$ singularity exec <container> /usr/local/bin/lighter
$ podman run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a_sample_mt.sh

```bash
$ singularity exec <container> /usr/local/bin/a_sample_mt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addadapters.sh

```bash
$ singularity exec <container> /usr/local/bin/addadapters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applyvariants.sh

```bash
$ singularity exec <container> /usr/local/bin/applyvariants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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