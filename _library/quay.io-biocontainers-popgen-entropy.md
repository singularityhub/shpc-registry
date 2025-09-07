---
layout: container
name:  "quay.io/biocontainers/popgen-entropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/popgen-entropy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/popgen-entropy/container.yaml"
updated_at: "2025-09-07 03:40:15.611103"
latest: "2.0--h1913c9f_11"
container_url: "https://biocontainers.pro/tools/popgen-entropy"
aliases:
 - "entropy"
 - "estpost.entropy"
 - "mirror_server"
 - "mirror_server_stop"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
versions:
 - "2.0--hc73b757_6"
 - "2.0--hc73b757_7"
 - "2.0--h0469059_8"
 - "2.0--h3009346_9"
 - "2.0--h0d220d2_10"
 - "2.0--h1913c9f_11"
description: "shpc-registry automated BioContainers addition for popgen-entropy"
config: {"url": "https://biocontainers.pro/tools/popgen-entropy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for popgen-entropy", "latest": {"2.0--h1913c9f_11": "sha256:e43832ac6aba9bb753786e50ea5e9f5e441fce5472d9e602431782df19cf01b1"}, "tags": {"2.0--hc73b757_6": "sha256:a33eabe9f3d808b95f540c19038eb00db7427490200a8bfc73517eb0da919bc2", "2.0--hc73b757_7": "sha256:f0e6eb5c76f55a7399fa9304d89ba8a39f1bc5c492abb76db3bdea0a9caa6b10", "2.0--h0469059_8": "sha256:d83e249b0e2356d0f90c865ba0d6199b979686a1bfba44234fb477554506b40e", "2.0--h3009346_9": "sha256:4e38a9ca9c3f684e4944c5c7c455f5141e8386525f06bc8c9710891e07d44ba8", "2.0--h0d220d2_10": "sha256:1284faf6dab026bcdf1f93e400af39152689a1b258d4ce52f85c325a39e433c4", "2.0--h1913c9f_11": "sha256:e43832ac6aba9bb753786e50ea5e9f5e441fce5472d9e602431782df19cf01b1"}, "docker": "quay.io/biocontainers/popgen-entropy", "aliases": {"entropy": "/usr/local/bin/entropy", "estpost.entropy": "/usr/local/bin/estpost.entropy", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/popgen-entropy.
shpc-registry automated BioContainers addition for popgen-entropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/popgen-entropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/popgen-entropy:2.0--h1913c9f_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/popgen-entropy/2.0--h1913c9f_11
$ module help quay.io/biocontainers/popgen-entropy/2.0--h1913c9f_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### popgen-entropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### popgen-entropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### popgen-entropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### popgen-entropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### popgen-entropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### popgen-entropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### entropy

```bash
$ singularity exec <container> /usr/local/bin/entropy
$ podman run --it --rm --entrypoint /usr/local/bin/entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estpost.entropy

```bash
$ singularity exec <container> /usr/local/bin/estpost.entropy
$ podman run --it --rm --entrypoint /usr/local/bin/estpost.entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estpost.entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
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