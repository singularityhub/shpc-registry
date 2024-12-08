---
layout: container
name:  "quay.io/biocontainers/bioconductor-minimumdistance"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-minimumdistance/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-minimumdistance/container.yaml"
updated_at: "2024-12-08 03:57:16.274021"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-minimumdistance"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-minimumdistance"
config: {"url": "https://biocontainers.pro/tools/bioconductor-minimumdistance", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-minimumdistance", "latest": {"1.46.0--r43hdfd78af_0": "sha256:507ed6ccaf52017517fbde79d313ff00c13e8de5a067c66120c02fbd73e80292"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:f4305dcd3aac9a96865a76c19a309eb5d4b20a7cc3317bf10a4ceb8e8d43b464", "1.42.0--r42hdfd78af_0": "sha256:39c5d9770a222678f4acc44e5b515e249bbbe9e5236a95b9745ab5de281b6bb1", "1.44.0--r43hdfd78af_0": "sha256:23547d7b08f6c478e190185288df3ca425f140e41daefe3729bd5ec4bc1977e1", "1.46.0--r43hdfd78af_0": "sha256:507ed6ccaf52017517fbde79d313ff00c13e8de5a067c66120c02fbd73e80292"}, "docker": "quay.io/biocontainers/bioconductor-minimumdistance"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-minimumdistance.
shpc-registry automated BioContainers addition for bioconductor-minimumdistance
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-minimumdistance
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-minimumdistance:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-minimumdistance/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-minimumdistance/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-minimumdistance-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minimumdistance-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minimumdistance-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-minimumdistance-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-minimumdistance-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-minimumdistance-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-minimumdistance

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