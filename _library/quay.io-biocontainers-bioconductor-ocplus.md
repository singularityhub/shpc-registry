---
layout: container
name:  "quay.io/biocontainers/bioconductor-ocplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ocplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ocplus/container.yaml"
updated_at: "2025-03-12 03:25:30.960113"
latest: "1.80.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ocplus"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.80.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ocplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ocplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ocplus", "latest": {"1.80.0--r44hdfd78af_0": "sha256:d5a1d609fb596f45b4e8d39b7d8173c70272fcbc225e13657823b2d6d011129a"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:4bded9f427e95d51c563651210c79304bc9ccd6e5f3da3615e27c01b9257913f", "1.72.0--r42hdfd78af_0": "sha256:743db89bcfa46b591857ba0a43272c8bc38842f2ecc021ec19d218ded2aa7ddd", "1.74.0--r43hdfd78af_0": "sha256:1a3f36bc4926adca2e6a9b2a479806d7022e1524dc2e51ac13cd95664a047054", "1.76.0--r43hdfd78af_0": "sha256:3cc7e019654f657f622f1f8482dd7c18374dd2869b6dace81e16efc6c3270034", "1.80.0--r44hdfd78af_0": "sha256:d5a1d609fb596f45b4e8d39b7d8173c70272fcbc225e13657823b2d6d011129a"}, "docker": "quay.io/biocontainers/bioconductor-ocplus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ocplus.
shpc-registry automated BioContainers addition for bioconductor-ocplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ocplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ocplus:1.80.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ocplus/1.80.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ocplus/1.80.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ocplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ocplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ocplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ocplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ocplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ocplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ocplus

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