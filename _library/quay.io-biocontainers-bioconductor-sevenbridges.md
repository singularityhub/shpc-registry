---
layout: container
name:  "quay.io/biocontainers/bioconductor-sevenbridges"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sevenbridges/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sevenbridges/container.yaml"
updated_at: "2023-04-26 03:23:25.430644"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sevenbridges"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sevenbridges"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sevenbridges", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sevenbridges", "latest": {"1.28.0--r42hdfd78af_0": "sha256:93b0a23e94444abed9ed620db62b29aa67921d192cb802c6ac062abb0c0dc3b9"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:b73cb5e2300bb999ffccc42bac1b1d3c854ad52100e5ed3ca112500a7153046f", "1.28.0--r42hdfd78af_0": "sha256:93b0a23e94444abed9ed620db62b29aa67921d192cb802c6ac062abb0c0dc3b9"}, "docker": "quay.io/biocontainers/bioconductor-sevenbridges"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sevenbridges.
shpc-registry automated BioContainers addition for bioconductor-sevenbridges
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sevenbridges
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sevenbridges:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sevenbridges/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sevenbridges/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sevenbridges-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sevenbridges-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sevenbridges-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sevenbridges-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sevenbridges-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sevenbridges-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sevenbridges

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