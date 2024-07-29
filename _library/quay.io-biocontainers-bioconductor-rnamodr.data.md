---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnamodr.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnamodr.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnamodr.data/container.yaml"
updated_at: "2024-07-29 17:16:34.406550"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnamodr.data"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnamodr.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnamodr.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnamodr.data", "latest": {"1.16.0--r43hdfd78af_0": "sha256:c1327db97178b519608c742688c169b1e63c78aa6a01006bebc51d27dc0cc2db"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:7fea50e299c4f84f96ade804b29fd45795c23aeaf7a65038418e474c21eeef50", "1.12.0--r42hdfd78af_0": "sha256:69006bea4e7fc03c2ccb6e2834e1974ee27ab12c0eef0327cba58fc461991d7d", "1.14.0--r43hdfd78af_0": "sha256:e6f70e912033d9e3002a7924affd415f569b188fbaa6d00fea002fc2e4b2f50a", "1.16.0--r43hdfd78af_0": "sha256:c1327db97178b519608c742688c169b1e63c78aa6a01006bebc51d27dc0cc2db"}, "docker": "quay.io/biocontainers/bioconductor-rnamodr.data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnamodr.data.
shpc-registry automated BioContainers addition for bioconductor-rnamodr.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.data:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnamodr.data/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnamodr.data/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnamodr.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnamodr.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnamodr.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnamodr.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnamodr.data

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