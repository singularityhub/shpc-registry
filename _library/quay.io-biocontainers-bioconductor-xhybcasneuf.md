---
layout: container
name:  "quay.io/biocontainers/bioconductor-xhybcasneuf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xhybcasneuf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xhybcasneuf/container.yaml"
updated_at: "2023-08-02 02:35:34.832219"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xhybcasneuf"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xhybcasneuf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xhybcasneuf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xhybcasneuf", "latest": {"1.38.0--r43hdfd78af_0": "sha256:8134d6277c54d6e32b9b2e2287335c76362471a5f60d315cb3c10cbaf02037c2"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:77ebdc528a4e8df041d1b68eef0a084fe7f8b32a1f7ed253da2e1a0aca29c65a", "1.36.0--r42hdfd78af_0": "sha256:b252f02b165d936a3e659b6ad5456588f914f93c629ad557efdd56e27a934a82", "1.38.0--r43hdfd78af_0": "sha256:8134d6277c54d6e32b9b2e2287335c76362471a5f60d315cb3c10cbaf02037c2"}, "docker": "quay.io/biocontainers/bioconductor-xhybcasneuf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xhybcasneuf.
shpc-registry automated BioContainers addition for bioconductor-xhybcasneuf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xhybcasneuf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xhybcasneuf:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xhybcasneuf/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xhybcasneuf/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xhybcasneuf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xhybcasneuf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xhybcasneuf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xhybcasneuf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xhybcasneuf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xhybcasneuf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xhybcasneuf

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