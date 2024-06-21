---
layout: container
name:  "quay.io/biocontainers/bioconductor-calm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-calm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-calm/container.yaml"
updated_at: "2024-06-21 03:06:55.106704"
latest: "1.16.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-calm"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-calm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-calm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-calm", "latest": {"1.16.0--r43hdfd78af_1": "sha256:d2b4f66df3b33ce83ae97057c0aca25e69ee9369e131b6259126b9f468a4ddce"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:858659121abac4147701ff616c8367adc45c70d0a2e194efcf54b01730176f85", "1.12.0--r42hdfd78af_0": "sha256:0a1eedd3df9dff6320293ce44f6a0e00dfef677d5fbbc393322ca08ce522e351", "1.14.0--r43hdfd78af_0": "sha256:5cf689b729a86b79c0a081e1602e5176c23d509843860976659bb00c626876b7", "1.16.0--r43hdfd78af_1": "sha256:d2b4f66df3b33ce83ae97057c0aca25e69ee9369e131b6259126b9f468a4ddce"}, "docker": "quay.io/biocontainers/bioconductor-calm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-calm.
shpc-registry automated BioContainers addition for bioconductor-calm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-calm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-calm:1.16.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-calm/1.16.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-calm/1.16.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-calm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-calm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-calm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-calm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-calm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-calm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-calm

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