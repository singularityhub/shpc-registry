---
layout: container
name:  "quay.io/biocontainers/decodiphy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/decodiphy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/decodiphy/container.yaml"
updated_at: "2026-06-26 07:01:03.606172"
latest: "1.4.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/decodiphy"
aliases:
 - "decodiphy"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.2.3--pyhdfd78af_0"
 - "1.3.3--pyhdfd78af_0"
 - "1.4.1--pyhdfd78af_1"
description: "singularity registry hpc automated addition for decodiphy"
config: {"url": "https://biocontainers.pro/tools/decodiphy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for decodiphy", "latest": {"1.4.1--pyhdfd78af_1": "sha256:05991e56d89d8f4e078939bb69bb8bb5ef8d6cd9ac4620826206e4a910bc83f8"}, "tags": {"1.2.3--pyhdfd78af_0": "sha256:caef315da2b290f91952a7a4a221fc1a991da7fdcebb596a549e6641ff008838", "1.3.3--pyhdfd78af_0": "sha256:207da6c5e00ec81373bb54789e57066a6641c3c14bc17c45efb4987744dc36b3", "1.4.1--pyhdfd78af_1": "sha256:05991e56d89d8f4e078939bb69bb8bb5ef8d6cd9ac4620826206e4a910bc83f8"}, "docker": "quay.io/biocontainers/decodiphy", "aliases": {"decodiphy": "/usr/local/bin/decodiphy", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/decodiphy.
singularity registry hpc automated addition for decodiphy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/decodiphy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/decodiphy:1.4.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/decodiphy/1.4.1--pyhdfd78af_1
$ module help quay.io/biocontainers/decodiphy/1.4.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### decodiphy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### decodiphy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### decodiphy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### decodiphy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### decodiphy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### decodiphy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### decodiphy

```bash
$ singularity exec <container> /usr/local/bin/decodiphy
$ podman run --it --rm --entrypoint /usr/local/bin/decodiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/decodiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
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