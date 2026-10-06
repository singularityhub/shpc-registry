---
layout: container
name:  "quay.io/biocontainers/mgnifam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgnifam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgnifam/container.yaml"
updated_at: "2026-10-06 09:29:24.218661"
latest: "4.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mgnifam"
aliases:
 - "mgnifam"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "2.0.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "3.1.0--pyhdfd78af_0"
 - "3.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mgnifam"
config: {"url": "https://biocontainers.pro/tools/mgnifam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mgnifam", "latest": {"4.0.0--pyhdfd78af_0": "sha256:b20f78cff92cc73ac15168e11228244ca8362b355cbc35675523e036564eb3fe"}, "tags": {"2.0.0--pyhdfd78af_0": "sha256:b71d052ee18921c9b7a01da9e0ee4a2a8139ccdce7016e194ba898c0212c1947", "4.0.0--pyhdfd78af_0": "sha256:b20f78cff92cc73ac15168e11228244ca8362b355cbc35675523e036564eb3fe", "3.1.0--pyhdfd78af_0": "sha256:7f24816a0d561da8406f8482b550bc5686e82f0c0b388a31d6069f056e2c0c09", "3.0.0--pyhdfd78af_0": "sha256:eb5318160e53aae9c0cdae616b162d3abbc58c24f992923b13572d9e31597cda"}, "docker": "quay.io/biocontainers/mgnifam", "aliases": {"mgnifam": "/usr/local/bin/mgnifam", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgnifam.
singularity registry hpc automated addition for mgnifam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgnifam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgnifam:4.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgnifam/4.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mgnifam/4.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgnifam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgnifam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgnifam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgnifam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgnifam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgnifam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mgnifam

```bash
$ singularity exec <container> /usr/local/bin/mgnifam
$ podman run --it --rm --entrypoint /usr/local/bin/mgnifam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgnifam   -v ${PWD} -w ${PWD} <container> -c " $@"
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