---
layout: container
name:  "quay.io/biocontainers/spliceai"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spliceai/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spliceai/container.yaml"
updated_at: "2024-11-21 03:00:44.263159"
latest: "1.3.1--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/spliceai"

versions:
 - "1.3.1--pyh864c0ab_1"
 - "1.3--py_1"
description: "shpc-registry automated BioContainers addition for spliceai"
config: {"url": "https://biocontainers.pro/tools/spliceai", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spliceai", "latest": {"1.3.1--pyh864c0ab_1": "sha256:dcbe88faa015c5a92490b25d54a3fda981d0efaf73821f82ed088d8261754c78"}, "tags": {"1.3.1--pyh864c0ab_1": "sha256:dcbe88faa015c5a92490b25d54a3fda981d0efaf73821f82ed088d8261754c78", "1.3--py_1": "sha256:0060b4c768619f48b34b9461168e1b43c0ea5d60f802d612854cc3ec46d326b4"}, "docker": "quay.io/biocontainers/spliceai"}
---

This module is a singularity container wrapper for quay.io/biocontainers/spliceai.
shpc-registry automated BioContainers addition for spliceai
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spliceai
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spliceai:1.3.1--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spliceai/1.3.1--pyh864c0ab_1
$ module help quay.io/biocontainers/spliceai/1.3.1--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spliceai-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spliceai-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spliceai-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spliceai-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spliceai-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spliceai-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### spliceai

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