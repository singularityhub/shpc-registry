---
layout: container
name:  "quay.io/biocontainers/synapseclient"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/synapseclient/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/synapseclient/container.yaml"
updated_at: "2022-10-27 00:47:07.780245"
latest: "2.7.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/synapseclient"
aliases:
 - "keyring"
 - "synapse"
versions:
 - "2.7.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for synapseclient"
config: {"url": "https://biocontainers.pro/tools/synapseclient", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for synapseclient", "latest": {"2.7.0--pyh7cba7a3_0": "sha256:c50226759523160f06f15d49f1f0bc65ccb33328afce86b9a9cf9ff36aa08084"}, "tags": {"2.7.0--pyh7cba7a3_0": "sha256:c50226759523160f06f15d49f1f0bc65ccb33328afce86b9a9cf9ff36aa08084"}, "docker": "quay.io/biocontainers/synapseclient", "aliases": {"keyring": "/usr/local/bin/keyring", "synapse": "/usr/local/bin/synapse"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/synapseclient.
shpc-registry automated BioContainers addition for synapseclient
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/synapseclient
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/synapseclient:2.7.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/synapseclient/2.7.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/synapseclient/2.7.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### synapseclient-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### synapseclient-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### synapseclient-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### synapseclient-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### synapseclient-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### synapseclient-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### synapse

```bash
$ singularity exec <container> /usr/local/bin/synapse
$ podman run --it --rm --entrypoint /usr/local/bin/synapse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/synapse   -v ${PWD} -w ${PWD} <container> -c " $@"
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