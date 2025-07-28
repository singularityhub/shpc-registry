---
layout: container
name:  "quay.io/biocontainers/bioconductor-healthyflowdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-healthyflowdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-healthyflowdata/container.yaml"
updated_at: "2025-07-28 09:30:04.673049"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-healthyflowdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-healthyflowdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-healthyflowdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-healthyflowdata", "latest": {"1.44.0--r44hdfd78af_0": "sha256:1b4cc6ff0850cfc66e9248a4273010809f57c669b444d430c0d060cb48646273"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:7e4ecea8b9d6f3fdc698405a9f6913cc243019b3040f8daa335ee9611c8e2e37", "1.36.0--r42hdfd78af_0": "sha256:72f357b2182968a6b2a98875c5beefeb05a854dab0c9a22fcf585650cbf2c7ea", "1.38.0--r43hdfd78af_0": "sha256:540f66561e75448bafd9cf07bc31d1dcded9fb70849723a80e8545d1cc1863ab", "1.40.0--r43hdfd78af_0": "sha256:8f4321cc33488161f34ee5ae6181bc479ca6e7b4c872fd466058c40c7c55de46", "1.44.0--r44hdfd78af_0": "sha256:1b4cc6ff0850cfc66e9248a4273010809f57c669b444d430c0d060cb48646273"}, "docker": "quay.io/biocontainers/bioconductor-healthyflowdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-healthyflowdata.
shpc-registry automated BioContainers addition for bioconductor-healthyflowdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-healthyflowdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-healthyflowdata:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-healthyflowdata/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-healthyflowdata/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-healthyflowdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-healthyflowdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-healthyflowdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-healthyflowdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-healthyflowdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-healthyflowdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-healthyflowdata

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