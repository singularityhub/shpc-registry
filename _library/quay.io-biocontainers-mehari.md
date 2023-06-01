---
layout: container
name:  "quay.io/biocontainers/mehari"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mehari/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mehari/container.yaml"
updated_at: "2023-06-01 03:33:06.237582"
latest: "0.3.1--h7e29777_2"
container_url: "https://biocontainers.pro/tools/mehari"
aliases:
 - "mehari"
versions:
 - "0.2.0--he55741f_0"
 - "0.3.1--h7e29777_2"
 - "0.2.1--he55741f_0"
description: "singularity registry hpc automated addition for mehari"
config: {"url": "https://biocontainers.pro/tools/mehari", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mehari", "latest": {"0.3.1--h7e29777_2": "sha256:5715d9dbb6b3ed8a7bf15092d79b01b7bd277e6ca7b0a835a39d80268135af52"}, "tags": {"0.2.0--he55741f_0": "sha256:3cc52cbadfa7f224506f03af8f2138629b65371f436c95a832445c0ce827d121", "0.3.1--h7e29777_2": "sha256:5715d9dbb6b3ed8a7bf15092d79b01b7bd277e6ca7b0a835a39d80268135af52", "0.2.1--he55741f_0": "sha256:6bc5bd19b9263d093ece69b3789c95ab44c6a4b6d7b7a180794e15f640a15719"}, "docker": "quay.io/biocontainers/mehari", "aliases": {"mehari": "/usr/local/bin/mehari"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mehari.
singularity registry hpc automated addition for mehari
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mehari
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mehari:0.3.1--h7e29777_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mehari/0.3.1--h7e29777_2
$ module help quay.io/biocontainers/mehari/0.3.1--h7e29777_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mehari-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mehari-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mehari-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mehari-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mehari-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mehari-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mehari

```bash
$ singularity exec <container> /usr/local/bin/mehari
$ podman run --it --rm --entrypoint /usr/local/bin/mehari   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mehari   -v ${PWD} -w ${PWD} <container> -c " $@"
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