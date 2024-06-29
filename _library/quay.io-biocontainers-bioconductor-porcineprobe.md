---
layout: container
name:  "quay.io/biocontainers/bioconductor-porcineprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-porcineprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-porcineprobe/container.yaml"
updated_at: "2024-06-29 02:52:31.660264"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-porcineprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-porcineprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-porcineprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-porcineprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:c9a988ea1438bacc1222827c738b4bf2b17cec13a93031c003988fd23627c2ee"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:fd4620b9fb0e285a13cb90a141a01353353fa39ae44687ab31871e3b774b4247", "2.18.0--r42hdfd78af_10": "sha256:39d96e0c45c39ed49f6ef7885f5d7bf92d745a5ab011b643f74ef66f2498e17c", "2.18.0--r43hdfd78af_11": "sha256:b8f3f807192aec9adfce6271a1ab47baabfcafae8df8c407825c9701b9a3b629", "2.18.0--r43hdfd78af_12": "sha256:c9a988ea1438bacc1222827c738b4bf2b17cec13a93031c003988fd23627c2ee"}, "docker": "quay.io/biocontainers/bioconductor-porcineprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-porcineprobe.
shpc-registry automated BioContainers addition for bioconductor-porcineprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-porcineprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-porcineprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-porcineprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-porcineprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-porcineprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-porcineprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-porcineprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-porcineprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-porcineprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-porcineprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-porcineprobe

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