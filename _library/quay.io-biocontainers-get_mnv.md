---
layout: container
name:  "quay.io/biocontainers/get_mnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/get_mnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/get_mnv/container.yaml"
updated_at: "2026-01-10 03:56:26.652498"
latest: "1.0.0--ha7a4ace_1"
container_url: "https://biocontainers.pro/tools/get_mnv"
aliases:
 - "get_mnv"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.0--ha7a4ace_1"
description: "singularity registry hpc automated addition for get_mnv"
config: {"url": "https://biocontainers.pro/tools/get_mnv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for get_mnv", "latest": {"1.0.0--ha7a4ace_1": "sha256:1063eb6b98905f92e34b9f5dd7c2c59d164e9a88f71e1373a708a432dc20df95"}, "tags": {"1.0.0--ha7a4ace_1": "sha256:1063eb6b98905f92e34b9f5dd7c2c59d164e9a88f71e1373a708a432dc20df95"}, "docker": "quay.io/biocontainers/get_mnv", "aliases": {"get_mnv": "/usr/local/bin/get_mnv", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/get_mnv.
singularity registry hpc automated addition for get_mnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/get_mnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/get_mnv:1.0.0--ha7a4ace_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/get_mnv/1.0.0--ha7a4ace_1
$ module help quay.io/biocontainers/get_mnv/1.0.0--ha7a4ace_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### get_mnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### get_mnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### get_mnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### get_mnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### get_mnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### get_mnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_mnv

```bash
$ singularity exec <container> /usr/local/bin/get_mnv
$ podman run --it --rm --entrypoint /usr/local/bin/get_mnv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_mnv   -v ${PWD} -w ${PWD} <container> -c " $@"
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