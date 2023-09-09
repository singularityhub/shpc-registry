---
layout: container
name:  "quay.io/biocontainers/bioconductor-prostatecancerstockholm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prostatecancerstockholm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prostatecancerstockholm/container.yaml"
updated_at: "2023-09-09 02:24:51.960920"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prostatecancerstockholm"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prostatecancerstockholm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prostatecancerstockholm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prostatecancerstockholm", "latest": {"1.28.0--r43hdfd78af_0": "sha256:b5db83a05faba525a899ae35a2d3a40bc28f54f07713e4f35ba66410a50c1ae4"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:1e0fb9c4e1ca359b2d3e81e3453211c0e76f02c1b0e43e80019bd54217a8ded5", "1.26.0--r42hdfd78af_0": "sha256:01741c4ad08e0e02ddb16fdfced7173b894914defb81050ee25559fd24450713", "1.28.0--r43hdfd78af_0": "sha256:b5db83a05faba525a899ae35a2d3a40bc28f54f07713e4f35ba66410a50c1ae4"}, "docker": "quay.io/biocontainers/bioconductor-prostatecancerstockholm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prostatecancerstockholm.
shpc-registry automated BioContainers addition for bioconductor-prostatecancerstockholm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancerstockholm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancerstockholm:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prostatecancerstockholm/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prostatecancerstockholm/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prostatecancerstockholm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancerstockholm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancerstockholm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prostatecancerstockholm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prostatecancerstockholm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prostatecancerstockholm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prostatecancerstockholm

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