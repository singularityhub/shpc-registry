---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylsig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylsig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylsig/container.yaml"
updated_at: "2024-06-27 02:41:15.809823"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylsig"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylsig"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylsig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylsig", "latest": {"1.12.0--r43hdfd78af_0": "sha256:47961c23cad21676b3a1f87487b09f85cddf10d33062614a6567faedc20ac0c8"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:d3e845880b55ad55be33c67b44d577580dd09cb94070a24ded50709406081a72", "1.10.0--r42hdfd78af_0": "sha256:7e72a99bddb8e72683d93512a3341126eb3dffe115774a867999673dd2a88bfa", "1.12.0--r43hdfd78af_0": "sha256:47961c23cad21676b3a1f87487b09f85cddf10d33062614a6567faedc20ac0c8"}, "docker": "quay.io/biocontainers/bioconductor-methylsig"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylsig.
shpc-registry automated BioContainers addition for bioconductor-methylsig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylsig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylsig:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylsig/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylsig/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylsig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylsig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylsig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylsig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylsig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylsig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylsig

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