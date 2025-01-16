---
layout: container
name:  "quay.io/biocontainers/gsalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gsalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gsalign/container.yaml"
updated_at: "2025-01-16 03:07:06.940260"
latest: "1.0.22--hcb620b3_7"
container_url: "https://biocontainers.pro/tools/gsalign"
aliases:
 - "GSAlign"
 - "bwt_index"
versions:
 - "1.0.9--hdb83ec4_0"
 - "1.0.22--hc9193f5_2"
 - "1.0.22--h8b853e6_4"
 - "1.0.22--h8b853e6_5"
 - "1.0.22--hd175d40_6"
 - "1.0.22--hcb620b3_7"
description: "shpc-registry automated BioContainers addition for gsalign"
config: {"url": "https://biocontainers.pro/tools/gsalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gsalign", "latest": {"1.0.22--hcb620b3_7": "sha256:47a9d16d4b0abc6c8ed7eb129ef79757a2cb41bc8795be5a97de747a4a981c1f"}, "tags": {"1.0.9--hdb83ec4_0": "sha256:4ee1b07cef62ce3715f3fa4805ec32de2daba325d09c002fe6874e27e91e1fbb", "1.0.22--hc9193f5_2": "sha256:8d787f216254bcf85e7a0b257cf2a32a2af4fb9da9e60e6675dfcb211cb5615b", "1.0.22--h8b853e6_4": "sha256:36b5a76a23f729f06faa6ba9fff54df4a8e80fba2e4cc4cc4a262b7857eae9fc", "1.0.22--h8b853e6_5": "sha256:501ee5bddceb5db4893f3fe1dfa4911117654bbb799bed34aea524d1ec7cb190", "1.0.22--hd175d40_6": "sha256:b0c45b090cc1c0dadfe3464e6efc4c7068e3862018bef0034d0d08683803653c", "1.0.22--hcb620b3_7": "sha256:47a9d16d4b0abc6c8ed7eb129ef79757a2cb41bc8795be5a97de747a4a981c1f"}, "docker": "quay.io/biocontainers/gsalign", "aliases": {"GSAlign": "/usr/local/bin/GSAlign", "bwt_index": "/usr/local/bin/bwt_index"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gsalign.
shpc-registry automated BioContainers addition for gsalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gsalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gsalign:1.0.22--hcb620b3_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gsalign/1.0.22--hcb620b3_7
$ module help quay.io/biocontainers/gsalign/1.0.22--hcb620b3_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gsalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gsalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gsalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gsalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gsalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gsalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GSAlign

```bash
$ singularity exec <container> /usr/local/bin/GSAlign
$ podman run --it --rm --entrypoint /usr/local/bin/GSAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GSAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwt_index

```bash
$ singularity exec <container> /usr/local/bin/bwt_index
$ podman run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
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