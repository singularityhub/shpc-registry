---
layout: container
name:  "quay.io/biocontainers/bioconductor-srnadiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-srnadiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-srnadiff/container.yaml"
updated_at: "2023-08-08 02:52:41.752249"
latest: "1.18.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-srnadiff"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r40h5f743cb_0"
 - "1.18.0--r42hc247a5b_0"
 - "1.14.0--r41hc247a5b_2"
 - "1.12.2--r41h399db7b_0"
 - "1.10.1--r40h399db7b_0"
 - "1.18.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-srnadiff"
config: {"url": "https://biocontainers.pro/tools/bioconductor-srnadiff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-srnadiff", "latest": {"1.18.0--r42hf17093f_1": "sha256:0f82645801925c4e5669e1faeba6fbb6562a65138dceeeb20152d7c51c18548f"}, "tags": {"1.8.0--r40h5f743cb_0": "sha256:89ea9f33aa6fbf9cf90faee540f9da52134e2242b9e1760d180a7b79875b71cf", "1.18.0--r42hc247a5b_0": "sha256:e041de989ecc5e35a04feaa50878e6a80fbe438295ee7ae824a2ca249c68506c", "1.14.0--r41hc247a5b_2": "sha256:dd353c3d2449165457625232ea4f1d367b6252a879cc0fa0153b4e95cd902ca3", "1.12.2--r41h399db7b_0": "sha256:9dce7f5e1adbd005dfaca8910b2729e8cd59d2de414a7ff2eaa8d077639d7677", "1.10.1--r40h399db7b_0": "sha256:b0fd963364a6fa438780aa09346677377d029dc25690935aa537ff8a0bdecf2c", "1.18.0--r42hf17093f_1": "sha256:0f82645801925c4e5669e1faeba6fbb6562a65138dceeeb20152d7c51c18548f"}, "docker": "quay.io/biocontainers/bioconductor-srnadiff", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-srnadiff.
shpc-registry automated BioContainers addition for bioconductor-srnadiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-srnadiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-srnadiff:1.18.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-srnadiff/1.18.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-srnadiff/1.18.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-srnadiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srnadiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srnadiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-srnadiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-srnadiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-srnadiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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