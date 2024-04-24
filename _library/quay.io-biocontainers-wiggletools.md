---
layout: container
name:  "quay.io/biocontainers/wiggletools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wiggletools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wiggletools/container.yaml"
updated_at: "2024-04-24 03:05:29.252756"
latest: "1.2.11--hdd126ab_6"
container_url: "https://biocontainers.pro/tools/wiggletools"
aliases:
 - "wiggletools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.2.8--he98db58_2"
 - "1.2.11--h31cdec7_4"
 - "1.2.11--h71cb2ef_5"
 - "1.2.11--hdd126ab_6"
description: "shpc-registry automated BioContainers addition for wiggletools"
config: {"url": "https://biocontainers.pro/tools/wiggletools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wiggletools", "latest": {"1.2.11--hdd126ab_6": "sha256:5d248282f153b2cdef2ce0437fb7502477964f996b7aac87079f51c0558ab0b2"}, "tags": {"1.2.8--he98db58_2": "sha256:3ff83dfd89d41e43630d3279838430860b67ab72897a288f10ded38c6e3fff68", "1.2.11--h31cdec7_4": "sha256:20285b609ceeacc3b33fc9820ec1283ae16a875ec3eb1c2def1cda241936bbda", "1.2.11--h71cb2ef_5": "sha256:78a23a79a33a14674e735a55ead8118c97f77cd7b981f3dddb2265f886ffdf5a", "1.2.11--hdd126ab_6": "sha256:5d248282f153b2cdef2ce0437fb7502477964f996b7aac87079f51c0558ab0b2"}, "docker": "quay.io/biocontainers/wiggletools", "aliases": {"wiggletools": "/usr/local/bin/wiggletools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wiggletools.
shpc-registry automated BioContainers addition for wiggletools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wiggletools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wiggletools:1.2.11--hdd126ab_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wiggletools/1.2.11--hdd126ab_6
$ module help quay.io/biocontainers/wiggletools/1.2.11--hdd126ab_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wiggletools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wiggletools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wiggletools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wiggletools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wiggletools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wiggletools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wiggletools

```bash
$ singularity exec <container> /usr/local/bin/wiggletools
$ podman run --it --rm --entrypoint /usr/local/bin/wiggletools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wiggletools   -v ${PWD} -w ${PWD} <container> -c " $@"
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