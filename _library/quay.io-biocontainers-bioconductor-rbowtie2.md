---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbowtie2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbowtie2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbowtie2/container.yaml"
updated_at: "2024-11-06 02:54:57.104980"
latest: "2.8.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rbowtie2"

versions:
 - "2.0.0--r41he06c1ba_2"
 - "2.4.0--r42he06c1ba_0"
 - "2.4.0--r42h639f7a0_1"
 - "2.6.0--r43h639f7a0_0"
 - "2.8.0--r43hf17093f_0"
 - "2.8.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rbowtie2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbowtie2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbowtie2", "latest": {"2.8.0--r43hf17093f_1": "sha256:c2f6b7c3b3478a45291570d6ed62d53c44cf6d3bf2afe4ac524577358b28009c"}, "tags": {"2.0.0--r41he06c1ba_2": "sha256:bb26b0a663dc59c90296d8f6772bffcb4080e2b75a4d54fef0b0285426e637a3", "2.4.0--r42he06c1ba_0": "sha256:b4f16088639ce0c82658ca4a13e3cc45fe982d41e11af01c1fc971bca2925086", "2.4.0--r42h639f7a0_1": "sha256:6a54fced241e4a40453f34862db0fb59dce451fbf105231d524d82c38dec0ed6", "2.6.0--r43h639f7a0_0": "sha256:e13033bb0c0a287128e00683dd3ca5290bb5345fa464e4627c05f1397011201c", "2.8.0--r43hf17093f_0": "sha256:c8ea23e8d24db1b1992724116965a69fe5f5b7310098f60dd4a007b34acb8214", "2.8.0--r43hf17093f_1": "sha256:c2f6b7c3b3478a45291570d6ed62d53c44cf6d3bf2afe4ac524577358b28009c"}, "docker": "quay.io/biocontainers/bioconductor-rbowtie2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbowtie2.
shpc-registry automated BioContainers addition for bioconductor-rbowtie2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbowtie2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbowtie2:2.8.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbowtie2/2.8.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-rbowtie2/2.8.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbowtie2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbowtie2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbowtie2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbowtie2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbowtie2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbowtie2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbowtie2

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