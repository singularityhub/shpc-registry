---
layout: container
name:  "quay.io/biocontainers/hicstuff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hicstuff/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hicstuff/container.yaml"
updated_at: "2022-10-27 00:33:56.216930"
latest: "3.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hicstuff"
aliases:
 - "hicstuff"
versions:
 - "3.1.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for hicstuff"
config: {"url": "https://biocontainers.pro/tools/hicstuff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hicstuff", "latest": {"3.1.5--pyhdfd78af_0": "sha256:fed76d89a1c0460bbb9066c99383e14e67068f89a908879e2cc9bd6fb955c9d9"}, "tags": {"3.1.5--pyhdfd78af_0": "sha256:fed76d89a1c0460bbb9066c99383e14e67068f89a908879e2cc9bd6fb955c9d9"}, "docker": "quay.io/biocontainers/hicstuff", "aliases": {"hicstuff": "/usr/local/bin/hicstuff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hicstuff.
shpc-registry automated BioContainers addition for hicstuff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hicstuff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hicstuff:3.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hicstuff/3.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/hicstuff/3.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hicstuff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hicstuff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hicstuff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hicstuff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hicstuff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hicstuff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hicstuff

```bash
$ singularity exec <container> /usr/local/bin/hicstuff
$ podman run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
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