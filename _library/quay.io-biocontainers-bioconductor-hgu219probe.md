---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu219probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu219probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu219probe/container.yaml"
updated_at: "2025-01-05 03:17:42.543472"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu219probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu219probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu219probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu219probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:6b87c4409792b2d3195667f0b94f563c3a61b4b30a8664c4c807aca4defc9989"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b1897162cc3eb19699bd4efd51361d2f87c0e0a29a171dea66fcfb778d70e91a", "2.18.0--r42hdfd78af_10": "sha256:7cdb1d1920329d7a5aa0c3110757c26c4c431905e6ec0d8885a42bc35ab9a596", "2.18.0--r43hdfd78af_11": "sha256:65dd98fb7f8f56277b9036fb00b92db1f135734b767b19bec4e7785cec26c0ea", "2.18.0--r43hdfd78af_12": "sha256:bc86fee9e2b47f0d77bac7c5c8d15d105a46a6e710bbe01b305cf3ed45b48bdb", "2.18.0--r44hdfd78af_13": "sha256:6b87c4409792b2d3195667f0b94f563c3a61b4b30a8664c4c807aca4defc9989"}, "docker": "quay.io/biocontainers/bioconductor-hgu219probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu219probe.
shpc-registry automated BioContainers addition for bioconductor-hgu219probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu219probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu219probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu219probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu219probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu219probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu219probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu219probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu219probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu219probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu219probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu219probe

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