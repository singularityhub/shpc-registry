---
layout: container
name:  "quay.io/biocontainers/soapdenovo2-errorcorrection"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapdenovo2-errorcorrection/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapdenovo2-errorcorrection/container.yaml"
updated_at: "2024-02-06 02:26:53.014231"
latest: "2.0--h21ec9f0_7"
container_url: "https://biocontainers.pro/tools/soapdenovo2-errorcorrection"
aliases:
 - "ErrorCorrection"
versions:
 - "2.0--h7ff8a90_5"
 - "2.0--h21ec9f0_7"
description: "shpc-registry automated BioContainers addition for soapdenovo2-errorcorrection"
config: {"url": "https://biocontainers.pro/tools/soapdenovo2-errorcorrection", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapdenovo2-errorcorrection", "latest": {"2.0--h21ec9f0_7": "sha256:d1d06373ce6d654c5ea28c5fccf84f9d34d5bf99057f50ad4fd44bfdc8fe92ab"}, "tags": {"2.0--h7ff8a90_5": "sha256:3f43af7f78c29789ad244fd4ff84a8e283f6533dbc4207b5fe78b8b3f37442af", "2.0--h21ec9f0_7": "sha256:d1d06373ce6d654c5ea28c5fccf84f9d34d5bf99057f50ad4fd44bfdc8fe92ab"}, "docker": "quay.io/biocontainers/soapdenovo2-errorcorrection", "aliases": {"ErrorCorrection": "/usr/local/bin/ErrorCorrection"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapdenovo2-errorcorrection.
shpc-registry automated BioContainers addition for soapdenovo2-errorcorrection
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapdenovo2-errorcorrection
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapdenovo2-errorcorrection:2.0--h21ec9f0_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapdenovo2-errorcorrection/2.0--h21ec9f0_7
$ module help quay.io/biocontainers/soapdenovo2-errorcorrection/2.0--h21ec9f0_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapdenovo2-errorcorrection-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-errorcorrection-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-errorcorrection-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapdenovo2-errorcorrection-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapdenovo2-errorcorrection-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapdenovo2-errorcorrection-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ErrorCorrection

```bash
$ singularity exec <container> /usr/local/bin/ErrorCorrection
$ podman run --it --rm --entrypoint /usr/local/bin/ErrorCorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ErrorCorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
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