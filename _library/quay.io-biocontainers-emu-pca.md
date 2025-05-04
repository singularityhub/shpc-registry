---
layout: container
name:  "quay.io/biocontainers/emu-pca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/emu-pca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/emu-pca/container.yaml"
updated_at: "2025-05-04 03:45:41.152055"
latest: "1.2.1--py312hc9302aa_0"
container_url: "https://biocontainers.pro/tools/emu-pca"
aliases:
 - "emu"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.0--py310h581d4b6_1"
 - "1.0--py312h1f1cfbb_1"
 - "1.1--py310h581d4b6_0"
 - "1.1--py310h20b60a1_1"
 - "1.2.1--py312hc9302aa_0"
description: "singularity registry hpc automated addition for emu-pca"
config: {"url": "https://biocontainers.pro/tools/emu-pca", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for emu-pca", "latest": {"1.2.1--py312hc9302aa_0": "sha256:381482bdaf3d2278e46787da3f490405c59f98786892b0acbf1e40050ae0ad35"}, "tags": {"1.0--py310h581d4b6_1": "sha256:fa78041d8e23d2d0b5a3fac6235bf3f62ddab1f24763c31a19e7251dc3d49376", "1.0--py312h1f1cfbb_1": "sha256:1e48f2f9058bedb8bffee7f8b9b8798ffe31f6c05a26ac39fc60af84ddb47504", "1.1--py310h581d4b6_0": "sha256:4af9c03456277fd7af82b28230e66bb3630f6088cfadcf0b0f1477d90bad8968", "1.1--py310h20b60a1_1": "sha256:ea5fcd2f442eec59210db7bb6baa67d481fedf2e70cc157a885f3cdc6d99a589", "1.2.1--py312hc9302aa_0": "sha256:381482bdaf3d2278e46787da3f490405c59f98786892b0acbf1e40050ae0ad35"}, "docker": "quay.io/biocontainers/emu-pca", "aliases": {"emu": "/usr/local/bin/emu", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/emu-pca.
singularity registry hpc automated addition for emu-pca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/emu-pca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/emu-pca:1.2.1--py312hc9302aa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/emu-pca/1.2.1--py312hc9302aa_0
$ module help quay.io/biocontainers/emu-pca/1.2.1--py312hc9302aa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emu-pca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emu-pca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emu-pca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emu-pca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emu-pca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emu-pca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### emu

```bash
$ singularity exec <container> /usr/local/bin/emu
$ podman run --it --rm --entrypoint /usr/local/bin/emu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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