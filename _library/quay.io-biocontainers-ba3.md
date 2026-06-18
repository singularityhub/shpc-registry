---
layout: container
name:  "quay.io/biocontainers/ba3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ba3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ba3/container.yaml"
updated_at: "2026-06-18 07:29:31.659962"
latest: "3.4.4--h193c6b0_0"
container_url: "https://biocontainers.pro/tools/ba3"
aliases:
 - "BA3"
 - "ref-cache"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "3.4.4--h193c6b0_0"
description: "singularity registry hpc automated addition for ba3"
config: {"url": "https://biocontainers.pro/tools/ba3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ba3", "latest": {"3.4.4--h193c6b0_0": "sha256:04add8762ca5f91f02261a5d325847591d544ac9cf0676de51c4edf9f0dcaaf8"}, "tags": {"3.4.4--h193c6b0_0": "sha256:04add8762ca5f91f02261a5d325847591d544ac9cf0676de51c4edf9f0dcaaf8"}, "docker": "quay.io/biocontainers/ba3", "aliases": {"BA3": "/usr/local/bin/BA3", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ba3.
singularity registry hpc automated addition for ba3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ba3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ba3:3.4.4--h193c6b0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ba3/3.4.4--h193c6b0_0
$ module help quay.io/biocontainers/ba3/3.4.4--h193c6b0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ba3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ba3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ba3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ba3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ba3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ba3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BA3

```bash
$ singularity exec <container> /usr/local/bin/BA3
$ podman run --it --rm --entrypoint /usr/local/bin/BA3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BA3   -v ${PWD} -w ${PWD} <container> -c " $@"
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