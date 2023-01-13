---
layout: container
name:  "quay.io/biocontainers/openduck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/openduck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/openduck/container.yaml"
updated_at: "2023-01-13 03:03:13.106548"
latest: "0.1.2--py_0"
container_url: "https://biocontainers.pro/tools/openduck"
aliases:
 - "duck_chunk"
 - "duck_prepare_sys"
 - "duck_smd_runs"
 - "frag_duck"
 - "get_wqb"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.1.2--py_0"
description: "shpc-registry automated BioContainers addition for openduck"
config: {"url": "https://biocontainers.pro/tools/openduck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for openduck", "latest": {"0.1.2--py_0": "sha256:28c0db678edbdeec5c7e8f1e54cdf8616b6af860af4920ccf82c6cc4991f50f7"}, "tags": {"0.1.2--py_0": "sha256:28c0db678edbdeec5c7e8f1e54cdf8616b6af860af4920ccf82c6cc4991f50f7"}, "docker": "quay.io/biocontainers/openduck", "aliases": {"duck_chunk": "/usr/local/bin/duck_chunk", "duck_prepare_sys": "/usr/local/bin/duck_prepare_sys", "duck_smd_runs": "/usr/local/bin/duck_smd_runs", "frag_duck": "/usr/local/bin/frag_duck", "get_wqb": "/usr/local/bin/get_wqb", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/openduck.
shpc-registry automated BioContainers addition for openduck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/openduck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/openduck:0.1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/openduck/0.1.2--py_0
$ module help quay.io/biocontainers/openduck/0.1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openduck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openduck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openduck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openduck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openduck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openduck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### duck_chunk

```bash
$ singularity exec <container> /usr/local/bin/duck_chunk
$ podman run --it --rm --entrypoint /usr/local/bin/duck_chunk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duck_chunk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duck_prepare_sys

```bash
$ singularity exec <container> /usr/local/bin/duck_prepare_sys
$ podman run --it --rm --entrypoint /usr/local/bin/duck_prepare_sys   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duck_prepare_sys   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duck_smd_runs

```bash
$ singularity exec <container> /usr/local/bin/duck_smd_runs
$ podman run --it --rm --entrypoint /usr/local/bin/duck_smd_runs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duck_smd_runs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frag_duck

```bash
$ singularity exec <container> /usr/local/bin/frag_duck
$ podman run --it --rm --entrypoint /usr/local/bin/frag_duck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frag_duck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_wqb

```bash
$ singularity exec <container> /usr/local/bin/get_wqb
$ podman run --it --rm --entrypoint /usr/local/bin/get_wqb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_wqb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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