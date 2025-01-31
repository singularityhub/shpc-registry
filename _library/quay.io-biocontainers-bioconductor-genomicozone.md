---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicozone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicozone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicozone/container.yaml"
updated_at: "2025-01-31 03:31:39.574878"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicozone"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicozone"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicozone", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicozone", "latest": {"1.20.0--r44hdfd78af_0": "sha256:5a931fd3293827439d70ef2c1cd9cb62bf5150532a89769d29f6d69e17fcd7d3"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:cbb3518068e749c9ddb8ff6fa798174240ff548e69fe40e68d3aa7cfd64c3fd6", "1.12.0--r42hdfd78af_0": "sha256:722d8e014c0da215fd9fb4a1860e589ab2c9b9c3a22e27f856691f5de32868b2", "1.14.0--r43hdfd78af_0": "sha256:93af7827f8bb51003f5c07b349b21179c4dbc8a0084722384b7dd6930b0715ea", "1.16.0--r43hdfd78af_0": "sha256:da90482bf903c2bd6880682826522a3ed0b9827e47bc678dfaa3ca776f806399", "1.20.0--r44hdfd78af_0": "sha256:5a931fd3293827439d70ef2c1cd9cb62bf5150532a89769d29f6d69e17fcd7d3"}, "docker": "quay.io/biocontainers/bioconductor-genomicozone"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicozone.
shpc-registry automated BioContainers addition for bioconductor-genomicozone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicozone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicozone:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicozone/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicozone/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicozone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicozone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicozone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicozone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicozone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicozone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicozone

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