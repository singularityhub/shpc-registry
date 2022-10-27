---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetsearch/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetsearch/container.yaml"
updated_at: "2022-10-27 00:33:10.976695"
latest: "1.50.1--r41hc0cfd56_1"
container_url: "https://biocontainers.pro/tools/bioconductor-targetsearch"

versions:
 - "1.50.1--r41hc0cfd56_1"
description: "shpc-registry automated BioContainers addition for bioconductor-targetsearch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetsearch", "latest": {"1.50.1--r41hc0cfd56_1": "sha256:030f627cdc84a6349e1a7cc56810f259f559c52858aca99aee1cfdfa766f0d00"}, "tags": {"1.50.1--r41hc0cfd56_1": "sha256:030f627cdc84a6349e1a7cc56810f259f559c52858aca99aee1cfdfa766f0d00"}, "docker": "quay.io/biocontainers/bioconductor-targetsearch"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetsearch.
shpc-registry automated BioContainers addition for bioconductor-targetsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearch:1.50.1--r41hc0cfd56_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetsearch/1.50.1--r41hc0cfd56_1
$ module help quay.io/biocontainers/bioconductor-targetsearch/1.50.1--r41hc0cfd56_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-targetsearch

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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