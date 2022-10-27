---
layout: container
name:  "quay.io/biocontainers/spectra-cluster-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spectra-cluster-cli/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spectra-cluster-cli/container.yaml"
updated_at: "2022-10-27 01:05:32.116980"
latest: "1.1.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/spectra-cluster-cli"
aliases:
 - "spectra-cluster-cli"
versions:
 - "1.1.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for spectra-cluster-cli"
config: {"url": "https://biocontainers.pro/tools/spectra-cluster-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spectra-cluster-cli", "latest": {"1.1.2--hdfd78af_1": "sha256:cf27ef9197eaf5570a0c8d177cf1cf11a4296a1a21ba4982b7dff37444456df3"}, "tags": {"1.1.2--hdfd78af_1": "sha256:cf27ef9197eaf5570a0c8d177cf1cf11a4296a1a21ba4982b7dff37444456df3"}, "docker": "quay.io/biocontainers/spectra-cluster-cli", "aliases": {"spectra-cluster-cli": "/usr/local/bin/spectra-cluster-cli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spectra-cluster-cli.
shpc-registry automated BioContainers addition for spectra-cluster-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spectra-cluster-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spectra-cluster-cli:1.1.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spectra-cluster-cli/1.1.2--hdfd78af_1
$ module help quay.io/biocontainers/spectra-cluster-cli/1.1.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spectra-cluster-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spectra-cluster-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spectra-cluster-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spectra-cluster-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spectra-cluster-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spectra-cluster-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spectra-cluster-cli

```bash
$ singularity exec <container> /usr/local/bin/spectra-cluster-cli
$ podman run --it --rm --entrypoint /usr/local/bin/spectra-cluster-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spectra-cluster-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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