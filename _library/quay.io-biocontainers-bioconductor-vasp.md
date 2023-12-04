---
layout: container
name:  "quay.io/biocontainers/bioconductor-vasp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vasp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vasp/container.yaml"
updated_at: "2023-12-04 02:41:44.267180"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vasp"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vasp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vasp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vasp", "latest": {"1.12.0--r43hdfd78af_0": "sha256:52bf24d601ac42072d3e09e0671dcb3ff2f516a71a53aa3fdd02f1cf8be9c1c9"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:6d63eb688987922f9de21f58c9bbce4978a4eede1a9838c3f5c893f530927562", "1.10.0--r42hdfd78af_0": "sha256:af2d993a93233d4dba6249a4d36e26dc7ecda19e1d34807f655f67b725eeae55", "1.12.0--r43hdfd78af_0": "sha256:52bf24d601ac42072d3e09e0671dcb3ff2f516a71a53aa3fdd02f1cf8be9c1c9"}, "docker": "quay.io/biocontainers/bioconductor-vasp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vasp.
shpc-registry automated BioContainers addition for bioconductor-vasp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vasp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vasp:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vasp/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vasp/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vasp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vasp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vasp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vasp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vasp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vasp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vasp

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