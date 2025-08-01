---
layout: container
name:  "quay.io/biocontainers/f5c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/f5c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/f5c/container.yaml"
updated_at: "2025-08-01 04:06:31.731551"
latest: "1.5--hee927d3_2"
container_url: "https://biocontainers.pro/tools/f5c"
aliases:
 - "f5c"
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
 - "1.1--h0326b38_1"
 - "1.2--h500492e_2"
 - "1.3--h500492e_0"
 - "1.4--h500492e_0"
 - "1.4--h56e2c18_1"
 - "1.2--h56e2c18_3"
 - "1.5--h56e2c18_1"
 - "1.5--hee927d3_2"
 - "1.2--hee927d3_4"
description: "shpc-registry automated BioContainers addition for f5c"
config: {"url": "https://biocontainers.pro/tools/f5c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for f5c", "latest": {"1.5--hee927d3_2": "sha256:6189a52250799862eeca0bd8284669af5dc648e98d3dfb22945e308ad6f7b885"}, "tags": {"1.1--h0326b38_1": "sha256:b491cfafa553e03de8e7eae3a7782d72dbe89c6821ddb9ba1cceffac75b18c4c", "1.2--h500492e_2": "sha256:2657c0828b00543f4bea74fd504a008d9e28d1dc9a03cd6fa190aaac442a6fde", "1.3--h500492e_0": "sha256:ceb3cc5c306e2b3827baa273c2ed26be10c511706162cb01e7718ec3ce0792e3", "1.4--h500492e_0": "sha256:f236b6f01f142d784afbd2f7865162a09ff361d728f210bf483b65a9d6f2119e", "1.4--h56e2c18_1": "sha256:5ee16b38bec16fb9e8f4edbec472aea4682f98a43cd6bcbb0b1135d8e8f2986e", "1.2--h56e2c18_3": "sha256:625e58023bd8c428e464da6d1d9d118cc90fc70234bf25cd1c0821c9254fc71a", "1.5--h56e2c18_1": "sha256:1223c2dbf16e3c6622143fcbfb8a036397d7236e106e492f9e9d34c2dcd31264", "1.5--hee927d3_2": "sha256:6189a52250799862eeca0bd8284669af5dc648e98d3dfb22945e308ad6f7b885", "1.2--hee927d3_4": "sha256:77e7c3ce30173f2a846c0c529dee2f944b5098eb04e3123f2ab862d8b97c0eb9"}, "docker": "quay.io/biocontainers/f5c", "aliases": {"f5c": "/usr/local/bin/f5c", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/f5c.
shpc-registry automated BioContainers addition for f5c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/f5c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/f5c:1.5--hee927d3_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/f5c/1.5--hee927d3_2
$ module help quay.io/biocontainers/f5c/1.5--hee927d3_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### f5c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### f5c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### f5c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### f5c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### f5c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### f5c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f5c

```bash
$ singularity exec <container> /usr/local/bin/f5c
$ podman run --it --rm --entrypoint /usr/local/bin/f5c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f5c   -v ${PWD} -w ${PWD} <container> -c " $@"
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