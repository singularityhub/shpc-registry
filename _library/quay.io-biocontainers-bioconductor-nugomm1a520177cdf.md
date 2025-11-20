---
layout: container
name:  "quay.io/biocontainers/bioconductor-nugomm1a520177cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nugomm1a520177cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nugomm1a520177cdf/container.yaml"
updated_at: "2025-11-20 03:16:24.179980"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-nugomm1a520177cdf"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nugomm1a520177cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177cdf", "latest": {"3.4.0--r44hdfd78af_13": "sha256:5c51aba5c675396022f6f1aa7e854a5bfe7c5b289eb4fc097b993b65db9e3f81"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:ee772d0df926e85c344b836a691013e4ad312441a5d02a700f704d720260a868", "3.4.0--r42hdfd78af_10": "sha256:d5a69e3c1cc26dacc2fe8cc4f5d3d4601d663199f6979aac67d403b3cf02b5f7", "3.4.0--r43hdfd78af_11": "sha256:7bd99d8a5dab2911b3983596c8a7cce9b3507c79ec5d825bd6068730b1827b9c", "3.4.0--r43hdfd78af_12": "sha256:74c5ea98d1f6acec1e4e691786a32aed2c21ac7cadec0df9a3b467ee173e6d29", "3.4.0--r44hdfd78af_13": "sha256:5c51aba5c675396022f6f1aa7e854a5bfe7c5b289eb4fc097b993b65db9e3f81"}, "docker": "quay.io/biocontainers/bioconductor-nugomm1a520177cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nugomm1a520177cdf.
shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177cdf:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nugomm1a520177cdf/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-nugomm1a520177cdf/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nugomm1a520177cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nugomm1a520177cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nugomm1a520177cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nugomm1a520177cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nugomm1a520177cdf

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