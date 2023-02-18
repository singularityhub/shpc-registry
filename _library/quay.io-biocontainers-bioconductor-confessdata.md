---
layout: container
name:  "quay.io/biocontainers/bioconductor-confessdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-confessdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-confessdata/container.yaml"
updated_at: "2023-02-18 02:47:36.788966"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-confessdata"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-confessdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-confessdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-confessdata", "latest": {"1.26.0--r42hdfd78af_0": "sha256:ff7ff9d9b31e825c8d43de26c750097028e9172170aebd4313efb24260c64387"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:9dc597a2dc14c4224136490c14bc1cfcf94cb052d1c82d765bfd77440d0d913c", "1.26.0--r42hdfd78af_0": "sha256:ff7ff9d9b31e825c8d43de26c750097028e9172170aebd4313efb24260c64387"}, "docker": "quay.io/biocontainers/bioconductor-confessdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-confessdata.
shpc-registry automated BioContainers addition for bioconductor-confessdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-confessdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-confessdata:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-confessdata/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-confessdata/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-confessdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-confessdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-confessdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-confessdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-confessdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-confessdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-confessdata

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