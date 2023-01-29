---
layout: container
name:  "quay.io/biocontainers/stereogene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stereogene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stereogene/container.yaml"
updated_at: "2023-01-29 02:50:54.762023"
latest: "2.20--h87f3376_4"
container_url: "https://biocontainers.pro/tools/stereogene"
aliases:
 - "Binner"
 - "Confounder"
 - "ParseGenes"
 - "Projector"
 - "Smoother"
 - "StereoGene"
versions:
 - "2.20--h87f3376_4"
description: "shpc-registry automated BioContainers addition for stereogene"
config: {"url": "https://biocontainers.pro/tools/stereogene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stereogene", "latest": {"2.20--h87f3376_4": "sha256:e53a555a358aa82cbe3631c4c49d25d468fe02c33950342b4f48dca1edd3f773"}, "tags": {"2.20--h87f3376_4": "sha256:e53a555a358aa82cbe3631c4c49d25d468fe02c33950342b4f48dca1edd3f773"}, "docker": "quay.io/biocontainers/stereogene", "aliases": {"Binner": "/usr/local/bin/Binner", "Confounder": "/usr/local/bin/Confounder", "ParseGenes": "/usr/local/bin/ParseGenes", "Projector": "/usr/local/bin/Projector", "Smoother": "/usr/local/bin/Smoother", "StereoGene": "/usr/local/bin/StereoGene"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stereogene.
shpc-registry automated BioContainers addition for stereogene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stereogene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stereogene:2.20--h87f3376_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stereogene/2.20--h87f3376_4
$ module help quay.io/biocontainers/stereogene/2.20--h87f3376_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stereogene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stereogene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stereogene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stereogene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stereogene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stereogene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Binner

```bash
$ singularity exec <container> /usr/local/bin/Binner
$ podman run --it --rm --entrypoint /usr/local/bin/Binner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Confounder

```bash
$ singularity exec <container> /usr/local/bin/Confounder
$ podman run --it --rm --entrypoint /usr/local/bin/Confounder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Confounder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseGenes

```bash
$ singularity exec <container> /usr/local/bin/ParseGenes
$ podman run --it --rm --entrypoint /usr/local/bin/ParseGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Projector

```bash
$ singularity exec <container> /usr/local/bin/Projector
$ podman run --it --rm --entrypoint /usr/local/bin/Projector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Projector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Smoother

```bash
$ singularity exec <container> /usr/local/bin/Smoother
$ podman run --it --rm --entrypoint /usr/local/bin/Smoother   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Smoother   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StereoGene

```bash
$ singularity exec <container> /usr/local/bin/StereoGene
$ podman run --it --rm --entrypoint /usr/local/bin/StereoGene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StereoGene   -v ${PWD} -w ${PWD} <container> -c " $@"
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