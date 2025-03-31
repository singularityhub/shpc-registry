---
layout: container
name:  "quay.io/biocontainers/bioconductor-stategra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stategra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stategra/container.yaml"
updated_at: "2025-03-31 03:27:30.222317"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stategra"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stategra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stategra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stategra", "latest": {"1.38.0--r43hdfd78af_0": "sha256:af094a0314ec41493fbbd0c9c8b8956ed487d950b61fad220170846b57dea1d5"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:208584d968acf7e426c7478f09fff71be3daef57b467831ef413df23293d6288", "1.34.0--r42hdfd78af_0": "sha256:abccfbf82dbd8e4b040654777b8a245fb51876eea0994ea5c44141bd66419fd0", "1.36.0--r43hdfd78af_0": "sha256:24d775941b7c2525753a1e63bda3ad782dd0b70a86a8b5df81b1cd6e9e5a1385", "1.38.0--r43hdfd78af_0": "sha256:af094a0314ec41493fbbd0c9c8b8956ed487d950b61fad220170846b57dea1d5"}, "docker": "quay.io/biocontainers/bioconductor-stategra"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stategra.
shpc-registry automated BioContainers addition for bioconductor-stategra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stategra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stategra:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stategra/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stategra/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stategra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stategra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stategra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stategra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stategra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stategra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-stategra

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