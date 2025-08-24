---
layout: container
name:  "quay.io/biocontainers/bioconductor-peca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-peca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-peca/container.yaml"
updated_at: "2025-08-24 03:38:17.700388"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-peca"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-peca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-peca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-peca", "latest": {"1.42.0--r44hdfd78af_0": "sha256:3bf05ea1a885c06d23653252d11aa7a00cf519755a5150526f411894f7705928"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:4207e7638070f92d91f786a52eab99848c5c28478c4f0c4210890c954a7bdee0", "1.34.0--r42hdfd78af_0": "sha256:23bd8f4ed455a0a9cca3bc330ba9f3a57ed701ed1ec83d8a8e202ea6120ddf25", "1.36.0--r43hdfd78af_0": "sha256:4a90e6c4673421d5106516b5cb78fbc7c8c721aeeaa73f0cd9804257d3acc6c3", "1.38.0--r43hdfd78af_0": "sha256:4f5a10a2b430353e09a4ea31cd6b7cb3bf07aba007971367bd269f30bb4895d3", "1.42.0--r44hdfd78af_0": "sha256:3bf05ea1a885c06d23653252d11aa7a00cf519755a5150526f411894f7705928"}, "docker": "quay.io/biocontainers/bioconductor-peca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-peca.
shpc-registry automated BioContainers addition for bioconductor-peca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-peca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-peca:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-peca/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-peca/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-peca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-peca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-peca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-peca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-peca

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