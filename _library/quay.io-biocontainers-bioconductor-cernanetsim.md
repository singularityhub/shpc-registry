---
layout: container
name:  "quay.io/biocontainers/bioconductor-cernanetsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cernanetsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cernanetsim/container.yaml"
updated_at: "2024-09-05 04:36:39.254427"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cernanetsim"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cernanetsim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cernanetsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cernanetsim", "latest": {"1.14.0--r43hdfd78af_0": "sha256:5b4ef09a88d4473aad2d75c61ff19e31ed6c75d6e666ce5b244b64487bd70a5d"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:bd1638693f7e75e6416da47c8115b356928fea61ec93009dfe50c65a5fb1896c", "1.10.0--r42hdfd78af_0": "sha256:563f23abcc17c6527af533a88e3dd30a3d26eb348775d4901f1997c240ac467c", "1.12.0--r43hdfd78af_0": "sha256:52b7ddaca3a913f21d70cb68952fc79088739fa5bcb4be32568da89b3507b9d9", "1.14.0--r43hdfd78af_0": "sha256:5b4ef09a88d4473aad2d75c61ff19e31ed6c75d6e666ce5b244b64487bd70a5d"}, "docker": "quay.io/biocontainers/bioconductor-cernanetsim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cernanetsim.
shpc-registry automated BioContainers addition for bioconductor-cernanetsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cernanetsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cernanetsim:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cernanetsim/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cernanetsim/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cernanetsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cernanetsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cernanetsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cernanetsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cernanetsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cernanetsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cernanetsim

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