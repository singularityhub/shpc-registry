---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95av2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95av2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95av2/container.yaml"
updated_at: "2024-04-18 02:57:11.452754"
latest: "2.2.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95av2"

versions:
 - "2.2.0--r41hdfd78af_9"
 - "2.2.0--r42hdfd78af_10"
 - "2.2.0--r43hdfd78af_11"
 - "2.2.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95av2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95av2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95av2", "latest": {"2.2.0--r43hdfd78af_12": "sha256:d92c456987a36277d570cf095a9e473d1abfb66a8ff1f8d96370a1a46c1b1fb7"}, "tags": {"2.2.0--r41hdfd78af_9": "sha256:d5abe939d42b1acf81943487e44bc0dc2205c46e75f09eef514a8e7c8d2e4258", "2.2.0--r42hdfd78af_10": "sha256:f86b5b5528ae28646adb374587c1d96ccadf2d4cb7c46266d9c308f5d29c34b9", "2.2.0--r43hdfd78af_11": "sha256:714704d6d26b884af60861ee4a61d9ecb3b07de6f277dd75187196aa5cec825b", "2.2.0--r43hdfd78af_12": "sha256:d92c456987a36277d570cf095a9e473d1abfb66a8ff1f8d96370a1a46c1b1fb7"}, "docker": "quay.io/biocontainers/bioconductor-hgu95av2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95av2.
shpc-registry automated BioContainers addition for bioconductor-hgu95av2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2:2.2.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95av2/2.2.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu95av2/2.2.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95av2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95av2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95av2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95av2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95av2

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