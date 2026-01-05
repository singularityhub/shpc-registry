---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipexoqual"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipexoqual/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipexoqual/container.yaml"
updated_at: "2026-01-05 04:41:09.337195"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipexoqual"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipexoqual"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipexoqual", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipexoqual", "latest": {"1.30.0--r44hdfd78af_0": "sha256:31699334c7c2751e21a4d08f05e4a784f239e76753d64e6fa10f5f6852851c37"}, "tags": {"1.8.0--r36_1": "sha256:6e3b95bf0580c8783b0e1ea6d35aa4ef1da71394a059c41ea250fcffd80502e8", "1.22.0--r42hdfd78af_0": "sha256:52c7198a4cbfdd40a7ce4eef310befacb9a846f3a3de7f026d33be683eb61924", "1.18.0--r41hdfd78af_0": "sha256:2e796a5187dca20fc86563a1987fef898d1dae87c7caf4527cf21fdb2ddcca82", "1.16.0--r41hdfd78af_0": "sha256:e3e9c320135e200066bfa8807b0df0be576a7a56b6eff192fbcd1a8e088f8604", "1.14.0--r40hdfd78af_1": "sha256:e5ccdf5dab998ea980313ba651de3fd770da68156377e9aef91c25a99dbee6a1", "1.12.0--r40_0": "sha256:d89ca9654c64da5891a5c140868e59498c9816b163518899b6c5acbdb7918e15", "1.24.0--r43hdfd78af_0": "sha256:6a960990ed4923e68e3dbfcf51ce4a2b81688a0ef8b1d7f96a71746b0a6884bc", "1.26.0--r43hdfd78af_0": "sha256:ffe0935246f6757c2ea78f7b03ef6522c843c2c0fdfce4a65188b87f587bf6bc", "1.30.0--r44hdfd78af_0": "sha256:31699334c7c2751e21a4d08f05e4a784f239e76753d64e6fa10f5f6852851c37"}, "docker": "quay.io/biocontainers/bioconductor-chipexoqual", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipexoqual.
shpc-registry automated BioContainers addition for bioconductor-chipexoqual
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipexoqual
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipexoqual:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipexoqual/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipexoqual/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipexoqual-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipexoqual-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipexoqual-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipexoqual-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipexoqual-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipexoqual-inspect-deffile:

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