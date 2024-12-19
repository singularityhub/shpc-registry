---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnu34probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnu34probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnu34probe/container.yaml"
updated_at: "2024-12-19 03:26:02.621448"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rnu34probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rnu34probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnu34probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnu34probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:ea6eb2f5a5fa6946ea658f7e06fbc8103f966e6ff6615dd596cb246decca0d0a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:bcf8e0924171ff2656cb2d32efa70c749b08afcf1fd8d6995c2988c25f514f34", "2.18.0--r42hdfd78af_10": "sha256:d828cf10266b85cbc39516070101a00781b4ab051683b75d65a48f93745fd683", "2.18.0--r43hdfd78af_11": "sha256:7170b8f009d2afb192af43535ea508d02ff2942365e8a197d138dd6068f4b2c2", "2.18.0--r43hdfd78af_12": "sha256:ea6eb2f5a5fa6946ea658f7e06fbc8103f966e6ff6615dd596cb246decca0d0a"}, "docker": "quay.io/biocontainers/bioconductor-rnu34probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnu34probe.
shpc-registry automated BioContainers addition for bioconductor-rnu34probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnu34probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnu34probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnu34probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rnu34probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnu34probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnu34probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnu34probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnu34probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnu34probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnu34probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnu34probe

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