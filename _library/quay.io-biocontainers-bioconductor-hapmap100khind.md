---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmap100khind"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmap100khind/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmap100khind/container.yaml"
updated_at: "2024-07-25 03:12:06.022783"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmap100khind"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.39.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmap100khind"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmap100khind", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmap100khind", "latest": {"1.44.0--r43hdfd78af_0": "sha256:c9d80df411b019532d828800e554c2cf54012f0a61473bef94c608b11418321d"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:b02c9bd0550c389e5f4de67deb905c2b85d1655f97a4e38ff25f89ce67385bb0", "1.39.0--r42hdfd78af_0": "sha256:aece7f3a2cbf1e9584fdb518ed69e3ae8a6b42fa6ffbc57c72d1420ffd030c6f", "1.42.0--r43hdfd78af_0": "sha256:a30e3063cb2e319c97d4e62ef0fcfd6a12c3cf8098b45f108b4bb8c1c2070872", "1.44.0--r43hdfd78af_0": "sha256:c9d80df411b019532d828800e554c2cf54012f0a61473bef94c608b11418321d"}, "docker": "quay.io/biocontainers/bioconductor-hapmap100khind"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmap100khind.
shpc-registry automated BioContainers addition for bioconductor-hapmap100khind
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap100khind
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap100khind:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmap100khind/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hapmap100khind/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmap100khind-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap100khind-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap100khind-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmap100khind-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmap100khind-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmap100khind-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmap100khind

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