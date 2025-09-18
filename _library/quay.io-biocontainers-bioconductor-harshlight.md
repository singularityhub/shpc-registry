---
layout: container
name:  "quay.io/biocontainers/bioconductor-harshlight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-harshlight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-harshlight/container.yaml"
updated_at: "2025-09-18 03:33:48.841701"
latest: "1.78.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-harshlight"

versions:
 - "1.66.0--r41hc0cfd56_2"
 - "1.70.0--r42hc0cfd56_0"
 - "1.70.0--r42ha9d7317_1"
 - "1.72.0--r43ha9d7317_0"
 - "1.74.0--r43ha9d7317_0"
 - "1.78.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-harshlight"
config: {"url": "https://biocontainers.pro/tools/bioconductor-harshlight", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-harshlight", "latest": {"1.78.0--r44h3df3fcb_0": "sha256:49f24a66687c637873de9b63645b220fd4eaac113c840bed5662d4e19ac5c2e7"}, "tags": {"1.66.0--r41hc0cfd56_2": "sha256:4b17c72c615160929b78955a0a76acc0806c6ce4a9c03b9e52359a0313c893af", "1.70.0--r42hc0cfd56_0": "sha256:0e2bfa62c0359ad1c88386c0e71c5dd3e92ba9ddbbeabebe64beb866535c12c7", "1.70.0--r42ha9d7317_1": "sha256:370c69285fda5ff6d18da759a3a6cf05b1ab03256434663a71fd6912f32c9468", "1.72.0--r43ha9d7317_0": "sha256:e0832ad6041fdff2d1678e018d765fb90a5663cc79c62a96e3e2352a6d70af78", "1.74.0--r43ha9d7317_0": "sha256:8d1ae486bded89aaf19b8a041deb79a0b475d03bc0b7a27501db149d4c8b3b14", "1.78.0--r44h3df3fcb_0": "sha256:49f24a66687c637873de9b63645b220fd4eaac113c840bed5662d4e19ac5c2e7"}, "docker": "quay.io/biocontainers/bioconductor-harshlight"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-harshlight.
shpc-registry automated BioContainers addition for bioconductor-harshlight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-harshlight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-harshlight:1.78.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-harshlight/1.78.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-harshlight/1.78.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-harshlight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harshlight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harshlight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-harshlight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-harshlight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-harshlight-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-harshlight

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