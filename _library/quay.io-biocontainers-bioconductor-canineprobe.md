---
layout: container
name:  "quay.io/biocontainers/bioconductor-canineprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-canineprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-canineprobe/container.yaml"
updated_at: "2023-09-23 02:53:18.473197"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-canineprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-canineprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-canineprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-canineprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:679be52b13f64cf4e4d4ce1be3a8b7e3a9519e69b0cc1f4814fa96aaafc31342"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:2d775c05027a9e3e2210d8868ed3f8946d26ecd82198465b356f3ce2a5425c3d", "2.18.0--r42hdfd78af_10": "sha256:733bf74cb55465afac2b34816c84d33aeddc45bef87516abf70f6ceb9667463f", "2.18.0--r43hdfd78af_11": "sha256:679be52b13f64cf4e4d4ce1be3a8b7e3a9519e69b0cc1f4814fa96aaafc31342"}, "docker": "quay.io/biocontainers/bioconductor-canineprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-canineprobe.
shpc-registry automated BioContainers addition for bioconductor-canineprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-canineprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-canineprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-canineprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-canineprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-canineprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canineprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canineprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-canineprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-canineprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-canineprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-canineprobe

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