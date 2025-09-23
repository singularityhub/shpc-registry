---
layout: container
name:  "quay.io/biocontainers/demultiplexer2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/demultiplexer2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/demultiplexer2/container.yaml"
updated_at: "2025-09-23 04:54:13.033226"
latest: "1.1.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/demultiplexer2"
aliases:
 - "demultiplexer2"
 - "luddite"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tqdm"
versions:
 - "1.1.5--pyhdfd78af_0"
 - "1.1.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for demultiplexer2"
config: {"url": "https://biocontainers.pro/tools/demultiplexer2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for demultiplexer2", "latest": {"1.1.6--pyhdfd78af_0": "sha256:bd7cf187d6773b0844a81e6994fb5a51d1ec073c2a8e6305d6a6215ca4d7d4dd"}, "tags": {"1.1.5--pyhdfd78af_0": "sha256:1db6976ac6d04ca0b9ed8b630774ab0b47e8064be89d49906f036cf26cfecbd2", "1.1.6--pyhdfd78af_0": "sha256:bd7cf187d6773b0844a81e6994fb5a51d1ec073c2a8e6305d6a6215ca4d7d4dd"}, "docker": "quay.io/biocontainers/demultiplexer2", "aliases": {"demultiplexer2": "/usr/local/bin/demultiplexer2", "luddite": "/usr/local/bin/luddite", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/demultiplexer2.
singularity registry hpc automated addition for demultiplexer2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/demultiplexer2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/demultiplexer2:1.1.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/demultiplexer2/1.1.6--pyhdfd78af_0
$ module help quay.io/biocontainers/demultiplexer2/1.1.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### demultiplexer2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### demultiplexer2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### demultiplexer2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### demultiplexer2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### demultiplexer2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### demultiplexer2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### demultiplexer2

```bash
$ singularity exec <container> /usr/local/bin/demultiplexer2
$ podman run --it --rm --entrypoint /usr/local/bin/demultiplexer2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demultiplexer2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luddite

```bash
$ singularity exec <container> /usr/local/bin/luddite
$ podman run --it --rm --entrypoint /usr/local/bin/luddite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luddite   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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