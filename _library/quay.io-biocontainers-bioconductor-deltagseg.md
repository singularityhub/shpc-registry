---
layout: container
name:  "quay.io/biocontainers/bioconductor-deltagseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deltagseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deltagseg/container.yaml"
updated_at: "2024-06-27 03:39:56.123726"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deltagseg"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.37.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-deltagseg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deltagseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deltagseg", "latest": {"1.42.0--r43hdfd78af_0": "sha256:121c22178cd89f3d72879b0ac5de9020097ddcaab3ec6a222d2b62e3a72abd45"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:278985f76cba1478a7e382e213edf950a907ed9daa699f7699d7cf845000e15a", "1.37.0--r42hdfd78af_0": "sha256:a55fd98ccabea6de5affae9a581356e70a28ee52826a86417e1fe0e281db6f3a", "1.40.0--r43hdfd78af_0": "sha256:a4bfb38e6b40ae83cbe7c44a17eac8831176e8eb9b8507019b98a1c0bcb0d49e", "1.42.0--r43hdfd78af_0": "sha256:121c22178cd89f3d72879b0ac5de9020097ddcaab3ec6a222d2b62e3a72abd45"}, "docker": "quay.io/biocontainers/bioconductor-deltagseg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deltagseg.
shpc-registry automated BioContainers addition for bioconductor-deltagseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deltagseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deltagseg:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deltagseg/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deltagseg/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deltagseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deltagseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deltagseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deltagseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deltagseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deltagseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deltagseg

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