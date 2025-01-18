---
layout: container
name:  "quay.io/biocontainers/codingorf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/codingorf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/codingorf/container.yaml"
updated_at: "2025-01-18 03:18:22.585200"
latest: "v1.0.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/codingorf"
aliases:
 - "codingorf"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "v1.0.0--pyh5e36f6f_0"
 - "1.0.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for codingorf"
config: {"url": "https://biocontainers.pro/tools/codingorf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for codingorf", "latest": {"v1.0.0--pyh5e36f6f_0": "sha256:9f6b9702b32921f712a8f5ec0aef60ef1044ca746c5be70d7b710625be965999"}, "tags": {"v1.0.0--pyh5e36f6f_0": "sha256:9f6b9702b32921f712a8f5ec0aef60ef1044ca746c5be70d7b710625be965999", "1.0.0--pyh5e36f6f_0": "sha256:565da739962e22fa43aa5ed6e0ee2309ad48f2dbbfaaef00e5575aa84302e524"}, "docker": "quay.io/biocontainers/codingorf", "aliases": {"codingorf": "/usr/local/bin/codingorf", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/codingorf.
shpc-registry automated BioContainers addition for codingorf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/codingorf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/codingorf:v1.0.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/codingorf/v1.0.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/codingorf/v1.0.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### codingorf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### codingorf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### codingorf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### codingorf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### codingorf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### codingorf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### codingorf

```bash
$ singularity exec <container> /usr/local/bin/codingorf
$ podman run --it --rm --entrypoint /usr/local/bin/codingorf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codingorf   -v ${PWD} -w ${PWD} <container> -c " $@"
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