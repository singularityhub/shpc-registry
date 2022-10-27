---
layout: container
name:  "quay.io/biocontainers/blockclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blockclust/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/blockclust/container.yaml"
updated_at: "2022-10-27 01:05:22.874532"
latest: "1.1.0--py36r41h2ad2d48_7"
container_url: "https://biocontainers.pro/tools/blockclust"
aliases:
 - ".blockclust-post-link.sh"
 - ".blockclust-pre-unlink.sh"
 - "EDeN"
 - "blockclust"
 - "blockclust.py"
 - "blockclust_plot.r"
versions:
 - "1.1.0--py36r41h2ad2d48_7"
description: "shpc-registry automated BioContainers addition for blockclust"
config: {"url": "https://biocontainers.pro/tools/blockclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blockclust", "latest": {"1.1.0--py36r41h2ad2d48_7": "sha256:2216d30f270c5e8df9ff3e8d17f2581e5814e69ce1039033c46411093f67e7e4"}, "tags": {"1.1.0--py36r41h2ad2d48_7": "sha256:2216d30f270c5e8df9ff3e8d17f2581e5814e69ce1039033c46411093f67e7e4"}, "docker": "quay.io/biocontainers/blockclust", "aliases": {".blockclust-post-link.sh": "/usr/local/bin/.blockclust-post-link.sh", ".blockclust-pre-unlink.sh": "/usr/local/bin/.blockclust-pre-unlink.sh", "EDeN": "/usr/local/bin/EDeN", "blockclust": "/usr/local/bin/blockclust", "blockclust.py": "/usr/local/bin/blockclust.py", "blockclust_plot.r": "/usr/local/bin/blockclust_plot.r"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blockclust.
shpc-registry automated BioContainers addition for blockclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blockclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blockclust:1.1.0--py36r41h2ad2d48_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blockclust/1.1.0--py36r41h2ad2d48_7
$ module help quay.io/biocontainers/blockclust/1.1.0--py36r41h2ad2d48_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blockclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blockclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blockclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blockclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blockclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blockclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .blockclust-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.blockclust-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.blockclust-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.blockclust-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .blockclust-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.blockclust-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.blockclust-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.blockclust-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EDeN

```bash
$ singularity exec <container> /usr/local/bin/EDeN
$ podman run --it --rm --entrypoint /usr/local/bin/EDeN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EDeN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust

```bash
$ singularity exec <container> /usr/local/bin/blockclust
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust.py

```bash
$ singularity exec <container> /usr/local/bin/blockclust.py
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust_plot.r

```bash
$ singularity exec <container> /usr/local/bin/blockclust_plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
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