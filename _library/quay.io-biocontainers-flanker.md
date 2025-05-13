---
layout: container
name:  "quay.io/biocontainers/flanker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flanker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flanker/container.yaml"
updated_at: "2025-05-13 03:36:48.648468"
latest: "0.1.5--py_0"
container_url: "https://biocontainers.pro/tools/flanker"
aliases:
 - "abricate"
 - "abricate-get_db"
 - "flanker"
 - "any2fasta"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
versions:
 - "0.1.5--py_0"
description: "shpc-registry automated BioContainers addition for flanker"
config: {"url": "https://biocontainers.pro/tools/flanker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flanker", "latest": {"0.1.5--py_0": "sha256:9bdedadf71d11b3003d0e406a27f23becb944c803aa52fd732ad5beaf608aa89"}, "tags": {"0.1.5--py_0": "sha256:9bdedadf71d11b3003d0e406a27f23becb944c803aa52fd732ad5beaf608aa89"}, "docker": "quay.io/biocontainers/flanker", "aliases": {"abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "flanker": "/usr/local/bin/flanker", "any2fasta": "/usr/local/bin/any2fasta", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flanker.
shpc-registry automated BioContainers addition for flanker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flanker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flanker:0.1.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flanker/0.1.5--py_0
$ module help quay.io/biocontainers/flanker/0.1.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flanker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flanker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flanker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flanker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flanker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flanker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flanker

```bash
$ singularity exec <container> /usr/local/bin/flanker
$ podman run --it --rm --entrypoint /usr/local/bin/flanker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flanker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
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