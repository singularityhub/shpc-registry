---
layout: container
name:  "quay.io/biocontainers/oarfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oarfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oarfish/container.yaml"
updated_at: "2024-04-03 02:42:17.010566"
latest: "0.4.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/oarfish"
aliases:
 - "oarfish"
versions:
 - "0.2.0--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
 - "0.4.0--h4349ce8_0"
 - "0.3.1--h4349ce8_0"
description: "singularity registry hpc automated addition for oarfish"
config: {"url": "https://biocontainers.pro/tools/oarfish", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for oarfish", "latest": {"0.4.0--h4349ce8_0": "sha256:6a6e229e78b74856baf6e8f41530c01a135fb07e644a624c8e16335de4e8c061"}, "tags": {"0.2.0--h4349ce8_0": "sha256:946f787788361fd60c6321a867d46742a656d1d5b2631789a511e171a7ada166", "0.3.0--h4349ce8_0": "sha256:c208006ead82df89ab7e6f6c736ebf5cf51bcb45192c5abf8753e7519c1e0401", "0.4.0--h4349ce8_0": "sha256:6a6e229e78b74856baf6e8f41530c01a135fb07e644a624c8e16335de4e8c061", "0.3.1--h4349ce8_0": "sha256:ffe25e630dcd9c1a5abeff38a3aec8ead311454ecbec9d09623a07b4617ef780"}, "docker": "quay.io/biocontainers/oarfish", "aliases": {"oarfish": "/usr/local/bin/oarfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oarfish.
singularity registry hpc automated addition for oarfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oarfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oarfish:0.4.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oarfish/0.4.0--h4349ce8_0
$ module help quay.io/biocontainers/oarfish/0.4.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oarfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oarfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oarfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oarfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oarfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oarfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oarfish

```bash
$ singularity exec <container> /usr/local/bin/oarfish
$ podman run --it --rm --entrypoint /usr/local/bin/oarfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oarfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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