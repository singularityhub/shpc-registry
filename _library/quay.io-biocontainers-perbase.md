---
layout: container
name:  "quay.io/biocontainers/perbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perbase/container.yaml"
updated_at: "2025-01-20 04:12:04.422083"
latest: "0.10.1--h15397dd_0"
container_url: "https://biocontainers.pro/tools/perbase"
aliases:
 - "perbase"
versions:
 - "0.8.5--h93ac3e5_1"
 - "0.8.5--h787ab5b_3"
 - "0.9.0--h787ab5b_0"
 - "0.9.0--hb527e7b_2"
 - "0.10.0--hb527e7b_0"
 - "0.10.1--h15397dd_0"
description: "shpc-registry automated BioContainers addition for perbase"
config: {"url": "https://biocontainers.pro/tools/perbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perbase", "latest": {"0.10.1--h15397dd_0": "sha256:59f257144ef8f168cbb7b2f919b4f1e97fb5e31137045d78ce1aa19244a825ed"}, "tags": {"0.8.5--h93ac3e5_1": "sha256:306bfc77a7e69036f16afb048c93abef6661c15ea5c4d21c13bb108935d90328", "0.8.5--h787ab5b_3": "sha256:aceec74cd00d995a86cbcb077ac8f177311bc751faa0f3429ebecfeed3eadc35", "0.9.0--h787ab5b_0": "sha256:0cba2dbcc507e4108fb8c2bf4e5932ac869835daa72a0b7196607748cc19bb1e", "0.9.0--hb527e7b_2": "sha256:2740ce11e96d110112886faad130eb988840977042bc18c39dde91d4f4e43a05", "0.10.0--hb527e7b_0": "sha256:be63c3a57beef37e87eff1b8db2939cf3f74de3db1d783ec63a99b86bd45e002", "0.10.1--h15397dd_0": "sha256:59f257144ef8f168cbb7b2f919b4f1e97fb5e31137045d78ce1aa19244a825ed"}, "docker": "quay.io/biocontainers/perbase", "aliases": {"perbase": "/usr/local/bin/perbase"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perbase.
shpc-registry automated BioContainers addition for perbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perbase:0.10.1--h15397dd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perbase/0.10.1--h15397dd_0
$ module help quay.io/biocontainers/perbase/0.10.1--h15397dd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perbase

```bash
$ singularity exec <container> /usr/local/bin/perbase
$ podman run --it --rm --entrypoint /usr/local/bin/perbase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perbase   -v ${PWD} -w ${PWD} <container> -c " $@"
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