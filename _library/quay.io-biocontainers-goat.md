---
layout: container
name:  "quay.io/biocontainers/goat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/goat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/goat/container.yaml"
updated_at: "2024-07-22 03:39:05.515565"
latest: "0.2.5--h9d3141d_2"
container_url: "https://biocontainers.pro/tools/goat"
aliases:
 - "goat-cli"
versions:
 - "0.2.0--h92d785c_0"
 - "0.2.5--h92d785c_0"
 - "0.2.5--h9d3141d_2"
description: "shpc-registry automated BioContainers addition for goat"
config: {"url": "https://biocontainers.pro/tools/goat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for goat", "latest": {"0.2.5--h9d3141d_2": "sha256:6f0470a092a28424edcb2a3fd3d2dcc963f94e768c9f466f1b4c6f546cc260d5"}, "tags": {"0.2.0--h92d785c_0": "sha256:b8b9f6fb938aabf6ff97e9f78334fe19da86c65ea2de6054c98bab12f07dc1d6", "0.2.5--h92d785c_0": "sha256:c2328cf080c4bb54a0fc848617c13f131006cad9303d81f82b88aaa655b1e3fd", "0.2.5--h9d3141d_2": "sha256:6f0470a092a28424edcb2a3fd3d2dcc963f94e768c9f466f1b4c6f546cc260d5"}, "docker": "quay.io/biocontainers/goat", "aliases": {"goat-cli": "/usr/local/bin/goat-cli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/goat.
shpc-registry automated BioContainers addition for goat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/goat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/goat:0.2.5--h9d3141d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/goat/0.2.5--h9d3141d_2
$ module help quay.io/biocontainers/goat/0.2.5--h9d3141d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### goat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### goat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### goat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### goat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### goat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### goat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### goat-cli

```bash
$ singularity exec <container> /usr/local/bin/goat-cli
$ podman run --it --rm --entrypoint /usr/local/bin/goat-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/goat-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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