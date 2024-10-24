---
layout: container
name:  "quay.io/biocontainers/bioconductor-diffgeneanalysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-diffgeneanalysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-diffgeneanalysis/container.yaml"
updated_at: "2024-10-24 03:35:23.757182"
latest: "1.84.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-diffgeneanalysis"

versions:
 - "1.76.0--r41hdfd78af_0"
 - "1.80.0--r42hdfd78af_0"
 - "1.82.0--r43hdfd78af_0"
 - "1.84.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-diffgeneanalysis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-diffgeneanalysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-diffgeneanalysis", "latest": {"1.84.0--r43hdfd78af_0": "sha256:b4beca502cf7c7519aaa156fb7d737e7a18c86f97fba37580f3f836dcb3bf713"}, "tags": {"1.76.0--r41hdfd78af_0": "sha256:1f1fdad20da77f6e4f1d005b4ce12a5f30b0f8e0775cfa64f4284e7b60bb5bf5", "1.80.0--r42hdfd78af_0": "sha256:6316567d8466ffeeea091ded1e6c05ee883cc17a522d293bbc6ad4788ed605d6", "1.82.0--r43hdfd78af_0": "sha256:0bd4ce37377f9d655994c9424fc01f8b659857c1ef584fa6ffe38362ded54fc8", "1.84.0--r43hdfd78af_0": "sha256:b4beca502cf7c7519aaa156fb7d737e7a18c86f97fba37580f3f836dcb3bf713"}, "docker": "quay.io/biocontainers/bioconductor-diffgeneanalysis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-diffgeneanalysis.
shpc-registry automated BioContainers addition for bioconductor-diffgeneanalysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-diffgeneanalysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-diffgeneanalysis:1.84.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-diffgeneanalysis/1.84.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-diffgeneanalysis/1.84.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-diffgeneanalysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffgeneanalysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffgeneanalysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-diffgeneanalysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-diffgeneanalysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-diffgeneanalysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-diffgeneanalysis

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