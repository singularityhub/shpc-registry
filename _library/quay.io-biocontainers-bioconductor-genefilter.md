---
layout: container
name:  "quay.io/biocontainers/bioconductor-genefilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genefilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genefilter/container.yaml"
updated_at: "2025-01-17 03:05:17.509578"
latest: "1.88.0--r44h81e381d_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genefilter"

versions:
 - "1.76.0--r41h38f54d8_2"
 - "1.80.0--r42h38f54d8_0"
 - "1.80.0--r42ha1e849b_1"
 - "1.82.1--r43ha1e849b_0"
 - "1.84.0--r43ha1e849b_0"
 - "1.84.0--r43ha1e849b_1"
 - "1.88.0--r44h81e381d_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genefilter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genefilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genefilter", "latest": {"1.88.0--r44h81e381d_0": "sha256:2f58c30f97700d703845761353c1879ce6d9c1e63e57735c96da5f405fcef8e7"}, "tags": {"1.76.0--r41h38f54d8_2": "sha256:2c36dd9a71a0014a4905740549d8d6352f694116d191623803b52dc7597e833d", "1.80.0--r42h38f54d8_0": "sha256:bb0e456be2899b4ca41d58f34a2ff83c6b215aba32221af8497b567d6bdad0e8", "1.80.0--r42ha1e849b_1": "sha256:9e84bdc813e1a2521750a2cab4017ae2d187520662c6281bbaf6255980a6388f", "1.82.1--r43ha1e849b_0": "sha256:1753dbaef49366ad4bc676f5056684720d5c4235ef310279c3d2eb1511b332bb", "1.84.0--r43ha1e849b_0": "sha256:72e12959ec8238730621e2563f23c9932f403bb8b1d213284a8b8f005095a25a", "1.84.0--r43ha1e849b_1": "sha256:b7237f4d0ee376a559108eec5d172333691f23fc8225adb3d278f825db425157", "1.88.0--r44h81e381d_0": "sha256:2f58c30f97700d703845761353c1879ce6d9c1e63e57735c96da5f405fcef8e7"}, "docker": "quay.io/biocontainers/bioconductor-genefilter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genefilter.
shpc-registry automated BioContainers addition for bioconductor-genefilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genefilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genefilter:1.88.0--r44h81e381d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genefilter/1.88.0--r44h81e381d_0
$ module help quay.io/biocontainers/bioconductor-genefilter/1.88.0--r44h81e381d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genefilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genefilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genefilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genefilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genefilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genefilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genefilter

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