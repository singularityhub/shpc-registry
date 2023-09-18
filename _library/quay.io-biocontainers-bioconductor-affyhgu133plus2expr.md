---
layout: container
name:  "quay.io/biocontainers/bioconductor-affyhgu133plus2expr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affyhgu133plus2expr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affyhgu133plus2expr/container.yaml"
updated_at: "2023-09-18 02:36:30.776090"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affyhgu133plus2expr"

versions:
 - "1.28.0--r41hdfd78af_1"
 - "1.31.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affyhgu133plus2expr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affyhgu133plus2expr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affyhgu133plus2expr", "latest": {"1.34.0--r43hdfd78af_0": "sha256:77610bd5b1cbc0f8629677682ffa36c65a01edccdab3ca02bc3c8e9fade67d8f"}, "tags": {"1.28.0--r41hdfd78af_1": "sha256:73ab9d47237f519505a4faceb1cfefd0e0a90f388611185365dd7a36ef1e9785", "1.31.0--r42hdfd78af_0": "sha256:1180c26fc0bef5e9dd098f41118510d3527648d99a3ef9764494098f07c162b9", "1.34.0--r43hdfd78af_0": "sha256:77610bd5b1cbc0f8629677682ffa36c65a01edccdab3ca02bc3c8e9fade67d8f"}, "docker": "quay.io/biocontainers/bioconductor-affyhgu133plus2expr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affyhgu133plus2expr.
shpc-registry automated BioContainers addition for bioconductor-affyhgu133plus2expr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affyhgu133plus2expr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affyhgu133plus2expr:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affyhgu133plus2expr/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affyhgu133plus2expr/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affyhgu133plus2expr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyhgu133plus2expr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyhgu133plus2expr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affyhgu133plus2expr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affyhgu133plus2expr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affyhgu133plus2expr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affyhgu133plus2expr

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