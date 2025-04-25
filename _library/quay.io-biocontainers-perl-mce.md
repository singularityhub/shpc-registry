---
layout: container
name:  "quay.io/biocontainers/perl-mce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-mce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-mce/container.yaml"
updated_at: "2025-04-25 02:58:57.792634"
latest: "1.901--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-mce"

versions:
 - "1.881--pl5321hdfd78af_0"
 - "1.884--pl5321hdfd78af_0"
 - "1.888--pl5321hdfd78af_0"
 - "1.897--pl5321hdfd78af_0"
 - "1.896--pl5321hdfd78af_0"
 - "1.895--pl5321hdfd78af_0"
 - "1.894--pl5321hdfd78af_0"
 - "1.893--pl5321hdfd78af_0"
 - "1.898--pl5321hdfd78af_0"
 - "1.900--pl5321hdfd78af_0"
 - "1.899--pl5321hdfd78af_0"
 - "1.901--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-mce"
config: {"url": "https://biocontainers.pro/tools/perl-mce", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-mce", "latest": {"1.901--pl5321hdfd78af_0": "sha256:fbc231c3b8894b97298c611af8710caa468e8e33b61e83b9d23b00c482f16884"}, "tags": {"1.881--pl5321hdfd78af_0": "sha256:2e83ce1420d72486b317d36f4b93a19af6b2ca3f9ba3da4c74eb1b6117431b11", "1.884--pl5321hdfd78af_0": "sha256:299ee7e7cfd32dee3bc6592345517af2ad1fbda882aa5dee08595d76ee662b2d", "1.888--pl5321hdfd78af_0": "sha256:6c900d4bd6bb41fce2577b23ee387e661c6dda66b6576b50ffe2e569068af12b", "1.897--pl5321hdfd78af_0": "sha256:8545254b4b098196451ce2bb373c4f33cdd15aa0c21c566f557d755c23881fa8", "1.896--pl5321hdfd78af_0": "sha256:4c280b135096f67edc764937c138d8aaf855da0d22132e04206806a306793c1f", "1.895--pl5321hdfd78af_0": "sha256:d88ec5d796d94e14e1d041b949b242028337270e1ceac1ff2679581a2ab23ea3", "1.894--pl5321hdfd78af_0": "sha256:f4f7f361183d91ebc614ba26d1b6cfc2547b21408c0575265cd334fafc5c5470", "1.893--pl5321hdfd78af_0": "sha256:02ce28423d3da77d036d387d19f41d41073ab85b76fed55bc42ca2a0621cc54e", "1.898--pl5321hdfd78af_0": "sha256:cea19a7ce22b1f116ba0cdf00df407fa60e0db14e57824456b2afa6cc4d0375b", "1.900--pl5321hdfd78af_0": "sha256:7efab1a2f246e36c37e08883173c5dc3ea7f6e92423a18d7d9e1aeb829d2faec", "1.899--pl5321hdfd78af_0": "sha256:ebed023c93b93284c91dfd5c54d21e6c6388a41d8ccdb62a45cc3dcae24d9ecf", "1.901--pl5321hdfd78af_0": "sha256:fbc231c3b8894b97298c611af8710caa468e8e33b61e83b9d23b00c482f16884"}, "docker": "quay.io/biocontainers/perl-mce"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-mce.
shpc-registry automated BioContainers addition for perl-mce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-mce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-mce:1.901--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-mce/1.901--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-mce/1.901--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-mce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-mce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-mce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-mce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-mce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-mce-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-mce

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