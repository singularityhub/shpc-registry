---
layout: container
name:  "quay.io/biocontainers/multiqc-bcbio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multiqc-bcbio/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/multiqc-bcbio/container.yaml"
updated_at: "2022-10-27 00:48:01.094984"
latest: "0.2.9--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/multiqc-bcbio"

versions:
 - "0.2.9--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for multiqc-bcbio"
config: {"url": "https://biocontainers.pro/tools/multiqc-bcbio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multiqc-bcbio", "latest": {"0.2.9--pyh3252c3a_0": "sha256:b531c82f3e4d9a3853710ab8b4cbd04cd60ba9bc4e72ac447f733fc57637815c"}, "tags": {"0.2.9--pyh3252c3a_0": "sha256:b531c82f3e4d9a3853710ab8b4cbd04cd60ba9bc4e72ac447f733fc57637815c"}, "docker": "quay.io/biocontainers/multiqc-bcbio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/multiqc-bcbio.
shpc-registry automated BioContainers addition for multiqc-bcbio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multiqc-bcbio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multiqc-bcbio:0.2.9--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multiqc-bcbio/0.2.9--pyh3252c3a_0
$ module help quay.io/biocontainers/multiqc-bcbio/0.2.9--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multiqc-bcbio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-bcbio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-bcbio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multiqc-bcbio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multiqc-bcbio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multiqc-bcbio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### multiqc-bcbio

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