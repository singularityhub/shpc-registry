---
layout: container
name:  "quay.io/biocontainers/bioconductor-metaboliteidmapping"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metaboliteidmapping/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metaboliteidmapping/container.yaml"
updated_at: "2023-08-11 03:10:38.374209"
latest: "1.0.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-metaboliteidmapping"

versions:
 - "1.0.0--r41hdfd78af_2"
 - "1.0.0--r42hdfd78af_3"
 - "1.0.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-metaboliteidmapping"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metaboliteidmapping", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metaboliteidmapping", "latest": {"1.0.0--r43hdfd78af_4": "sha256:94ade45b71883f79ce5b2df8112bfcc2345830612165f4928fe755f92376b0d6"}, "tags": {"1.0.0--r41hdfd78af_2": "sha256:6ea3850b4d6feab379bbb80886f10f444e73ebbc5c5d75a9fa708d5a28f99235", "1.0.0--r42hdfd78af_3": "sha256:ccf50652c17ced99174199c811f992a5a66c64fa65c9438c308e433fa7cf89e0", "1.0.0--r43hdfd78af_4": "sha256:94ade45b71883f79ce5b2df8112bfcc2345830612165f4928fe755f92376b0d6"}, "docker": "quay.io/biocontainers/bioconductor-metaboliteidmapping"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metaboliteidmapping.
shpc-registry automated BioContainers addition for bioconductor-metaboliteidmapping
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metaboliteidmapping
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metaboliteidmapping:1.0.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metaboliteidmapping/1.0.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-metaboliteidmapping/1.0.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metaboliteidmapping-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaboliteidmapping-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaboliteidmapping-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metaboliteidmapping-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metaboliteidmapping-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metaboliteidmapping-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metaboliteidmapping

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