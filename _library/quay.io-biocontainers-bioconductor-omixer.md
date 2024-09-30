---
layout: container
name:  "quay.io/biocontainers/bioconductor-omixer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omixer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omixer/container.yaml"
updated_at: "2024-09-30 03:32:09.265983"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omixer"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omixer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omixer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omixer", "latest": {"1.12.0--r43hdfd78af_0": "sha256:30bbad5f65f590f879e542fb933df39aceddeda9d2cc8cd45ba349f53bda4924"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:89ad416faea6b8590fa8e7a92876de338446e7dd34b363a51791fae91f3902ed", "1.8.0--r42hdfd78af_0": "sha256:341496cc60358a6fef04081663b01e5fcb8ffff51daca196efa48c0ac096dd08", "1.10.0--r43hdfd78af_0": "sha256:45e941c476155979908572f820e3579af26cb5ab22f3dea71a0ec4ad297f4663", "1.12.0--r43hdfd78af_0": "sha256:30bbad5f65f590f879e542fb933df39aceddeda9d2cc8cd45ba349f53bda4924"}, "docker": "quay.io/biocontainers/bioconductor-omixer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omixer.
shpc-registry automated BioContainers addition for bioconductor-omixer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omixer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omixer:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omixer/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omixer/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omixer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omixer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omixer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omixer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omixer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omixer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-omixer

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