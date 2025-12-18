---
layout: container
name:  "quay.io/biocontainers/r-seurat-data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-seurat-data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-seurat-data/container.yaml"
updated_at: "2025-12-18 03:28:33.089928"
latest: "0.2.2.9002--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-seurat-data"
aliases:
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
versions:
 - "0.2.1--r43h9ee0642_0"
 - "0.2.1--r44h9ee0642_1"
 - "0.2.2.9002--r44hdfd78af_0"
description: "singularity registry hpc automated addition for r-seurat-data"
config: {"url": "https://biocontainers.pro/tools/r-seurat-data", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-seurat-data", "latest": {"0.2.2.9002--r44hdfd78af_0": "sha256:4b8547b86ac072d6a2f784e62988ff66c08329888fd9d0e7fa9541353cb48ffa"}, "tags": {"0.2.1--r43h9ee0642_0": "sha256:06832e01dd21fe6919413e9bb3fc043aa4539ea1d44ec8fc29b5f19f3b991f9f", "0.2.1--r44h9ee0642_1": "sha256:de15bd812a41c3dcd6ba243035d141af6f804d5bfc5e2a3653cf834f5345346f", "0.2.2.9002--r44hdfd78af_0": "sha256:4b8547b86ac072d6a2f784e62988ff66c08329888fd9d0e7fa9541353cb48ffa"}, "docker": "quay.io/biocontainers/r-seurat-data", "aliases": {"pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-seurat-data.
singularity registry hpc automated addition for r-seurat-data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-seurat-data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-seurat-data:0.2.2.9002--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-seurat-data/0.2.2.9002--r44hdfd78af_0
$ module help quay.io/biocontainers/r-seurat-data/0.2.2.9002--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-seurat-data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-seurat-data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-seurat-data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-seurat-data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-seurat-data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-seurat-data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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