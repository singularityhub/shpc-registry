---
layout: container
name:  "quay.io/biocontainers/bioconductor-herper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-herper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-herper/container.yaml"
updated_at: "2024-09-16 03:03:38.716273"
latest: "1.12.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-herper"

versions:
 - "1.3.0--r41hdfd78af_0"
 - "1.7.2--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-herper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-herper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-herper", "latest": {"1.12.0--r43hdfd78af_1": "sha256:058231f2dcd9e31bad827076b7e8109fce5c91a91a6e1bdd001e6e89e4130317"}, "tags": {"1.3.0--r41hdfd78af_0": "sha256:99e28373a57a68fc90b9ca94aff2a976cdd4cde5b40e4a22659857beec210149", "1.7.2--r42hdfd78af_0": "sha256:9be69816c8df664a813f635e3ca3544fc8174722853308dd37aa6e3b7ddb052c", "1.10.0--r43hdfd78af_0": "sha256:94b884db21239cf10e9ba87182891f1f04c23fb1f4313003461d56f20370e183", "1.12.0--r43hdfd78af_1": "sha256:058231f2dcd9e31bad827076b7e8109fce5c91a91a6e1bdd001e6e89e4130317"}, "docker": "quay.io/biocontainers/bioconductor-herper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-herper.
shpc-registry automated BioContainers addition for bioconductor-herper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-herper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-herper:1.12.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-herper/1.12.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-herper/1.12.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-herper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-herper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-herper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-herper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-herper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-herper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-herper

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