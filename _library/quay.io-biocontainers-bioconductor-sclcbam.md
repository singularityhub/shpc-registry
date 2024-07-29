---
layout: container
name:  "quay.io/biocontainers/bioconductor-sclcbam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sclcbam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sclcbam/container.yaml"
updated_at: "2024-07-29 17:24:04.470263"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sclcbam"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sclcbam"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sclcbam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sclcbam", "latest": {"1.34.0--r43hdfd78af_0": "sha256:60bd5b7a799b4d3781421342dc801399d93aabc6406d7433d7b5d31264e119ca"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:22852f8511bdc01fb1e6c23ec0aa121b068cb6d13cddea1f00b3351ced569622", "1.29.0--r42hdfd78af_0": "sha256:d732f4dc596dedcf61e2f0758ae439e4e6d2ffda48743ff767bf0e7ea2e72ca8", "1.32.0--r43hdfd78af_0": "sha256:36b6c68b5a6d11ecb6428251412f39235ce84d0a789502cbd2b6a59c271e467e", "1.34.0--r43hdfd78af_0": "sha256:60bd5b7a799b4d3781421342dc801399d93aabc6406d7433d7b5d31264e119ca"}, "docker": "quay.io/biocontainers/bioconductor-sclcbam"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sclcbam.
shpc-registry automated BioContainers addition for bioconductor-sclcbam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sclcbam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sclcbam:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sclcbam/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sclcbam/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sclcbam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sclcbam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sclcbam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sclcbam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sclcbam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sclcbam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sclcbam

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