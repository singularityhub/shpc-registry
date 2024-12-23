---
layout: container
name:  "quay.io/biocontainers/bioconductor-ramr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ramr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ramr/container.yaml"
updated_at: "2024-12-23 02:59:58.022094"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ramr"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ramr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ramr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ramr", "latest": {"1.10.0--r43hdfd78af_0": "sha256:11027bb14db878855ecc26b300499d443ed94f411006fda3764ea4999d41e42e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:5101cb7045e88a3324ba6c50d2b88356c2d6c59dbff14a54eece728396e812c2", "1.6.0--r42hdfd78af_0": "sha256:78c5500b4734768e324c29e4925e8a93b72fe6b6c9559489353387f3b662db98", "1.8.0--r43hdfd78af_0": "sha256:8a63c0e48d081fa65c69c0342b6a5271ef64cb9c4e7b3545a657cda1034cbedb", "1.10.0--r43hdfd78af_0": "sha256:11027bb14db878855ecc26b300499d443ed94f411006fda3764ea4999d41e42e"}, "docker": "quay.io/biocontainers/bioconductor-ramr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ramr.
shpc-registry automated BioContainers addition for bioconductor-ramr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ramr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ramr:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ramr/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ramr/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ramr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ramr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ramr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ramr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ramr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ramr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ramr

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