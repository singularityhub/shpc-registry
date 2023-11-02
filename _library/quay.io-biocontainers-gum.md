---
layout: container
name:  "quay.io/biocontainers/gum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gum/container.yaml"
updated_at: "2023-11-02 02:30:49.823167"
latest: "1.1.1--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/gum"

versions:
 - "1.1.1--hd03093a_0"
 - "1.1.1--hdcf5f25_2"
description: "singularity registry hpc automated addition for gum"
config: {"url": "https://biocontainers.pro/tools/gum", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gum", "latest": {"1.1.1--hdcf5f25_2": "sha256:8c24cec3d187e36ce655cd52fd4bf10eb7a71614d87a0ae054537693ded0c9db"}, "tags": {"1.1.1--hd03093a_0": "sha256:9273fc07278541221b5317a469bab11d54e0887c5f9506f0ba635adab2ff0e4b", "1.1.1--hdcf5f25_2": "sha256:8c24cec3d187e36ce655cd52fd4bf10eb7a71614d87a0ae054537693ded0c9db"}, "docker": "quay.io/biocontainers/gum"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gum.
singularity registry hpc automated addition for gum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gum:1.1.1--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gum/1.1.1--hdcf5f25_2
$ module help quay.io/biocontainers/gum/1.1.1--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gum

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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