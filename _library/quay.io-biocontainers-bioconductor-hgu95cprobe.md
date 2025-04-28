---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95cprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95cprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95cprobe/container.yaml"
updated_at: "2025-04-28 04:08:30.419999"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95cprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95cprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95cprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95cprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:826557791dd82f22861a28db1246045f4eb7c17e27b677341930e8dd6c4e9b59"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f0d6bb34497eb02eac722bda4742dd7228365d2f6e78bd4b0001a9abb98a7cab", "2.18.0--r42hdfd78af_10": "sha256:ea3c99250e28056f5df4c994ef1dafe560e87fad7031b5695043654b0e94026e", "2.18.0--r43hdfd78af_11": "sha256:6a8e736f7566a4ea8ba7c9cdbe8cd31ad63838fb753a1aaefbd93545406ba626", "2.18.0--r43hdfd78af_12": "sha256:8585b3b0ebe702af2c7cbff1f23aa6bbe63bd64953c06b354cd64a063c1ca2e4", "2.18.0--r44hdfd78af_13": "sha256:826557791dd82f22861a28db1246045f4eb7c17e27b677341930e8dd6c4e9b59"}, "docker": "quay.io/biocontainers/bioconductor-hgu95cprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95cprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu95cprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95cprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95cprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95cprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu95cprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95cprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95cprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95cprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95cprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95cprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95cprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95cprobe

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