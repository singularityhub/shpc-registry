---
layout: container
name:  "quay.io/biocontainers/bioconductor-biomformat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biomformat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biomformat/container.yaml"
updated_at: "2023-11-12 02:44:26.072538"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biomformat"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biomformat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biomformat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biomformat", "latest": {"1.28.0--r43hdfd78af_0": "sha256:463ad051acf9ac6875b98a1e5da657204bc8b644af095222927e29552a751a7e"}, "tags": {"1.8.0--r351_0": "sha256:53ea0ba24cf1b038ef84ef86b7dfcac96582675caf374b45de206dacac7dabf9", "1.26.0--r42hdfd78af_0": "sha256:b626cc9aeda70c955b5d17c11b41cbe2b9fab466621ad2080456163286f3baf0", "1.22.0--r41hdfd78af_0": "sha256:fa26c6b1abea085b296391a64cfdd8ee3d88f118fb8cc047ab9014764b796239", "1.20.0--r41hdfd78af_0": "sha256:64f8d6b13662fec97053122c8e8cd0d25b012c851931edda13116851cdd23a59", "1.18.0--r40hdfd78af_1": "sha256:d56452aea777a469305ad5ba097268689178a11aac9a6f9e24d33b1c1edfa982", "1.16.0--r40_0": "sha256:4239eb75dbedf61842d4e9669461bf7b325e0f9adea79ce5eda9c21d987193d8", "1.28.0--r43hdfd78af_0": "sha256:463ad051acf9ac6875b98a1e5da657204bc8b644af095222927e29552a751a7e"}, "docker": "quay.io/biocontainers/bioconductor-biomformat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biomformat.
shpc-registry automated BioContainers addition for bioconductor-biomformat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biomformat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biomformat:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biomformat/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biomformat/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biomformat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomformat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomformat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biomformat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biomformat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biomformat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biomformat

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