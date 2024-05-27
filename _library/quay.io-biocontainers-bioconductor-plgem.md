---
layout: container
name:  "quay.io/biocontainers/bioconductor-plgem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plgem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plgem/container.yaml"
updated_at: "2024-05-27 02:49:58.604214"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plgem"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plgem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plgem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plgem", "latest": {"1.74.0--r43hdfd78af_0": "sha256:42bacd56591ee6ad52f4d80c858ca8db817066b3be528d121ce06521ec43cc4a"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:887302c2dc0d7090ce32d927b575b68d521a7b694bbd33f53ca0abdbd284ea66", "1.70.0--r42hdfd78af_0": "sha256:da98b069b3ef2356812b88188808be9548801fc8a4ba4b0765ff60bd7aaf1c21", "1.72.0--r43hdfd78af_0": "sha256:abe1343a606811bd1da0e8a61d1097b9ad6008c1b6f57dbab8288da979796d0c", "1.74.0--r43hdfd78af_0": "sha256:42bacd56591ee6ad52f4d80c858ca8db817066b3be528d121ce06521ec43cc4a"}, "docker": "quay.io/biocontainers/bioconductor-plgem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plgem.
shpc-registry automated BioContainers addition for bioconductor-plgem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plgem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plgem:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plgem/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-plgem/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plgem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plgem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plgem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plgem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plgem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plgem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plgem

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