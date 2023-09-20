---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcaspar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcaspar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcaspar/container.yaml"
updated_at: "2023-09-20 02:28:53.890989"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcaspar"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcaspar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcaspar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcaspar", "latest": {"1.46.0--r43hdfd78af_0": "sha256:ccad3ae3864456709fd8baaca9e02183e39708ee3dd11aed18ed9c4d57d70d43"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:62e7ef8f59289c9e4da8ab185b14f28ddb71e08d3277f96d243e32f3cd9f0d39", "1.44.0--r42hdfd78af_0": "sha256:f9cf72f2c15e7e69ed2355e87314a8300b6ec1488362becdeea16aec055f97a5", "1.46.0--r43hdfd78af_0": "sha256:ccad3ae3864456709fd8baaca9e02183e39708ee3dd11aed18ed9c4d57d70d43"}, "docker": "quay.io/biocontainers/bioconductor-rcaspar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcaspar.
shpc-registry automated BioContainers addition for bioconductor-rcaspar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcaspar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcaspar:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcaspar/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcaspar/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcaspar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcaspar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcaspar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcaspar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcaspar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcaspar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rcaspar

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