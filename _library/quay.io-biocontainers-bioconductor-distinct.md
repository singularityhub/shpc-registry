---
layout: container
name:  "quay.io/biocontainers/bioconductor-distinct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-distinct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-distinct/container.yaml"
updated_at: "2024-12-09 03:11:05.337618"
latest: "1.12.2--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-distinct"

versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.2--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-distinct"
config: {"url": "https://biocontainers.pro/tools/bioconductor-distinct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-distinct", "latest": {"1.12.2--r43hf17093f_0": "sha256:b71ceb640b7b96b519ee30ab1c82bdbc66e61cc8246df6e5e4a3b004ed44403e"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:30688b1389360b9eda0606d2868bda169ff893f0d77ee6b96569c92429848869", "1.10.0--r42hc247a5b_0": "sha256:586889d983ef45d30915d5a2e520de60b270f33896257718c80ebf060c100f6a", "1.10.0--r42hf17093f_1": "sha256:00ea17a1760f16c614e9bf986848c8d9a2cdf047e104cf039ff5f00753a179fa", "1.12.2--r43hf17093f_0": "sha256:b71ceb640b7b96b519ee30ab1c82bdbc66e61cc8246df6e5e4a3b004ed44403e"}, "docker": "quay.io/biocontainers/bioconductor-distinct"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-distinct.
shpc-registry automated BioContainers addition for bioconductor-distinct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-distinct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-distinct:1.12.2--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-distinct/1.12.2--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-distinct/1.12.2--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-distinct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-distinct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-distinct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-distinct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-distinct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-distinct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-distinct

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