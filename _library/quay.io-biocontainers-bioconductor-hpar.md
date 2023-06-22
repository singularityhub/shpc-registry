---
layout: container
name:  "quay.io/biocontainers/bioconductor-hpar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hpar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hpar/container.yaml"
updated_at: "2023-06-22 03:13:53.486872"
latest: "1.40.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hpar"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hpar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hpar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hpar", "latest": {"1.40.0--r42hdfd78af_0": "sha256:29a228ba1a5560bca8998fb7b10264156e283b58a7cf97e47f206db1a81eb94a"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:d714ef320c784ed284037cffbf5d80903586edf16ab6619b476c9b86a30bfad6", "1.40.0--r42hdfd78af_0": "sha256:29a228ba1a5560bca8998fb7b10264156e283b58a7cf97e47f206db1a81eb94a"}, "docker": "quay.io/biocontainers/bioconductor-hpar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hpar.
shpc-registry automated BioContainers addition for bioconductor-hpar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hpar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hpar:1.40.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hpar/1.40.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hpar/1.40.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hpar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hpar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hpar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hpar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hpar

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