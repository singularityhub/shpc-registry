---
layout: container
name:  "quay.io/biocontainers/bioconductor-anota"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anota/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anota/container.yaml"
updated_at: "2024-02-13 03:02:31.245929"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anota"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anota"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anota", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anota", "latest": {"1.50.0--r43hdfd78af_0": "sha256:e39e1dc908585f113f76dd4b5ad901307af70a037f219480e952dae9144ff63a"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:ea61ea6f8a23660e256118e9302185ae63f7f517232e2e9a4815802395cff345", "1.46.0--r42hdfd78af_0": "sha256:7a91ba920d69dc821e500d719a1460cd30d81b74f0642ed5dd31e436cb9093cf", "1.48.0--r43hdfd78af_0": "sha256:72df0109cc4f50e267a50edc82a5a5de6e3f1b59566d7732f5f62598f7e4ce4f", "1.50.0--r43hdfd78af_0": "sha256:e39e1dc908585f113f76dd4b5ad901307af70a037f219480e952dae9144ff63a"}, "docker": "quay.io/biocontainers/bioconductor-anota"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anota.
shpc-registry automated BioContainers addition for bioconductor-anota
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anota
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anota:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anota/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anota/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anota-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anota-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anota-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anota-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anota-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anota-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-anota

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