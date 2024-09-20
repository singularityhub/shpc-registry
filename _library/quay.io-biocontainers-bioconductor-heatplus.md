---
layout: container
name:  "quay.io/biocontainers/bioconductor-heatplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-heatplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-heatplus/container.yaml"
updated_at: "2024-09-20 03:47:00.199666"
latest: "3.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-heatplus"

versions:
 - "3.2.0--r41hdfd78af_0"
 - "3.6.0--r42hdfd78af_0"
 - "3.8.0--r43hdfd78af_0"
 - "3.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-heatplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-heatplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-heatplus", "latest": {"3.10.0--r43hdfd78af_0": "sha256:8471c2dd14a5c2781e12b57d8c922c05920211e4b2b5ab4e3e144a7dde291b3f"}, "tags": {"3.2.0--r41hdfd78af_0": "sha256:af996e312aa757687d68478acb516f6dd1efaf8e917791ec2876ff37302e61c8", "3.6.0--r42hdfd78af_0": "sha256:07dae01af4a2d320674b58fe86ceea76a680600901ca3efdb9b8636c2c14863d", "3.8.0--r43hdfd78af_0": "sha256:f8e0fa5311eaa88ef8ced5c9a54213b85b7c3f9a5f7f25697b473ee93e871c44", "3.10.0--r43hdfd78af_0": "sha256:8471c2dd14a5c2781e12b57d8c922c05920211e4b2b5ab4e3e144a7dde291b3f"}, "docker": "quay.io/biocontainers/bioconductor-heatplus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-heatplus.
shpc-registry automated BioContainers addition for bioconductor-heatplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-heatplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-heatplus:3.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-heatplus/3.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-heatplus/3.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-heatplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heatplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heatplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-heatplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-heatplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-heatplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-heatplus

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