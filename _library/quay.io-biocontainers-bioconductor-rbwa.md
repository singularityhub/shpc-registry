---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbwa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbwa/container.yaml"
updated_at: "2025-04-04 03:46:02.947255"
latest: "1.6.0--r43hd5da469_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rbwa"

versions:
 - "1.2.0--r42h87de86e_0"
 - "1.2.0--r42hd5da469_2"
 - "1.4.0--r43hd5da469_0"
 - "1.6.0--r43hd5da469_0"
description: "singularity registry hpc automated addition for bioconductor-rbwa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbwa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-rbwa", "latest": {"1.6.0--r43hd5da469_0": "sha256:a2155fcdd2466460e209c5b6faedddf3bca5c077c0bb3905d483154e55394c73"}, "tags": {"1.2.0--r42h87de86e_0": "sha256:b175f0ae1a0d4013e9605bcc5f027906a26aa23c2b653ba19cc942521840218b", "1.2.0--r42hd5da469_2": "sha256:64e5d286a34936a3b7efbdb3c97c8eb297528bc16171e0a0e582d5d8a70d0558", "1.4.0--r43hd5da469_0": "sha256:f0b0be863b738793f638b4ab7ee539a09af3e4c7ee55cb73f90f2e34c957518e", "1.6.0--r43hd5da469_0": "sha256:a2155fcdd2466460e209c5b6faedddf3bca5c077c0bb3905d483154e55394c73"}, "docker": "quay.io/biocontainers/bioconductor-rbwa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbwa.
singularity registry hpc automated addition for bioconductor-rbwa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbwa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbwa:1.6.0--r43hd5da469_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbwa/1.6.0--r43hd5da469_0
$ module help quay.io/biocontainers/bioconductor-rbwa/1.6.0--r43hd5da469_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbwa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbwa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbwa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbwa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbwa

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