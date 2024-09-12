---
layout: container
name:  "quay.io/biocontainers/bioconductor-hivprtplus2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hivprtplus2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hivprtplus2cdf/container.yaml"
updated_at: "2024-09-12 03:13:10.590652"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hivprtplus2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hivprtplus2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hivprtplus2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hivprtplus2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:b27e40d365d02913814898ea8a42f0539b731dfa0feb45d7f44f9d586b648e0f"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:6baaa8d350900db571a0eceae5a526119d6d94640a217a440507948e20c0ea0d", "2.18.0--r42hdfd78af_10": "sha256:3fae1ea83f30944fcd6713e2ab273b6a7fd7f93cfc1bd66087a0c9a859387d49", "2.18.0--r43hdfd78af_11": "sha256:168164194b4155ce138c87d19b735b102b8007f593c002556995fc5b6e3db9c4", "2.18.0--r43hdfd78af_12": "sha256:b27e40d365d02913814898ea8a42f0539b731dfa0feb45d7f44f9d586b648e0f"}, "docker": "quay.io/biocontainers/bioconductor-hivprtplus2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hivprtplus2cdf.
shpc-registry automated BioContainers addition for bioconductor-hivprtplus2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hivprtplus2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hivprtplus2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hivprtplus2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hivprtplus2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hivprtplus2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hivprtplus2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hivprtplus2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hivprtplus2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hivprtplus2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hivprtplus2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hivprtplus2cdf

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