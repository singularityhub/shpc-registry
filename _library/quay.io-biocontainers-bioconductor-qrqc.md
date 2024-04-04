---
layout: container
name:  "quay.io/biocontainers/bioconductor-qrqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qrqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qrqc/container.yaml"
updated_at: "2024-04-04 04:04:52.616530"
latest: "1.52.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-qrqc"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
 - "1.52.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-qrqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qrqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qrqc", "latest": {"1.52.0--r42ha9d7317_1": "sha256:4593a5006a6e7fb079370c35f118bde0c29b8dae7aefd5100c04fc46fd22931d"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:5a7238717a8fc2c737d0cd1e533234769e7fcb59f450cf93d1ae715ab4e34b7d", "1.52.0--r42hc0cfd56_0": "sha256:550b242f58c032995187ac2026df27ba647abfb74f22bfce761eaf941e129ea7", "1.52.0--r42ha9d7317_1": "sha256:4593a5006a6e7fb079370c35f118bde0c29b8dae7aefd5100c04fc46fd22931d"}, "docker": "quay.io/biocontainers/bioconductor-qrqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qrqc.
shpc-registry automated BioContainers addition for bioconductor-qrqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qrqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qrqc:1.52.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qrqc/1.52.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-qrqc/1.52.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qrqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qrqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qrqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qrqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qrqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qrqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qrqc

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