---
layout: container
name:  "quay.io/biocontainers/bioconductor-ripat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ripat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ripat/container.yaml"
updated_at: "2025-12-10 04:13:15.086520"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ripat"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ripat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ripat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ripat", "latest": {"1.10.0--r43hdfd78af_0": "sha256:b6d18a9332ad883c0800bc428719c1e74477b192e94dac8756115d19bfccd5c0"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:759ffb313189da631d2186a84235848ac5147db393c9d2d1dbda27eec93c4748", "1.8.0--r42hdfd78af_0": "sha256:562a51a0f69a6a0d9250097c5b3d5c1bff7b237afc68d8d4101c659c64533178", "1.10.0--r43hdfd78af_0": "sha256:b6d18a9332ad883c0800bc428719c1e74477b192e94dac8756115d19bfccd5c0"}, "docker": "quay.io/biocontainers/bioconductor-ripat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ripat.
shpc-registry automated BioContainers addition for bioconductor-ripat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ripat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ripat:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ripat/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ripat/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ripat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ripat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ripat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ripat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ripat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ripat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ripat

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