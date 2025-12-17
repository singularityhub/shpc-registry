---
layout: container
name:  "quay.io/biocontainers/bioconductor-rrvgo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rrvgo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rrvgo/container.yaml"
updated_at: "2025-12-17 16:03:22.592065"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rrvgo"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rrvgo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rrvgo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rrvgo", "latest": {"1.18.0--r44hdfd78af_0": "sha256:368e6bfac6bd34c79d46ea956bb922b8ace4d76bb43592c7d72b0786c6d95727"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:ce506aa0bb51320cea491d407e70a79c650e5e6dcf0111470051f81d44b9b164", "1.10.0--r42hdfd78af_0": "sha256:7728272f645ae55c3a999b052b7824b0d3da2ceb37bea2e402ec16da5db8f689", "1.12.0--r43hdfd78af_0": "sha256:4add18b4988e3f2147d5d3975b5f213eead4e92d95be18e1b644918e8b293184", "1.14.0--r43hdfd78af_0": "sha256:83110e983194e25d2088fb95341b826755a4c0308cb5a126aa5858bf2cd2486b", "1.18.0--r44hdfd78af_0": "sha256:368e6bfac6bd34c79d46ea956bb922b8ace4d76bb43592c7d72b0786c6d95727"}, "docker": "quay.io/biocontainers/bioconductor-rrvgo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rrvgo.
shpc-registry automated BioContainers addition for bioconductor-rrvgo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rrvgo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rrvgo:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rrvgo/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rrvgo/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rrvgo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rrvgo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rrvgo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rrvgo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rrvgo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rrvgo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rrvgo

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