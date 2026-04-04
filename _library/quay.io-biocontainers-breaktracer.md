---
layout: container
name:  "quay.io/biocontainers/breaktracer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/breaktracer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/breaktracer/container.yaml"
updated_at: "2026-04-04 05:13:16.349240"
latest: "0.2.6--hd6466ae_0"
container_url: "https://biocontainers.pro/tools/breaktracer"
aliases:
 - "breaktracer"
 - "ref-cache"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.6--hd6466ae_0"
description: "singularity registry hpc automated addition for breaktracer"
config: {"url": "https://biocontainers.pro/tools/breaktracer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for breaktracer", "latest": {"0.2.6--hd6466ae_0": "sha256:54ec9659ce6c1e3093317b0684342dbad8e850156bccb4d8f711137098774e70"}, "tags": {"0.2.6--hd6466ae_0": "sha256:54ec9659ce6c1e3093317b0684342dbad8e850156bccb4d8f711137098774e70"}, "docker": "quay.io/biocontainers/breaktracer", "aliases": {"breaktracer": "/usr/local/bin/breaktracer", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/breaktracer.
singularity registry hpc automated addition for breaktracer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/breaktracer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/breaktracer:0.2.6--hd6466ae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/breaktracer/0.2.6--hd6466ae_0
$ module help quay.io/biocontainers/breaktracer/0.2.6--hd6466ae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### breaktracer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### breaktracer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### breaktracer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### breaktracer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### breaktracer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### breaktracer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### breaktracer

```bash
$ singularity exec <container> /usr/local/bin/breaktracer
$ podman run --it --rm --entrypoint /usr/local/bin/breaktracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/breaktracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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