---
layout: container
name:  "quay.io/biocontainers/kallisto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kallisto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kallisto/container.yaml"
updated_at: "2025-02-12 02:50:52.312671"
latest: "0.51.1--ha4fb952_1"
container_url: "https://biocontainers.pro/tools/kallisto"
aliases:
 - "kallisto"
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
 - "0.48.0--h15996b6_2"
 - "0.50.0--hc877fd6_0"
 - "0.50.1--hc877fd6_0"
 - "0.50.1--hc877fd6_1"
 - "0.50.1--h6de1650_2"
 - "0.51.0--h6de1650_0"
 - "0.51.1--heb0cbe2_0"
 - "0.51.1--ha4fb952_1"
description: "shpc-registry automated BioContainers addition for kallisto"
config: {"url": "https://biocontainers.pro/tools/kallisto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kallisto", "latest": {"0.51.1--ha4fb952_1": "sha256:f2dc85d6d55e1c3bfdc437a7738b1217d0f81ee9c1c62013b5dd3b867713d482"}, "tags": {"0.48.0--h15996b6_2": "sha256:e44c2964d20ee3fb46488f77752e904168bf0c343759b02a4ab852361512c103", "0.50.0--hc877fd6_0": "sha256:179723a1556f0da8349e67cea06bdca3ae1d532ceef13df23200c7d2ec1a0b3c", "0.50.1--hc877fd6_0": "sha256:b53e7a001384640d78d7efe8de63660d98432515fc74e041e575aa22fbf057b9", "0.50.1--hc877fd6_1": "sha256:303df2157635a4a3c5f8aca72cb6cc66c6f7bb2a1a867ea66d540681ff3748ab", "0.50.1--h6de1650_2": "sha256:141d52cfdab16459e822d32603c0cb5610ba7c63f857003a36047aae6116b98f", "0.51.0--h6de1650_0": "sha256:ac162325c726daccfb5d65cf7eee3629dab9710c7d9b32be192db51301a5a18b", "0.51.1--heb0cbe2_0": "sha256:b054a431d79c8f7ee65ee5fa0e9869da122b08bd669c957ed35dfca45ceacb39", "0.51.1--ha4fb952_1": "sha256:f2dc85d6d55e1c3bfdc437a7738b1217d0f81ee9c1c62013b5dd3b867713d482"}, "docker": "quay.io/biocontainers/kallisto", "aliases": {"kallisto": "/usr/local/bin/kallisto", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kallisto.
shpc-registry automated BioContainers addition for kallisto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kallisto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kallisto:0.51.1--ha4fb952_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kallisto/0.51.1--ha4fb952_1
$ module help quay.io/biocontainers/kallisto/0.51.1--ha4fb952_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kallisto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kallisto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kallisto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kallisto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
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