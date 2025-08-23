---
layout: container
name:  "quay.io/biocontainers/gtdbtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gtdbtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gtdbtk/container.yaml"
updated_at: "2025-08-23 03:41:08.254195"
latest: "2.4.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/gtdbtk"
aliases:
 - "download-db.sh"
 - "gtdbtk"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "fastANI"
 - "dendropy-format"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
versions:
 - "2.1.1--pyhdfd78af_1"
 - "2.2.4--pyhdfd78af_0"
 - "2.2.5--pyhdfd78af_0"
 - "2.3.2--pyhdfd78af_0"
 - "2.2.6--pyhdfd78af_1"
 - "2.4.0--pyhdfd78af_1"
 - "2.4.0--pyhdfd78af_2"
 - "2.4.1--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for gtdbtk"
config: {"url": "https://biocontainers.pro/tools/gtdbtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gtdbtk", "latest": {"2.4.1--pyhdfd78af_1": "sha256:f5fa73861f8ea6db1ae2399487c2eae808fc4347360b7b1fc220e02b20c8c57b"}, "tags": {"2.1.1--pyhdfd78af_1": "sha256:8a3f3b4416fb8c01f7c3c73cb05309c6b85d81a9028f8db8f9ef783e72c63bcb", "2.2.4--pyhdfd78af_0": "sha256:d764fd7c96a5432ba0cd6f0a26f95eded43bf4ede59f9d07ddd2e8b9c5b1e33a", "2.2.5--pyhdfd78af_0": "sha256:b80d22d8e73b4fdc78421a7c079f32071c4f08bbf444b8b1ee29622b6d8e394b", "2.3.2--pyhdfd78af_0": "sha256:7bf2afebb6899138b313133995269aa3fc1df4a9ec9aa019577aa98bc66ab517", "2.2.6--pyhdfd78af_1": "sha256:a00fe47cbc1a74026fb2506bdd92c35153a4929e8c61dfb52d5739536f6564a6", "2.4.0--pyhdfd78af_1": "sha256:c2de30bd02c2be74e607ce3ca98ad1bd88a1eafaa0c805f507efd77171f8e5d7", "2.4.0--pyhdfd78af_2": "sha256:14b6d86a7d9fa45feff6be2b083ff28e928d70c336638919178fabae0935b24e", "2.4.1--pyhdfd78af_1": "sha256:f5fa73861f8ea6db1ae2399487c2eae808fc4347360b7b1fc220e02b20c8c57b"}, "docker": "quay.io/biocontainers/gtdbtk", "aliases": {"download-db.sh": "/usr/local/bin/download-db.sh", "gtdbtk": "/usr/local/bin/gtdbtk", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "fastANI": "/usr/local/bin/fastANI", "dendropy-format": "/usr/local/bin/dendropy-format", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gtdbtk.
shpc-registry automated BioContainers addition for gtdbtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gtdbtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gtdbtk:2.4.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gtdbtk/2.4.1--pyhdfd78af_1
$ module help quay.io/biocontainers/gtdbtk/2.4.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gtdbtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gtdbtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gtdbtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gtdbtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gtdbtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gtdbtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### download-db.sh

```bash
$ singularity exec <container> /usr/local/bin/download-db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtdbtk

```bash
$ singularity exec <container> /usr/local/bin/gtdbtk
$ podman run --it --rm --entrypoint /usr/local/bin/gtdbtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtdbtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
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