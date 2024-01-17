---
layout: container
name:  "quay.io/biocontainers/htslib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htslib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htslib/container.yaml"
updated_at: "2024-01-17 03:01:11.637854"
latest: "1.17--h6bc39ce_1"
container_url: "https://biocontainers.pro/tools/htslib"
aliases:
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.9--h244ad75_9"
 - "1.16--h6bc39ce_0"
 - "1.15.1--h6bc39ce_1"
 - "1.14--h9753748_2"
 - "1.13--h9093b5e_0"
 - "1.12--h9093b5e_1"
 - "1.17--h6bc39ce_0"
 - "1.17--h6bc39ce_1"
description: "shpc-registry automated BioContainers addition for htslib"
config: {"url": "https://biocontainers.pro/tools/htslib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for htslib", "latest": {"1.17--h6bc39ce_1": "sha256:4186ec57b8f92ad5d87d5992553985703f70f941def0967138a001dc6ee94d15"}, "tags": {"1.9--h244ad75_9": "sha256:fb71016f0da0e0eca1f1bfa6f2c6519edfbd1f34e99146cdb21848730c2424e6", "1.16--h6bc39ce_0": "sha256:bf2eee651d4d046236342539b79cb508088426e554dcf121e2df0eb6c8b39538", "1.15.1--h6bc39ce_1": "sha256:673c2abd7b6cb2e53e3df0e8dcbb46f4de87bb858150bcac6efc2bf3f34214e5", "1.14--h9753748_2": "sha256:f0a033ee9eb770a32062b44ab6fe5406376f002796d3c1ab037889eec0e435ed", "1.13--h9093b5e_0": "sha256:393c9fa17a41923bc362195ede93316bf0bb1c7ab0c68a62bfb80826e08950ad", "1.12--h9093b5e_1": "sha256:f1966b161b274bfffaad728f76072d4e243866204aef3b913519231f28d6ba56", "1.17--h6bc39ce_0": "sha256:d6ef41ea2628e9be0e011da30c58c88688e3696647f386dddee505d6f88b09ac", "1.17--h6bc39ce_1": "sha256:4186ec57b8f92ad5d87d5992553985703f70f941def0967138a001dc6ee94d15"}, "docker": "quay.io/biocontainers/htslib", "aliases": {"htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htslib.
shpc-registry automated BioContainers addition for htslib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htslib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htslib:1.17--h6bc39ce_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htslib/1.17--h6bc39ce_1
$ module help quay.io/biocontainers/htslib/1.17--h6bc39ce_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htslib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htslib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htslib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htslib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htslib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htslib-inspect-deffile:

```bash
$ singularity inspect -d <container>
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