---
layout: container
name:  "quay.io/biocontainers/bioconductor-marr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-marr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-marr/container.yaml"
updated_at: "2024-07-08 03:22:28.174403"
latest: "1.12.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-marr"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-marr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-marr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-marr", "latest": {"1.12.0--r43hf17093f_0": "sha256:8552214fa34fcda051387a8ccb0b39e878d1e4707bb6a8bcf42bb609e5940608"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:d51ada54a125eecbac88b074298a22aaa55f6ec626c5b03f00424193be09701d", "1.8.0--r42hc247a5b_0": "sha256:6050bcf0f6490b359dbb9cf47c58c2909743281eabbacc047d080d3cfb74c98c", "1.8.0--r42hf17093f_1": "sha256:72acc139994882e72f95f72dc169923a52f5ae6e5fdb5476aae640aaf176f74a", "1.10.0--r43hf17093f_0": "sha256:d2bf8f1054a1eb4df178a7bb25e85d7b130201933342490469b7302bb1c91ad3", "1.12.0--r43hf17093f_0": "sha256:8552214fa34fcda051387a8ccb0b39e878d1e4707bb6a8bcf42bb609e5940608"}, "docker": "quay.io/biocontainers/bioconductor-marr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-marr.
shpc-registry automated BioContainers addition for bioconductor-marr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-marr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-marr:1.12.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-marr/1.12.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-marr/1.12.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-marr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-marr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-marr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-marr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-marr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-marr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-marr

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