---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosgenome1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosgenome1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosgenome1probe/container.yaml"
updated_at: "2025-12-24 03:58:00.616593"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-drosgenome1probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-drosgenome1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosgenome1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosgenome1probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:46734bf6db4c9d79d7f7d72e47c26451e0c2c96edcb13376eed8b4d90476b056"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:bd1b6315588f6b5f3e1f35650da5c24e394e836de69437a6ded2b52c02832c5e", "2.18.0--r42hdfd78af_10": "sha256:b064553cd27a7ee4ae96c01ab2cdd2aa32f866cd16b9fe38215201f4b0402611", "2.18.0--r43hdfd78af_11": "sha256:67838d223fac1f285561bb8da9476de378509cf7acb69425960c8dda11d41fd5", "2.18.0--r43hdfd78af_12": "sha256:1d4327c95844a0f0e9c0be49151572545c19e26d4b9f97ea4c0ec10eff913c72", "2.18.0--r44hdfd78af_13": "sha256:46734bf6db4c9d79d7f7d72e47c26451e0c2c96edcb13376eed8b4d90476b056"}, "docker": "quay.io/biocontainers/bioconductor-drosgenome1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosgenome1probe.
shpc-registry automated BioContainers addition for bioconductor-drosgenome1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosgenome1probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-drosgenome1probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosgenome1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosgenome1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosgenome1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosgenome1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drosgenome1probe

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