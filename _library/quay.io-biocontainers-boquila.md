---
layout: container
name:  "quay.io/biocontainers/boquila"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/boquila/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/boquila/container.yaml"
updated_at: "2024-10-01 03:11:42.721219"
latest: "0.6.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/boquila"
aliases:
 - "boquila"
versions:
 - "0.6.0--hdfd78af_0"
 - "0.6.1--hdfd78af_0"
description: "singularity registry hpc automated addition for boquila"
config: {"url": "https://biocontainers.pro/tools/boquila", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for boquila", "latest": {"0.6.1--hdfd78af_0": "sha256:47b2696d859a14c70d1a4351a0281710ddcb80c73abc65f9bd4b060f8ee7b6f6"}, "tags": {"0.6.0--hdfd78af_0": "sha256:87eccf9ce054cbd981f39f47a6e738cfef526a4294ca7c41487a723e7a9a3337", "0.6.1--hdfd78af_0": "sha256:47b2696d859a14c70d1a4351a0281710ddcb80c73abc65f9bd4b060f8ee7b6f6"}, "docker": "quay.io/biocontainers/boquila", "aliases": {"boquila": "/usr/local/bin/boquila"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/boquila.
singularity registry hpc automated addition for boquila
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/boquila
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/boquila:0.6.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/boquila/0.6.1--hdfd78af_0
$ module help quay.io/biocontainers/boquila/0.6.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### boquila-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### boquila-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### boquila-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### boquila-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### boquila-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### boquila-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### boquila

```bash
$ singularity exec <container> /usr/local/bin/boquila
$ podman run --it --rm --entrypoint /usr/local/bin/boquila   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boquila   -v ${PWD} -w ${PWD} <container> -c " $@"
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