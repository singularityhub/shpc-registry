---
layout: container
name:  "quay.io/biocontainers/biopet-scatterregions"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biopet-scatterregions/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biopet-scatterregions/container.yaml"
updated_at: "2022-10-27 00:57:34.571318"
latest: "0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/biopet-scatterregions"
aliases:
 - "biopet-scatterregions"
versions:
 - "0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for biopet-scatterregions"
config: {"url": "https://biocontainers.pro/tools/biopet-scatterregions", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biopet-scatterregions", "latest": {"0.2--hdfd78af_1": "sha256:a4b50f0a876464cdff85ab25e621c54b05145bd87323450fd9b9d9a7dbdcfa18"}, "tags": {"0.2--hdfd78af_1": "sha256:a4b50f0a876464cdff85ab25e621c54b05145bd87323450fd9b9d9a7dbdcfa18"}, "docker": "quay.io/biocontainers/biopet-scatterregions", "aliases": {"biopet-scatterregions": "/usr/local/bin/biopet-scatterregions"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biopet-scatterregions.
shpc-registry automated BioContainers addition for biopet-scatterregions
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biopet-scatterregions
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biopet-scatterregions:0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biopet-scatterregions/0.2--hdfd78af_1
$ module help quay.io/biocontainers/biopet-scatterregions/0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biopet-scatterregions-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biopet-scatterregions-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biopet-scatterregions-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biopet-scatterregions-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biopet-scatterregions-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biopet-scatterregions-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biopet-scatterregions

```bash
$ singularity exec <container> /usr/local/bin/biopet-scatterregions
$ podman run --it --rm --entrypoint /usr/local/bin/biopet-scatterregions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biopet-scatterregions   -v ${PWD} -w ${PWD} <container> -c " $@"
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