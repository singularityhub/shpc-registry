---
layout: container
name:  "quay.io/biocontainers/pgrc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgrc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgrc/container.yaml"
updated_at: "2025-01-10 03:24:54.245984"
latest: "2.0.2--h9948957_1"
container_url: "https://biocontainers.pro/tools/pgrc"
aliases:
 - "PgRC"
versions:
 - "2.0--h4ac6f70_0"
 - "2.0.1--h4ac6f70_0"
 - "2.0.2--h4ac6f70_0"
 - "2.0.2--h9948957_1"
description: "singularity registry hpc automated addition for pgrc"
config: {"url": "https://biocontainers.pro/tools/pgrc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pgrc", "latest": {"2.0.2--h9948957_1": "sha256:790ecc12a8f576c0c1cefe4f5915e27cfcec9cd75cfaf4b8d1b4bacfb9a12784"}, "tags": {"2.0--h4ac6f70_0": "sha256:c67075aed9bc8c15aeb8ba33025b262f82f27ab845f767321e790095a353f474", "2.0.1--h4ac6f70_0": "sha256:a224c2123eba84051132630e61bdff24208f250a63ece3ef43c56dbef9d85443", "2.0.2--h4ac6f70_0": "sha256:ca9712f13e433e996f55505b3dcf394ccf35fec99432a12915da1c0399c2a258", "2.0.2--h9948957_1": "sha256:790ecc12a8f576c0c1cefe4f5915e27cfcec9cd75cfaf4b8d1b4bacfb9a12784"}, "docker": "quay.io/biocontainers/pgrc", "aliases": {"PgRC": "/usr/local/bin/PgRC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgrc.
singularity registry hpc automated addition for pgrc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgrc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgrc:2.0.2--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgrc/2.0.2--h9948957_1
$ module help quay.io/biocontainers/pgrc/2.0.2--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgrc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgrc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgrc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgrc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgrc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgrc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PgRC

```bash
$ singularity exec <container> /usr/local/bin/PgRC
$ podman run --it --rm --entrypoint /usr/local/bin/PgRC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PgRC   -v ${PWD} -w ${PWD} <container> -c " $@"
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