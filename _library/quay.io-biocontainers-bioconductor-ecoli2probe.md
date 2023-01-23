---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecoli2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecoli2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecoli2probe/container.yaml"
updated_at: "2023-01-23 03:29:16.311999"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-ecoli2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-ecoli2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecoli2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecoli2probe", "latest": {"2.18.0--r42hdfd78af_10": "sha256:12282cc533eec25f10648ff2f9edadd1ed1907f0ef3c4de19b0e8e2122cf8cef"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:74f07839fe9b101b3a51e5f363d7eed41f818ae2a60a24437ae66808c5c80c5b", "2.18.0--r42hdfd78af_10": "sha256:12282cc533eec25f10648ff2f9edadd1ed1907f0ef3c4de19b0e8e2122cf8cef"}, "docker": "quay.io/biocontainers/bioconductor-ecoli2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecoli2probe.
shpc-registry automated BioContainers addition for bioconductor-ecoli2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoli2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoli2probe:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecoli2probe/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-ecoli2probe/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecoli2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoli2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoli2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecoli2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecoli2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecoli2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ecoli2probe

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