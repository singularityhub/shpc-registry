---
layout: container
name:  "quay.io/biocontainers/binspreader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/binspreader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/binspreader/container.yaml"
updated_at: "2023-10-31 02:38:55.472250"
latest: "3.16.0.dev--h95f258a_0"
container_url: "https://biocontainers.pro/tools/binspreader"
aliases:
 - "bin-refine"
versions:
 - "3.16.0.dev--h95f258a_0"
description: "singularity registry hpc automated addition for binspreader"
config: {"url": "https://biocontainers.pro/tools/binspreader", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for binspreader", "latest": {"3.16.0.dev--h95f258a_0": "sha256:2183bcd1b6c29d72852914c279ede71aa389f5809348f52949153e155bf76cde"}, "tags": {"3.16.0.dev--h95f258a_0": "sha256:2183bcd1b6c29d72852914c279ede71aa389f5809348f52949153e155bf76cde"}, "docker": "quay.io/biocontainers/binspreader", "aliases": {"bin-refine": "/usr/local/bin/bin-refine"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/binspreader.
singularity registry hpc automated addition for binspreader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/binspreader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/binspreader:3.16.0.dev--h95f258a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/binspreader/3.16.0.dev--h95f258a_0
$ module help quay.io/biocontainers/binspreader/3.16.0.dev--h95f258a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### binspreader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### binspreader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### binspreader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### binspreader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### binspreader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### binspreader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bin-refine

```bash
$ singularity exec <container> /usr/local/bin/bin-refine
$ podman run --it --rm --entrypoint /usr/local/bin/bin-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bin-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
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