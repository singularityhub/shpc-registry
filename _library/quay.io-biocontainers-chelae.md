---
layout: container
name:  "quay.io/biocontainers/chelae"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chelae/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chelae/container.yaml"
updated_at: "2026-06-05 07:18:12.969086"
latest: "0.1.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/chelae"
aliases:
 - "chelae"
versions:
 - "0.1.0--hfa8f182_0"
description: "singularity registry hpc automated addition for chelae"
config: {"url": "https://biocontainers.pro/tools/chelae", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chelae", "latest": {"0.1.0--hfa8f182_0": "sha256:1405eaab8ee7882c08143485af6d337d7feb6ea9dc2041c22d955e04921e255e"}, "tags": {"0.1.0--hfa8f182_0": "sha256:1405eaab8ee7882c08143485af6d337d7feb6ea9dc2041c22d955e04921e255e"}, "docker": "quay.io/biocontainers/chelae", "aliases": {"chelae": "/usr/local/bin/chelae"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chelae.
singularity registry hpc automated addition for chelae
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chelae
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chelae:0.1.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chelae/0.1.0--hfa8f182_0
$ module help quay.io/biocontainers/chelae/0.1.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chelae-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chelae-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chelae-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chelae-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chelae-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chelae-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chelae

```bash
$ singularity exec <container> /usr/local/bin/chelae
$ podman run --it --rm --entrypoint /usr/local/bin/chelae   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chelae   -v ${PWD} -w ${PWD} <container> -c " $@"
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