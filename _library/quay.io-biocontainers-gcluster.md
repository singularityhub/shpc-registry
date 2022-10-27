---
layout: container
name:  "quay.io/biocontainers/gcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gcluster/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gcluster/container.yaml"
updated_at: "2022-10-27 00:39:33.259812"
latest: "2.0.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/gcluster"
aliases:
 - "Gcluster.pl"
 - "interested_gene_generation.pl"
 - "test.pl"
versions:
 - "2.0.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for gcluster"
config: {"url": "https://biocontainers.pro/tools/gcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gcluster", "latest": {"2.0.5--hdfd78af_1": "sha256:7388de9566bf822b6e59b40e9a9e14022985004d165a1f6f265048a049102bd4"}, "tags": {"2.0.5--hdfd78af_1": "sha256:7388de9566bf822b6e59b40e9a9e14022985004d165a1f6f265048a049102bd4"}, "docker": "quay.io/biocontainers/gcluster", "aliases": {"Gcluster.pl": "/usr/local/bin/Gcluster.pl", "interested_gene_generation.pl": "/usr/local/bin/interested_gene_generation.pl", "test.pl": "/usr/local/bin/test.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gcluster.
shpc-registry automated BioContainers addition for gcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gcluster:2.0.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gcluster/2.0.5--hdfd78af_1
$ module help quay.io/biocontainers/gcluster/2.0.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gcluster.pl

```bash
$ singularity exec <container> /usr/local/bin/Gcluster.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Gcluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gcluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interested_gene_generation.pl

```bash
$ singularity exec <container> /usr/local/bin/interested_gene_generation.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interested_gene_generation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interested_gene_generation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.pl

```bash
$ singularity exec <container> /usr/local/bin/test.pl
$ podman run --it --rm --entrypoint /usr/local/bin/test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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