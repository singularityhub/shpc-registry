---
layout: container
name:  "quay.io/biocontainers/cat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cat/container.yaml"
updated_at: "2025-10-03 03:19:01.795745"
latest: "6.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/cat"
aliases:
 - "CAT"
 - "bzcat"
 - "lz4cat"
 - "lzcat"
 - "xzcat"
 - "zstdcat"
 - "diamond"
 - "prodigal"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "5.2.3--hdfd78af_1"
 - "5.3--hdfd78af_0"
 - "6.0.1--hdfd78af_0"
 - "6.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for cat"
config: {"url": "https://biocontainers.pro/tools/cat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cat", "latest": {"6.0.1--hdfd78af_1": "sha256:46141a8b0571c83aeb2021b1a1a6aada752e3b36e71f00458bf1f291f3513e1b"}, "tags": {"5.2.3--hdfd78af_1": "sha256:b3992ecb211f6d2ab5d87cb6d19941ce9e5040fbb9551d0afe46d5e54c4cd971", "5.3--hdfd78af_0": "sha256:df32b3c754d6b8d4242eed88e653b1bfd4a84aa3571bb8815a31efb916665e7d", "6.0.1--hdfd78af_0": "sha256:b49a7ea99ee9c0ec761a0ecd1c65e9422be83377489121192f35f8cadae1a0c4", "6.0.1--hdfd78af_1": "sha256:46141a8b0571c83aeb2021b1a1a6aada752e3b36e71f00458bf1f291f3513e1b"}, "docker": "quay.io/biocontainers/cat", "aliases": {"CAT": "/usr/local/bin/CAT", "bzcat": "/usr/local/bin/bzcat", "lz4cat": "/usr/local/bin/lz4cat", "lzcat": "/usr/local/bin/lzcat", "xzcat": "/usr/local/bin/xzcat", "zstdcat": "/usr/local/bin/zstdcat", "diamond": "/usr/local/bin/diamond", "prodigal": "/usr/local/bin/prodigal", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cat.
shpc-registry automated BioContainers addition for cat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cat:6.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cat/6.0.1--hdfd78af_1
$ module help quay.io/biocontainers/cat/6.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CAT

```bash
$ singularity exec <container> /usr/local/bin/CAT
$ podman run --it --rm --entrypoint /usr/local/bin/CAT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CAT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzcat

```bash
$ singularity exec <container> /usr/local/bin/bzcat
$ podman run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lz4cat

```bash
$ singularity exec <container> /usr/local/bin/lz4cat
$ podman run --it --rm --entrypoint /usr/local/bin/lz4cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lz4cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lzcat

```bash
$ singularity exec <container> /usr/local/bin/lzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzcat

```bash
$ singularity exec <container> /usr/local/bin/xzcat
$ podman run --it --rm --entrypoint /usr/local/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zstdcat

```bash
$ singularity exec <container> /usr/local/bin/zstdcat
$ podman run --it --rm --entrypoint /usr/local/bin/zstdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zstdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
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