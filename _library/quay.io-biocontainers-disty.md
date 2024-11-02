---
layout: container
name:  "quay.io/biocontainers/disty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/disty/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/disty/container.yaml"
updated_at: "2024-11-02 03:28:15.469362"
latest: "0.1.0--hdcf5f25_7"
container_url: "https://biocontainers.pro/tools/disty"
aliases:
 - "disty"
versions:
 - "0.1.0--hd03093a_5"
 - "0.1.0--hdcf5f25_7"
description: "shpc-registry automated BioContainers addition for disty"
config: {"url": "https://biocontainers.pro/tools/disty", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for disty", "latest": {"0.1.0--hdcf5f25_7": "sha256:9d829648a3b8f76165a2a8dfb557c74d0cafba4f983b0c38a2ccda1daf6b5911"}, "tags": {"0.1.0--hd03093a_5": "sha256:db726204cfcd37a5789ea55421acfbe5c5b9ce2ecf4f53114fccf28d5973ce12", "0.1.0--hdcf5f25_7": "sha256:9d829648a3b8f76165a2a8dfb557c74d0cafba4f983b0c38a2ccda1daf6b5911"}, "docker": "quay.io/biocontainers/disty", "aliases": {"disty": "/usr/local/bin/disty"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/disty.
shpc-registry automated BioContainers addition for disty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/disty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/disty:0.1.0--hdcf5f25_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/disty/0.1.0--hdcf5f25_7
$ module help quay.io/biocontainers/disty/0.1.0--hdcf5f25_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### disty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### disty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### disty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### disty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### disty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### disty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### disty

```bash
$ singularity exec <container> /usr/local/bin/disty
$ podman run --it --rm --entrypoint /usr/local/bin/disty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disty   -v ${PWD} -w ${PWD} <container> -c " $@"
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