---
layout: container
name:  "quay.io/biocontainers/bioconductor-cemitool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cemitool/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cemitool/container.yaml"
updated_at: "2025-12-04 03:31:02.677630"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cemitool"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.3--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.1--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cemitool"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cemitool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cemitool", "latest": {"1.30.0--r44hdfd78af_0": "sha256:5c819c76a904e8ca350352c71c198a3b24bf7fbdd6b750ad2507a04fd66638af"}, "tags": {"1.8.3--r36_0": "sha256:7b40d649edbea1a378ff4232aca7edbc893cde92169315618f41c58904a4651b", "1.22.0--r42hdfd78af_0": "sha256:615edd5ff4b6a5fc2da8fccf0ee6ccd074fdece0be52e03f7f7a13ca76f9514e", "1.18.1--r41hdfd78af_0": "sha256:ef5fbc0687d5727fbc1db85229289618ed11a1b67af6cf96f830e1af1af5d50e", "1.16.0--r41hdfd78af_0": "sha256:6681245217d0af29d9041df05db33286d783e3e1f904441072bb951a226d3d3c", "1.14.1--r40hdfd78af_0": "sha256:6ebd2d9550fa21ec70b85092980450c82cd1ecae643a1695f7cbbfb5de87973b", "1.12.0--r40_0": "sha256:7fc4f260833c3291d05dab51dfe0c298fe33b8e4730d6281e4f9ebca14194a66", "1.24.0--r43hdfd78af_0": "sha256:9733f8f561d961e623f9b05d59aa1234af53fc978d5ca103bce59e0ac5e5d65a", "1.26.0--r43hdfd78af_0": "sha256:025dce3fa7689dabd5901b3d831474abca4733aa47039ef2a0e31022809821a2", "1.30.0--r44hdfd78af_0": "sha256:5c819c76a904e8ca350352c71c198a3b24bf7fbdd6b750ad2507a04fd66638af"}, "docker": "quay.io/biocontainers/bioconductor-cemitool", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cemitool.
shpc-registry automated BioContainers addition for bioconductor-cemitool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cemitool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cemitool:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cemitool/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cemitool/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cemitool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cemitool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cemitool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cemitool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cemitool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cemitool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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