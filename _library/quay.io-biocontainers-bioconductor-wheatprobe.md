---
layout: container
name:  "quay.io/biocontainers/bioconductor-wheatprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wheatprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wheatprobe/container.yaml"
updated_at: "2023-11-07 03:06:53.850001"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-wheatprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-wheatprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wheatprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wheatprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:cc5cc5c4d5e797ead3c7f26c8cb19b35e5d89a2f18289f0871a54a3c5841d22b"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:444bc9708fc582c5b519ca4fbdb92fcc829faf9af66cbfa31450581eba8a89bb", "2.18.0--r41hdfd78af_10": "sha256:386bd3a3324603becaad34c3e8d9ebe2c7546b798b452533383febcbc147f872", "2.18.0--r42hdfd78af_11": "sha256:8d7aa05a540d0264c30e632d60f8c133cbecfb301283421f4facc4b9824678da", "2.18.0--r43hdfd78af_12": "sha256:cc5cc5c4d5e797ead3c7f26c8cb19b35e5d89a2f18289f0871a54a3c5841d22b"}, "docker": "quay.io/biocontainers/bioconductor-wheatprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wheatprobe.
shpc-registry automated BioContainers addition for bioconductor-wheatprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wheatprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wheatprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wheatprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-wheatprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wheatprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wheatprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wheatprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wheatprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wheatprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wheatprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-wheatprobe

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