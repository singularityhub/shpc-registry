---
layout: container
name:  "quay.io/biocontainers/bioconductor-mlp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mlp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mlp/container.yaml"
updated_at: "2023-10-25 02:30:18.879322"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mlp"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mlp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mlp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mlp", "latest": {"1.48.0--r43hdfd78af_0": "sha256:273c7e99b856bfa2a03736f94f101c3ae31917f6130326279438f44071cb28aa"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:d81f68d39ce74fe64e33401aa14f090a90edde9214041d0c9730143b68c915e1", "1.46.0--r42hdfd78af_0": "sha256:522ee36dffdecd99fd512fe072adace1c0c5f726c2939a0396e856617cde816c", "1.48.0--r43hdfd78af_0": "sha256:273c7e99b856bfa2a03736f94f101c3ae31917f6130326279438f44071cb28aa"}, "docker": "quay.io/biocontainers/bioconductor-mlp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mlp.
shpc-registry automated BioContainers addition for bioconductor-mlp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mlp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mlp:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mlp/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mlp/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mlp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mlp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mlp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mlp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mlp

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