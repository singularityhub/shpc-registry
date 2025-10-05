---
layout: container
name:  "quay.io/biocontainers/bioconductor-kegggraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kegggraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kegggraph/container.yaml"
updated_at: "2025-10-05 03:55:48.794048"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-kegggraph"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-kegggraph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kegggraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kegggraph", "latest": {"1.66.0--r44hdfd78af_0": "sha256:54ca0b3076267b46f3ec61896ce5d6a7a4ce29629c6fb927c2ed7cca8b5857f4"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:cbde28c73b7093f7c4b5f3377f58f118af9d296cfd2692e4b7aa77826afb97ed", "1.58.0--r42hdfd78af_0": "sha256:8137d8bb6f92c62b1639137ea7e3d8f2ad920c28c48e24d1dadc6d5735e787ca", "1.60.0--r43hdfd78af_0": "sha256:633b1526c8101172b171d17a0a0134fb17b22e8fee43d0e413513ed0f0c0d0f9", "1.62.0--r43hdfd78af_0": "sha256:053bee68f49a440ee0011097d6a6867364804cf2ce1ef48cd747593baa172d96", "1.66.0--r44hdfd78af_0": "sha256:54ca0b3076267b46f3ec61896ce5d6a7a4ce29629c6fb927c2ed7cca8b5857f4"}, "docker": "quay.io/biocontainers/bioconductor-kegggraph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kegggraph.
shpc-registry automated BioContainers addition for bioconductor-kegggraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kegggraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kegggraph:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kegggraph/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-kegggraph/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kegggraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kegggraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kegggraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kegggraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kegggraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kegggraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-kegggraph

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