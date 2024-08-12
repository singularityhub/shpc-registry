---
layout: container
name:  "quay.io/biocontainers/bioconductor-metamsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metamsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metamsdata/container.yaml"
updated_at: "2024-08-12 03:11:49.557181"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metamsdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metamsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metamsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metamsdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:364e9edc9ac2a5c0ae7a3b52700c3be49d7e76f4180dee4d283a843f4b5458e8"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:50b47e407d1190d11bb481b78a3afa756d37e51e1bde4ac58f26836454db8714", "1.33.0--r42hdfd78af_0": "sha256:759521e4f226f50e57051b62a2329e2c328fbcb15dee8c4848d00049ca17275b", "1.36.0--r43hdfd78af_0": "sha256:dbb502bd3602d8e4620b5c94996bd744c2c6ccd88ed26e15cd92301e018ce488", "1.38.0--r43hdfd78af_0": "sha256:364e9edc9ac2a5c0ae7a3b52700c3be49d7e76f4180dee4d283a843f4b5458e8"}, "docker": "quay.io/biocontainers/bioconductor-metamsdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metamsdata.
shpc-registry automated BioContainers addition for bioconductor-metamsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metamsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metamsdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metamsdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metamsdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metamsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metamsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metamsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metamsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metamsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metamsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metamsdata

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