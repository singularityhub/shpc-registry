---
layout: container
name:  "quay.io/biocontainers/ibdmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ibdmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ibdmix/container.yaml"
updated_at: "2024-10-02 03:37:06.254380"
latest: "1.0.1--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/ibdmix"
aliases:
 - "generate_gt"
 - "gt_lods"
 - "ibdmix"
versions:
 - "1.0.1--h9f5acd7_0"
 - "1.0.1--h4ac6f70_2"
description: "singularity registry hpc automated addition for ibdmix"
config: {"url": "https://biocontainers.pro/tools/ibdmix", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ibdmix", "latest": {"1.0.1--h4ac6f70_2": "sha256:860a6f03f6971c5179a7bd68e56969864a5c7159a600a2787a992a2a047f6856"}, "tags": {"1.0.1--h9f5acd7_0": "sha256:a32dfb581a988f7f443cfee3481c9d5093c1a4b349f2f32d38b645c556ca68a2", "1.0.1--h4ac6f70_2": "sha256:860a6f03f6971c5179a7bd68e56969864a5c7159a600a2787a992a2a047f6856"}, "docker": "quay.io/biocontainers/ibdmix", "aliases": {"generate_gt": "/usr/local/bin/generate_gt", "gt_lods": "/usr/local/bin/gt_lods", "ibdmix": "/usr/local/bin/ibdmix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ibdmix.
singularity registry hpc automated addition for ibdmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ibdmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ibdmix:1.0.1--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ibdmix/1.0.1--h4ac6f70_2
$ module help quay.io/biocontainers/ibdmix/1.0.1--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ibdmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ibdmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ibdmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ibdmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ibdmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ibdmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### generate_gt

```bash
$ singularity exec <container> /usr/local/bin/generate_gt
$ podman run --it --rm --entrypoint /usr/local/bin/generate_gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt_lods

```bash
$ singularity exec <container> /usr/local/bin/gt_lods
$ podman run --it --rm --entrypoint /usr/local/bin/gt_lods   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt_lods   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibdmix

```bash
$ singularity exec <container> /usr/local/bin/ibdmix
$ podman run --it --rm --entrypoint /usr/local/bin/ibdmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibdmix   -v ${PWD} -w ${PWD} <container> -c " $@"
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