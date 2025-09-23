---
layout: container
name:  "quay.io/biocontainers/mypmfs_py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mypmfs_py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mypmfs_py/container.yaml"
updated_at: "2025-09-23 03:03:11.638184"
latest: "0.1.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mypmfs_py"
aliases:
 - "mypmfs_py"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.1.7--pyhdfd78af_0"
 - "0.1.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mypmfs_py"
config: {"url": "https://biocontainers.pro/tools/mypmfs_py", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mypmfs_py", "latest": {"0.1.8--pyhdfd78af_0": "sha256:74807605cff9f91f6e95428daed4354799c81df247e269680257ae20cd6e1a23"}, "tags": {"0.1.7--pyhdfd78af_0": "sha256:30cee1ca9a79df5ab402309abe273ba54d51040abf674382b44a6865f2ff46de", "0.1.8--pyhdfd78af_0": "sha256:74807605cff9f91f6e95428daed4354799c81df247e269680257ae20cd6e1a23"}, "docker": "quay.io/biocontainers/mypmfs_py", "aliases": {"mypmfs_py": "/usr/local/bin/mypmfs_py", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mypmfs_py.
singularity registry hpc automated addition for mypmfs_py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mypmfs_py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mypmfs_py:0.1.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mypmfs_py/0.1.8--pyhdfd78af_0
$ module help quay.io/biocontainers/mypmfs_py/0.1.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mypmfs_py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mypmfs_py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mypmfs_py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mypmfs_py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mypmfs_py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mypmfs_py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mypmfs_py

```bash
$ singularity exec <container> /usr/local/bin/mypmfs_py
$ podman run --it --rm --entrypoint /usr/local/bin/mypmfs_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mypmfs_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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