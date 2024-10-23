---
layout: container
name:  "quay.io/biocontainers/bioconductor-metabocoreutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metabocoreutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metabocoreutils/container.yaml"
updated_at: "2024-10-23 03:08:36.030671"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metabocoreutils"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metabocoreutils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metabocoreutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metabocoreutils", "latest": {"1.10.0--r43hdfd78af_0": "sha256:c3a566b2b7c2d290e69710dca02023d33eb4fe2df20b924a0582e4cd15efaea9"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:4bd83e2bd44751fa7eb0a510554f97c5c0bf8af7bdc5af3beb34f854630b94b8", "1.6.0--r42hdfd78af_0": "sha256:094fe1539b1d940f4974b7f092c65dce4deb850b96cd009cc49082dc19b70cc6", "1.8.0--r43hdfd78af_0": "sha256:aaf703d6e97fb0651d79349f92b82b703ff0597f7303ce122c2e4be1973f6b74", "1.10.0--r43hdfd78af_0": "sha256:c3a566b2b7c2d290e69710dca02023d33eb4fe2df20b924a0582e4cd15efaea9"}, "docker": "quay.io/biocontainers/bioconductor-metabocoreutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metabocoreutils.
shpc-registry automated BioContainers addition for bioconductor-metabocoreutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metabocoreutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metabocoreutils:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metabocoreutils/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metabocoreutils/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metabocoreutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabocoreutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabocoreutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metabocoreutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metabocoreutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metabocoreutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metabocoreutils

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