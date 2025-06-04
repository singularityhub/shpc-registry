---
layout: container
name:  "quay.io/biocontainers/bioconductor-knowseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-knowseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-knowseq/container.yaml"
updated_at: "2025-06-04 03:48:46.492655"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-knowseq"
aliases:
 - "pandoc"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-knowseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-knowseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-knowseq", "latest": {"1.16.0--r43hdfd78af_0": "sha256:fc8414988ca732d70cf7b4d64f19ea02cb508b482ef73055ed996be7f7df0fd9"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4fdada097d3a961c449bf2251ed1c655f135840b8f67601a1213e9b46a675b8a", "1.12.0--r42hdfd78af_0": "sha256:ba4eaa903b370b7bd679bee00b4cb96b1498b6220747aa1da8cf89ace50d7866", "1.14.0--r43hdfd78af_0": "sha256:f6b4fdc12f7792bddcdf4e870c423af346817cc69be4536b0587b076764dd9bb", "1.16.0--r43hdfd78af_0": "sha256:fc8414988ca732d70cf7b4d64f19ea02cb508b482ef73055ed996be7f7df0fd9"}, "docker": "quay.io/biocontainers/bioconductor-knowseq", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-knowseq.
shpc-registry automated BioContainers addition for bioconductor-knowseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-knowseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-knowseq:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-knowseq/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-knowseq/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-knowseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-knowseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-knowseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-knowseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-knowseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-knowseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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