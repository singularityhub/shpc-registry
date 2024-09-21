---
layout: container
name:  "quay.io/biocontainers/bioconductor-rattus.norvegicus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rattus.norvegicus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rattus.norvegicus/container.yaml"
updated_at: "2024-09-21 03:26:52.774194"
latest: "1.3.1--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rattus.norvegicus"

versions:
 - "1.3.1--r41hdfd78af_9"
 - "1.3.1--r42hdfd78af_10"
 - "1.3.1--r43hdfd78af_11"
 - "1.3.1--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rattus.norvegicus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rattus.norvegicus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rattus.norvegicus", "latest": {"1.3.1--r43hdfd78af_12": "sha256:1f06d4b117f05fbad12103fa267465b46eed7a31b031e77fc9e3eee3a3e08e6e"}, "tags": {"1.3.1--r41hdfd78af_9": "sha256:5c71c7664c66440c55060799175f28b8f27e80586b18c0bbb5c88f4078e78e93", "1.3.1--r42hdfd78af_10": "sha256:a2043f173d8b56e1583024b26116198847c631cd86897298cee2dc91a9b7f040", "1.3.1--r43hdfd78af_11": "sha256:b1e724618d92950d342f435d4d8c6f06c7cdacaaf71423e06db0a47c56a71202", "1.3.1--r43hdfd78af_12": "sha256:1f06d4b117f05fbad12103fa267465b46eed7a31b031e77fc9e3eee3a3e08e6e"}, "docker": "quay.io/biocontainers/bioconductor-rattus.norvegicus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rattus.norvegicus.
shpc-registry automated BioContainers addition for bioconductor-rattus.norvegicus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rattus.norvegicus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rattus.norvegicus:1.3.1--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rattus.norvegicus/1.3.1--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rattus.norvegicus/1.3.1--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rattus.norvegicus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattus.norvegicus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattus.norvegicus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rattus.norvegicus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rattus.norvegicus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rattus.norvegicus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rattus.norvegicus

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