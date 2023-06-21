---
layout: container
name:  "quay.io/biocontainers/bioconductor-tinesath1cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tinesath1cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tinesath1cdf/container.yaml"
updated_at: "2023-06-21 03:16:18.822164"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tinesath1cdf"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.35.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tinesath1cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tinesath1cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tinesath1cdf", "latest": {"1.36.0--r42hdfd78af_0": "sha256:5db6e45d14364a2cc2fb8b8798a7fdd283ddb4caa6c2265b5203ffa6b6d4f38d"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:f3ba60fbf58ceca383f7465d23c7c1639bef611ae825b1eee0286339f2ee567e", "1.36.0--r42hdfd78af_0": "sha256:5db6e45d14364a2cc2fb8b8798a7fdd283ddb4caa6c2265b5203ffa6b6d4f38d", "1.35.0--r42hdfd78af_0": "sha256:0222f4dc0f21f76954f9c060349a5a5dba2d1329aac83ddb3da149ac097728e8"}, "docker": "quay.io/biocontainers/bioconductor-tinesath1cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tinesath1cdf.
shpc-registry automated BioContainers addition for bioconductor-tinesath1cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tinesath1cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tinesath1cdf:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tinesath1cdf/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tinesath1cdf/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tinesath1cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tinesath1cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tinesath1cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tinesath1cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tinesath1cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tinesath1cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tinesath1cdf

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