---
layout: container
name:  "quay.io/biocontainers/arcas-hla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arcas-hla/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/arcas-hla/container.yaml"
updated_at: "2022-10-27 01:00:17.293927"
latest: "0.5.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/arcas-hla"
aliases:
 - "arcasHLA"
 - "git-lfs"
 - "kallisto"
versions:
 - "0.5.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for arcas-hla"
config: {"url": "https://biocontainers.pro/tools/arcas-hla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arcas-hla", "latest": {"0.5.0--hdfd78af_0": "sha256:85af348c01828a4f10da7f658b999e442413650c4fc3df5c07bb714c8d22868c"}, "tags": {"0.5.0--hdfd78af_0": "sha256:85af348c01828a4f10da7f658b999e442413650c4fc3df5c07bb714c8d22868c"}, "docker": "quay.io/biocontainers/arcas-hla", "aliases": {"arcasHLA": "/usr/local/bin/arcasHLA", "git-lfs": "/usr/local/bin/git-lfs", "kallisto": "/usr/local/bin/kallisto"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arcas-hla.
shpc-registry automated BioContainers addition for arcas-hla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arcas-hla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arcas-hla:0.5.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arcas-hla/0.5.0--hdfd78af_0
$ module help quay.io/biocontainers/arcas-hla/0.5.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arcas-hla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arcas-hla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arcas-hla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arcas-hla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arcas-hla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arcas-hla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arcasHLA

```bash
$ singularity exec <container> /usr/local/bin/arcasHLA
$ podman run --it --rm --entrypoint /usr/local/bin/arcasHLA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcasHLA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-lfs

```bash
$ singularity exec <container> /usr/local/bin/git-lfs
$ podman run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
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