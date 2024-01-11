---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytofpower"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytofpower/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytofpower/container.yaml"
updated_at: "2024-01-11 03:56:56.816984"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytofpower"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cytofpower"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytofpower", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cytofpower", "latest": {"1.8.0--r43hdfd78af_0": "sha256:45e3c08b56808c2dc78d29c2a81353a6464730bec6b03fb5c59005051b87f8e5"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:dbb489e7547da2881bbf25a9f46360610c89e231a68f6003134037d3fbdaebb4", "1.4.0--r42hdfd78af_0": "sha256:64267da491fb27a87e37452a0d12ddd4da01ad1ab49567ca158810963c1bb567", "1.6.0--r43hdfd78af_0": "sha256:2c754e34377208b87212c72d410ab661f07a730a7a1f7c7b0dc535677fc8ae6c", "1.8.0--r43hdfd78af_0": "sha256:45e3c08b56808c2dc78d29c2a81353a6464730bec6b03fb5c59005051b87f8e5"}, "docker": "quay.io/biocontainers/bioconductor-cytofpower"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytofpower.
shpc-registry automated BioContainers addition for bioconductor-cytofpower
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytofpower
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytofpower:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytofpower/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cytofpower/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytofpower-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytofpower-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytofpower-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytofpower-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytofpower-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytofpower-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytofpower

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