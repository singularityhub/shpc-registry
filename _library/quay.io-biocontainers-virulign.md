---
layout: container
name:  "quay.io/biocontainers/virulign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/virulign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/virulign/container.yaml"
updated_at: "2026-01-22 04:11:40.493164"
latest: "1.1.1--hf316886_6"
container_url: "https://biocontainers.pro/tools/virulign"
aliases:
 - "virulign"
versions:
 - "1.1.1--h9f5acd7_2"
 - "1.1.1--h4ac6f70_4"
 - "1.1.1--h9948957_5"
 - "1.1.1--hf316886_6"
description: "shpc-registry automated BioContainers addition for virulign"
config: {"url": "https://biocontainers.pro/tools/virulign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for virulign", "latest": {"1.1.1--hf316886_6": "sha256:cef0e602787b373fcba2dd95edbbd7ea1b6ab127b5e53d3ee751c4ad1c1d4d68"}, "tags": {"1.1.1--h9f5acd7_2": "sha256:d0d85a3485f228fb3fac5c0ca8e1e9d7a2238a50eaffdfeada3ffab43bd1175f", "1.1.1--h4ac6f70_4": "sha256:8a0e7fa3d92a3b24a7583148afab7da8008d07329fab4d021fc2a52bca7f65cd", "1.1.1--h9948957_5": "sha256:542307408754af8a11a4c3646b955bc262cb3ee1e2f8e3591e0b5d4864293da3", "1.1.1--hf316886_6": "sha256:cef0e602787b373fcba2dd95edbbd7ea1b6ab127b5e53d3ee751c4ad1c1d4d68"}, "docker": "quay.io/biocontainers/virulign", "aliases": {"virulign": "/usr/local/bin/virulign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/virulign.
shpc-registry automated BioContainers addition for virulign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/virulign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/virulign:1.1.1--hf316886_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/virulign/1.1.1--hf316886_6
$ module help quay.io/biocontainers/virulign/1.1.1--hf316886_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### virulign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### virulign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### virulign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### virulign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### virulign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### virulign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### virulign

```bash
$ singularity exec <container> /usr/local/bin/virulign
$ podman run --it --rm --entrypoint /usr/local/bin/virulign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virulign   -v ${PWD} -w ${PWD} <container> -c " $@"
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