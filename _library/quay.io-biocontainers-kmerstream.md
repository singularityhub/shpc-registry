---
layout: container
name:  "quay.io/biocontainers/kmerstream"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmerstream/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmerstream/container.yaml"
updated_at: "2024-01-01 03:18:32.971777"
latest: "1.1--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/kmerstream"
aliases:
 - "KmerStream"
 - "KmerStreamEstimate.py"
 - "KmerStreamJoin"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.1--hd03093a_3"
 - "1.1--hd03093a_4"
 - "1.1--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for kmerstream"
config: {"url": "https://biocontainers.pro/tools/kmerstream", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmerstream", "latest": {"1.1--hdcf5f25_5": "sha256:46fae3d2c60bcd5eceb3a4b0f1fb04a29801ebb182d5bd2372113615e64e81f1"}, "tags": {"1.1--hd03093a_3": "sha256:0e23b0fd1581335b41e230e6acedaafb6576d8187b75021da9b7a27c5edbc596", "1.1--hd03093a_4": "sha256:5eac6f283be6d2176b24ce61aaf9e56f9ed4650bce2df5e7ceab954926a5ba42", "1.1--hdcf5f25_5": "sha256:46fae3d2c60bcd5eceb3a4b0f1fb04a29801ebb182d5bd2372113615e64e81f1"}, "docker": "quay.io/biocontainers/kmerstream", "aliases": {"KmerStream": "/usr/local/bin/KmerStream", "KmerStreamEstimate.py": "/usr/local/bin/KmerStreamEstimate.py", "KmerStreamJoin": "/usr/local/bin/KmerStreamJoin", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmerstream.
shpc-registry automated BioContainers addition for kmerstream
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmerstream
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmerstream:1.1--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmerstream/1.1--hdcf5f25_5
$ module help quay.io/biocontainers/kmerstream/1.1--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmerstream-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmerstream-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmerstream-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmerstream-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmerstream-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmerstream-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### KmerStream

```bash
$ singularity exec <container> /usr/local/bin/KmerStream
$ podman run --it --rm --entrypoint /usr/local/bin/KmerStream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerStream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerStreamEstimate.py

```bash
$ singularity exec <container> /usr/local/bin/KmerStreamEstimate.py
$ podman run --it --rm --entrypoint /usr/local/bin/KmerStreamEstimate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerStreamEstimate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerStreamJoin

```bash
$ singularity exec <container> /usr/local/bin/KmerStreamJoin
$ podman run --it --rm --entrypoint /usr/local/bin/KmerStreamJoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerStreamJoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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