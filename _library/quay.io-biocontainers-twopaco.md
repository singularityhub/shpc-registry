---
layout: container
name:  "quay.io/biocontainers/twopaco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/twopaco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/twopaco/container.yaml"
updated_at: "2024-12-13 03:47:54.626598"
latest: "1.0.0--hbb2dabb_2"
container_url: "https://biocontainers.pro/tools/twopaco"
aliases:
 - "graphdump"
 - "twopaco"
versions:
 - "1.0.0--h7bb7ee6_0"
 - "1.0.0--h7bb7ee6_1"
 - "1.0.0--hbb2dabb_2"
description: "shpc-registry automated BioContainers addition for twopaco"
config: {"url": "https://biocontainers.pro/tools/twopaco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for twopaco", "latest": {"1.0.0--hbb2dabb_2": "sha256:d76465c13320fd2941af4697d94c637982f40cb32901c17506e6171bb88214b3"}, "tags": {"1.0.0--h7bb7ee6_0": "sha256:4298066fa23a4a32f94d04a0d52bf4d43f22dfa79125828c3497b725953b2462", "1.0.0--h7bb7ee6_1": "sha256:f86ca8684971a699bd6f336f108b265a51af57f85810ae1df0a89b966213e5e9", "1.0.0--hbb2dabb_2": "sha256:d76465c13320fd2941af4697d94c637982f40cb32901c17506e6171bb88214b3"}, "docker": "quay.io/biocontainers/twopaco", "aliases": {"graphdump": "/usr/local/bin/graphdump", "twopaco": "/usr/local/bin/twopaco"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/twopaco.
shpc-registry automated BioContainers addition for twopaco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/twopaco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/twopaco:1.0.0--hbb2dabb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/twopaco/1.0.0--hbb2dabb_2
$ module help quay.io/biocontainers/twopaco/1.0.0--hbb2dabb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### twopaco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### twopaco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### twopaco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### twopaco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### twopaco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### twopaco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphdump

```bash
$ singularity exec <container> /usr/local/bin/graphdump
$ podman run --it --rm --entrypoint /usr/local/bin/graphdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twopaco

```bash
$ singularity exec <container> /usr/local/bin/twopaco
$ podman run --it --rm --entrypoint /usr/local/bin/twopaco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twopaco   -v ${PWD} -w ${PWD} <container> -c " $@"
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