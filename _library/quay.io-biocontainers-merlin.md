---
layout: container
name:  "quay.io/biocontainers/merlin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/merlin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/merlin/container.yaml"
updated_at: "2023-06-02 03:12:15.218563"
latest: "1.1.2--hdcf5f25_7"
container_url: "https://biocontainers.pro/tools/merlin"
aliases:
 - "hapmapConverter"
 - "merlin"
 - "merlin-offline"
 - "merlin-regress"
 - "minx"
 - "minx-offline"
 - "pedmerge"
 - "pedstats"
 - "pedwipe"
versions:
 - "1.1.2--hd03093a_5"
 - "1.1.2--hdcf5f25_7"
description: "shpc-registry automated BioContainers addition for merlin"
config: {"url": "https://biocontainers.pro/tools/merlin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for merlin", "latest": {"1.1.2--hdcf5f25_7": "sha256:06a26eb9409dd01b91716025548cbac7d0b46be655aa01a066949bd40b464dec"}, "tags": {"1.1.2--hd03093a_5": "sha256:144620fb3de22d03342ec56cdf86770c4365da5f66b426e804b1ae343460c380", "1.1.2--hdcf5f25_7": "sha256:06a26eb9409dd01b91716025548cbac7d0b46be655aa01a066949bd40b464dec"}, "docker": "quay.io/biocontainers/merlin", "aliases": {"hapmapConverter": "/usr/local/bin/hapmapConverter", "merlin": "/usr/local/bin/merlin", "merlin-offline": "/usr/local/bin/merlin-offline", "merlin-regress": "/usr/local/bin/merlin-regress", "minx": "/usr/local/bin/minx", "minx-offline": "/usr/local/bin/minx-offline", "pedmerge": "/usr/local/bin/pedmerge", "pedstats": "/usr/local/bin/pedstats", "pedwipe": "/usr/local/bin/pedwipe"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/merlin.
shpc-registry automated BioContainers addition for merlin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/merlin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/merlin:1.1.2--hdcf5f25_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/merlin/1.1.2--hdcf5f25_7
$ module help quay.io/biocontainers/merlin/1.1.2--hdcf5f25_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### merlin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### merlin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### merlin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### merlin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### merlin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### merlin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hapmapConverter

```bash
$ singularity exec <container> /usr/local/bin/hapmapConverter
$ podman run --it --rm --entrypoint /usr/local/bin/hapmapConverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapmapConverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin

```bash
$ singularity exec <container> /usr/local/bin/merlin
$ podman run --it --rm --entrypoint /usr/local/bin/merlin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin-offline

```bash
$ singularity exec <container> /usr/local/bin/merlin-offline
$ podman run --it --rm --entrypoint /usr/local/bin/merlin-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin-regress

```bash
$ singularity exec <container> /usr/local/bin/merlin-regress
$ podman run --it --rm --entrypoint /usr/local/bin/merlin-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minx

```bash
$ singularity exec <container> /usr/local/bin/minx
$ podman run --it --rm --entrypoint /usr/local/bin/minx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minx-offline

```bash
$ singularity exec <container> /usr/local/bin/minx-offline
$ podman run --it --rm --entrypoint /usr/local/bin/minx-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minx-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedmerge

```bash
$ singularity exec <container> /usr/local/bin/pedmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pedmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedstats

```bash
$ singularity exec <container> /usr/local/bin/pedstats
$ podman run --it --rm --entrypoint /usr/local/bin/pedstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedwipe

```bash
$ singularity exec <container> /usr/local/bin/pedwipe
$ podman run --it --rm --entrypoint /usr/local/bin/pedwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
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