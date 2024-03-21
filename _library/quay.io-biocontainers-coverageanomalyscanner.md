---
layout: container
name:  "quay.io/biocontainers/coverageanomalyscanner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coverageanomalyscanner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/coverageanomalyscanner/container.yaml"
updated_at: "2024-03-21 04:16:58.090181"
latest: "0.2.3--h77de753_2"
container_url: "https://biocontainers.pro/tools/coverageanomalyscanner"
aliases:
 - "cas"
versions:
 - "0.2.3--h47defd3_0"
 - "0.2.3--h77de753_2"
description: "singularity registry hpc automated addition for coverageanomalyscanner"
config: {"url": "https://biocontainers.pro/tools/coverageanomalyscanner", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for coverageanomalyscanner", "latest": {"0.2.3--h77de753_2": "sha256:738f6f8e29272f6371bda95c32d6eaf647ccee4d232aebf8669c24b142573b1e"}, "tags": {"0.2.3--h47defd3_0": "sha256:ac94da7cb2b85d9ae9c8f2e115631cc986a79f660510a796545e793e50c2db29", "0.2.3--h77de753_2": "sha256:738f6f8e29272f6371bda95c32d6eaf647ccee4d232aebf8669c24b142573b1e"}, "docker": "quay.io/biocontainers/coverageanomalyscanner", "aliases": {"cas": "/usr/local/bin/cas"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coverageanomalyscanner.
singularity registry hpc automated addition for coverageanomalyscanner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coverageanomalyscanner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coverageanomalyscanner:0.2.3--h77de753_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coverageanomalyscanner/0.2.3--h77de753_2
$ module help quay.io/biocontainers/coverageanomalyscanner/0.2.3--h77de753_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coverageanomalyscanner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coverageanomalyscanner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coverageanomalyscanner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coverageanomalyscanner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coverageanomalyscanner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coverageanomalyscanner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cas

```bash
$ singularity exec <container> /usr/local/bin/cas
$ podman run --it --rm --entrypoint /usr/local/bin/cas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cas   -v ${PWD} -w ${PWD} <container> -c " $@"
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