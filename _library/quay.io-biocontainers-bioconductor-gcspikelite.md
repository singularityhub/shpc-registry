---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcspikelite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcspikelite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcspikelite/container.yaml"
updated_at: "2023-05-01 03:23:18.377430"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcspikelite"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.35.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcspikelite"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcspikelite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcspikelite", "latest": {"1.36.0--r42hdfd78af_0": "sha256:d3ac302560e62d3355744d0e31a3610f920f8dba479748d4438a259cd3bd0ad1"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:0ec23b2d8a7bd2bd6c478e185b3b7c80d30cfe84b7fa32f027a01287861422f8", "1.36.0--r42hdfd78af_0": "sha256:d3ac302560e62d3355744d0e31a3610f920f8dba479748d4438a259cd3bd0ad1", "1.35.0--r42hdfd78af_0": "sha256:1cd4fc5011c2379f6672bf77a4aa84dd7eede24983a08b5f04952788bed1aab6"}, "docker": "quay.io/biocontainers/bioconductor-gcspikelite"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcspikelite.
shpc-registry automated BioContainers addition for bioconductor-gcspikelite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcspikelite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcspikelite:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcspikelite/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gcspikelite/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcspikelite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcspikelite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcspikelite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcspikelite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcspikelite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcspikelite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gcspikelite

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