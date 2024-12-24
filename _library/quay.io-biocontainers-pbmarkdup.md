---
layout: container
name:  "quay.io/biocontainers/pbmarkdup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbmarkdup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbmarkdup/container.yaml"
updated_at: "2024-12-24 03:29:13.657402"
latest: "1.1.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbmarkdup"
aliases:
 - "pbmarkdup"
versions:
 - "1.0.2--0"
 - "1.0.3--h9ee0642_0"
 - "1.1.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for pbmarkdup"
config: {"url": "https://biocontainers.pro/tools/pbmarkdup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbmarkdup", "latest": {"1.1.0--h9ee0642_0": "sha256:fe95bcac1e809b1230e8526a8feb8d5e6648113439309a68a6de0919c83a5a2d"}, "tags": {"1.0.2--0": "sha256:fa876b4e8673e6b5e77b9c9022d9a61d1796a5a02a29df21c4debc7afababece", "1.0.3--h9ee0642_0": "sha256:4d67bb1b30c687a5ff1318796c0a89cdc4fd5c8a092f4847c97863ed659addcd", "1.1.0--h9ee0642_0": "sha256:fe95bcac1e809b1230e8526a8feb8d5e6648113439309a68a6de0919c83a5a2d"}, "docker": "quay.io/biocontainers/pbmarkdup", "aliases": {"pbmarkdup": "/usr/local/bin/pbmarkdup"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbmarkdup.
shpc-registry automated BioContainers addition for pbmarkdup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbmarkdup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbmarkdup:1.1.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbmarkdup/1.1.0--h9ee0642_0
$ module help quay.io/biocontainers/pbmarkdup/1.1.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbmarkdup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbmarkdup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbmarkdup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbmarkdup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbmarkdup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbmarkdup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbmarkdup

```bash
$ singularity exec <container> /usr/local/bin/pbmarkdup
$ podman run --it --rm --entrypoint /usr/local/bin/pbmarkdup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmarkdup   -v ${PWD} -w ${PWD} <container> -c " $@"
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