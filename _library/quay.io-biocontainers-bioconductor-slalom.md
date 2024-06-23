---
layout: container
name:  "quay.io/biocontainers/bioconductor-slalom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-slalom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-slalom/container.yaml"
updated_at: "2024-06-23 02:57:26.618143"
latest: "1.24.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-slalom"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.0--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-slalom"
config: {"url": "https://biocontainers.pro/tools/bioconductor-slalom", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-slalom", "latest": {"1.24.0--r43hf17093f_0": "sha256:0097477d9547309aa72f6196dc8fea55c633e678598510efe5026c20dbb5fcd6"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:6696d408ba45ea0971fa8a4b34e5e3e38dcf81628dd1d95cb36f607c35e7c727", "1.20.0--r42hc247a5b_0": "sha256:3a93c6b4ccc5aeb0ff6b9543d3d57865eea2183c22e6a5dacdcec755b4f62d3c", "1.16.0--r41hc247a5b_2": "sha256:75b51fe6538e4e5de2ebffd13c91b540e60caf32299a1e5a26a03c83c9f750b9", "1.14.0--r41h399db7b_0": "sha256:674cdcb8ecf52fb935ec039866d46823ad62d9537e52487adf0c618ae050e544", "1.12.0--r40h399db7b_1": "sha256:07c317679c1bb5baf6a89b189fec04c52d94bcbc8f391e712ee8e04b672d8dae", "1.10.0--r40h5f743cb_0": "sha256:be4250eb10c671bcbf712397dc0219d4805d80fc6787b6e566d63a734ced5cdd", "1.20.0--r42hf17093f_1": "sha256:02207b2799cb8070a4b28e28ae9d9bf4defe1d3e27894714b27e16892b9737e1", "1.22.0--r43hf17093f_0": "sha256:96e5a2823b30386f310d8ac0749a0c19c2eac9678ff9ef43475e63f55636c3eb", "1.24.0--r43hf17093f_0": "sha256:0097477d9547309aa72f6196dc8fea55c633e678598510efe5026c20dbb5fcd6"}, "docker": "quay.io/biocontainers/bioconductor-slalom", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-slalom.
shpc-registry automated BioContainers addition for bioconductor-slalom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-slalom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-slalom:1.24.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-slalom/1.24.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-slalom/1.24.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-slalom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-slalom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-slalom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-slalom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-slalom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-slalom-inspect-deffile:

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