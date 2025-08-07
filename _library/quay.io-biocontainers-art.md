---
layout: container
name:  "quay.io/biocontainers/art"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/art/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/art/container.yaml"
updated_at: "2025-08-07 04:38:07.768221"
latest: "2016.06.05--h0704011_13"
container_url: "https://biocontainers.pro/tools/art"
aliases:
 - "art_454"
 - "art_SOLiD"
 - "art_illumina"
versions:
 - "3.19.15--1"
 - "2016.06.05--h589041f_9"
 - "2016.06.05--heacdb12_11"
 - "2016.06.05--heacdb12_12"
 - "2016.06.05--h0704011_13"
description: "shpc-registry automated BioContainers addition for art"
config: {"url": "https://biocontainers.pro/tools/art", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for art", "latest": {"2016.06.05--h0704011_13": "sha256:18a9360667bb1f50e0368709efee3390e6ed733cf3c6eadd0f6ea441f143ff60"}, "tags": {"3.19.15--1": "sha256:ab044ce2994ce719c71f28525cba596c355299427e15dce039fdc061570a39ee", "2016.06.05--h589041f_9": "sha256:c2828d1a3a7d3b3accd5b555ce3e35bb3605e55cd3fab1b5f212653970c80362", "2016.06.05--heacdb12_11": "sha256:a4eb6dbc9fd82f5dab4f7e849b66ac23d731cf6041aed3aba7702a73a2643020", "2016.06.05--heacdb12_12": "sha256:e6f22e6b767978e96a44142ee1f708060ab88e2a4a973bf3ffbc7147c8b47005", "2016.06.05--h0704011_13": "sha256:18a9360667bb1f50e0368709efee3390e6ed733cf3c6eadd0f6ea441f143ff60"}, "docker": "quay.io/biocontainers/art", "aliases": {"art_454": "/usr/local/bin/art_454", "art_SOLiD": "/usr/local/bin/art_SOLiD", "art_illumina": "/usr/local/bin/art_illumina"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/art.
shpc-registry automated BioContainers addition for art
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/art
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/art:2016.06.05--h0704011_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/art/2016.06.05--h0704011_13
$ module help quay.io/biocontainers/art/2016.06.05--h0704011_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### art-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### art-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### art-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### art-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### art-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### art-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### art_454

```bash
$ singularity exec <container> /usr/local/bin/art_454
$ podman run --it --rm --entrypoint /usr/local/bin/art_454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_SOLiD

```bash
$ singularity exec <container> /usr/local/bin/art_SOLiD
$ podman run --it --rm --entrypoint /usr/local/bin/art_SOLiD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_SOLiD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### art_illumina

```bash
$ singularity exec <container> /usr/local/bin/art_illumina
$ podman run --it --rm --entrypoint /usr/local/bin/art_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
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