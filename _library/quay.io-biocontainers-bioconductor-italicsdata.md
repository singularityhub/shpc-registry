---
layout: container
name:  "quay.io/biocontainers/bioconductor-italicsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-italicsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-italicsdata/container.yaml"
updated_at: "2025-07-18 10:29:04.909806"
latest: "2.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-italicsdata"

versions:
 - "2.32.0--r41hdfd78af_1"
 - "2.36.0--r42hdfd78af_0"
 - "2.38.0--r43hdfd78af_0"
 - "2.40.0--r43hdfd78af_0"
 - "2.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-italicsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-italicsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-italicsdata", "latest": {"2.44.0--r44hdfd78af_0": "sha256:c8ccdc6f5a6ca24f67a3081b428ab7e8fe48ac7d9c3903377fb478335eb7162b"}, "tags": {"2.32.0--r41hdfd78af_1": "sha256:3e980c35c846274dad61dab2ce3dc8557ac34d053e70ae9fd2343eb25a0469cb", "2.36.0--r42hdfd78af_0": "sha256:ce574f2034def617207ced60a91ad200e85cf90221cc2d6dda492c6900c8b34b", "2.38.0--r43hdfd78af_0": "sha256:2c60e308d7a07b7fd3e8d15c3a5fd1e309d42fd2454df8c4cd354ca869091b06", "2.40.0--r43hdfd78af_0": "sha256:9abefebf61f87b975cdb40a1aee27bccc29a74e18d7591cdd954df47f43db397", "2.44.0--r44hdfd78af_0": "sha256:c8ccdc6f5a6ca24f67a3081b428ab7e8fe48ac7d9c3903377fb478335eb7162b"}, "docker": "quay.io/biocontainers/bioconductor-italicsdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-italicsdata.
shpc-registry automated BioContainers addition for bioconductor-italicsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-italicsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-italicsdata:2.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-italicsdata/2.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-italicsdata/2.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-italicsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-italicsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-italicsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-italicsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-italicsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-italicsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-italicsdata

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