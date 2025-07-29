---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationdbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationdbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationdbi/container.yaml"
updated_at: "2025-07-29 04:38:52.714248"
latest: "1.68.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationdbi"

versions:
 - "1.56.2--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.2--r43hdfd78af_0"
 - "1.64.1--r43hdfd78af_0"
 - "1.68.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationdbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationdbi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationdbi", "latest": {"1.68.0--r44hdfd78af_0": "sha256:812f8fa424f8bb6bd7c72950c1bd381dd76ca428014fde435df9a63e0468c256"}, "tags": {"1.56.2--r41hdfd78af_0": "sha256:f4754894b7675f9cc3de91ec2a27681c5cabb25190e225b63d78d2202eb771a2", "1.60.0--r42hdfd78af_0": "sha256:e086b8d2a7f2c69110a26a5c20c56c3b131d750fc6f88615c366c9088ba06346", "1.62.2--r43hdfd78af_0": "sha256:b59c300a7fda74821bf447ff9945272abeed2e2ea008957cdc275d5bdbefda6a", "1.64.1--r43hdfd78af_0": "sha256:2d3d460efbc639fafc82bf67ad3c500652db44bd7b1c1bb2632271b3f8659135", "1.68.0--r44hdfd78af_0": "sha256:812f8fa424f8bb6bd7c72950c1bd381dd76ca428014fde435df9a63e0468c256"}, "docker": "quay.io/biocontainers/bioconductor-annotationdbi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationdbi.
shpc-registry automated BioContainers addition for bioconductor-annotationdbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationdbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationdbi:1.68.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationdbi/1.68.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationdbi/1.68.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationdbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationdbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationdbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationdbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationdbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationdbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-annotationdbi

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