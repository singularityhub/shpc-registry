---
layout: container
name:  "quay.io/biocontainers/bioconductor-interactionset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-interactionset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-interactionset/container.yaml"
updated_at: "2024-12-02 03:15:13.078344"
latest: "1.30.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-interactionset"
aliases:
 - "wget"
versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.1--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-interactionset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-interactionset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-interactionset", "latest": {"1.30.0--r43hf17093f_1": "sha256:d5254e358d92a05378fb6d9c427a1d2b32c91e6c38e00d3deffe42ab34456baf"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:62037b4b18b467b3ff5e2541057589596a717206d216f5f1dc03e0d21cf689da", "1.26.0--r42hc247a5b_0": "sha256:0de4011b1a39ef7a0c972614b3e75d426077635d53a99771fccfed60e84f5a1b", "1.22.0--r41hc247a5b_2": "sha256:96bd715684fa5fe238787a63279f44ee7a9ece445be9067a20efdaebc56c221c", "1.20.0--r41h399db7b_0": "sha256:70c08a8b8d5d8a648852ce7249d591a6c41cc7e7328a7be4f64fd81110686a62", "1.18.0--r40h399db7b_1": "sha256:1bb757dd6a863257738332ce30bdc703dc0d5b2140ec53353c9d701ba83023d2", "1.16.0--r40h5f743cb_0": "sha256:9c6c900523fff39fe44cc936fc4b3ceefe1b1d5325cf873a77b071419858cbb6", "1.26.0--r42hf17093f_1": "sha256:588d5336b0f66ddb6a8706096b048ccc7238c52282b9cf4f6e85ee27314f3187", "1.28.1--r43hf17093f_0": "sha256:2aca6a81b86a6d1b716118656392e0e4a212170478549de0384cc244b1f5c686", "1.30.0--r43hf17093f_0": "sha256:4bf64fb457a938739a20d22df9137a22dab757d499928602fb3477d1180aa8d0", "1.30.0--r43hf17093f_1": "sha256:d5254e358d92a05378fb6d9c427a1d2b32c91e6c38e00d3deffe42ab34456baf"}, "docker": "quay.io/biocontainers/bioconductor-interactionset", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-interactionset.
shpc-registry automated BioContainers addition for bioconductor-interactionset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-interactionset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-interactionset:1.30.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-interactionset/1.30.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-interactionset/1.30.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-interactionset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactionset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactionset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-interactionset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-interactionset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-interactionset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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