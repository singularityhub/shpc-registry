---
layout: container
name:  "quay.io/biocontainers/fq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fq/container.yaml"
updated_at: "2023-10-12 03:04:43.267890"
latest: "0.11.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/fq"
aliases:
 - "fq"
versions:
 - "0.9.1--h9ee0642_0"
 - "0.10.0--h9ee0642_0"
 - "0.11.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for fq"
config: {"url": "https://biocontainers.pro/tools/fq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fq", "latest": {"0.11.0--h9ee0642_0": "sha256:27ed2cc8998659e3a4261d6484d7e173805936733d7a1a80fc00f871c62c2156"}, "tags": {"0.9.1--h9ee0642_0": "sha256:4018a43410a1c364043daca1acf792b1516bdc68c416bc7e73ce3395e770e913", "0.10.0--h9ee0642_0": "sha256:dd565b9463020d46207a68312310c2bcb62e367c69a3195f1c2a06acf72a0c92", "0.11.0--h9ee0642_0": "sha256:27ed2cc8998659e3a4261d6484d7e173805936733d7a1a80fc00f871c62c2156"}, "docker": "quay.io/biocontainers/fq", "aliases": {"fq": "/usr/local/bin/fq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fq.
shpc-registry automated BioContainers addition for fq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fq:0.11.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fq/0.11.0--h9ee0642_0
$ module help quay.io/biocontainers/fq/0.11.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fq

```bash
$ singularity exec <container> /usr/local/bin/fq
$ podman run --it --rm --entrypoint /usr/local/bin/fq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq   -v ${PWD} -w ${PWD} <container> -c " $@"
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