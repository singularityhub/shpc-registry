---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigspack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigspack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigspack/container.yaml"
updated_at: "2024-06-08 03:04:58.487856"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sigspack"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sigspack"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigspack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigspack", "latest": {"1.16.0--r43hdfd78af_0": "sha256:d85e8ea2d8c9f0a121ec44232761e69e8c4c276b24b89da71aa1bd3d2cf0626e"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a8515295fbbeea66477bd8848881454890a5eb3ef54ba1cd38bce1f79433985c", "1.12.0--r42hdfd78af_0": "sha256:077a8ebc39b7f3126d79ed67eda92a88573da3409c00a1bd7ed0a041bc98cae8", "1.14.0--r43hdfd78af_0": "sha256:4e8bfc06c7c0db387aff4f9c31670eab19ed7a8944688b2ab3832467923dcc6f", "1.16.0--r43hdfd78af_0": "sha256:d85e8ea2d8c9f0a121ec44232761e69e8c4c276b24b89da71aa1bd3d2cf0626e"}, "docker": "quay.io/biocontainers/bioconductor-sigspack"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigspack.
shpc-registry automated BioContainers addition for bioconductor-sigspack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigspack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigspack:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigspack/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sigspack/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigspack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigspack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigspack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigspack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigspack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigspack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sigspack

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