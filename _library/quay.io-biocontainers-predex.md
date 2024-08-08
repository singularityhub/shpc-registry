---
layout: container
name:  "quay.io/biocontainers/predex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/predex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/predex/container.yaml"
updated_at: "2024-08-08 04:24:12.798353"
latest: "0.9.3--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/predex"
aliases:
 - "predex"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.9.3--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for predex"
config: {"url": "https://biocontainers.pro/tools/predex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for predex", "latest": {"0.9.3--pyh5e36f6f_0": "sha256:a629326ed726c76aebc5e66e34f10cfaacb6cd4911567791e504484d89c0fb0c"}, "tags": {"0.9.3--pyh5e36f6f_0": "sha256:a629326ed726c76aebc5e66e34f10cfaacb6cd4911567791e504484d89c0fb0c"}, "docker": "quay.io/biocontainers/predex", "aliases": {"predex": "/usr/local/bin/predex", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/predex.
shpc-registry automated BioContainers addition for predex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/predex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/predex:0.9.3--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/predex/0.9.3--pyh5e36f6f_0
$ module help quay.io/biocontainers/predex/0.9.3--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### predex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### predex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### predex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### predex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### predex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### predex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### predex

```bash
$ singularity exec <container> /usr/local/bin/predex
$ podman run --it --rm --entrypoint /usr/local/bin/predex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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