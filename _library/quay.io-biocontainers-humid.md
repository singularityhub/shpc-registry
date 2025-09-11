---
layout: container
name:  "quay.io/biocontainers/humid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/humid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/humid/container.yaml"
updated_at: "2025-09-11 05:10:04.006906"
latest: "1.0.4--heae3180_2"
container_url: "https://biocontainers.pro/tools/humid"
aliases:
 - "humid"
 - "igzip"
versions:
 - "1.0.2--h5f740d0_0"
 - "1.0.2--hadf994f_2"
 - "1.0.4--hadf994f_0"
 - "1.0.4--h125f33a_1"
 - "1.0.4--heae3180_2"
description: "singularity registry hpc automated addition for humid"
config: {"url": "https://biocontainers.pro/tools/humid", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for humid", "latest": {"1.0.4--heae3180_2": "sha256:f875e6d2738e9b1a022a0ee8a48b904d6d81046a52e4367209bb5b51b35d70bf"}, "tags": {"1.0.2--h5f740d0_0": "sha256:92ffab70af8abdad85fde89082996a41034d2fc84d9411737874feee0dc56607", "1.0.2--hadf994f_2": "sha256:7697ee0e41ad92d29020a12752e9eb7d309be4ca4cbbeed7ca6361379ebc8ef9", "1.0.4--hadf994f_0": "sha256:dc4ab3d1826aa5d3c8573a8a25feb638c8091cd310a8b593648743de54828b94", "1.0.4--h125f33a_1": "sha256:54d52a6ca89dba057759034c3d78c00d4ee30f04dee0d687ae3c1088bd350095", "1.0.4--heae3180_2": "sha256:f875e6d2738e9b1a022a0ee8a48b904d6d81046a52e4367209bb5b51b35d70bf"}, "docker": "quay.io/biocontainers/humid", "aliases": {"humid": "/usr/local/bin/humid", "igzip": "/usr/local/bin/igzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/humid.
singularity registry hpc automated addition for humid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/humid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/humid:1.0.4--heae3180_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/humid/1.0.4--heae3180_2
$ module help quay.io/biocontainers/humid/1.0.4--heae3180_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### humid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### humid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### humid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### humid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### humid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### humid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### humid

```bash
$ singularity exec <container> /usr/local/bin/humid
$ podman run --it --rm --entrypoint /usr/local/bin/humid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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