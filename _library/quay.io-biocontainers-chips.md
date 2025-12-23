---
layout: container
name:  "quay.io/biocontainers/chips"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chips/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chips/container.yaml"
updated_at: "2025-12-23 04:10:35.143247"
latest: "2.4--h43eeafb_7"
container_url: "https://biocontainers.pro/tools/chips"
aliases:
 - "chips"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.4--hea94271_4"
 - "2.4--hff880f7_5"
 - "2.4--h6ab5fc9_6"
 - "2.4--h43eeafb_7"
description: "shpc-registry automated BioContainers addition for chips"
config: {"url": "https://biocontainers.pro/tools/chips", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chips", "latest": {"2.4--h43eeafb_7": "sha256:927b61e8e7c1c90878aa9b41485e23a116355cf096e985126461378591d4d859"}, "tags": {"2.4--hea94271_4": "sha256:d72b484a2ed1cd8228eb7a576446bc4a4060e95abea6964e03929dbb71e9b163", "2.4--hff880f7_5": "sha256:ca16cc23f9c75fa3d524e60e9178acca9e3d3065c59004ec94432adddd677322", "2.4--h6ab5fc9_6": "sha256:3270a8092e44f226cb8537a30d32dad90fec7e002b14d5c6ddf8d26502059ce0", "2.4--h43eeafb_7": "sha256:927b61e8e7c1c90878aa9b41485e23a116355cf096e985126461378591d4d859"}, "docker": "quay.io/biocontainers/chips", "aliases": {"chips": "/usr/local/bin/chips", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chips.
shpc-registry automated BioContainers addition for chips
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chips
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chips:2.4--h43eeafb_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chips/2.4--h43eeafb_7
$ module help quay.io/biocontainers/chips/2.4--h43eeafb_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chips-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chips-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chips-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chips-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chips-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chips-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chips

```bash
$ singularity exec <container> /usr/local/bin/chips
$ podman run --it --rm --entrypoint /usr/local/bin/chips   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chips   -v ${PWD} -w ${PWD} <container> -c " $@"
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