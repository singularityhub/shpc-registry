---
layout: container
name:  "quay.io/biocontainers/bioconductor-chippeakanno"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chippeakanno/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chippeakanno/container.yaml"
updated_at: "2025-03-08 02:33:12.863258"
latest: "3.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chippeakanno"

versions:
 - "3.28.0--r41hdfd78af_0"
 - "3.32.0--r42hdfd78af_0"
 - "3.34.1--r43hdfd78af_0"
 - "3.36.0--r43hdfd78af_0"
 - "3.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chippeakanno"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chippeakanno", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chippeakanno", "latest": {"3.40.0--r44hdfd78af_0": "sha256:23258765b48fb77280d144fb7c2817d707f8ff5f7c7c1c7f431f291cac301900"}, "tags": {"3.28.0--r41hdfd78af_0": "sha256:e49cef3379e15a4c7105f5a4348979e9db1855dd00efba6211dfc5286882cc0e", "3.32.0--r42hdfd78af_0": "sha256:098d63eeefda46a3624aee4980a95c606e0bca3537be3f0bb9ae288c88129bac", "3.34.1--r43hdfd78af_0": "sha256:53dcb6b1af539b8834fc65a34e001f3c952017bc3b1dc9528741505e9850346d", "3.36.0--r43hdfd78af_0": "sha256:7aa1d52c40fcf561fa947bb68f65b914ebadf70063ad24d33e501b42e85d6445", "3.40.0--r44hdfd78af_0": "sha256:23258765b48fb77280d144fb7c2817d707f8ff5f7c7c1c7f431f291cac301900"}, "docker": "quay.io/biocontainers/bioconductor-chippeakanno"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chippeakanno.
shpc-registry automated BioContainers addition for bioconductor-chippeakanno
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chippeakanno
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chippeakanno:3.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chippeakanno/3.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chippeakanno/3.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chippeakanno-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chippeakanno-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chippeakanno-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chippeakanno-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chippeakanno-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chippeakanno-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chippeakanno

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