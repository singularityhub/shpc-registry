---
layout: container
name:  "quay.io/biocontainers/mentalist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mentalist/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mentalist/container.yaml"
updated_at: "2022-10-27 00:39:20.227640"
latest: "0.2.4--hec16e2b_5"
container_url: "https://biocontainers.pro/tools/mentalist"
aliases:
 - ".julia-post-link.sh"
 - ".julia-pre-unlink.sh"
 - "MentaLiST.jl"
 - "build_db_functions.jl"
 - "calling_functions.jl"
 - "db_graph.jl"
 - "julia"
 - "julia-debug"
 - "mentalist"
 - "mlst_download_functions.jl"
versions:
 - "0.2.4--hec16e2b_5"
description: "shpc-registry automated BioContainers addition for mentalist"
config: {"url": "https://biocontainers.pro/tools/mentalist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mentalist", "latest": {"0.2.4--hec16e2b_5": "sha256:fb531110f12b434acb5b77e6a504338403892e5a56e0b8bd814ada30cd2d8009"}, "tags": {"0.2.4--hec16e2b_5": "sha256:fb531110f12b434acb5b77e6a504338403892e5a56e0b8bd814ada30cd2d8009"}, "docker": "quay.io/biocontainers/mentalist", "aliases": {".julia-post-link.sh": "/usr/local/bin/.julia-post-link.sh", ".julia-pre-unlink.sh": "/usr/local/bin/.julia-pre-unlink.sh", "MentaLiST.jl": "/usr/local/bin/MentaLiST.jl", "build_db_functions.jl": "/usr/local/bin/build_db_functions.jl", "calling_functions.jl": "/usr/local/bin/calling_functions.jl", "db_graph.jl": "/usr/local/bin/db_graph.jl", "julia": "/usr/local/bin/julia", "julia-debug": "/usr/local/bin/julia-debug", "mentalist": "/usr/local/bin/mentalist", "mlst_download_functions.jl": "/usr/local/bin/mlst_download_functions.jl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mentalist.
shpc-registry automated BioContainers addition for mentalist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mentalist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mentalist:0.2.4--hec16e2b_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mentalist/0.2.4--hec16e2b_5
$ module help quay.io/biocontainers/mentalist/0.2.4--hec16e2b_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mentalist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mentalist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mentalist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mentalist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mentalist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mentalist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .julia-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.julia-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.julia-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.julia-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .julia-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.julia-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.julia-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.julia-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MentaLiST.jl

```bash
$ singularity exec <container> /usr/local/bin/MentaLiST.jl
$ podman run --it --rm --entrypoint /usr/local/bin/MentaLiST.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MentaLiST.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_db_functions.jl

```bash
$ singularity exec <container> /usr/local/bin/build_db_functions.jl
$ podman run --it --rm --entrypoint /usr/local/bin/build_db_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_db_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calling_functions.jl

```bash
$ singularity exec <container> /usr/local/bin/calling_functions.jl
$ podman run --it --rm --entrypoint /usr/local/bin/calling_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calling_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_graph.jl

```bash
$ singularity exec <container> /usr/local/bin/db_graph.jl
$ podman run --it --rm --entrypoint /usr/local/bin/db_graph.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_graph.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### julia

```bash
$ singularity exec <container> /usr/local/bin/julia
$ podman run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### julia-debug

```bash
$ singularity exec <container> /usr/local/bin/julia-debug
$ podman run --it --rm --entrypoint /usr/local/bin/julia-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/julia-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mentalist

```bash
$ singularity exec <container> /usr/local/bin/mentalist
$ podman run --it --rm --entrypoint /usr/local/bin/mentalist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mentalist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst_download_functions.jl

```bash
$ singularity exec <container> /usr/local/bin/mlst_download_functions.jl
$ podman run --it --rm --entrypoint /usr/local/bin/mlst_download_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst_download_functions.jl   -v ${PWD} -w ${PWD} <container> -c " $@"
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