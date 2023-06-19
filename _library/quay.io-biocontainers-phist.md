---
layout: container
name:  "quay.io/biocontainers/phist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phist/container.yaml"
updated_at: "2023-06-19 03:29:03.562070"
latest: "1.0.0--py310hd03093a_0"
container_url: "https://biocontainers.pro/tools/phist"
aliases:
 - "kmer-db"
 - "phist"
 - "phist.py"
 - "matcher"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.0.0--py310hd03093a_0"
description: "singularity registry hpc automated addition for phist"
config: {"url": "https://biocontainers.pro/tools/phist", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phist", "latest": {"1.0.0--py310hd03093a_0": "sha256:d497c280cb71ec4231c99a7df31e1d7de1b745fdba97231cbfa7c682bcd88b7d"}, "tags": {"1.0.0--py310hd03093a_0": "sha256:d497c280cb71ec4231c99a7df31e1d7de1b745fdba97231cbfa7c682bcd88b7d"}, "docker": "quay.io/biocontainers/phist", "aliases": {"kmer-db": "/usr/local/bin/kmer-db", "phist": "/usr/local/bin/phist", "phist.py": "/usr/local/bin/phist.py", "matcher": "/usr/local/bin/matcher", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phist.
singularity registry hpc automated addition for phist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phist:1.0.0--py310hd03093a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phist/1.0.0--py310hd03093a_0
$ module help quay.io/biocontainers/phist/1.0.0--py310hd03093a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmer-db

```bash
$ singularity exec <container> /usr/local/bin/kmer-db
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist

```bash
$ singularity exec <container> /usr/local/bin/phist
$ podman run --it --rm --entrypoint /usr/local/bin/phist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist.py

```bash
$ singularity exec <container> /usr/local/bin/phist.py
$ podman run --it --rm --entrypoint /usr/local/bin/phist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matcher

```bash
$ singularity exec <container> /usr/local/bin/matcher
$ podman run --it --rm --entrypoint /usr/local/bin/matcher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matcher   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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