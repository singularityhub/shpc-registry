---
layout: container
name:  "quay.io/biocontainers/bistreroc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bistreroc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bistreroc/container.yaml"
updated_at: "2026-10-10 19:07:31.537130"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bistreroc"
aliases:
 - "bistreroc"
 - "fc-genconf"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "x86_64-conda-linux-gnu.cfg"
 - "numpy-config"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bistreroc"
config: {"url": "https://biocontainers.pro/tools/bistreroc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bistreroc", "latest": {"0.1.0--pyhdfd78af_0": "sha256:f98026866d159303b3a6f303c0cfb43ecebf86b3a18fc290086c480f3ba4c2f4"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:f98026866d159303b3a6f303c0cfb43ecebf86b3a18fc290086c480f3ba4c2f4"}, "docker": "quay.io/biocontainers/bistreroc", "aliases": {"bistreroc": "/usr/local/bin/bistreroc", "fc-genconf": "/usr/local/bin/fc-genconf", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bistreroc.
singularity registry hpc automated addition for bistreroc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bistreroc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bistreroc:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bistreroc/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/bistreroc/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bistreroc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bistreroc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bistreroc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bistreroc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bistreroc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bistreroc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bistreroc

```bash
$ singularity exec <container> /usr/local/bin/bistreroc
$ podman run --it --rm --entrypoint /usr/local/bin/bistreroc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bistreroc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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