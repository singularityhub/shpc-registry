---
layout: container
name:  "quay.io/biocontainers/bioconductor-medicagocdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-medicagocdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-medicagocdf/container.yaml"
updated_at: "2023-03-13 02:45:35.891505"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-medicagocdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-medicagocdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-medicagocdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-medicagocdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:455fed89b4cc4cf3857c3b21caffa5f7b227c71944dea7b4e21bc2a9175c920b"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c61df49512416f095d2676f42be08af7d5213a75d514980f309a668ba03db619", "2.18.0--r42hdfd78af_10": "sha256:455fed89b4cc4cf3857c3b21caffa5f7b227c71944dea7b4e21bc2a9175c920b"}, "docker": "quay.io/biocontainers/bioconductor-medicagocdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-medicagocdf.
shpc-registry automated BioContainers addition for bioconductor-medicagocdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-medicagocdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-medicagocdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-medicagocdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-medicagocdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-medicagocdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medicagocdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medicagocdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-medicagocdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-medicagocdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-medicagocdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-medicagocdf

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