---
layout: container
name:  "quay.io/biocontainers/bioconductor-mpfe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mpfe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mpfe/container.yaml"
updated_at: "2025-03-18 03:06:17.913994"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mpfe"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mpfe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mpfe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mpfe", "latest": {"1.42.0--r44hdfd78af_0": "sha256:9fbf24f00296ccd2efba4bf452cac4eea771d570b3fdb6e00f94ada0e6a072fb"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:6285c59668988fc751a5d4aa8306e6c2e6b5a7fc283c6e3f8e4c0248190856a7", "1.34.0--r42hdfd78af_0": "sha256:9a03f2dd5a5cbca74e6ffe9e957c11bcca1f99e41d78ddf303234276fa729804", "1.36.0--r43hdfd78af_0": "sha256:5fc0dd5221907bbf43d987863cd8365bb0856d190738a17d7ff1bb095dfa1e05", "1.38.0--r43hdfd78af_0": "sha256:f5c2c6a7f048278405f17683e03888eb9853e686f8f100cb72c89223b8c279a3", "1.42.0--r44hdfd78af_0": "sha256:9fbf24f00296ccd2efba4bf452cac4eea771d570b3fdb6e00f94ada0e6a072fb"}, "docker": "quay.io/biocontainers/bioconductor-mpfe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mpfe.
shpc-registry automated BioContainers addition for bioconductor-mpfe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mpfe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mpfe:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mpfe/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mpfe/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mpfe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpfe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpfe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mpfe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mpfe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mpfe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mpfe

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