---
layout: container
name:  "quay.io/biocontainers/bioconductor-opossom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-opossom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-opossom/container.yaml"
updated_at: "2024-04-01 04:15:30.794737"
latest: "2.20.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-opossom"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r40h399db7b_1"
 - "2.16.0--r42hc247a5b_0"
 - "2.12.0--r41hc247a5b_2"
 - "2.10.0--r41h399db7b_0"
 - "2.16.0--r42hf17093f_1"
 - "2.18.0--r43hf17093f_0"
 - "2.20.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-opossom"
config: {"url": "https://biocontainers.pro/tools/bioconductor-opossom", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-opossom", "latest": {"2.20.0--r43hf17093f_0": "sha256:ffad6496fa9672c20878d38cb4aad00638fd6a24e3760924bf899a7afcf407e7"}, "tags": {"2.8.0--r40h399db7b_1": "sha256:04f9f710ffb40cb770ff3252f709449ac806b211608158b5e0375ce77d1941d6", "2.16.0--r42hc247a5b_0": "sha256:f508b69a45cea98df0145b4d151ba8a4e7ef6127a423a87d6689ab2e2c386aab", "2.12.0--r41hc247a5b_2": "sha256:85a086bed33f934005f3ff6137480075cbb8c3658db55eb227d1f1f59816d069", "2.10.0--r41h399db7b_0": "sha256:24034c05b6520cc3deb48f304bf56b7bcd22910b0b8089d64250e5a85572db12", "2.16.0--r42hf17093f_1": "sha256:2635eb069f094a2f1c7fcf0f75565fd381697da6ec3afe4108ff664c34086a9f", "2.18.0--r43hf17093f_0": "sha256:4cd86870d3ea89c16963d8454e6e922859db96bb5bffe2a3dcd1b988472b1d76", "2.20.0--r43hf17093f_0": "sha256:ffad6496fa9672c20878d38cb4aad00638fd6a24e3760924bf899a7afcf407e7"}, "docker": "quay.io/biocontainers/bioconductor-opossom", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-opossom.
shpc-registry automated BioContainers addition for bioconductor-opossom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-opossom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-opossom:2.20.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-opossom/2.20.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-opossom/2.20.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-opossom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opossom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opossom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-opossom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-opossom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-opossom-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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