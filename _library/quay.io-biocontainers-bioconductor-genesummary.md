---
layout: container
name:  "quay.io/biocontainers/bioconductor-genesummary"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genesummary/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genesummary/container.yaml"
updated_at: "2024-10-02 03:08:50.024603"
latest: "0.99.6--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genesummary"

versions:
 - "0.99.3--r41hdfd78af_1"
 - "0.99.4--r42hdfd78af_0"
 - "0.99.4--r43hdfd78af_1"
 - "0.99.6--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genesummary"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genesummary", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genesummary", "latest": {"0.99.6--r43hdfd78af_0": "sha256:e3bc2bfe29c2dc24569d2ad2003994150658ebcad640fa367cbfb8137d322b47"}, "tags": {"0.99.3--r41hdfd78af_1": "sha256:75fede957c04d01042e582d65353bcd84eb9985a71add115b8af2111afcfd25e", "0.99.4--r42hdfd78af_0": "sha256:b97056810a15e7089d58554e6509944de73d729152a4cbac51b5ce346b218072", "0.99.4--r43hdfd78af_1": "sha256:7b9d4e1b01c49bee152b2fbf08d91d2d608cc4f0c3c0fa5d7fae03a42c23bf72", "0.99.6--r43hdfd78af_0": "sha256:e3bc2bfe29c2dc24569d2ad2003994150658ebcad640fa367cbfb8137d322b47"}, "docker": "quay.io/biocontainers/bioconductor-genesummary"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genesummary.
shpc-registry automated BioContainers addition for bioconductor-genesummary
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genesummary
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genesummary:0.99.6--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genesummary/0.99.6--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genesummary/0.99.6--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genesummary-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genesummary-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genesummary-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genesummary-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genesummary-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genesummary-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genesummary

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