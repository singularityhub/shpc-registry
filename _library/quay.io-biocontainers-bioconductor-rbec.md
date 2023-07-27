---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbec/container.yaml"
updated_at: "2023-07-27 05:33:30.259379"
latest: "1.6.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rbec"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rbec"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbec", "latest": {"1.6.0--r42hf17093f_1": "sha256:6d40113b49b40f54e5d599c4c0b852bff61763e1252a385510edc5940cd8866e"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:3e9f94d0700d48e4ba59d1be2e2de8933718036ebf173e7280ad07b121384332", "1.6.0--r42hc247a5b_0": "sha256:6cf26bce79a22ff9642a5f56085db0d00c8170dbe00d18748d56bc34cc99571f", "1.6.0--r42hf17093f_1": "sha256:6d40113b49b40f54e5d599c4c0b852bff61763e1252a385510edc5940cd8866e"}, "docker": "quay.io/biocontainers/bioconductor-rbec"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbec.
shpc-registry automated BioContainers addition for bioconductor-rbec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbec:1.6.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbec/1.6.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-rbec/1.6.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbec

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