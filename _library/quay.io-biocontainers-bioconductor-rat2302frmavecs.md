---
layout: container
name:  "quay.io/biocontainers/bioconductor-rat2302frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rat2302frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rat2302frmavecs/container.yaml"
updated_at: "2024-12-19 04:20:21.955790"
latest: "0.99.11--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-rat2302frmavecs"

versions:
 - "0.99.11--r41hdfd78af_8"
 - "0.99.11--r42hdfd78af_9"
 - "0.99.11--r43hdfd78af_10"
 - "0.99.11--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-rat2302frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rat2302frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rat2302frmavecs", "latest": {"0.99.11--r43hdfd78af_11": "sha256:daff0665f4b68964ea78cc566a99306d56b39c5883cfbe8e33f1a7b6c41831ad"}, "tags": {"0.99.11--r41hdfd78af_8": "sha256:ecb525816e6697282b3c1fb959c75806596721be53f5e057dd644e1dc03fd442", "0.99.11--r42hdfd78af_9": "sha256:ae3e8cf3c8cf24fd372e70e538b844335270f4f99401e011e6f96ffc05a6e035", "0.99.11--r43hdfd78af_10": "sha256:cbe97eebc7d3478d3592b6febd0d8281553a8c7af0de1152473b8415a3e18a3f", "0.99.11--r43hdfd78af_11": "sha256:daff0665f4b68964ea78cc566a99306d56b39c5883cfbe8e33f1a7b6c41831ad"}, "docker": "quay.io/biocontainers/bioconductor-rat2302frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rat2302frmavecs.
shpc-registry automated BioContainers addition for bioconductor-rat2302frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302frmavecs:0.99.11--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rat2302frmavecs/0.99.11--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-rat2302frmavecs/0.99.11--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rat2302frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rat2302frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rat2302frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rat2302frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rat2302frmavecs

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