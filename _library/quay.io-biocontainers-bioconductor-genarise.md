---
layout: container
name:  "quay.io/biocontainers/bioconductor-genarise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genarise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genarise/container.yaml"
updated_at: "2024-05-01 02:52:10.546559"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genarise"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genarise"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genarise", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genarise", "latest": {"1.78.0--r43hdfd78af_0": "sha256:1d5eeff2aebb5e2efc33df26524c722068a95830e1d6ba92a7c7969be6718a66"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:8dad6c6dedae5d939d71efc9c152850ce5265a338c8893eeec81536333c456f7", "1.74.0--r42hdfd78af_0": "sha256:5d2fd7f04b75a772bb121b0a21ec25765c546448be97fc37cb9564c19dfffe8b", "1.76.0--r43hdfd78af_0": "sha256:11658199ab196414eaff827d7013c4562d421aad2619928f3b4b1254743e9f7c", "1.78.0--r43hdfd78af_0": "sha256:1d5eeff2aebb5e2efc33df26524c722068a95830e1d6ba92a7c7969be6718a66"}, "docker": "quay.io/biocontainers/bioconductor-genarise"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genarise.
shpc-registry automated BioContainers addition for bioconductor-genarise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genarise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genarise:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genarise/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genarise/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genarise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genarise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genarise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genarise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genarise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genarise-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genarise

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