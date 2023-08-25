---
layout: container
name:  "quay.io/biocontainers/bioconductor-scoreinvhap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scoreinvhap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scoreinvhap/container.yaml"
updated_at: "2023-08-25 02:38:27.611203"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scoreinvhap"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.1--r40hdfd78af_0"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scoreinvhap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scoreinvhap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scoreinvhap", "latest": {"1.22.0--r43hdfd78af_0": "sha256:4b1d738213f39b8360017626178a585eea6f6b9195024b090a9be22036b5f112"}, "tags": {"1.8.0--r36_0": "sha256:7c5c41d7649e5128b89c03562833b6ed6a393b46051c248b09501ae8179e8d5c", "1.20.0--r42hdfd78af_0": "sha256:ee7789c77b3e42c3eafbee69b59e4dfdf4bdb0c9324cdc4db6ef8ab3d27f7fcd", "1.16.0--r41hdfd78af_0": "sha256:5ea36666c22a7a4d7385c411236462da6cf16cb1beb5599117ce71c5b09f7090", "1.14.0--r41hdfd78af_0": "sha256:0b53fa1002133077ad1afabe73016f5baea0dffab637608982fa5070d5001afe", "1.12.1--r40hdfd78af_0": "sha256:9ef6e6a2241cf97abd36df4f3db2c94ed34a93fbb854a25c454e51acc9e420c8", "1.10.0--r40_0": "sha256:7636c982b7402fdccd8ea29b81b36a3edb8664feb95521d8b0437040240974e5", "1.22.0--r43hdfd78af_0": "sha256:4b1d738213f39b8360017626178a585eea6f6b9195024b090a9be22036b5f112"}, "docker": "quay.io/biocontainers/bioconductor-scoreinvhap", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scoreinvhap.
shpc-registry automated BioContainers addition for bioconductor-scoreinvhap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scoreinvhap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scoreinvhap:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scoreinvhap/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scoreinvhap/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scoreinvhap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scoreinvhap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scoreinvhap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scoreinvhap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scoreinvhap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scoreinvhap-inspect-deffile:

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