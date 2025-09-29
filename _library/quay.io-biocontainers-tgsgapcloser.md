---
layout: container
name:  "quay.io/biocontainers/tgsgapcloser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tgsgapcloser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tgsgapcloser/container.yaml"
updated_at: "2025-09-29 03:47:52.372435"
latest: "1.2.1--h6f25541_4"
container_url: "https://biocontainers.pro/tools/tgsgapcloser"
aliases:
 - "tgsgapcloser"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
versions:
 - "1.0.3--h5b5514e_2"
 - "1.2.1--h5b5514e_0"
 - "1.2.1--h5b5514e_1"
 - "1.2.1--hdb21b49_2"
 - "1.2.1--h6f25541_4"
description: "shpc-registry automated BioContainers addition for tgsgapcloser"
config: {"url": "https://biocontainers.pro/tools/tgsgapcloser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tgsgapcloser", "latest": {"1.2.1--h6f25541_4": "sha256:8d3a913269be74119a770b14813c43b2d01c2bd1521f9f5f781a3005c9d78191"}, "tags": {"1.0.3--h5b5514e_2": "sha256:1fc88341f01e741a698333ca9f885fd612aa8068833143f8ec4bf6884ee20b02", "1.2.1--h5b5514e_0": "sha256:b068a33532204d9d16428933040de7d52a98ef630eea8aa73f0f854c1e7d0ea2", "1.2.1--h5b5514e_1": "sha256:d8db4efcd6ed2d41273132304e25817783de9d2ca8fd77f3d9145a878a73c1ba", "1.2.1--hdb21b49_2": "sha256:a395e575ab90a72ae07da6e69e15e1ee93454c5082b3aa15386f0bf8817b993e", "1.2.1--h6f25541_4": "sha256:8d3a913269be74119a770b14813c43b2d01c2bd1521f9f5f781a3005c9d78191"}, "docker": "quay.io/biocontainers/tgsgapcloser", "aliases": {"tgsgapcloser": "/usr/local/bin/tgsgapcloser", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tgsgapcloser.
shpc-registry automated BioContainers addition for tgsgapcloser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tgsgapcloser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tgsgapcloser:1.2.1--h6f25541_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tgsgapcloser/1.2.1--h6f25541_4
$ module help quay.io/biocontainers/tgsgapcloser/1.2.1--h6f25541_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tgsgapcloser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tgsgapcloser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tgsgapcloser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tgsgapcloser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tgsgapcloser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tgsgapcloser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tgsgapcloser

```bash
$ singularity exec <container> /usr/local/bin/tgsgapcloser
$ podman run --it --rm --entrypoint /usr/local/bin/tgsgapcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tgsgapcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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