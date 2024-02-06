---
layout: container
name:  "quay.io/biocontainers/bioconductor-arrayqualitymetrics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-arrayqualitymetrics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-arrayqualitymetrics/container.yaml"
updated_at: "2024-02-06 03:00:31.753771"
latest: "3.58.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-arrayqualitymetrics"

versions:
 - "3.50.0--r41hdfd78af_0"
 - "3.54.0--r42hdfd78af_0"
 - "3.56.0--r43hdfd78af_0"
 - "3.58.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-arrayqualitymetrics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-arrayqualitymetrics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-arrayqualitymetrics", "latest": {"3.58.0--r43hdfd78af_0": "sha256:f1d2ea3b04285dbec942a6b4f681666933a8b16b34fb7b0e2838286812062594"}, "tags": {"3.50.0--r41hdfd78af_0": "sha256:f87de19b4db758a8f709405ef80669f3517ac6e83879443a007bb261206dba28", "3.54.0--r42hdfd78af_0": "sha256:910bcb15bc4ce2ef8f3f837bab28c939fca598845e2d627ec7994e12e3c89727", "3.56.0--r43hdfd78af_0": "sha256:1fd468a1a1902ef81f008b59cfcb5153d8647c3174cff26b2abba46d6a893e76", "3.58.0--r43hdfd78af_0": "sha256:f1d2ea3b04285dbec942a6b4f681666933a8b16b34fb7b0e2838286812062594"}, "docker": "quay.io/biocontainers/bioconductor-arrayqualitymetrics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-arrayqualitymetrics.
shpc-registry automated BioContainers addition for bioconductor-arrayqualitymetrics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayqualitymetrics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayqualitymetrics:3.58.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-arrayqualitymetrics/3.58.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-arrayqualitymetrics/3.58.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-arrayqualitymetrics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayqualitymetrics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayqualitymetrics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-arrayqualitymetrics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-arrayqualitymetrics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-arrayqualitymetrics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-arrayqualitymetrics

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