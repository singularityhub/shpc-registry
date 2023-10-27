---
layout: container
name:  "quay.io/biocontainers/singularity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/singularity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/singularity/container.yaml"
updated_at: "2023-10-27 03:21:03.533919"
latest: "3.8.6"
container_url: "https://biocontainers.pro/tools/singularity"
aliases:
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "cnitool"
 - "docker-run.sh"
 - "exec-plugins.sh"
 - "jq"
 - "mksquashfs"
 - "onig-config"
 - "priv-net-run.sh"
 - "release.sh"
 - "run-singularity"
 - "scmp_sys_resolver"
 - "singularity"
 - "unsquashfs"
versions:
 - "3.5.3"
 - "3.8.6"
description: "shpc-registry automated BioContainers addition for singularity"
config: {"url": "https://biocontainers.pro/tools/singularity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for singularity", "latest": {"3.8.6": "sha256:406ddd780aadf667504d4fb91e46a1f5f9eedd77b9dca50adecab603a702384a"}, "tags": {"3.5.3": "sha256:beb7f16f0f1b46f0c300d43cb189f7a76ff38688c8aa9d733dec56ca120c704f", "3.8.6": "sha256:406ddd780aadf667504d4fb91e46a1f5f9eedd77b9dca50adecab603a702384a"}, "docker": "quay.io/biocontainers/singularity", "aliases": {"bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "cnitool": "/usr/local/bin/cnitool", "docker-run.sh": "/usr/local/bin/docker-run.sh", "exec-plugins.sh": "/usr/local/bin/exec-plugins.sh", "jq": "/usr/local/bin/jq", "mksquashfs": "/usr/local/bin/mksquashfs", "onig-config": "/usr/local/bin/onig-config", "priv-net-run.sh": "/usr/local/bin/priv-net-run.sh", "release.sh": "/usr/local/bin/release.sh", "run-singularity": "/usr/local/bin/run-singularity", "scmp_sys_resolver": "/usr/local/bin/scmp_sys_resolver", "singularity": "/usr/local/bin/singularity", "unsquashfs": "/usr/local/bin/unsquashfs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/singularity.
shpc-registry automated BioContainers addition for singularity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/singularity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/singularity:3.8.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/singularity/3.8.6
$ module help quay.io/biocontainers/singularity/3.8.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### singularity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### singularity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### singularity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### singularity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### singularity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### singularity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnitool

```bash
$ singularity exec <container> /usr/local/bin/cnitool
$ podman run --it --rm --entrypoint /usr/local/bin/cnitool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnitool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-run.sh

```bash
$ singularity exec <container> /usr/local/bin/docker-run.sh
$ podman run --it --rm --entrypoint /usr/local/bin/docker-run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exec-plugins.sh

```bash
$ singularity exec <container> /usr/local/bin/exec-plugins.sh
$ podman run --it --rm --entrypoint /usr/local/bin/exec-plugins.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exec-plugins.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mksquashfs

```bash
$ singularity exec <container> /usr/local/bin/mksquashfs
$ podman run --it --rm --entrypoint /usr/local/bin/mksquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mksquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### priv-net-run.sh

```bash
$ singularity exec <container> /usr/local/bin/priv-net-run.sh
$ podman run --it --rm --entrypoint /usr/local/bin/priv-net-run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/priv-net-run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### release.sh

```bash
$ singularity exec <container> /usr/local/bin/release.sh
$ podman run --it --rm --entrypoint /usr/local/bin/release.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/release.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-singularity

```bash
$ singularity exec <container> /usr/local/bin/run-singularity
$ podman run --it --rm --entrypoint /usr/local/bin/run-singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmp_sys_resolver

```bash
$ singularity exec <container> /usr/local/bin/scmp_sys_resolver
$ podman run --it --rm --entrypoint /usr/local/bin/scmp_sys_resolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmp_sys_resolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singularity

```bash
$ singularity exec <container> /usr/local/bin/singularity
$ podman run --it --rm --entrypoint /usr/local/bin/singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unsquashfs

```bash
$ singularity exec <container> /usr/local/bin/unsquashfs
$ podman run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
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