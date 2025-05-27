---
layout: container
name:  "quay.io/biocontainers/shark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shark/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shark/container.yaml"
updated_at: "2025-05-27 23:00:45.606313"
latest: "1.2.0--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/shark"
aliases:
 - "shark"
versions:
 - "1.2.0--hd03093a_2"
 - "1.2.0--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for shark"
config: {"url": "https://biocontainers.pro/tools/shark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shark", "latest": {"1.2.0--hdcf5f25_4": "sha256:2e2cffdbd391479fc3e44898fe26136561cd3a4da976e4c4e4fc8c61d76ac063"}, "tags": {"1.2.0--hd03093a_2": "sha256:74328f24292a91afd091a19a0d1cb3e9582ee5f7e98bc2997606f81bb64493af", "1.2.0--hdcf5f25_4": "sha256:2e2cffdbd391479fc3e44898fe26136561cd3a4da976e4c4e4fc8c61d76ac063"}, "docker": "quay.io/biocontainers/shark", "aliases": {"shark": "/usr/local/bin/shark"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shark.
shpc-registry automated BioContainers addition for shark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shark:1.2.0--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shark/1.2.0--hdcf5f25_4
$ module help quay.io/biocontainers/shark/1.2.0--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shark

```bash
$ singularity exec <container> /usr/local/bin/shark
$ podman run --it --rm --entrypoint /usr/local/bin/shark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shark   -v ${PWD} -w ${PWD} <container> -c " $@"
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