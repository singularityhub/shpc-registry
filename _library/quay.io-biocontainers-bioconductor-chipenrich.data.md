---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipenrich.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipenrich.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipenrich.data/container.yaml"
updated_at: "2023-06-03 02:54:50.657414"
latest: "2.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipenrich.data"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.18.0--r41hdfd78af_1"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.10.0--r36_0"
 - "2.22.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipenrich.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipenrich.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipenrich.data", "latest": {"2.22.0--r42hdfd78af_0": "sha256:ff8c6ac20afaf9dcb8115c8b5a667bc42b8d79de809da24fac8c1addb658eb3f"}, "tags": {"2.8.0--r36_1": "sha256:6178e60ed4d52731cf252cd73220232f85b4ee2451d28b48ef4c800a3a6c5d1b", "2.18.0--r41hdfd78af_1": "sha256:63a702815d8591eea49ae38b5e1c999ba8376a3b5eecae6c5c3c8835e87fe5a8", "2.16.0--r41hdfd78af_0": "sha256:4e062cd7e72c3b84ce3afc9bd18f693888befb3d2d418108834b9bd386f06c4e", "2.14.0--r40hdfd78af_1": "sha256:c3c91b02bd9b64ef729f2c3c953a82cf74333def2764dc432f625a7db2222ec8", "2.12.0--r40_0": "sha256:458bd33f577c1f078494c76b9fcc5a9791d412cbf653cef0a0e11fc844632cc1", "2.10.0--r36_0": "sha256:b2241cb479d7da843c1ce8388450a4bf1b06cb3280bfaf6dd109fb58b0ea43b0", "2.22.0--r42hdfd78af_0": "sha256:ff8c6ac20afaf9dcb8115c8b5a667bc42b8d79de809da24fac8c1addb658eb3f"}, "docker": "quay.io/biocontainers/bioconductor-chipenrich.data", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipenrich.data.
shpc-registry automated BioContainers addition for bioconductor-chipenrich.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipenrich.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipenrich.data:2.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipenrich.data/2.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipenrich.data/2.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipenrich.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipenrich.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipenrich.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipenrich.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipenrich.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipenrich.data-inspect-deffile:

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