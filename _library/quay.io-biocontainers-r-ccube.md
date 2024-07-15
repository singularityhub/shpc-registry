---
layout: container
name:  "quay.io/biocontainers/r-ccube"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ccube/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ccube/container.yaml"
updated_at: "2024-07-15 02:53:00.084649"
latest: "1.0_beta.1--r43hdbdd923_6"
container_url: "https://biocontainers.pro/tools/r-ccube"

versions:
 - "1.0_beta.1--r41h46c59ee_1"
 - "1.0_beta.1--r42h46c59ee_2"
 - "1.0_beta.1--r42he153687_4"
 - "1.0_beta.1--r43he153687_5"
 - "1.0_beta.1--r43hdbdd923_6"
description: "shpc-registry automated BioContainers addition for r-ccube"
config: {"url": "https://biocontainers.pro/tools/r-ccube", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ccube", "latest": {"1.0_beta.1--r43hdbdd923_6": "sha256:065895dcbbc8ef6327e92ee0ec663504d6e2404e4ae7184c5bb0ebcef915ae41"}, "tags": {"1.0_beta.1--r41h46c59ee_1": "sha256:88ef4c800eadf6640eabc8db3502bd241773702f07db48353f5f286dd26110f5", "1.0_beta.1--r42h46c59ee_2": "sha256:04fb357f16795109854eb04600a650f95917609aef29d4a625e95a42d50caa5c", "1.0_beta.1--r42he153687_4": "sha256:0482ff191487ddcd45e6af68bc1d3d13cdbe3d1e970c873ba11def9db6e5a878", "1.0_beta.1--r43he153687_5": "sha256:65cd907820c2594c61d116866b694f4211b810a2ccd7b7391c9de280792237c0", "1.0_beta.1--r43hdbdd923_6": "sha256:065895dcbbc8ef6327e92ee0ec663504d6e2404e4ae7184c5bb0ebcef915ae41"}, "docker": "quay.io/biocontainers/r-ccube"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ccube.
shpc-registry automated BioContainers addition for r-ccube
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ccube
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ccube:1.0_beta.1--r43hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ccube/1.0_beta.1--r43hdbdd923_6
$ module help quay.io/biocontainers/r-ccube/1.0_beta.1--r43hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ccube-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ccube-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ccube-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ccube-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ccube-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ccube-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ccube

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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