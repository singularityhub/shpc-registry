---
layout: container
name:  "quay.io/biocontainers/bioconductor-moe430aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moe430aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moe430aprobe/container.yaml"
updated_at: "2023-10-19 02:25:41.846586"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-moe430aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-moe430aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moe430aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moe430aprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:b75cc90ec19d4ac78c1eaed56516bc08a1e75131c1bdd547ebccec94a78c70a2"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:33f3fcb949a46616a3bad2d607fa2adb4f06b786c7042735f7e5d8f75e607c94", "2.18.0--r42hdfd78af_10": "sha256:94f0c3259edd16ff0ddcd8686c78ce6aa8280ec888dda9f4a5d7f999116ef193", "2.18.0--r43hdfd78af_11": "sha256:b75cc90ec19d4ac78c1eaed56516bc08a1e75131c1bdd547ebccec94a78c70a2"}, "docker": "quay.io/biocontainers/bioconductor-moe430aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moe430aprobe.
shpc-registry automated BioContainers addition for bioconductor-moe430aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430aprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moe430aprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-moe430aprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moe430aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moe430aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moe430aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moe430aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moe430aprobe

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