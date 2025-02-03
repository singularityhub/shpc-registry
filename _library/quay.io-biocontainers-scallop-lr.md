---
layout: container
name:  "quay.io/biocontainers/scallop-lr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scallop-lr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scallop-lr/container.yaml"
updated_at: "2025-02-03 03:23:13.183372"
latest: "0.9.2--h503566f_10"
container_url: "https://biocontainers.pro/tools/scallop-lr"
aliases:
 - "scallop-lr"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.9.2--hefd527f_6"
 - "0.9.2--h66ab1b6_7"
 - "0.9.2--h5642b88_8"
 - "0.9.2--h503566f_10"
description: "shpc-registry automated BioContainers addition for scallop-lr"
config: {"url": "https://biocontainers.pro/tools/scallop-lr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scallop-lr", "latest": {"0.9.2--h503566f_10": "sha256:bf2416909393f1ca0ef04bf7d0ecd544988cb0f283a65a962c25b58f22f87884"}, "tags": {"0.9.2--hefd527f_6": "sha256:9049acde847eb56a54bd743a3c54c3880b3f675b47ae553544a34f522854b994", "0.9.2--h66ab1b6_7": "sha256:c11f6d76c660381e7d4ad14f0f6f0dfcbe63b6f6d530841cd7f69847a5e3b2ae", "0.9.2--h5642b88_8": "sha256:8a901fb37c4a6422633245f4d128a675b50dc7a059f6a264bbab6f38ca5cbb4d", "0.9.2--h503566f_10": "sha256:bf2416909393f1ca0ef04bf7d0ecd544988cb0f283a65a962c25b58f22f87884"}, "docker": "quay.io/biocontainers/scallop-lr", "aliases": {"scallop-lr": "/usr/local/bin/scallop-lr", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scallop-lr.
shpc-registry automated BioContainers addition for scallop-lr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scallop-lr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scallop-lr:0.9.2--h503566f_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scallop-lr/0.9.2--h503566f_10
$ module help quay.io/biocontainers/scallop-lr/0.9.2--h503566f_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scallop-lr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scallop-lr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scallop-lr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scallop-lr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scallop-lr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scallop-lr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scallop-lr

```bash
$ singularity exec <container> /usr/local/bin/scallop-lr
$ podman run --it --rm --entrypoint /usr/local/bin/scallop-lr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scallop-lr   -v ${PWD} -w ${PWD} <container> -c " $@"
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