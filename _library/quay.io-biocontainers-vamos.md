---
layout: container
name:  "quay.io/biocontainers/vamos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vamos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vamos/container.yaml"
updated_at: "2023-12-09 03:01:01.090194"
latest: "1.3.6--hd7d8470_0"
container_url: "https://biocontainers.pro/tools/vamos"
aliases:
 - "vamos"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.2.6--hd7d8470_0"
 - "1.3.6--hd7d8470_0"
description: "singularity registry hpc automated addition for vamos"
config: {"url": "https://biocontainers.pro/tools/vamos", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vamos", "latest": {"1.3.6--hd7d8470_0": "sha256:9ac2de5e2480677c8e29be1f20584ff812aceebe1d89340c289ea836959bd9e1"}, "tags": {"1.2.6--hd7d8470_0": "sha256:479ebf30b12dc718ee1b18e72d73ca8aa1f5cc0fa98016b645754d961987fde6", "1.3.6--hd7d8470_0": "sha256:9ac2de5e2480677c8e29be1f20584ff812aceebe1d89340c289ea836959bd9e1"}, "docker": "quay.io/biocontainers/vamos", "aliases": {"vamos": "/usr/local/bin/vamos", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vamos.
singularity registry hpc automated addition for vamos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vamos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vamos:1.3.6--hd7d8470_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vamos/1.3.6--hd7d8470_0
$ module help quay.io/biocontainers/vamos/1.3.6--hd7d8470_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vamos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vamos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vamos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vamos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vamos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vamos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vamos

```bash
$ singularity exec <container> /usr/local/bin/vamos
$ podman run --it --rm --entrypoint /usr/local/bin/vamos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vamos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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