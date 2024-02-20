---
layout: container
name:  "quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db/container.yaml"
updated_at: "2024-02-20 03:03:08.371687"
latest: "1.4.1--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-gghumanmethcancerpanelv1.db"

versions:
 - "1.4.1--r41hdfd78af_9"
 - "1.4.1--r42hdfd78af_10"
 - "1.4.1--r43hdfd78af_11"
 - "1.4.1--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-gghumanmethcancerpanelv1.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gghumanmethcancerpanelv1.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gghumanmethcancerpanelv1.db", "latest": {"1.4.1--r43hdfd78af_12": "sha256:abb62bd19ed778c5f9ae0792de81938de82fccdde3a9095969063ca6bb9004f9"}, "tags": {"1.4.1--r41hdfd78af_9": "sha256:4f26d92cafe0dac833df9a49c0b90e65423f48cbee9b8cf82abbf30498151495", "1.4.1--r42hdfd78af_10": "sha256:7ebfdfa2d7177c31308936e2e51ff394cef4d46f723eb5cb2652224538faa788", "1.4.1--r43hdfd78af_11": "sha256:3318953e43ba43b729cc8474bfb6835e53e48d69531130c1258e8a25f1d170eb", "1.4.1--r43hdfd78af_12": "sha256:abb62bd19ed778c5f9ae0792de81938de82fccdde3a9095969063ca6bb9004f9"}, "docker": "quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db.
shpc-registry automated BioContainers addition for bioconductor-gghumanmethcancerpanelv1.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db:1.4.1--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db/1.4.1--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-gghumanmethcancerpanelv1.db/1.4.1--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gghumanmethcancerpanelv1.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gghumanmethcancerpanelv1.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gghumanmethcancerpanelv1.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gghumanmethcancerpanelv1.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gghumanmethcancerpanelv1.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gghumanmethcancerpanelv1.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gghumanmethcancerpanelv1.db

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