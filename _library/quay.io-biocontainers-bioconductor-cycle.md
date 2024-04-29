---
layout: container
name:  "quay.io/biocontainers/bioconductor-cycle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cycle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cycle/container.yaml"
updated_at: "2024-04-29 03:05:49.637392"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cycle"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cycle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cycle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cycle", "latest": {"1.56.0--r43hdfd78af_0": "sha256:8f7dbce30de88896c13476769ebb396303e9e6ea91ecd4392bc47cc0f19c4875"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:81a49e266bdd37853249515739b968aa493c970210b92001b3b16063e74ff8ab", "1.52.0--r42hdfd78af_0": "sha256:5f1875d148858c1d860402a116f0fa6cf8a942f8ce9eea9df7ac90ad8291b794", "1.54.0--r43hdfd78af_0": "sha256:e514b3780585eea9c64149c1b12af3a1a3f6f10cc7a09c4595ec32c949b56220", "1.56.0--r43hdfd78af_0": "sha256:8f7dbce30de88896c13476769ebb396303e9e6ea91ecd4392bc47cc0f19c4875"}, "docker": "quay.io/biocontainers/bioconductor-cycle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cycle.
shpc-registry automated BioContainers addition for bioconductor-cycle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cycle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cycle:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cycle/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cycle/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cycle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cycle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cycle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cycle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cycle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cycle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cycle

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