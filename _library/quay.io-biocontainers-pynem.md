---
layout: container
name:  "quay.io/biocontainers/pynem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pynem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pynem/container.yaml"
updated_at: "2026-11-06 09:35:12.160895"
latest: "0.6.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pynem"
aliases:
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "numpy-config"
versions:
 - "0.6.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pynem"
config: {"url": "https://biocontainers.pro/tools/pynem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pynem", "latest": {"0.6.1--pyhdfd78af_0": "sha256:a37502ba17b7ed3c4f8c19fea3dfd13dd965992fca7257490dfbdbb44b8bc3fd"}, "tags": {"0.6.1--pyhdfd78af_0": "sha256:a37502ba17b7ed3c4f8c19fea3dfd13dd965992fca7257490dfbdbb44b8bc3fd"}, "docker": "quay.io/biocontainers/pynem", "aliases": {"idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pynem.
singularity registry hpc automated addition for pynem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pynem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pynem:0.6.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pynem/0.6.1--pyhdfd78af_0
$ module help quay.io/biocontainers/pynem/0.6.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pynem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pynem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pynem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pynem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pynem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pynem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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