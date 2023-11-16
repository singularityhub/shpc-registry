---
layout: container
name:  "quay.io/biocontainers/bioconductor-metaneighbor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metaneighbor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metaneighbor/container.yaml"
updated_at: "2023-11-16 03:20:35.409934"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metaneighbor"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r40h5f743cb_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metaneighbor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metaneighbor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metaneighbor", "latest": {"1.20.0--r43hdfd78af_0": "sha256:c121da39d4f207d97afff2b948dae7e001b4a7d0ab8bc102d49d13ea8ad08cf4"}, "tags": {"1.8.0--r40h5f743cb_0": "sha256:f23833c6e80a38c6c17f3984387ad93684b8f210e485ccd6ab7713f85ae34deb", "1.18.0--r42hdfd78af_0": "sha256:94fab1e7422ed9e45adae1129603842403cd6a41f454a6006983b8ff467e8d4c", "1.14.0--r41hdfd78af_0": "sha256:b5fa68c098f6a530c1948366f288eed70703a4e0cda6cc082bef263f0192ea23", "1.12.0--r41hdfd78af_0": "sha256:b312b3c6a14c5823c3b68c5d369480e446709eba812611d316f377f415df23ba", "1.10.0--r40hdfd78af_1": "sha256:54cf3849a22787d97f93ad2ff8d3c5006db6164d9836da72f85f3c50d10c8164", "1.20.0--r43hdfd78af_0": "sha256:c121da39d4f207d97afff2b948dae7e001b4a7d0ab8bc102d49d13ea8ad08cf4"}, "docker": "quay.io/biocontainers/bioconductor-metaneighbor", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metaneighbor.
shpc-registry automated BioContainers addition for bioconductor-metaneighbor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metaneighbor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metaneighbor:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metaneighbor/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metaneighbor/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metaneighbor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaneighbor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaneighbor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metaneighbor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metaneighbor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metaneighbor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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