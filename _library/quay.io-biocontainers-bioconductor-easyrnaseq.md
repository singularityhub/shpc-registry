---
layout: container
name:  "quay.io/biocontainers/bioconductor-easyrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-easyrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-easyrnaseq/container.yaml"
updated_at: "2024-06-23 03:02:10.372851"
latest: "2.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-easyrnaseq"

versions:
 - "2.30.0--r41hdfd78af_0"
 - "2.34.0--r42hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
 - "2.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-easyrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-easyrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-easyrnaseq", "latest": {"2.38.0--r43hdfd78af_0": "sha256:b102f774a8c5f9de23871208520060e755f8946ac0356d9bead5fa1f787deeec"}, "tags": {"2.30.0--r41hdfd78af_0": "sha256:22c3f3b6083adf20982cd07afb453f718aa4af6bcc2d441dc7abeec17f41c1a7", "2.34.0--r42hdfd78af_0": "sha256:f88fb5ebafeb5ea73e9c92c5c0a1c5fe3166b51ab82bfd23b5d13f2050b8a10a", "2.36.0--r43hdfd78af_0": "sha256:b712c2f82c850fc0e322a9ee4fde48e93c06dbfdd8bc9158c8ce6b861ee63076", "2.38.0--r43hdfd78af_0": "sha256:b102f774a8c5f9de23871208520060e755f8946ac0356d9bead5fa1f787deeec"}, "docker": "quay.io/biocontainers/bioconductor-easyrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-easyrnaseq.
shpc-registry automated BioContainers addition for bioconductor-easyrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-easyrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-easyrnaseq:2.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-easyrnaseq/2.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-easyrnaseq/2.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-easyrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easyrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easyrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-easyrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-easyrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-easyrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-easyrnaseq

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