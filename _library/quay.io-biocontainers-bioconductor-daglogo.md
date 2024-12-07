---
layout: container
name:  "quay.io/biocontainers/bioconductor-daglogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-daglogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-daglogo/container.yaml"
updated_at: "2024-12-07 02:12:55.445589"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-daglogo"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-daglogo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-daglogo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-daglogo", "latest": {"1.40.0--r43hdfd78af_0": "sha256:8329b35b0b8abab50198df14ae6576e2cd1f1d037b7e067b1dd0195f8820b6ba"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:d10773b3a7ce39127ac5e66af105cb840f8906c564cc716c67a46215d162ca7f", "1.36.0--r42hdfd78af_0": "sha256:2319bf2cd74ba69c8a18dd41b94bba32ab29e6488513f1c4e027befc2d085864", "1.38.0--r43hdfd78af_0": "sha256:d9763cc79cf36ab0001b8602e6d6d2f9491007cb6c2cb5d108b189e2b7280a79", "1.40.0--r43hdfd78af_0": "sha256:8329b35b0b8abab50198df14ae6576e2cd1f1d037b7e067b1dd0195f8820b6ba"}, "docker": "quay.io/biocontainers/bioconductor-daglogo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-daglogo.
shpc-registry automated BioContainers addition for bioconductor-daglogo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-daglogo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-daglogo:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-daglogo/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-daglogo/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-daglogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-daglogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-daglogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-daglogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-daglogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-daglogo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-daglogo

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