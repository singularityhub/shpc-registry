---
layout: container
name:  "quay.io/biocontainers/bioconductor-abarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-abarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-abarray/container.yaml"
updated_at: "2025-09-04 03:46:36.824259"
latest: "1.74.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-abarray"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.74.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-abarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-abarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-abarray", "latest": {"1.74.0--r44hdfd78af_0": "sha256:076ab0af91e5a95fed16d8f7ce6d8f62b4e37c222f3bf2949d9cd3364227b509"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:137a9d0885b497ca9fac7d4bea9112004367014e3ef8499be38968edb9de63d4", "1.66.0--r42hdfd78af_0": "sha256:8a717cc48a327383989961bb124fe020704842d989ff1d6d08b49f9b1b3c58bb", "1.68.0--r43hdfd78af_0": "sha256:f0b0cfb526e196d7f7168063df6d4e8c9dee6721cb5192b8c77974111519e532", "1.70.0--r43hdfd78af_0": "sha256:f000475e704babb9d973176070ec48a67f9ff111a50bcc41d822f856950f6542", "1.74.0--r44hdfd78af_0": "sha256:076ab0af91e5a95fed16d8f7ce6d8f62b4e37c222f3bf2949d9cd3364227b509"}, "docker": "quay.io/biocontainers/bioconductor-abarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-abarray.
shpc-registry automated BioContainers addition for bioconductor-abarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-abarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-abarray:1.74.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-abarray/1.74.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-abarray/1.74.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-abarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-abarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-abarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-abarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-abarray

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