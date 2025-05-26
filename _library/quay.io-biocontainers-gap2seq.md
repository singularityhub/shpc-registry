---
layout: container
name:  "quay.io/biocontainers/gap2seq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gap2seq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gap2seq/container.yaml"
updated_at: "2025-05-26 12:06:07.566475"
latest: "3.1--py39h6c8c9e3_3"
container_url: "https://biocontainers.pro/tools/gap2seq"
aliases:
 - "Gap2Seq"
 - "Gap2Seq-core"
 - "GapCutter"
 - "GapMerger"
 - "ReadFilter"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "3.1--py39h6c8c9e3_3"
 - "3.1--py310h7bb695f_3"
description: "shpc-registry automated BioContainers addition for gap2seq"
config: {"url": "https://biocontainers.pro/tools/gap2seq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gap2seq", "latest": {"3.1--py39h6c8c9e3_3": "sha256:95662347fd6aa7f8454b67a2385c37039fe7863b676c1d0eee351db6dbbdd406"}, "tags": {"3.1--py39h6c8c9e3_3": "sha256:95662347fd6aa7f8454b67a2385c37039fe7863b676c1d0eee351db6dbbdd406", "3.1--py310h7bb695f_3": "sha256:9a4108cb19e5e6b9d12d54a98c7deb9579cb90017c7df6f2f28e60311001b36f"}, "docker": "quay.io/biocontainers/gap2seq", "aliases": {"Gap2Seq": "/usr/local/bin/Gap2Seq", "Gap2Seq-core": "/usr/local/bin/Gap2Seq-core", "GapCutter": "/usr/local/bin/GapCutter", "GapMerger": "/usr/local/bin/GapMerger", "ReadFilter": "/usr/local/bin/ReadFilter", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gap2seq.
shpc-registry automated BioContainers addition for gap2seq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gap2seq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gap2seq:3.1--py39h6c8c9e3_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gap2seq/3.1--py39h6c8c9e3_3
$ module help quay.io/biocontainers/gap2seq/3.1--py39h6c8c9e3_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gap2seq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gap2seq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gap2seq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gap2seq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gap2seq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gap2seq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gap2Seq

```bash
$ singularity exec <container> /usr/local/bin/Gap2Seq
$ podman run --it --rm --entrypoint /usr/local/bin/Gap2Seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gap2Seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Gap2Seq-core

```bash
$ singularity exec <container> /usr/local/bin/Gap2Seq-core
$ podman run --it --rm --entrypoint /usr/local/bin/Gap2Seq-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gap2Seq-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GapCutter

```bash
$ singularity exec <container> /usr/local/bin/GapCutter
$ podman run --it --rm --entrypoint /usr/local/bin/GapCutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GapCutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GapMerger

```bash
$ singularity exec <container> /usr/local/bin/GapMerger
$ podman run --it --rm --entrypoint /usr/local/bin/GapMerger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GapMerger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadFilter

```bash
$ singularity exec <container> /usr/local/bin/ReadFilter
$ podman run --it --rm --entrypoint /usr/local/bin/ReadFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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