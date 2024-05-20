---
layout: container
name:  "quay.io/biocontainers/biobasehttptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobasehttptools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobasehttptools/container.yaml"
updated_at: "2024-05-20 02:47:39.772766"
latest: "1.1.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/biobasehttptools"
aliases:
 - "AccessionToTaxId"
 - "AccessionToTaxId-bin"
 - "FetchSequence"
 - "FetchSequence-bin"
 - "GeneIdToGOTerms"
 - "GeneIdToGOTerms-bin"
 - "GeneIdToUniProtId"
 - "GeneIdToUniProtId-bin"
versions:
 - "1.1.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for biobasehttptools"
config: {"url": "https://biocontainers.pro/tools/biobasehttptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobasehttptools", "latest": {"1.1.0--hdfd78af_1": "sha256:b0004e4ac380706db293dfe396fe9faedf5e5cb3816b79ba5380655372715c07"}, "tags": {"1.1.0--hdfd78af_1": "sha256:b0004e4ac380706db293dfe396fe9faedf5e5cb3816b79ba5380655372715c07"}, "docker": "quay.io/biocontainers/biobasehttptools", "aliases": {"AccessionToTaxId": "/usr/local/bin/AccessionToTaxId", "AccessionToTaxId-bin": "/usr/local/bin/AccessionToTaxId-bin", "FetchSequence": "/usr/local/bin/FetchSequence", "FetchSequence-bin": "/usr/local/bin/FetchSequence-bin", "GeneIdToGOTerms": "/usr/local/bin/GeneIdToGOTerms", "GeneIdToGOTerms-bin": "/usr/local/bin/GeneIdToGOTerms-bin", "GeneIdToUniProtId": "/usr/local/bin/GeneIdToUniProtId", "GeneIdToUniProtId-bin": "/usr/local/bin/GeneIdToUniProtId-bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobasehttptools.
shpc-registry automated BioContainers addition for biobasehttptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobasehttptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobasehttptools:1.1.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobasehttptools/1.1.0--hdfd78af_1
$ module help quay.io/biocontainers/biobasehttptools/1.1.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobasehttptools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobasehttptools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobasehttptools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobasehttptools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobasehttptools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobasehttptools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AccessionToTaxId

```bash
$ singularity exec <container> /usr/local/bin/AccessionToTaxId
$ podman run --it --rm --entrypoint /usr/local/bin/AccessionToTaxId   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AccessionToTaxId   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AccessionToTaxId-bin

```bash
$ singularity exec <container> /usr/local/bin/AccessionToTaxId-bin
$ podman run --it --rm --entrypoint /usr/local/bin/AccessionToTaxId-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AccessionToTaxId-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FetchSequence

```bash
$ singularity exec <container> /usr/local/bin/FetchSequence
$ podman run --it --rm --entrypoint /usr/local/bin/FetchSequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FetchSequence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FetchSequence-bin

```bash
$ singularity exec <container> /usr/local/bin/FetchSequence-bin
$ podman run --it --rm --entrypoint /usr/local/bin/FetchSequence-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FetchSequence-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeneIdToGOTerms

```bash
$ singularity exec <container> /usr/local/bin/GeneIdToGOTerms
$ podman run --it --rm --entrypoint /usr/local/bin/GeneIdToGOTerms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneIdToGOTerms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeneIdToGOTerms-bin

```bash
$ singularity exec <container> /usr/local/bin/GeneIdToGOTerms-bin
$ podman run --it --rm --entrypoint /usr/local/bin/GeneIdToGOTerms-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneIdToGOTerms-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeneIdToUniProtId

```bash
$ singularity exec <container> /usr/local/bin/GeneIdToUniProtId
$ podman run --it --rm --entrypoint /usr/local/bin/GeneIdToUniProtId   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneIdToUniProtId   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeneIdToUniProtId-bin

```bash
$ singularity exec <container> /usr/local/bin/GeneIdToUniProtId-bin
$ podman run --it --rm --entrypoint /usr/local/bin/GeneIdToUniProtId-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneIdToUniProtId-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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