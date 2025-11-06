---
layout: container
name:  "quay.io/biocontainers/super-focus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/super-focus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/super-focus/container.yaml"
updated_at: "2025-11-06 03:50:17.419072"
latest: "1.6--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/super-focus"
aliases:
 - "prerapsearch"
 - "rapsearch"
 - "superfocus"
 - "superfocus_downloadDB"
 - "mmseqs"
 - "jellyfish"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "diamond"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
versions:
 - "1.6--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for super-focus"
config: {"url": "https://biocontainers.pro/tools/super-focus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for super-focus", "latest": {"1.6--pyhdfd78af_1": "sha256:d638c5b4b8528890f384b4f18f3c194cb3d56725b5fb315cb99d8cf7804df7f9"}, "tags": {"1.6--pyhdfd78af_1": "sha256:d638c5b4b8528890f384b4f18f3c194cb3d56725b5fb315cb99d8cf7804df7f9"}, "docker": "quay.io/biocontainers/super-focus", "aliases": {"prerapsearch": "/usr/local/bin/prerapsearch", "rapsearch": "/usr/local/bin/rapsearch", "superfocus": "/usr/local/bin/superfocus", "superfocus_downloadDB": "/usr/local/bin/superfocus_downloadDB", "mmseqs": "/usr/local/bin/mmseqs", "jellyfish": "/usr/local/bin/jellyfish", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "diamond": "/usr/local/bin/diamond", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/super-focus.
shpc-registry automated BioContainers addition for super-focus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/super-focus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/super-focus:1.6--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/super-focus/1.6--pyhdfd78af_1
$ module help quay.io/biocontainers/super-focus/1.6--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### super-focus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### super-focus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### super-focus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### super-focus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### super-focus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### super-focus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prerapsearch

```bash
$ singularity exec <container> /usr/local/bin/prerapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapsearch

```bash
$ singularity exec <container> /usr/local/bin/rapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### superfocus

```bash
$ singularity exec <container> /usr/local/bin/superfocus
$ podman run --it --rm --entrypoint /usr/local/bin/superfocus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/superfocus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### superfocus_downloadDB

```bash
$ singularity exec <container> /usr/local/bin/superfocus_downloadDB
$ podman run --it --rm --entrypoint /usr/local/bin/superfocus_downloadDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/superfocus_downloadDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
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