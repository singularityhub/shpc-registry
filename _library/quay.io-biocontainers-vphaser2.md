---
layout: container
name:  "quay.io/biocontainers/vphaser2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vphaser2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vphaser2/container.yaml"
updated_at: "2024-09-30 04:48:31.748644"
latest: "2.0--h2d38e66_13"
container_url: "https://biocontainers.pro/tools/vphaser2"
aliases:
 - "variant_caller"
 - "vphaser2"
 - "bamtools"
versions:
 - "2.0--h22a709c_9"
 - "2.0--h1b026d1_11"
 - "2.0--h1b026d1_12"
 - "2.0--h2d38e66_13"
description: "shpc-registry automated BioContainers addition for vphaser2"
config: {"url": "https://biocontainers.pro/tools/vphaser2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vphaser2", "latest": {"2.0--h2d38e66_13": "sha256:105584e22a039010ee172ff2803078b46fe4d3dffa70b60434e5447a58c46fc7"}, "tags": {"2.0--h22a709c_9": "sha256:38ed87b31e9d6aefb26c3071f71e8678467b7d52c63ce3925e940022db956fd7", "2.0--h1b026d1_11": "sha256:918ac4c76056e7a5542e38216bce3d52c24db0ec142b5428c86bf1c01629dd60", "2.0--h1b026d1_12": "sha256:4805d8dda8fe1830c3368bb8f1957d0a0ddb25c367235b4d3eef7866d9da137d", "2.0--h2d38e66_13": "sha256:105584e22a039010ee172ff2803078b46fe4d3dffa70b60434e5447a58c46fc7"}, "docker": "quay.io/biocontainers/vphaser2", "aliases": {"variant_caller": "/usr/local/bin/variant_caller", "vphaser2": "/usr/local/bin/vphaser2", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vphaser2.
shpc-registry automated BioContainers addition for vphaser2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vphaser2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vphaser2:2.0--h2d38e66_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vphaser2/2.0--h2d38e66_13
$ module help quay.io/biocontainers/vphaser2/2.0--h2d38e66_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vphaser2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vphaser2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vphaser2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vphaser2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vphaser2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vphaser2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### variant_caller

```bash
$ singularity exec <container> /usr/local/bin/variant_caller
$ podman run --it --rm --entrypoint /usr/local/bin/variant_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vphaser2

```bash
$ singularity exec <container> /usr/local/bin/vphaser2
$ podman run --it --rm --entrypoint /usr/local/bin/vphaser2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vphaser2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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