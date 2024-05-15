---
layout: container
name:  "quay.io/biocontainers/bioconductor-rat2302probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rat2302probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rat2302probe/container.yaml"
updated_at: "2024-05-15 03:02:40.751310"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rat2302probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rat2302probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rat2302probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rat2302probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:f430f6ae9a790f0a7557584d70897c87986dd06246ff1cabab6c4cb70dabc73f"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a9ec47a45ba1027f2dc1809fd2fca14f5db937b9bc54563ae3732c841dbaf004", "2.18.0--r42hdfd78af_10": "sha256:ce52eec94fd757bab9ebe198c0a461475552d798a473e8f13997ed89ac66d8c4", "2.18.0--r43hdfd78af_11": "sha256:82a4a092b70ba7352c6192160868111dd4e780c3bbdee1d3cf972d13ccd21ca4", "2.18.0--r43hdfd78af_12": "sha256:f430f6ae9a790f0a7557584d70897c87986dd06246ff1cabab6c4cb70dabc73f"}, "docker": "quay.io/biocontainers/bioconductor-rat2302probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rat2302probe.
shpc-registry automated BioContainers addition for bioconductor-rat2302probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rat2302probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rat2302probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rat2302probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rat2302probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rat2302probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rat2302probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rat2302probe

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