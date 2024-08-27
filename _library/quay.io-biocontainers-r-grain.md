---
layout: container
name:  "quay.io/biocontainers/r-grain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-grain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-grain/container.yaml"
updated_at: "2024-08-27 06:25:08.497497"
latest: "1.4.1--r43h21a89ab_0"
container_url: "https://biocontainers.pro/tools/r-grain"

versions:
 - "1.3_0--r41hecf12ef_6"
 - "1.3.11--r42hecf12ef_1"
 - "1.3.12--r42hecf12ef_0"
 - "1.3.13--r42hecf12ef_1"
 - "1.3.13--r42h21a89ab_2"
 - "1.3.13--r43h21a89ab_3"
 - "1.3.14--r43h21a89ab_0"
 - "1.4.0--r43h21a89ab_0"
 - "1.4.1--r43h21a89ab_0"
description: "shpc-registry automated BioContainers addition for r-grain"
config: {"url": "https://biocontainers.pro/tools/r-grain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-grain", "latest": {"1.4.1--r43h21a89ab_0": "sha256:2dee1abacc157c8c1a5d0e39f78856c9d2563fdbe6a142084e26ce9132530c77"}, "tags": {"1.3_0--r41hecf12ef_6": "sha256:6b4d1ea59a0d63edffdbbd7516ef66340e23d3a296dc9ecc161349bed1a1e98b", "1.3.11--r42hecf12ef_1": "sha256:2178aa3229d0653dc2c6cee473ea6992882be661e2c606ee5e175f87a794c5a4", "1.3.12--r42hecf12ef_0": "sha256:bc556d7a8ff478e4761960e13bc2bbf6aa4ad28429faa79aa0ef6dce4c305240", "1.3.13--r42hecf12ef_1": "sha256:8bcd11a5f4feef7e71caeea0016c4116edffdafa89123181f964934f19acf8ed", "1.3.13--r42h21a89ab_2": "sha256:50bdf7789d110e7cc0a3f3c437a8b2f43f1b661aa7f665ddeec4dea1e9479d8f", "1.3.13--r43h21a89ab_3": "sha256:c9457f3be8484bbd104d24c1fad2a1ea336fb747578c407227ea5282528eb7bb", "1.3.14--r43h21a89ab_0": "sha256:71fa1ced1b36ccfad8c487b606b78cab0da373a0ac46705a835ec11307ebec6d", "1.4.0--r43h21a89ab_0": "sha256:3e1ae70450db1b13cbadf578508970de6fb3e4fdb01af08477f2b54adaa022de", "1.4.1--r43h21a89ab_0": "sha256:2dee1abacc157c8c1a5d0e39f78856c9d2563fdbe6a142084e26ce9132530c77"}, "docker": "quay.io/biocontainers/r-grain"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-grain.
shpc-registry automated BioContainers addition for r-grain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-grain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-grain:1.4.1--r43h21a89ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-grain/1.4.1--r43h21a89ab_0
$ module help quay.io/biocontainers/r-grain/1.4.1--r43h21a89ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-grain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-grain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-grain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-grain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-grain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-grain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-grain

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