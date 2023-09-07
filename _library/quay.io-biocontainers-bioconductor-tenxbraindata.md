---
layout: container
name:  "quay.io/biocontainers/bioconductor-tenxbraindata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tenxbraindata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tenxbraindata/container.yaml"
updated_at: "2023-09-07 03:27:56.687036"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tenxbraindata"
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
 - "1.8.0--r40_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.18.0--r42hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tenxbraindata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tenxbraindata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tenxbraindata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:d79c2dcfa57d8936db0da065359b8b3d0a1a2e7ba6fda14c5671db274f7edf39"}, "tags": {"1.8.0--r40_0": "sha256:c3870cc26da4a80eb1caeff5e05ac4c368fa6869aa9287633c0f800aca81c0a5", "1.14.0--r41hdfd78af_1": "sha256:ec4d1338c353e407efe5844a10fbaa7858b6a891d8524e585ae6e33d248ae023", "1.12.0--r41hdfd78af_0": "sha256:84a11e6b027e4b58281021b62415085ca0935e9bf7c9b04c9cdcfa53441780f1", "1.10.0--r40hdfd78af_1": "sha256:54d48c64323f5632501bc6f95aa7c054f13d9607083cfc2feebb556e7fca4fc8", "1.18.0--r42hdfd78af_0": "sha256:0957a1e48903384562d4f56e142efc03c0a834754a030ac7846d6a064cf6b5fe", "1.20.0--r43hdfd78af_0": "sha256:d79c2dcfa57d8936db0da065359b8b3d0a1a2e7ba6fda14c5671db274f7edf39"}, "docker": "quay.io/biocontainers/bioconductor-tenxbraindata", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tenxbraindata.
shpc-registry automated BioContainers addition for bioconductor-tenxbraindata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxbraindata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxbraindata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tenxbraindata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tenxbraindata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tenxbraindata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxbraindata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxbraindata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tenxbraindata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tenxbraindata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tenxbraindata-inspect-deffile:

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