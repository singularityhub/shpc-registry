---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhdf5client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhdf5client/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhdf5client/container.yaml"
updated_at: "2025-11-05 03:47:06.997523"
latest: "1.28.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rhdf5client"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_0"
 - "1.20.0--r42hc0cfd56_0"
 - "1.16.0--r41hc0cfd56_2"
 - "1.14.0--r41hd029910_0"
 - "1.12.0--r40hd029910_1"
 - "1.10.0--r40h037d062_0"
 - "1.20.0--r42ha9d7317_1"
 - "1.22.0--r43ha9d7317_0"
 - "1.24.0--r43ha9d7317_0"
 - "1.28.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rhdf5client"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhdf5client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhdf5client", "latest": {"1.28.0--r44h3df3fcb_0": "sha256:78ee67f2c8ecf80836e4f22d889f556b781a60664600a1052d3fe91e592c9d12"}, "tags": {"1.8.0--r36h516909a_0": "sha256:2ddcc7db778c4a9ecc0d389703ac657afc392811b11e07ad4baece504dfa20d7", "1.20.0--r42hc0cfd56_0": "sha256:99bc44e1a7a34dbf990992aaa6f33e310889b12cebd19c0a960ca498d859e930", "1.16.0--r41hc0cfd56_2": "sha256:3695d85b84e87de422518b4cc0fd438eb02485dea48f059f133045ded3e1df64", "1.14.0--r41hd029910_0": "sha256:7b67e4d85fe8875f86b3464e5317e94f78464cd8d9c3fc65fe9a4b0066c2ca60", "1.12.0--r40hd029910_1": "sha256:226dfd84e0552818ea9435a62eac8a22d37472b3e28c81ad67fac735357a9e36", "1.10.0--r40h037d062_0": "sha256:ee51a8540afc39418a5048c6804675dbc4640e542d06d0a24b9fe9759b5c3525", "1.20.0--r42ha9d7317_1": "sha256:5fb6d8b360bf9902a36c0bef8fc9e2364f8b1074aaccf26865b469ab9e73dead", "1.22.0--r43ha9d7317_0": "sha256:06fa4ebd374aa3d63c82fd0560456b9ced6aa4c8b83f19c62f26aae2db454d97", "1.24.0--r43ha9d7317_0": "sha256:07410b6f27cd583c5a7352f98cbc1537eff7e371a3cd5e06629da2299ef46999", "1.28.0--r44h3df3fcb_0": "sha256:78ee67f2c8ecf80836e4f22d889f556b781a60664600a1052d3fe91e592c9d12"}, "docker": "quay.io/biocontainers/bioconductor-rhdf5client", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhdf5client.
shpc-registry automated BioContainers addition for bioconductor-rhdf5client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5client:1.28.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhdf5client/1.28.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-rhdf5client/1.28.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhdf5client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhdf5client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhdf5client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhdf5client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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