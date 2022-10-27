---
layout: container
name:  "quay.io/biocontainers/rkp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rkp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rkp/container.yaml"
updated_at: "2022-10-27 01:09:43.885038"
latest: "0.1.0--py_0"
container_url: "https://biocontainers.pro/tools/rkp"
aliases:
 - "RKP.py"
 - "create_kmers.sh"
 - "heatmap.R"
 - "map_kmers.sh"
versions:
 - "0.1.0--py_0"
description: "shpc-registry automated BioContainers addition for rkp"
config: {"url": "https://biocontainers.pro/tools/rkp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rkp", "latest": {"0.1.0--py_0": "sha256:97620022a7ee1bfe1a1b474e21918dbdeb7ce19daca52e1bcfc2ed5428fb305f"}, "tags": {"0.1.0--py_0": "sha256:97620022a7ee1bfe1a1b474e21918dbdeb7ce19daca52e1bcfc2ed5428fb305f"}, "docker": "quay.io/biocontainers/rkp", "aliases": {"RKP.py": "/usr/local/bin/RKP.py", "create_kmers.sh": "/usr/local/bin/create_kmers.sh", "heatmap.R": "/usr/local/bin/heatmap.R", "map_kmers.sh": "/usr/local/bin/map_kmers.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rkp.
shpc-registry automated BioContainers addition for rkp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rkp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rkp:0.1.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rkp/0.1.0--py_0
$ module help quay.io/biocontainers/rkp/0.1.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rkp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rkp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rkp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rkp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rkp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rkp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RKP.py

```bash
$ singularity exec <container> /usr/local/bin/RKP.py
$ podman run --it --rm --entrypoint /usr/local/bin/RKP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RKP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_kmers.sh

```bash
$ singularity exec <container> /usr/local/bin/create_kmers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_kmers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_kmers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heatmap.R

```bash
$ singularity exec <container> /usr/local/bin/heatmap.R
$ podman run --it --rm --entrypoint /usr/local/bin/heatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_kmers.sh

```bash
$ singularity exec <container> /usr/local/bin/map_kmers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/map_kmers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_kmers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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