---
layout: container
name:  "quay.io/biocontainers/bioconductor-matter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-matter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-matter/container.yaml"
updated_at: "2024-08-01 03:08:22.280510"
latest: "2.4.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-matter"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.3--r351hf484d3e_0"
 - "2.0.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "2.0.0--r42hf17093f_1"
 - "2.2.0--r43hf17093f_0"
 - "2.4.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-matter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-matter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-matter", "latest": {"2.4.0--r43hf17093f_0": "sha256:b76f1ea91734e6cf6b4fd1d64b758292527f7253bd23d0c3db9094fcb9d126e0"}, "tags": {"1.8.3--r351hf484d3e_0": "sha256:20a34c35fae8ae2c232c7fd9ac16a459d848e8a38d5362d6176f359c3f14bb4e", "2.0.0--r42hc247a5b_0": "sha256:2e8d8dc2a8d6a81784b226aafc8b4411d7e707f8e6f1061979df01c4f50034dc", "1.20.0--r41hc247a5b_2": "sha256:ef5d3b51ecf912b4fe7d10c062f9b6f717f48cc271774da77bb5e066a77bdb70", "1.18.0--r41h399db7b_0": "sha256:477844e7c78a516e8c33ff0804434ba038b4b90478b9331377c2fa40d858ef80", "1.16.0--r40h399db7b_1": "sha256:24926bee2693ec0f482d3446aaf9d35ad5918461ca3042d9c3991ada978e6e83", "1.14.0--r40h5f743cb_0": "sha256:466c01c93e107614a09ce65dcda772db91557db71204f732600c079f20569132", "2.0.0--r42hf17093f_1": "sha256:71bf7ad83798095b20a2324ac342eddb5d876b3477e452a6cdcbccf5015a42ac", "2.2.0--r43hf17093f_0": "sha256:7c261beee64a3aac5a7712d3d587bf98540ce8924580dbe0a762e19403a38665", "2.4.0--r43hf17093f_0": "sha256:b76f1ea91734e6cf6b4fd1d64b758292527f7253bd23d0c3db9094fcb9d126e0"}, "docker": "quay.io/biocontainers/bioconductor-matter", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-matter.
shpc-registry automated BioContainers addition for bioconductor-matter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-matter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-matter:2.4.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-matter/2.4.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-matter/2.4.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-matter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-matter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-matter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-matter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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