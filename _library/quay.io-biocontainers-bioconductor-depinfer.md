---
layout: container
name:  "quay.io/biocontainers/bioconductor-depinfer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-depinfer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-depinfer/container.yaml"
updated_at: "2024-06-06 03:02:10.009947"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-depinfer"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-depinfer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-depinfer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-depinfer", "latest": {"1.6.0--r43hdfd78af_0": "sha256:90da36bfadf4e7e6dea15037d099cf058328f7a8765edbc2d3dc1104ada547dc"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:f17079d2fb3e663f9ef57d4a473f5d70b88979370817c401fc77e3f9a481a929", "1.4.0--r43hdfd78af_0": "sha256:39639d2fb1c983e4d84ddd380f3389a6fafa1e170a56f6d1c29a59f8cb64f97b", "1.6.0--r43hdfd78af_0": "sha256:90da36bfadf4e7e6dea15037d099cf058328f7a8765edbc2d3dc1104ada547dc"}, "docker": "quay.io/biocontainers/bioconductor-depinfer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-depinfer.
singularity registry hpc automated addition for bioconductor-depinfer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-depinfer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-depinfer:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-depinfer/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-depinfer/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-depinfer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-depinfer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-depinfer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-depinfer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-depinfer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-depinfer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-depinfer

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