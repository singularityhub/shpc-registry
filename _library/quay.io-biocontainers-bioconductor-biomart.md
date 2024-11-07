---
layout: container
name:  "quay.io/biocontainers/bioconductor-biomart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biomart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biomart/container.yaml"
updated_at: "2024-11-07 02:55:30.886207"
latest: "2.58.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biomart"

versions:
 - "2.50.0--r41hdfd78af_0"
 - "2.54.0--r42hdfd78af_0"
 - "2.56.1--r43hdfd78af_0"
 - "2.58.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biomart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biomart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biomart", "latest": {"2.58.0--r43hdfd78af_0": "sha256:85051bafc019136042f39e62d224af3649576b8f3fb160565b7bccf76b4c6460"}, "tags": {"2.50.0--r41hdfd78af_0": "sha256:d8902dcd51bb7a7c86f7690660002569016dde35c8ec777185c00aa8f1a50e93", "2.54.0--r42hdfd78af_0": "sha256:7e7f694afbfb2c926d2482e8c4d3c6a5cc3b1e39db36d1c4376a51e4bd538168", "2.56.1--r43hdfd78af_0": "sha256:425c0f1f2935ae99d62516483f1324245d7e2acf0fab94e3ead9f190c88e5857", "2.58.0--r43hdfd78af_0": "sha256:85051bafc019136042f39e62d224af3649576b8f3fb160565b7bccf76b4c6460"}, "docker": "quay.io/biocontainers/bioconductor-biomart"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biomart.
shpc-registry automated BioContainers addition for bioconductor-biomart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biomart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biomart:2.58.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biomart/2.58.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biomart/2.58.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biomart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biomart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biomart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biomart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biomart

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