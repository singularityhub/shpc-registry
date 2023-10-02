---
layout: container
name:  "quay.io/biocontainers/bioconductor-aggregatebiovar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aggregatebiovar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aggregatebiovar/container.yaml"
updated_at: "2023-10-02 03:02:24.843071"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aggregatebiovar"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aggregatebiovar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aggregatebiovar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aggregatebiovar", "latest": {"1.10.0--r43hdfd78af_0": "sha256:8303704dec8980139a865a00e70271606a588f0b04b7529945e9854c212410c6"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:acedd03811fad2a91da150d743b241be11ff3720e37ca8b8a12ec631585dff3a", "1.8.0--r42hdfd78af_0": "sha256:a61b5fa188901538afb569013f965e2e6bd4dd991b9d1d240b1247db6eead1b8", "1.10.0--r43hdfd78af_0": "sha256:8303704dec8980139a865a00e70271606a588f0b04b7529945e9854c212410c6"}, "docker": "quay.io/biocontainers/bioconductor-aggregatebiovar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aggregatebiovar.
shpc-registry automated BioContainers addition for bioconductor-aggregatebiovar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aggregatebiovar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aggregatebiovar:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aggregatebiovar/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aggregatebiovar/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aggregatebiovar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aggregatebiovar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aggregatebiovar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aggregatebiovar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aggregatebiovar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aggregatebiovar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-aggregatebiovar

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