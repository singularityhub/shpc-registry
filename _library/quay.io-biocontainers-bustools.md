---
layout: container
name:  "quay.io/biocontainers/bustools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bustools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bustools/container.yaml"
updated_at: "2025-01-20 04:23:31.648390"
latest: "0.44.1--h6f0a7f7_1"
container_url: "https://biocontainers.pro/tools/bustools"
aliases:
 - "bustools"
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
 - "0.41.0--h15996b6_2"
 - "0.42.0--h15996b6_0"
 - "0.42.0--h1339bb5_2"
 - "0.43.0--h1339bb5_0"
 - "0.43.1--h1339bb5_0"
 - "0.43.2--h1339bb5_0"
 - "0.43.2--he1fd2f9_1"
 - "0.43.2--he1fd2f9_2"
 - "0.44.0--he1fd2f9_0"
 - "0.44.1--he1fd2f9_0"
 - "0.44.1--h6f0a7f7_1"
description: "shpc-registry automated BioContainers addition for bustools"
config: {"url": "https://biocontainers.pro/tools/bustools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bustools", "latest": {"0.44.1--h6f0a7f7_1": "sha256:58b0fe62b641715faa5dcc24216d04b56b44253c2fd65d06d82abf7b2dd7c08e"}, "tags": {"0.41.0--h15996b6_2": "sha256:97f0688f3fc0c4f8f642f52e0b1643e4921b816f1a7855bba5dbe31a904c924c", "0.42.0--h15996b6_0": "sha256:fd56d2b95a3883b71e1291d881a6edee6d3824e120197c4d459d140d09a5b22a", "0.42.0--h1339bb5_2": "sha256:4860c533cc2896e8c39232f20313dbe5c68ae2f69947c15ee5f2f05c16114484", "0.43.0--h1339bb5_0": "sha256:da0076fe9156776215baa4e97d81104ec6e573b99604fdc3a88fda6a4d5be087", "0.43.1--h1339bb5_0": "sha256:7161b58d937aa00dce2e77848ccc27fb517ad2d211a08352541e680338b33489", "0.43.2--h1339bb5_0": "sha256:dc2608fcf4917f6acb1e7445f4f2011af88d6811627654dc4d5abe902028fca0", "0.43.2--he1fd2f9_1": "sha256:a7293219292ba5cf8ff8023a90190252d4d5a336e52d4bbb7cc9ca24e8dfba66", "0.43.2--he1fd2f9_2": "sha256:1498806028f79f80a0a89d5765733a8386bc992749472ecc8d0c18bbc93e8f20", "0.44.0--he1fd2f9_0": "sha256:b4a5ae90844dae00bd6572c82c72a808e0c33a16ab892b0337b0a663868910ec", "0.44.1--he1fd2f9_0": "sha256:d618abda1155814a9db24f28f0f99e0b3c2b48f8bf42a55789de516253066f81", "0.44.1--h6f0a7f7_1": "sha256:58b0fe62b641715faa5dcc24216d04b56b44253c2fd65d06d82abf7b2dd7c08e"}, "docker": "quay.io/biocontainers/bustools", "aliases": {"bustools": "/usr/local/bin/bustools", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bustools.
shpc-registry automated BioContainers addition for bustools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bustools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bustools:0.44.1--h6f0a7f7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bustools/0.44.1--h6f0a7f7_1
$ module help quay.io/biocontainers/bustools/0.44.1--h6f0a7f7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bustools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bustools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bustools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bustools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bustools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bustools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bustools

```bash
$ singularity exec <container> /usr/local/bin/bustools
$ podman run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
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