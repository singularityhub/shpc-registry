---
layout: container
name:  "ghcr.io/autamus/intel-mkl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/intel-mkl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/intel-mkl/container.yaml"
updated_at: "2024-06-29 02:32:40.548060"
latest: "2020.4.304"
container_url: "https://github.com/orgs/autamus/packages/container/package/intel-mkl"

versions:
 - "2020.4.304"
 - "latest"
description: "Intel oneAPI Math Kernel Library, formerly just Intel Math Kernel Library, is a library of optimized math routines for science, engineering, and financial applications."
config: {"docker": "ghcr.io/autamus/intel-mkl", "url": "https://github.com/orgs/autamus/packages/container/package/intel-mkl", "maintainer": "@vsoch", "description": "Intel oneAPI Math Kernel Library, formerly just Intel Math Kernel Library, is a library of optimized math routines for science, engineering, and financial applications.", "latest": {"2020.4.304": "sha256:63b34cf7c73fc23f07d661ae58f935bad1e79ebd4b69f3f585b47d0a70481f51"}, "tags": {"2020.4.304": "sha256:63b34cf7c73fc23f07d661ae58f935bad1e79ebd4b69f3f585b47d0a70481f51", "latest": "sha256:63b34cf7c73fc23f07d661ae58f935bad1e79ebd4b69f3f585b47d0a70481f51"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/intel-mkl.
Intel oneAPI Math Kernel Library, formerly just Intel Math Kernel Library, is a library of optimized math routines for science, engineering, and financial applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/intel-mkl
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/intel-mkl:2020.4.304
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/intel-mkl/2020.4.304
$ module help ghcr.io/autamus/intel-mkl/2020.4.304
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### intel-mkl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### intel-mkl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### intel-mkl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### intel-mkl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### intel-mkl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### intel-mkl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### intel-mkl

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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