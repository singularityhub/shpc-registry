---
layout: container
name:  "quay.io/biocontainers/bioconductor-lea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lea/container.yaml"
updated_at: "2025-03-08 03:03:29.836070"
latest: "3.18.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lea"

versions:
 - "3.6.0--r41hc0cfd56_2"
 - "3.10.0--r42hc0cfd56_0"
 - "3.10.0--r42ha9d7317_1"
 - "3.12.2--r43ha9d7317_0"
 - "3.14.0--r43ha9d7317_0"
 - "3.18.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lea", "latest": {"3.18.0--r44h3df3fcb_0": "sha256:e0610ca24626e10f8c0582af88626e23c7a4decf2c1722eacd1f48753985b851"}, "tags": {"3.6.0--r41hc0cfd56_2": "sha256:3f695ff5825c63fad701e58b95394c76a847ae403a09e04a4472419e2209a5e5", "3.10.0--r42hc0cfd56_0": "sha256:eb7d0fc2b1fad8de2c5d015f7b40726b7cfc5fb98b860908d3ec4e2d54ff6184", "3.10.0--r42ha9d7317_1": "sha256:25d876cfcd70f4e3f5908d813180064f1586b3f7143f8143ac5f36bc1e15ee17", "3.12.2--r43ha9d7317_0": "sha256:c893efbac88ba39d55aa8e39e994fdcf526844fc7526491b29e16b32a90e8f96", "3.14.0--r43ha9d7317_0": "sha256:c7c65e42da93b54d45f99246804566beb1a9628826b554469eddf18db8d976d6", "3.18.0--r44h3df3fcb_0": "sha256:e0610ca24626e10f8c0582af88626e23c7a4decf2c1722eacd1f48753985b851"}, "docker": "quay.io/biocontainers/bioconductor-lea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lea.
shpc-registry automated BioContainers addition for bioconductor-lea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lea:3.18.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lea/3.18.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-lea/3.18.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lea

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