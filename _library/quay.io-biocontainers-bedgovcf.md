---
layout: container
name:  "quay.io/biocontainers/bedgovcf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bedgovcf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bedgovcf/container.yaml"
updated_at: "2024-05-21 03:20:54.100662"
latest: "0.1.1--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/bedgovcf"
aliases:
 - "bedgovcf"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.0--h9ee0642_0"
 - "0.1.1--h9ee0642_1"
description: "singularity registry hpc automated addition for bedgovcf"
config: {"url": "https://biocontainers.pro/tools/bedgovcf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bedgovcf", "latest": {"0.1.1--h9ee0642_1": "sha256:4b23f82399abb27b75bb1376d08ff0972f6968999427d18e017ffd49e61aa56e"}, "tags": {"0.1.0--h9ee0642_0": "sha256:33f57ff12e8aad98aaaef0afed0cecb3acfbd5987ba2e0ec25b8f45904e2afc0", "0.1.1--h9ee0642_1": "sha256:4b23f82399abb27b75bb1376d08ff0972f6968999427d18e017ffd49e61aa56e"}, "docker": "quay.io/biocontainers/bedgovcf", "aliases": {"bedgovcf": "/usr/local/bin/bedgovcf", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bedgovcf.
singularity registry hpc automated addition for bedgovcf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bedgovcf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bedgovcf:0.1.1--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bedgovcf/0.1.1--h9ee0642_1
$ module help quay.io/biocontainers/bedgovcf/0.1.1--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bedgovcf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bedgovcf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bedgovcf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bedgovcf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bedgovcf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bedgovcf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedgovcf

```bash
$ singularity exec <container> /usr/local/bin/bedgovcf
$ podman run --it --rm --entrypoint /usr/local/bin/bedgovcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedgovcf   -v ${PWD} -w ${PWD} <container> -c " $@"
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