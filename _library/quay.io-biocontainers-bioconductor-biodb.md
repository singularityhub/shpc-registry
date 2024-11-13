---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodb/container.yaml"
updated_at: "2024-11-13 04:01:03.259739"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodb"

versions:
 - "1.2.2--r41hc247a5b_1"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodb", "latest": {"1.10.0--r43hf17093f_0": "sha256:720d899274c82f9d0673041a370afb311d9961ca416038695a36bd179e0c4289"}, "tags": {"1.2.2--r41hc247a5b_1": "sha256:eaf4b6be0624ad0fbd231ee7f8c80e555636582625654628b7bb9d5230c98099", "1.6.0--r42hc247a5b_0": "sha256:1a95df74b43a31827fc24900a01aea9f009afae3e8b72866cf4656d5980ff096", "1.6.0--r42hf17093f_1": "sha256:feca11aebebee1366f0024e5fad9c51bd929e88ea1607aaf960ffec5c571753b", "1.8.0--r43hf17093f_0": "sha256:b60d5c4b5e1052ed0f8f11ba9f6dd2849f168fc6eafa5dc4cac4be380138b748", "1.10.0--r43hf17093f_0": "sha256:720d899274c82f9d0673041a370afb311d9961ca416038695a36bd179e0c4289"}, "docker": "quay.io/biocontainers/bioconductor-biodb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodb.
shpc-registry automated BioContainers addition for bioconductor-biodb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodb:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodb/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-biodb/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodb

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