---
layout: container
name:  "quay.io/biocontainers/bioconductor-cogaps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cogaps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cogaps/container.yaml"
updated_at: "2024-08-24 03:06:45.637310"
latest: "3.22.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cogaps"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.0--r40h5f743cb_0"
 - "3.18.0--r42hc247a5b_0"
 - "3.14.0--r41hc247a5b_2"
 - "3.12.0--r41h399db7b_0"
 - "3.10.0--r40h399db7b_1"
 - "3.18.0--r42hf17093f_1"
 - "3.19.1--r43hf17093f_0"
 - "3.22.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cogaps"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cogaps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cogaps", "latest": {"3.22.0--r43hf17093f_0": "sha256:08555f090ad79d8088b3c24a11667ac8f4eca6b4975dcdfcf8ed68ff468a6d7d"}, "tags": {"3.8.0--r40h5f743cb_0": "sha256:4af7df9c6e35c82751d7f6e5b69710ed5d03a73cf3db439717fb513f7f40b759", "3.18.0--r42hc247a5b_0": "sha256:49d0b8f1d4004e1f7a5401dfe405d4237cbca772f48356ac7e32c900039560aa", "3.14.0--r41hc247a5b_2": "sha256:200da7f743759281d33ee51fe78346ec90c3b1ada3601217c978e20fe666aa42", "3.12.0--r41h399db7b_0": "sha256:0d378736085dcd546d0d3c3df99bd4a838fda64ebc938325b51d845aa4d8775c", "3.10.0--r40h399db7b_1": "sha256:aad6edec413d96294b344e528fa61e296410bfea632a2979c2c26d2ab63ffe1b", "3.18.0--r42hf17093f_1": "sha256:3dd206adea1439eb9eab0cc36789d63ed0799cc5b9d67630fae64f6d13658d77", "3.19.1--r43hf17093f_0": "sha256:f1bb8d60ba11692cd41d29f82cb3e291ec84983baa6131c77c3d296b783f9c4b", "3.22.0--r43hf17093f_0": "sha256:08555f090ad79d8088b3c24a11667ac8f4eca6b4975dcdfcf8ed68ff468a6d7d"}, "docker": "quay.io/biocontainers/bioconductor-cogaps", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cogaps.
shpc-registry automated BioContainers addition for bioconductor-cogaps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cogaps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cogaps:3.22.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cogaps/3.22.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cogaps/3.22.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cogaps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogaps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogaps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cogaps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cogaps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cogaps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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