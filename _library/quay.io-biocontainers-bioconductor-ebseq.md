---
layout: container
name:  "quay.io/biocontainers/bioconductor-ebseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ebseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ebseq/container.yaml"
updated_at: "2026-02-05 05:00:11.514009"
latest: "2.4.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ebseq"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "2.0.0--r43hf17093f_1"
 - "2.0.0--r43hf17093f_2"
 - "2.0.0--r43hf17093f_3"
 - "2.4.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ebseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ebseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ebseq", "latest": {"2.4.0--r44he5774e6_0": "sha256:179059187950d78f1569ef86fee4e7cff381a478a89c2e3fa80aaf8ac38dfc6f"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:d394a23f03830c05ce3fc9d7e62b63b217f1d38fc2dcfdca4a6f9e2ce3e82a67", "1.38.0--r42hdfd78af_0": "sha256:b1b608ae518bd6dd802c6cd7f17a2b8b28d1e505f7af575ff78cd5f878eb62f1", "1.40.0--r43hdfd78af_0": "sha256:fa661b683ab6b40872e9ad3b0cde5cef2797de0843c75f0dd12175ec4cbeaa3a", "2.0.0--r43hf17093f_1": "sha256:711aa306d187cc524443c475087dfcc552d0c149c9d1187034dabdeca315fb89", "2.0.0--r43hf17093f_2": "sha256:7aef570aa1443d4e0f43780febd42babf57d34dd698d3af954aa61f13a1e90a6", "2.0.0--r43hf17093f_3": "sha256:c05507931b7c6358287165c753171e6967eb5f63d550a58d554c7bb9f0065032", "2.4.0--r44he5774e6_0": "sha256:179059187950d78f1569ef86fee4e7cff381a478a89c2e3fa80aaf8ac38dfc6f"}, "docker": "quay.io/biocontainers/bioconductor-ebseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ebseq.
shpc-registry automated BioContainers addition for bioconductor-ebseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ebseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ebseq:2.4.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ebseq/2.4.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ebseq/2.4.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ebseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ebseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ebseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ebseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ebseq

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