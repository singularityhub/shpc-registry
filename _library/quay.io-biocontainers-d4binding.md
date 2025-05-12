---
layout: container
name:  "quay.io/biocontainers/d4binding"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/d4binding/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/d4binding/container.yaml"
updated_at: "2025-05-12 03:36:46.871421"
latest: "0.3.11--h503566f_2"
container_url: "https://biocontainers.pro/tools/d4binding"
aliases:
 - "starcode"
versions:
 - "0.3.4--h87f3376_0"
 - "0.3.11--hdbdd923_0"
 - "0.3.11--hdbdd923_1"
 - "0.3.11--h503566f_2"
description: "singularity registry hpc automated addition for d4binding"
config: {"url": "https://biocontainers.pro/tools/d4binding", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for d4binding", "latest": {"0.3.11--h503566f_2": "sha256:fac99582e1e585b2ba47b5b4270f6221176443dbe00f12ee02388805ecde7929"}, "tags": {"0.3.4--h87f3376_0": "sha256:5f55a16b97075b91f86c54ff4dd7fe11324af217880775ab1ee53433517657bb", "0.3.11--hdbdd923_0": "sha256:02616373b3a95aa54e0cc9290ffa351de52f314a6c52f3a5dd6dbf203a631fad", "0.3.11--hdbdd923_1": "sha256:609f9a78941e48399cc237c35cecb9dd33f80a051e7e2c8f0cb6b217618a325d", "0.3.11--h503566f_2": "sha256:fac99582e1e585b2ba47b5b4270f6221176443dbe00f12ee02388805ecde7929"}, "docker": "quay.io/biocontainers/d4binding", "aliases": {"starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/d4binding.
singularity registry hpc automated addition for d4binding
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/d4binding
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/d4binding:0.3.11--h503566f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/d4binding/0.3.11--h503566f_2
$ module help quay.io/biocontainers/d4binding/0.3.11--h503566f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### d4binding-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### d4binding-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### d4binding-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### d4binding-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### d4binding-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### d4binding-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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