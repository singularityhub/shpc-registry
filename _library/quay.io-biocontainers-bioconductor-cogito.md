---
layout: container
name:  "quay.io/biocontainers/bioconductor-cogito"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cogito/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cogito/container.yaml"
updated_at: "2024-04-19 03:07:43.769914"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cogito"
aliases:
 - "pandoc"
versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cogito"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cogito", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cogito", "latest": {"1.8.0--r43hdfd78af_0": "sha256:ec6b136b364c53b3f6f9ca52b488c7461f269fd9e159a33ed287bf585ac08cae"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:a7e1aaae7f25d70c9e4d46e347855bff1e5ffac979d6a51e39b032cdbd3ee085", "1.4.0--r42hdfd78af_0": "sha256:1297935cd8dd924372e1737219193d188e29a03b96c4e0939319cb70ca734132", "1.6.0--r43hdfd78af_0": "sha256:946f92afcb7ac915a875c2d61ac24eedd5bedb310ac002d39bc4b3aa1360e5a7", "1.8.0--r43hdfd78af_0": "sha256:ec6b136b364c53b3f6f9ca52b488c7461f269fd9e159a33ed287bf585ac08cae"}, "docker": "quay.io/biocontainers/bioconductor-cogito", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cogito.
shpc-registry automated BioContainers addition for bioconductor-cogito
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cogito
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cogito:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cogito/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cogito/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cogito-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogito-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogito-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cogito-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cogito-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cogito-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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