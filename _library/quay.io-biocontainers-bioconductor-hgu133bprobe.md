---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133bprobe/container.yaml"
updated_at: "2024-06-27 02:59:06.186919"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133bprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:16035533b63a3279c1cc3c4e58cbb5d2b00006fa1076fbdbcc6d72d1b846ddae"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:99c2681516ac9b89f735c2c0141fe76d0dbafd81652e46a5c3819f303977bc64", "2.18.0--r42hdfd78af_10": "sha256:ca6cd99e09efbc122484ce1ec50b34447e2cea41c50a53495277c0c24a861a5e", "2.18.0--r43hdfd78af_11": "sha256:1139f6bdde0f643b2188a08a6d76b4efa174b4e51397ba8dfd68a04e24382635", "2.18.0--r43hdfd78af_12": "sha256:16035533b63a3279c1cc3c4e58cbb5d2b00006fa1076fbdbcc6d72d1b846ddae"}, "docker": "quay.io/biocontainers/bioconductor-hgu133bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133bprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu133bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133bprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133bprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133bprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133bprobe

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