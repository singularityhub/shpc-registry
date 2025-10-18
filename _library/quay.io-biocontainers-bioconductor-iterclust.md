---
layout: container
name:  "quay.io/biocontainers/bioconductor-iterclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iterclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iterclust/container.yaml"
updated_at: "2025-10-18 03:05:21.650968"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iterclust"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iterclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iterclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iterclust", "latest": {"1.24.0--r43hdfd78af_0": "sha256:fa3b65519dab2ddedf0cdcea2f82af21a34fd3a25aff95d1a69b97767fcc7032"}, "tags": {"1.8.0--r36_0": "sha256:2c5cc86300a33cbee6d240193065e98f55d1809c19585128e4f9474684bfce1a", "1.20.0--r42hdfd78af_0": "sha256:c90ac8c6d40c911ce62e519cfda403218451716010f6e0ac190c5e1839365736", "1.16.0--r41hdfd78af_0": "sha256:11df31157e54093bba4a91ea4f7c7d8cf073e8a3e655c74aaf357c386c528af6", "1.14.0--r41hdfd78af_0": "sha256:ee8c199a59ce43a1a513d4969ac27d5d5794f0e9e678455e4bac448b263ea976", "1.12.0--r40hdfd78af_1": "sha256:acdd8a016ae82e0a143d2ab4334565b3b78bcad5f11e3329cfdd726206fe8394", "1.10.0--r40_0": "sha256:4de141a636a3a3515efcc003b298749b2088deed0de423b8fa8057e2018b2243", "1.22.0--r43hdfd78af_0": "sha256:3e5564283f2cd54006be77c02fdc29fe832f9ed511c9d7b6bf264fe76a1917b7", "1.24.0--r43hdfd78af_0": "sha256:fa3b65519dab2ddedf0cdcea2f82af21a34fd3a25aff95d1a69b97767fcc7032"}, "docker": "quay.io/biocontainers/bioconductor-iterclust", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iterclust.
shpc-registry automated BioContainers addition for bioconductor-iterclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iterclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iterclust:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iterclust/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iterclust/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iterclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iterclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iterclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iterclust-inspect-deffile:

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