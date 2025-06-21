---
layout: container
name:  "quay.io/biocontainers/bioconductor-bus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bus/container.yaml"
updated_at: "2025-06-21 04:01:47.723786"
latest: "1.62.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bus"

versions:
 - "1.50.0--r41hc247a5b_2"
 - "1.54.0--r42hc247a5b_0"
 - "1.54.0--r42hf17093f_1"
 - "1.56.0--r43hf17093f_0"
 - "1.58.0--r43hf17093f_0"
 - "1.58.0--r43hf17093f_1"
 - "1.62.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bus", "latest": {"1.62.0--r44he5774e6_0": "sha256:b218918fafdbb3daf4ae35b4b9ddc59bb446e1b52284d554940e2cc72e6817e3"}, "tags": {"1.50.0--r41hc247a5b_2": "sha256:5f33581b8184a90fc5b2e5ed9674d8d24d40d55196fece5282a071bd9a1ced04", "1.54.0--r42hc247a5b_0": "sha256:7b6dadc92bb50f3c4fc6bca337ad7aecf8d7cbe2134aa559651db16f8280f4c3", "1.54.0--r42hf17093f_1": "sha256:7e982a208723397ead20b10260ee48f57bdf99de6200bc4e8370f4eeead94553", "1.56.0--r43hf17093f_0": "sha256:1a52dca0fb0df95bf2a9984f569d92230edff23c6541a9f629aae1cbb2b51708", "1.58.0--r43hf17093f_0": "sha256:1ddf9b4445d76b2e9ade82063d33e12aaecf8e5f1aa8d7c89ab27a2e79ad9996", "1.58.0--r43hf17093f_1": "sha256:8cc1a82386905068617b2cbfbe572a85756e156f5f76e0a48d3ee8f42656992e", "1.62.0--r44he5774e6_0": "sha256:b218918fafdbb3daf4ae35b4b9ddc59bb446e1b52284d554940e2cc72e6817e3"}, "docker": "quay.io/biocontainers/bioconductor-bus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bus.
shpc-registry automated BioContainers addition for bioconductor-bus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bus:1.62.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bus/1.62.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-bus/1.62.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bus

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