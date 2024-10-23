---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahensdbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahensdbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahensdbs/container.yaml"
updated_at: "2024-10-23 02:56:58.956247"
latest: "1.1.10--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ahensdbs"

versions:
 - "1.1.4--r41hdfd78af_1"
 - "1.1.8--r42hdfd78af_0"
 - "1.1.8--r43hdfd78af_1"
 - "1.1.10--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ahensdbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahensdbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahensdbs", "latest": {"1.1.10--r43hdfd78af_0": "sha256:c2d37d0906ef324996e9a9f091d8475bfd8d02915f8174d8d56fd6d8da02d329"}, "tags": {"1.1.4--r41hdfd78af_1": "sha256:583c44f40f9c41fdba2cec7f162dc73a4447f34efef07b25ed020b5566f21b91", "1.1.8--r42hdfd78af_0": "sha256:f6c90771a7ab8a540a2f5ea79e0cb09de4806e40b196f85d48ade8a255931c13", "1.1.8--r43hdfd78af_1": "sha256:ba0ad0401e5975f71f38aab8461b693855ff5ebc24a796ad39b2c3b3523bb522", "1.1.10--r43hdfd78af_0": "sha256:c2d37d0906ef324996e9a9f091d8475bfd8d02915f8174d8d56fd6d8da02d329"}, "docker": "quay.io/biocontainers/bioconductor-ahensdbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahensdbs.
shpc-registry automated BioContainers addition for bioconductor-ahensdbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahensdbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahensdbs:1.1.10--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahensdbs/1.1.10--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ahensdbs/1.1.10--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahensdbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahensdbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahensdbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahensdbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahensdbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahensdbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahensdbs

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