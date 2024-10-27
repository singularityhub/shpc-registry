---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogene10stv1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogene10stv1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogene10stv1probe/container.yaml"
updated_at: "2024-10-27 03:27:23.080981"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mogene10stv1probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mogene10stv1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogene10stv1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogene10stv1probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:481ca910f19d27f4d2a63ffc12f4844137ef21e3148115574cfa0bdb38f6f282"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:20877f3b2cfea19e25460f8a21fc263d75a09002ff17d9856f06c5957a0dcf95", "2.18.0--r42hdfd78af_10": "sha256:9ca75a92bd48d9b1497cfab627a33fb86c7cf9aeaed1de6d1aa7372653c55efe", "2.18.0--r43hdfd78af_11": "sha256:bf5580fd0ee040512ff08646c5c8c7017f931a6dbedd1ce6c371c87b586eebe2", "2.18.0--r43hdfd78af_12": "sha256:481ca910f19d27f4d2a63ffc12f4844137ef21e3148115574cfa0bdb38f6f282"}, "docker": "quay.io/biocontainers/bioconductor-mogene10stv1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogene10stv1probe.
shpc-registry automated BioContainers addition for bioconductor-mogene10stv1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene10stv1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene10stv1probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogene10stv1probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mogene10stv1probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogene10stv1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene10stv1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene10stv1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogene10stv1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogene10stv1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogene10stv1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogene10stv1probe

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