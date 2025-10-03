---
layout: container
name:  "quay.io/biocontainers/p7zip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/p7zip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/p7zip/container.yaml"
updated_at: "2025-10-03 03:39:37.248780"
latest: "16.02"
container_url: "https://biocontainers.pro/tools/p7zip"
aliases:
 - "7z"
 - "7za"
 - "7zr"
versions:
 - "15.09--h2d50403_4"
 - "16.02"
description: "shpc-registry automated BioContainers addition for p7zip"
config: {"url": "https://biocontainers.pro/tools/p7zip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for p7zip", "latest": {"16.02": "sha256:731aaeef376a95510b4f99d2f0f04be8ec6c737809f09a74438cbebf6cca02d8"}, "tags": {"15.09--h2d50403_4": "sha256:5021131f4c3832d27b62c847e927c745730b0ac355caddec7b9fe8b35d75e632", "16.02": "sha256:731aaeef376a95510b4f99d2f0f04be8ec6c737809f09a74438cbebf6cca02d8"}, "docker": "quay.io/biocontainers/p7zip", "aliases": {"7z": "/usr/local/bin/7z", "7za": "/usr/local/bin/7za", "7zr": "/usr/local/bin/7zr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/p7zip.
shpc-registry automated BioContainers addition for p7zip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/p7zip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/p7zip:16.02
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/p7zip/16.02
$ module help quay.io/biocontainers/p7zip/16.02
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### p7zip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### p7zip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### p7zip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### p7zip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### p7zip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### p7zip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 7z

```bash
$ singularity exec <container> /usr/local/bin/7z
$ podman run --it --rm --entrypoint /usr/local/bin/7z   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7z   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 7za

```bash
$ singularity exec <container> /usr/local/bin/7za
$ podman run --it --rm --entrypoint /usr/local/bin/7za   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7za   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 7zr

```bash
$ singularity exec <container> /usr/local/bin/7zr
$ podman run --it --rm --entrypoint /usr/local/bin/7zr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7zr   -v ${PWD} -w ${PWD} <container> -c " $@"
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