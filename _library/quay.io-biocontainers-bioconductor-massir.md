---
layout: container
name:  "quay.io/biocontainers/bioconductor-massir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-massir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-massir/container.yaml"
updated_at: "2024-02-09 02:45:28.237921"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-massir"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-massir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-massir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-massir", "latest": {"1.38.0--r43hdfd78af_0": "sha256:650d5f67558f57a05635007819ce329f29835e47db979a95f0ed2fde107c286a"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:d132c1f741d7ba3da557af179447c4f8c48630e9a70b59a9873784ec351e66e0", "1.34.0--r42hdfd78af_0": "sha256:c1686d39c196557acd1a8cbdbdc98a3a1fd4b0c74370a3bf577ce23b512cfe16", "1.36.0--r43hdfd78af_0": "sha256:38c6cd93c6d661e14c79a528c5538fe70ff274b8ce81cbd206fd0a64acd40268", "1.38.0--r43hdfd78af_0": "sha256:650d5f67558f57a05635007819ce329f29835e47db979a95f0ed2fde107c286a"}, "docker": "quay.io/biocontainers/bioconductor-massir"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-massir.
shpc-registry automated BioContainers addition for bioconductor-massir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-massir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-massir:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-massir/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-massir/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-massir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-massir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-massir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-massir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-massir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-massir

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