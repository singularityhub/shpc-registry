---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellmigration"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellmigration/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellmigration/container.yaml"
updated_at: "2025-02-04 03:22:28.854203"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellmigration"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellmigration"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellmigration", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellmigration", "latest": {"1.14.0--r44hdfd78af_0": "sha256:ff8871d6ef85c7b3c8ddc2d73c44b821ee3161fe04f5c1275ca31de2e4f2b855"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:e696eab412b7757e4b5f2869f54a4e6eef98fd2d7840c4332129596688438dc0", "1.6.0--r42hdfd78af_0": "sha256:9752665a38303530886526fef2a97e83c155fbdfdc5593f738b6ec8433690901", "1.8.0--r43hdfd78af_0": "sha256:dff465a164399f18c4959e178885656b0f704d0dde158c9532b6780dcf9d313b", "1.10.0--r43hdfd78af_0": "sha256:8b1ebac0e4ca9959c42dcdd040488f170a772234d5fe262428d83c13dae8e58d", "1.14.0--r44hdfd78af_0": "sha256:ff8871d6ef85c7b3c8ddc2d73c44b821ee3161fe04f5c1275ca31de2e4f2b855"}, "docker": "quay.io/biocontainers/bioconductor-cellmigration"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellmigration.
shpc-registry automated BioContainers addition for bioconductor-cellmigration
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmigration
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmigration:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellmigration/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellmigration/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellmigration-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmigration-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmigration-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellmigration-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellmigration-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellmigration-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellmigration

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