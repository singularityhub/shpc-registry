---
layout: container
name:  "quay.io/biocontainers/bioconductor-caomicsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-caomicsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-caomicsv/container.yaml"
updated_at: "2023-06-18 03:23:15.386322"
latest: "1.24.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-caomicsv"

versions:
 - "1.24.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-caomicsv"
config: {"url": "https://biocontainers.pro/tools/bioconductor-caomicsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-caomicsv", "latest": {"1.24.0--r41hdfd78af_0": "sha256:d6a5222f4544081158325122aaf2c0cf37ac64361bd39cbffed14d1b8509ec07"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:d6a5222f4544081158325122aaf2c0cf37ac64361bd39cbffed14d1b8509ec07"}, "docker": "quay.io/biocontainers/bioconductor-caomicsv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-caomicsv.
shpc-registry automated BioContainers addition for bioconductor-caomicsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-caomicsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-caomicsv:1.24.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-caomicsv/1.24.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-caomicsv/1.24.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-caomicsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caomicsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caomicsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-caomicsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-caomicsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-caomicsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-caomicsv

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