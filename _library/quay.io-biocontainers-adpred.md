---
layout: container
name:  "quay.io/biocontainers/adpred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/adpred/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/adpred/container.yaml"
updated_at: "2022-10-27 00:53:18.590363"
latest: "1.2.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/adpred"
aliases:
 - "run-adpred"
versions:
 - "1.2.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for adpred"
config: {"url": "https://biocontainers.pro/tools/adpred", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for adpred", "latest": {"1.2.8--pyhdfd78af_0": "sha256:f4cf70e21de0a34f1f3af34bb98867ae72e8a2ddae0619fa7eaee3a1acd46c72"}, "tags": {"1.2.8--pyhdfd78af_0": "sha256:f4cf70e21de0a34f1f3af34bb98867ae72e8a2ddae0619fa7eaee3a1acd46c72"}, "docker": "quay.io/biocontainers/adpred", "aliases": {"run-adpred": "/usr/local/bin/run-adpred"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/adpred.
shpc-registry automated BioContainers addition for adpred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/adpred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/adpred:1.2.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/adpred/1.2.8--pyhdfd78af_0
$ module help quay.io/biocontainers/adpred/1.2.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adpred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adpred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adpred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adpred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adpred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adpred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-adpred

```bash
$ singularity exec <container> /usr/local/bin/run-adpred
$ podman run --it --rm --entrypoint /usr/local/bin/run-adpred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-adpred   -v ${PWD} -w ${PWD} <container> -c " $@"
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