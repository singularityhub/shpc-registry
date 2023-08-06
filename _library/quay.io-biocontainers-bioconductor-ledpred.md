---
layout: container
name:  "quay.io/biocontainers/bioconductor-ledpred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ledpred/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ledpred/container.yaml"
updated_at: "2023-08-06 02:49:03.288000"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ledpred"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ledpred"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ledpred", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ledpred", "latest": {"1.34.0--r43hdfd78af_0": "sha256:99292ddc169699577403f2ecaaa92a110ac5ab6e7cf780ba7f59ab4db876a28e"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:e281bd5747c43cad35127502852d92e6f1ba9ad9423cc0ccd912c71bd95749c0", "1.32.0--r42hdfd78af_0": "sha256:bc0d72c206467425a038c7d06bd516ffe7e8d794f1a6ac449ac3ffa4e1cf0a2e", "1.34.0--r43hdfd78af_0": "sha256:99292ddc169699577403f2ecaaa92a110ac5ab6e7cf780ba7f59ab4db876a28e"}, "docker": "quay.io/biocontainers/bioconductor-ledpred"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ledpred.
shpc-registry automated BioContainers addition for bioconductor-ledpred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ledpred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ledpred:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ledpred/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ledpred/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ledpred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ledpred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ledpred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ledpred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ledpred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ledpred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ledpred

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