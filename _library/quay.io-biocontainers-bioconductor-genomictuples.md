---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomictuples"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomictuples/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomictuples/container.yaml"
updated_at: "2024-04-18 02:29:13.215637"
latest: "1.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomictuples"

versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomictuples"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomictuples", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomictuples", "latest": {"1.36.0--r43hf17093f_0": "sha256:37163a0c0f9d1466f6b449b776e8e321f7d2c10bbda6bd4fb0359e4e1ac36cd0"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:ba646903267be89a5541677cc410b66802c81702330a95fef85df83c6557d57b", "1.32.0--r42hc247a5b_0": "sha256:29f3e7f0436601c5e745ecb0f3498b11f0dc7d54b417e3923a3a88b44bf2d162", "1.32.0--r42hf17093f_1": "sha256:52a168a34950d1fb709876c05afda917709b92844a3cc10f6b7ad60e641268ce", "1.34.0--r43hf17093f_0": "sha256:28994679e2ac45bb8e435e9908b67f5fe09eb3df878d97e2c685c2214c3ecf94", "1.36.0--r43hf17093f_0": "sha256:37163a0c0f9d1466f6b449b776e8e321f7d2c10bbda6bd4fb0359e4e1ac36cd0"}, "docker": "quay.io/biocontainers/bioconductor-genomictuples"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomictuples.
shpc-registry automated BioContainers addition for bioconductor-genomictuples
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomictuples
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomictuples:1.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomictuples/1.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-genomictuples/1.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomictuples-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomictuples-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomictuples-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomictuples-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomictuples-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomictuples-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomictuples

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