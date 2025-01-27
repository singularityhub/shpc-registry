---
layout: container
name:  "quay.io/biocontainers/bioconductor-lbe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lbe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lbe/container.yaml"
updated_at: "2025-01-27 03:00:03.446802"
latest: "1.74.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lbe"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.74.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lbe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lbe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lbe", "latest": {"1.74.0--r44hdfd78af_0": "sha256:709f0def979020a537a7664f576c4afcccc1efd4b4a579bf5260a2a5ad509127"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:c89c3283594306dbc33bd2a58443c60fdb3b192e91b092f2bd3c3b53fc2109ed", "1.66.0--r42hdfd78af_0": "sha256:b6d6d13aa8d1564040cdadb9866c5570a8402902903f14fb7dafb0656eb7153f", "1.68.0--r43hdfd78af_0": "sha256:a9bb3b8fe7b6bc7d87889313265d0da5f6b9c765731eea8bb3938f9f12af9603", "1.70.0--r43hdfd78af_0": "sha256:c94acc5f15ede300b7f91aa356dfa204c2e7cf5718fd83f6f6d4601912a27c8c", "1.74.0--r44hdfd78af_0": "sha256:709f0def979020a537a7664f576c4afcccc1efd4b4a579bf5260a2a5ad509127"}, "docker": "quay.io/biocontainers/bioconductor-lbe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lbe.
shpc-registry automated BioContainers addition for bioconductor-lbe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lbe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lbe:1.74.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lbe/1.74.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lbe/1.74.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lbe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lbe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lbe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lbe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lbe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lbe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lbe

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