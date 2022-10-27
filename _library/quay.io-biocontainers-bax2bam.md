---
layout: container
name:  "quay.io/biocontainers/bax2bam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bax2bam/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bax2bam/container.yaml"
updated_at: "2022-10-27 00:32:58.186138"
latest: "0.0.9--h018d624_7"
container_url: "https://biocontainers.pro/tools/bax2bam"
aliases:
 - ".bax2bam-post-link.sh"
 - ".blasr_libcpp-post-link.sh"
 - ".pbbam-post-link.sh"
 - ".pbcopper-post-link.sh"
 - "bax2bam"
 - "pbbamify"
versions:
 - "0.0.9--h018d624_7"
description: "shpc-registry automated BioContainers addition for bax2bam"
config: {"url": "https://biocontainers.pro/tools/bax2bam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bax2bam", "latest": {"0.0.9--h018d624_7": "sha256:4464f6126573dfc7bb28e4b1ab75183b6038220784f51f3f5d282868680bcdee"}, "tags": {"0.0.9--h018d624_7": "sha256:4464f6126573dfc7bb28e4b1ab75183b6038220784f51f3f5d282868680bcdee"}, "docker": "quay.io/biocontainers/bax2bam", "aliases": {".bax2bam-post-link.sh": "/usr/local/bin/.bax2bam-post-link.sh", ".blasr_libcpp-post-link.sh": "/usr/local/bin/.blasr_libcpp-post-link.sh", ".pbbam-post-link.sh": "/usr/local/bin/.pbbam-post-link.sh", ".pbcopper-post-link.sh": "/usr/local/bin/.pbcopper-post-link.sh", "bax2bam": "/usr/local/bin/bax2bam", "pbbamify": "/usr/local/bin/pbbamify"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bax2bam.
shpc-registry automated BioContainers addition for bax2bam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bax2bam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bax2bam:0.0.9--h018d624_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bax2bam/0.0.9--h018d624_7
$ module help quay.io/biocontainers/bax2bam/0.0.9--h018d624_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bax2bam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bax2bam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bax2bam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bax2bam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bax2bam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bax2bam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bax2bam-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bax2bam-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bax2bam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bax2bam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .blasr_libcpp-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.blasr_libcpp-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.blasr_libcpp-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.blasr_libcpp-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbbam-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbbam-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbbam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbbam-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcopper-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcopper-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcopper-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcopper-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bax2bam

```bash
$ singularity exec <container> /usr/local/bin/bax2bam
$ podman run --it --rm --entrypoint /usr/local/bin/bax2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bax2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbbamify

```bash
$ singularity exec <container> /usr/local/bin/pbbamify
$ podman run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
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