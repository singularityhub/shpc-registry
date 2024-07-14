---
layout: container
name:  "quay.io/biocontainers/bioconductor-safe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-safe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-safe/container.yaml"
updated_at: "2024-07-14 02:48:31.269729"
latest: "3.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-safe"

versions:
 - "3.34.0--r41hdfd78af_0"
 - "3.38.0--r42hdfd78af_0"
 - "3.40.0--r43hdfd78af_0"
 - "3.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-safe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-safe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-safe", "latest": {"3.42.0--r43hdfd78af_0": "sha256:b7217a9ca5b117134180a3d6beb6a729d7f2628a719e470f439385ff6593f2ca"}, "tags": {"3.34.0--r41hdfd78af_0": "sha256:209ffffbeb9ec009267fa37fa3a8f2dd32f351eb66e6812c7d349398c9ad3123", "3.38.0--r42hdfd78af_0": "sha256:1e726c7900eea77e821f8f1700a1728ef37548c84c98d1ee0f87473b3f76ef91", "3.40.0--r43hdfd78af_0": "sha256:4b2ea64e2accb672643662c1ff6beaaa8722dea4aeae9ef2b7e6e0dc71c8e626", "3.42.0--r43hdfd78af_0": "sha256:b7217a9ca5b117134180a3d6beb6a729d7f2628a719e470f439385ff6593f2ca"}, "docker": "quay.io/biocontainers/bioconductor-safe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-safe.
shpc-registry automated BioContainers addition for bioconductor-safe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-safe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-safe:3.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-safe/3.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-safe/3.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-safe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-safe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-safe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-safe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-safe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-safe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-safe

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