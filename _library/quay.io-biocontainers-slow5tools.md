---
layout: container
name:  "quay.io/biocontainers/slow5tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slow5tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slow5tools/container.yaml"
updated_at: "2023-05-20 02:52:59.882309"
latest: "1.0.0--h500492e_2"
container_url: "https://biocontainers.pro/tools/slow5tools"
aliases:
 - "slow5tools"
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
 - "0.6.0--h0326b38_2"
 - "1.0.0--h0326b38_0"
 - "0.9.0--h0326b38_0"
 - "0.8.0--h0326b38_0"
 - "0.7.0--h0326b38_0"
 - "1.0.0--h500492e_2"
 - "0.9.0--h500492e_2"
 - "0.8.0--h500492e_2"
 - "0.7.0--h500492e_2"
description: "shpc-registry automated BioContainers addition for slow5tools"
config: {"url": "https://biocontainers.pro/tools/slow5tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slow5tools", "latest": {"1.0.0--h500492e_2": "sha256:b49bda78b104cf8a27f41cfec9355d4dfcc7926f72a9cf68ee2e818a9d0f2ae5"}, "tags": {"0.6.0--h0326b38_2": "sha256:fa2549fa31797e890061e4e6c911d2d378486cf17f6e98adeb93f17500e5cdca", "1.0.0--h0326b38_0": "sha256:90f91ba8044f03abbe5fbfc26d59d59238a335b15ca0bbee4c78ee9af2f344bb", "0.9.0--h0326b38_0": "sha256:19de6d9091eb7b94692378a04127193cd49c5161d021363b57fef29293afa5f0", "0.8.0--h0326b38_0": "sha256:04b7875daa1314c2f8d4d5fffeb6b58e6391be2b69a704379453c3596ac88d21", "0.7.0--h0326b38_0": "sha256:179fa0baacc5088811445883d0867358899b69f7ec2bbebad607a28199a3c510", "1.0.0--h500492e_2": "sha256:b49bda78b104cf8a27f41cfec9355d4dfcc7926f72a9cf68ee2e818a9d0f2ae5", "0.9.0--h500492e_2": "sha256:07db5f4a67c5df285b9e32bb49dfe26ccd03766b60f51ec564a5a9535423a76b", "0.8.0--h500492e_2": "sha256:ce7670e7d0e14748524064882264ace57835657c193a4fabf253d0f50f74e190", "0.7.0--h500492e_2": "sha256:1a12a508d1a79311ba0577225222a84ce8c2ea4d61e66ff75e7a5417769ebd05"}, "docker": "quay.io/biocontainers/slow5tools", "aliases": {"slow5tools": "/usr/local/bin/slow5tools", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slow5tools.
shpc-registry automated BioContainers addition for slow5tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slow5tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slow5tools:1.0.0--h500492e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slow5tools/1.0.0--h500492e_2
$ module help quay.io/biocontainers/slow5tools/1.0.0--h500492e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slow5tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slow5tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slow5tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slow5tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slow5tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slow5tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slow5tools

```bash
$ singularity exec <container> /usr/local/bin/slow5tools
$ podman run --it --rm --entrypoint /usr/local/bin/slow5tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slow5tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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