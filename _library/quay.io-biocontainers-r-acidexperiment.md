---
layout: container
name:  "quay.io/biocontainers/r-acidexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidexperiment/container.yaml"
updated_at: "2023-03-07 03:36:44.054112"
latest: "0.4.5--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidexperiment"

versions:
 - "0.3.0--r41hdfd78af_0"
 - "0.4.4--r42hdfd78af_0"
 - "0.4.4--r42hdfd78af_1"
 - "0.4.5--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidexperiment"
config: {"url": "https://biocontainers.pro/tools/r-acidexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidexperiment", "latest": {"0.4.5--r42hdfd78af_0": "sha256:b80b37a52a231b6fb0f0572ca94db8c2a5491aa811c9625affd6863acbbd5d73"}, "tags": {"0.3.0--r41hdfd78af_0": "sha256:7f190b21233e13ed428108eed86005c9896f03d82fad42d5c45a5c81252b12a3", "0.4.4--r42hdfd78af_0": "sha256:9ce87bf63b684343a8b113ef9f829b60c53c8064805dce7746ebd1ee9cac6871", "0.4.4--r42hdfd78af_1": "sha256:565b32ae3b62788a82bf497ed2f5b1f948a7586c6ec242a62d410fe95a248de2", "0.4.5--r42hdfd78af_0": "sha256:b80b37a52a231b6fb0f0572ca94db8c2a5491aa811c9625affd6863acbbd5d73"}, "docker": "quay.io/biocontainers/r-acidexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidexperiment.
shpc-registry automated BioContainers addition for r-acidexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidexperiment:0.4.5--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidexperiment/0.4.5--r42hdfd78af_0
$ module help quay.io/biocontainers/r-acidexperiment/0.4.5--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidexperiment

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