---
layout: container
name:  "quay.io/biocontainers/jannovar-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jannovar-cli/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jannovar-cli/container.yaml"
updated_at: "2022-10-27 00:27:31.080256"
latest: "0.36--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/jannovar-cli"
aliases:
 - "jannovar"
versions:
 - "0.36--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for jannovar-cli"
config: {"url": "https://biocontainers.pro/tools/jannovar-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jannovar-cli", "latest": {"0.36--hdfd78af_0": "sha256:c3915b81caae3214aae6d105108c17c16010145974e0910cbf6983eeaeac8112"}, "tags": {"0.36--hdfd78af_0": "sha256:c3915b81caae3214aae6d105108c17c16010145974e0910cbf6983eeaeac8112"}, "docker": "quay.io/biocontainers/jannovar-cli", "aliases": {"jannovar": "/usr/local/bin/jannovar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jannovar-cli.
shpc-registry automated BioContainers addition for jannovar-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jannovar-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jannovar-cli:0.36--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jannovar-cli/0.36--hdfd78af_0
$ module help quay.io/biocontainers/jannovar-cli/0.36--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jannovar-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jannovar-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jannovar-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jannovar-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jannovar-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jannovar-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jannovar

```bash
$ singularity exec <container> /usr/local/bin/jannovar
$ podman run --it --rm --entrypoint /usr/local/bin/jannovar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jannovar   -v ${PWD} -w ${PWD} <container> -c " $@"
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