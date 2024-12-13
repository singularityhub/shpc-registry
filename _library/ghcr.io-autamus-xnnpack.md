---
layout: container
name:  "ghcr.io/autamus/xnnpack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/xnnpack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/xnnpack/container.yaml"
updated_at: "2024-12-13 03:05:33.971704"
latest: "2022.02.16"
container_url: "https://github.com/orgs/autamus/packages/container/package/xnnpack"

versions:
 - "2021.02.22"
 - "latest"
 - "2022.02.16"
description: "High-efficiency floating-point neural network inference operators for mobile, server, and Web"
config: {"docker": "ghcr.io/autamus/xnnpack", "url": "https://github.com/orgs/autamus/packages/container/package/xnnpack", "maintainer": "@vsoch", "description": "High-efficiency floating-point neural network inference operators for mobile, server, and Web", "latest": {"2022.02.16": "sha256:4d09e10aa897e4cda55ec21f4c104073ae6099b9c48a2230ce8f5dbdad5a1329"}, "tags": {"2021.02.22": "sha256:73c567e8a950b820fb8e1bdbd623a601869ab2c634ecd5790cc0af4dbb53dee0", "latest": "sha256:4d09e10aa897e4cda55ec21f4c104073ae6099b9c48a2230ce8f5dbdad5a1329", "2022.02.16": "sha256:4d09e10aa897e4cda55ec21f4c104073ae6099b9c48a2230ce8f5dbdad5a1329"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/xnnpack.
High-efficiency floating-point neural network inference operators for mobile, server, and Web
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/xnnpack
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/xnnpack:2022.02.16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/xnnpack/2022.02.16
$ module help ghcr.io/autamus/xnnpack/2022.02.16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xnnpack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xnnpack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xnnpack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xnnpack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xnnpack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xnnpack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### xnnpack

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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