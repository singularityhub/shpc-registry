---
layout: container
name:  "quay.io/biocontainers/fastqsplitter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastqsplitter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastqsplitter/container.yaml"
updated_at: "2025-03-09 02:48:33.242088"
latest: "1.2.0--py312h0fa9677_8"
container_url: "https://biocontainers.pro/tools/fastqsplitter"
aliases:
 - "fastqsplitter"
 - "igzip"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "pigz"
 - "unpigz"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
versions:
 - "1.2.0--py38hbff2b2d_3"
 - "1.2.0--py38he5da3d1_5"
 - "1.2.0--py310h4b81fae_5"
 - "1.2.0--py312hf67a6ed_6"
 - "1.2.0--py311haab0aaa_7"
 - "1.2.0--py312h0fa9677_8"
description: "shpc-registry automated BioContainers addition for fastqsplitter"
config: {"url": "https://biocontainers.pro/tools/fastqsplitter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastqsplitter", "latest": {"1.2.0--py312h0fa9677_8": "sha256:71904efac84a1227ef551ba2a82e20f68ed6ad1552b54fe7b041a47e91551f45"}, "tags": {"1.2.0--py38hbff2b2d_3": "sha256:9bd62e637a0a1f968653282b334a4fba2879fced60855cee971dcfd4ed7fc39a", "1.2.0--py38he5da3d1_5": "sha256:9ee4f5950b5bc624bbbca60a6664bec19a373ce9f1241398dcd58d3445fae53b", "1.2.0--py310h4b81fae_5": "sha256:30288bdb11accf31d33b8a6f52e502261302ff73a169f7eb442594cfd4efa02e", "1.2.0--py312hf67a6ed_6": "sha256:7b840a9159a3643f3f8ec54b10b91876d112aba40e06ef905c994f67448a9616", "1.2.0--py311haab0aaa_7": "sha256:a439a9c5b2ed9a76df0d85cb7ddea2dc5e75dbc576dee39754ac57e7795f2343", "1.2.0--py312h0fa9677_8": "sha256:71904efac84a1227ef551ba2a82e20f68ed6ad1552b54fe7b041a47e91551f45"}, "docker": "quay.io/biocontainers/fastqsplitter", "aliases": {"fastqsplitter": "/usr/local/bin/fastqsplitter", "igzip": "/usr/local/bin/igzip", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastqsplitter.
shpc-registry automated BioContainers addition for fastqsplitter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastqsplitter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastqsplitter:1.2.0--py312h0fa9677_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastqsplitter/1.2.0--py312h0fa9677_8
$ module help quay.io/biocontainers/fastqsplitter/1.2.0--py312h0fa9677_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastqsplitter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastqsplitter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastqsplitter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastqsplitter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastqsplitter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastqsplitter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastqsplitter

```bash
$ singularity exec <container> /usr/local/bin/fastqsplitter
$ podman run --it --rm --entrypoint /usr/local/bin/fastqsplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqsplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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