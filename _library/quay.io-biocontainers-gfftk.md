---
layout: container
name:  "quay.io/biocontainers/gfftk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfftk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfftk/container.yaml"
updated_at: "2024-12-24 03:30:25.625637"
latest: "24.10.30--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gfftk"
aliases:
 - "gfftk"
 - "table2asn"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "natsort"
versions:
 - "23.9.6--pyhdfd78af_0"
 - "23.12.5--pyhdfd78af_0"
 - "24.2.4--pyhdfd78af_0"
 - "24.10.30--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gfftk"
config: {"url": "https://biocontainers.pro/tools/gfftk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfftk", "latest": {"24.10.30--pyhdfd78af_0": "sha256:60cd05398abb849fe88920334b7815c85750bd6ad3d10f96e8644283f626ebc7"}, "tags": {"23.9.6--pyhdfd78af_0": "sha256:7f95a7662694bd17189f1fac7be32213b1fd737c4a53009ca34203a7e3d9d89a", "23.12.5--pyhdfd78af_0": "sha256:f3b42a8eeb360a5cbe27ae99c650d3ef098d7da8c8244e34c91dcd0a12ec2494", "24.2.4--pyhdfd78af_0": "sha256:1135e3ea6841e91f28efc9251c6f5a6f35a24e2034d590e72e185d8cc27b233d", "24.10.30--pyhdfd78af_0": "sha256:60cd05398abb849fe88920334b7815c85750bd6ad3d10f96e8644283f626ebc7"}, "docker": "quay.io/biocontainers/gfftk", "aliases": {"gfftk": "/usr/local/bin/gfftk", "table2asn": "/usr/local/bin/table2asn", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "natsort": "/usr/local/bin/natsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfftk.
singularity registry hpc automated addition for gfftk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfftk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfftk:24.10.30--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfftk/24.10.30--pyhdfd78af_0
$ module help quay.io/biocontainers/gfftk/24.10.30--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfftk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfftk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfftk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfftk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfftk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfftk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfftk

```bash
$ singularity exec <container> /usr/local/bin/gfftk
$ podman run --it --rm --entrypoint /usr/local/bin/gfftk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfftk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### table2asn

```bash
$ singularity exec <container> /usr/local/bin/table2asn
$ podman run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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