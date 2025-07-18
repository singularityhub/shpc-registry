---
layout: container
name:  "quay.io/biocontainers/lighter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lighter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lighter/container.yaml"
updated_at: "2025-07-18 10:35:36.124848"
latest: "1.1.3--h077b44d_2"
container_url: "https://biocontainers.pro/tools/lighter"
aliases:
 - "lighter"
versions:
 - "1.1.2--hd03093a_4"
 - "1.1.2--hdcf5f25_6"
 - "1.1.3--hdcf5f25_0"
 - "1.1.3--hdcf5f25_1"
 - "1.1.3--h077b44d_2"
description: "shpc-registry automated BioContainers addition for lighter"
config: {"url": "https://biocontainers.pro/tools/lighter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lighter", "latest": {"1.1.3--h077b44d_2": "sha256:e67bca8c85df6c27d9887afdb3e0a5bd45503fc492097f44ced9c53a6e5abdae"}, "tags": {"1.1.2--hd03093a_4": "sha256:79f4681de7ebb56f2fcf8f9152f24f5fb7554099a47c9c158abd5db306b7c57d", "1.1.2--hdcf5f25_6": "sha256:a637ddc32d1a2d7efe6d9db6a78c9cb1921b62474ef77e8949b3dc009a803f2f", "1.1.3--hdcf5f25_0": "sha256:6882a9510ed30be461756eb58af687379b81f3d08d5f81e23d9bdeb76ffbb3ba", "1.1.3--hdcf5f25_1": "sha256:99136c2d9e9dab03aeb076babbff1948252be4cdd03d0824f39b477a1d165aa3", "1.1.3--h077b44d_2": "sha256:e67bca8c85df6c27d9887afdb3e0a5bd45503fc492097f44ced9c53a6e5abdae"}, "docker": "quay.io/biocontainers/lighter", "aliases": {"lighter": "/usr/local/bin/lighter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lighter.
shpc-registry automated BioContainers addition for lighter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lighter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lighter:1.1.3--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lighter/1.1.3--h077b44d_2
$ module help quay.io/biocontainers/lighter/1.1.3--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lighter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lighter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lighter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lighter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lighter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lighter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lighter

```bash
$ singularity exec <container> /usr/local/bin/lighter
$ podman run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
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