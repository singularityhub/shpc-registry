---
layout: container
name:  "quay.io/biocontainers/bioconductor-assign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-assign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-assign/container.yaml"
updated_at: "2025-12-14 04:13:45.605190"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-assign"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-assign"
config: {"url": "https://biocontainers.pro/tools/bioconductor-assign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-assign", "latest": {"1.42.0--r44hdfd78af_0": "sha256:f409901cf5b5f2c24e73dc1b9c3b444e259927ab288612eb5e8aed11f01da67c"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:e2f04a9ffbe243aeae66852971ff4678ee5107148b8a60b72185b037793ca37a", "1.34.0--r42hdfd78af_0": "sha256:dfff90002e0809b523dc72572befdc916d544395e2ac45f6ebc8d20b67dac424", "1.36.0--r43hdfd78af_0": "sha256:c0dda534195618e2534ca7a22cc6199aade203cb469a438faaf010e87309fa12", "1.38.0--r43hdfd78af_0": "sha256:6e4f83c0ce37e8fc1280b5a0393c9494511e9d12c45f7e61ff3b73a93d327b86", "1.42.0--r44hdfd78af_0": "sha256:f409901cf5b5f2c24e73dc1b9c3b444e259927ab288612eb5e8aed11f01da67c"}, "docker": "quay.io/biocontainers/bioconductor-assign"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-assign.
shpc-registry automated BioContainers addition for bioconductor-assign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-assign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-assign:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-assign/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-assign/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-assign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-assign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-assign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-assign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-assign

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