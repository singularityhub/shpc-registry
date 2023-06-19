---
layout: container
name:  "quay.io/biocontainers/bioconductor-rae230acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rae230acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rae230acdf/container.yaml"
updated_at: "2023-06-19 03:19:03.670702"
latest: "2.18.0--r42hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-rae230acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-rae230acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rae230acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rae230acdf", "latest": {"2.18.0--r42hdfd78af_11": "sha256:46fe7d8d096c241c6347b4f01cfc9645ddc9cd5bd26c78aac3e4f99df1101cfa"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:ba957a7bce45ef984a957dd55b1f8ad3f73680352069f0b5ed4010f67b9fa9eb", "2.18.0--r42hdfd78af_11": "sha256:46fe7d8d096c241c6347b4f01cfc9645ddc9cd5bd26c78aac3e4f99df1101cfa"}, "docker": "quay.io/biocontainers/bioconductor-rae230acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rae230acdf.
shpc-registry automated BioContainers addition for bioconductor-rae230acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230acdf:2.18.0--r42hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rae230acdf/2.18.0--r42hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-rae230acdf/2.18.0--r42hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rae230acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rae230acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rae230acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rae230acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rae230acdf

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