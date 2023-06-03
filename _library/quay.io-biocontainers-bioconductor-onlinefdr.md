---
layout: container
name:  "quay.io/biocontainers/bioconductor-onlinefdr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-onlinefdr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-onlinefdr/container.yaml"
updated_at: "2023-06-03 03:37:16.883681"
latest: "2.6.0--r42hf17093f_2"
container_url: "https://biocontainers.pro/tools/bioconductor-onlinefdr"

versions:
 - "2.2.0--r41hc247a5b_2"
 - "2.6.0--r42hc247a5b_0"
 - "2.6.0--r42hf17093f_2"
description: "shpc-registry automated BioContainers addition for bioconductor-onlinefdr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-onlinefdr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-onlinefdr", "latest": {"2.6.0--r42hf17093f_2": "sha256:c5d7399485458f21519aadb528fd49d2a4a1fb7de2e596a8fd937f1359b4f930"}, "tags": {"2.2.0--r41hc247a5b_2": "sha256:b31fc934b6d6b4bcb73be92a10f244e04b6b4c96b5afaf5fc8ca89e76fa863ee", "2.6.0--r42hc247a5b_0": "sha256:9163f05f69bfa2e279d458b31a025a24fc29eee1b8d11e013f457111ab902cd7", "2.6.0--r42hf17093f_2": "sha256:c5d7399485458f21519aadb528fd49d2a4a1fb7de2e596a8fd937f1359b4f930"}, "docker": "quay.io/biocontainers/bioconductor-onlinefdr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-onlinefdr.
shpc-registry automated BioContainers addition for bioconductor-onlinefdr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-onlinefdr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-onlinefdr:2.6.0--r42hf17093f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-onlinefdr/2.6.0--r42hf17093f_2
$ module help quay.io/biocontainers/bioconductor-onlinefdr/2.6.0--r42hf17093f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-onlinefdr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-onlinefdr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-onlinefdr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-onlinefdr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-onlinefdr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-onlinefdr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-onlinefdr

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