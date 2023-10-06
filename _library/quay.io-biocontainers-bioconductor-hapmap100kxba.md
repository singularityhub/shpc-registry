---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmap100kxba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmap100kxba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmap100kxba/container.yaml"
updated_at: "2023-10-06 02:55:52.212535"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmap100kxba"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.39.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmap100kxba"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmap100kxba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmap100kxba", "latest": {"1.42.0--r43hdfd78af_0": "sha256:c145fb1baeb80d5acf89e77a89becc597a4d6a564716080bf60475ea047f7e2d"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:f249d4f5ca34ac695b6ed16173e5ada0af72ec3833c77b5c45ede298bc4b1a3a", "1.39.0--r42hdfd78af_0": "sha256:7aaf59d0d0efa8796f1de2bcd6a0a1f9f946d7082c5229a7e31df175c52c5699", "1.42.0--r43hdfd78af_0": "sha256:c145fb1baeb80d5acf89e77a89becc597a4d6a564716080bf60475ea047f7e2d"}, "docker": "quay.io/biocontainers/bioconductor-hapmap100kxba"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmap100kxba.
shpc-registry automated BioContainers addition for bioconductor-hapmap100kxba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap100kxba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap100kxba:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmap100kxba/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hapmap100kxba/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmap100kxba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap100kxba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap100kxba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmap100kxba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmap100kxba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmap100kxba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmap100kxba

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