---
layout: container
name:  "quay.io/biocontainers/bioconductor-tricycle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tricycle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tricycle/container.yaml"
updated_at: "2025-12-01 04:27:06.685072"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tricycle"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tricycle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tricycle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tricycle", "latest": {"1.14.0--r44hdfd78af_0": "sha256:a4e5e4c7fc4d770b44c091cabd3e95ae3d86f639177dc562ba834fd003870633"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:d9c1dfbd26233cac9a36d1465e4deda7e1f0f4542130347cb74cc2a469d4b336", "1.6.0--r42hdfd78af_0": "sha256:0579e71acae079f25e69d724b130e9de75285d83827158f74a74a4d793c1389c", "1.8.0--r43hdfd78af_0": "sha256:41873dc934bf14659dd0057dfbae8c4a9a60c55df7b6323a5f591f4133e6a14c", "1.10.0--r43hdfd78af_0": "sha256:44b862cbb41febeb1073cde994b43bf6fb86b035d02ec76523c3f6ce0e6fd7f0", "1.14.0--r44hdfd78af_0": "sha256:a4e5e4c7fc4d770b44c091cabd3e95ae3d86f639177dc562ba834fd003870633"}, "docker": "quay.io/biocontainers/bioconductor-tricycle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tricycle.
shpc-registry automated BioContainers addition for bioconductor-tricycle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tricycle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tricycle:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tricycle/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tricycle/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tricycle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tricycle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tricycle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tricycle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tricycle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tricycle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tricycle

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