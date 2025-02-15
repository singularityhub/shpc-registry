---
layout: container
name:  "quay.io/biocontainers/bioconductor-amplican"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-amplican/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-amplican/container.yaml"
updated_at: "2025-02-15 03:28:19.028873"
latest: "1.24.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-amplican"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.1--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-amplican"
config: {"url": "https://biocontainers.pro/tools/bioconductor-amplican", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-amplican", "latest": {"1.24.0--r43hf17093f_0": "sha256:da7849a96d9f572c17a07715f6307d7e389e012837710637d235e4b63ccd5452"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:744ec8d7f3b05afc5becf2a4acd3ba6b8c2fbac1374cefe97c4037b2aa2d740f", "1.16.0--r41hc247a5b_2": "sha256:30bf8a5ae6c186817feba02370c0254b011b2075fb7b49184ffd1cffd1e4434e", "1.14.0--r41h399db7b_0": "sha256:5527580989ae490a1e4619764334c5f47d24f47fad4a64b4434c017d704f808c", "1.12.0--r40h399db7b_1": "sha256:7d7f6d4ecc6deddd346c7a9cf9aac97a7b563101001371c6b4954038bb030673", "1.10.0--r40h5f743cb_0": "sha256:d5f5db4c1fd8f5da3955f2729396eeb6a4d2384fb72e3ef228d3446cfa5ec784", "1.20.0--r42hc247a5b_0": "sha256:b4278cc18d801603cb37670b696d70a972de79d0ab07b48ba441992c5e45d2a0", "1.20.0--r42hf17093f_1": "sha256:9350fedb8add43bd780d34e4aadb56715bf9aa1db38ee85f3efc08582ecaa6e4", "1.22.1--r43hf17093f_0": "sha256:68e5ab17ffd2f3ec46f7e963e4295228ae303a29eee5a072f48a0029dc2b3e97", "1.24.0--r43hf17093f_0": "sha256:da7849a96d9f572c17a07715f6307d7e389e012837710637d235e4b63ccd5452"}, "docker": "quay.io/biocontainers/bioconductor-amplican", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-amplican.
shpc-registry automated BioContainers addition for bioconductor-amplican
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-amplican
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-amplican:1.24.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-amplican/1.24.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-amplican/1.24.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-amplican-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amplican-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amplican-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-amplican-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-amplican-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-amplican-inspect-deffile:

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