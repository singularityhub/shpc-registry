---
layout: container
name:  "quay.io/biocontainers/perl-bio-phylo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-phylo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-phylo/container.yaml"
updated_at: "2025-04-23 03:37:15.517193"
latest: "0.58--pl5321hdfd78af_5"
container_url: "https://biocontainers.pro/tools/perl-bio-phylo"

versions:
 - "0.58--pl5321hdfd78af_4"
 - "0.58--pl5321hdfd78af_5"
description: "shpc-registry automated BioContainers addition for perl-bio-phylo"
config: {"url": "https://biocontainers.pro/tools/perl-bio-phylo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-phylo", "latest": {"0.58--pl5321hdfd78af_5": "sha256:e26f8fd4a7a0aaf46af4aa1ad2ecc8fd052ff6bd4b3050a988f9b7452132768e"}, "tags": {"0.58--pl5321hdfd78af_4": "sha256:716235c463ddf8a63daf863ae90b4cdae320dfdafa38a9dfbcc7bca565b94846", "0.58--pl5321hdfd78af_5": "sha256:e26f8fd4a7a0aaf46af4aa1ad2ecc8fd052ff6bd4b3050a988f9b7452132768e"}, "docker": "quay.io/biocontainers/perl-bio-phylo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-phylo.
shpc-registry automated BioContainers addition for perl-bio-phylo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-phylo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-phylo:0.58--pl5321hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-phylo/0.58--pl5321hdfd78af_5
$ module help quay.io/biocontainers/perl-bio-phylo/0.58--pl5321hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-phylo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-phylo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-phylo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-phylo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-phylo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-phylo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-bio-phylo

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