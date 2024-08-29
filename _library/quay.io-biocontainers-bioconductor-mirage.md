---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirage/container.yaml"
updated_at: "2024-08-29 03:19:03.311186"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirage"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirage"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirage", "latest": {"1.44.0--r43hdfd78af_0": "sha256:1084f9277b62bd8c2ca824f3c2243547fe95c7d216ebc73493955faa641fd758"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:380030860e91df32ae970ffbb5213ea88303b66b5607c50c4b5d17b6551b863d", "1.40.0--r42hdfd78af_0": "sha256:67473f9f0600c071fd2e9584eb632d5b68e4e7923dbbe1a1d07e7774702c89a2", "1.42.0--r43hdfd78af_0": "sha256:7fcfd7aa78c33ffe171628f98657b0724868bffdb4aff6ff940ecf34c91448f3", "1.44.0--r43hdfd78af_0": "sha256:1084f9277b62bd8c2ca824f3c2243547fe95c7d216ebc73493955faa641fd758"}, "docker": "quay.io/biocontainers/bioconductor-mirage"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirage.
shpc-registry automated BioContainers addition for bioconductor-mirage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirage:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirage/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirage/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirage

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