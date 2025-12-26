---
layout: container
name:  "quay.io/biocontainers/allelecodes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/allelecodes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/allelecodes/container.yaml"
updated_at: "2025-12-26 04:22:33.133089"
latest: "2.1--py313hdfd78af_0"
container_url: "https://biocontainers.pro/tools/allelecodes"
aliases:
 - "assignAlleleCodes"
 - "assignAlleleCodes_py3.6.py"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "2.1--py313hdfd78af_0"
description: "singularity registry hpc automated addition for allelecodes"
config: {"url": "https://biocontainers.pro/tools/allelecodes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for allelecodes", "latest": {"2.1--py313hdfd78af_0": "sha256:486ef8acd57c35d90bc9143545cd76613eb80d06a20bf7b4d1d97ed82f076174"}, "tags": {"2.1--py313hdfd78af_0": "sha256:486ef8acd57c35d90bc9143545cd76613eb80d06a20bf7b4d1d97ed82f076174"}, "docker": "quay.io/biocontainers/allelecodes", "aliases": {"assignAlleleCodes": "/usr/local/bin/assignAlleleCodes", "assignAlleleCodes_py3.6.py": "/usr/local/bin/assignAlleleCodes_py3.6.py", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/allelecodes.
singularity registry hpc automated addition for allelecodes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/allelecodes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/allelecodes:2.1--py313hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/allelecodes/2.1--py313hdfd78af_0
$ module help quay.io/biocontainers/allelecodes/2.1--py313hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### allelecodes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### allelecodes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### allelecodes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### allelecodes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### allelecodes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### allelecodes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assignAlleleCodes

```bash
$ singularity exec <container> /usr/local/bin/assignAlleleCodes
$ podman run --it --rm --entrypoint /usr/local/bin/assignAlleleCodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assignAlleleCodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assignAlleleCodes_py3.6.py

```bash
$ singularity exec <container> /usr/local/bin/assignAlleleCodes_py3.6.py
$ podman run --it --rm --entrypoint /usr/local/bin/assignAlleleCodes_py3.6.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assignAlleleCodes_py3.6.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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