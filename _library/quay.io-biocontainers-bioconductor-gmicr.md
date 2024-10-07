---
layout: container
name:  "quay.io/biocontainers/bioconductor-gmicr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gmicr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gmicr/container.yaml"
updated_at: "2024-10-07 03:21:02.375512"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gmicr"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gmicr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gmicr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gmicr", "latest": {"1.16.0--r43hdfd78af_0": "sha256:bf44aa7837fdb88d617985fa605408788f68f1f1c04e2f8a0c7706fad68ff1da"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:653aa524e1fdb1c3ae180d88b756b1c0ed846a73451c12215ae9c3d69cbbcdfa", "1.12.0--r42hdfd78af_0": "sha256:c013068d4fd6b63019797ad0ff95d45bab52d37efc49c125d68e3bcf4b98ac25", "1.14.0--r43hdfd78af_0": "sha256:5c88afc545d69b8d6327bd5824399536916fe01d4574b02d493647788c7cfd47", "1.16.0--r43hdfd78af_0": "sha256:bf44aa7837fdb88d617985fa605408788f68f1f1c04e2f8a0c7706fad68ff1da"}, "docker": "quay.io/biocontainers/bioconductor-gmicr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gmicr.
shpc-registry automated BioContainers addition for bioconductor-gmicr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gmicr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gmicr:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gmicr/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gmicr/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gmicr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmicr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmicr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gmicr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gmicr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gmicr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gmicr

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