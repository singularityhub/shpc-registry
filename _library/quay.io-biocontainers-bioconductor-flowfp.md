---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowfp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowfp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowfp/container.yaml"
updated_at: "2025-05-08 03:18:11.086119"
latest: "1.64.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowfp"

versions:
 - "1.52.0--r41hc0cfd56_2"
 - "1.55.0--r42hc0cfd56_0"
 - "1.55.0--r42ha9d7317_1"
 - "1.58.0--r43ha9d7317_0"
 - "1.60.0--r43ha9d7317_0"
 - "1.60.0--r43ha9d7317_1"
 - "1.64.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowfp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowfp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowfp", "latest": {"1.64.0--r44h3df3fcb_0": "sha256:4e42d78df1cd96de2467e693d7f80f5bf72bd85bea17eaaeeaa3f44c3d0cd698"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:ce96a5de066a42427c38cee6c22769f742c143c5eed6ae7dcfe7fa91cd914e39", "1.55.0--r42hc0cfd56_0": "sha256:b2bc182ff5417117b7b69d6f1d9fadf29a76b99ce5f3d01b577ffc887a6b14f9", "1.55.0--r42ha9d7317_1": "sha256:79837ea503477fb488e58bdb0b078c726635b7429b45e5176db06cd299578b33", "1.58.0--r43ha9d7317_0": "sha256:4913c2c3f2c068088565ab389c7771bc79b396edc880b604e11f7711e4d92ec9", "1.60.0--r43ha9d7317_0": "sha256:112b4ad9535f1d591090809cbcb72a65a3ec37d02916f1da33a438d99eac237c", "1.60.0--r43ha9d7317_1": "sha256:943f625393a5f0b33dd70d26a73ce7ef131d9c208ee6840e51008aacd9dca431", "1.64.0--r44h3df3fcb_0": "sha256:4e42d78df1cd96de2467e693d7f80f5bf72bd85bea17eaaeeaa3f44c3d0cd698"}, "docker": "quay.io/biocontainers/bioconductor-flowfp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowfp.
shpc-registry automated BioContainers addition for bioconductor-flowfp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowfp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowfp:1.64.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowfp/1.64.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-flowfp/1.64.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowfp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowfp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowfp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowfp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowfp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowfp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowfp

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