---
layout: container
name:  "quay.io/biocontainers/bioconductor-snadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snadata/container.yaml"
updated_at: "2024-10-05 03:16:19.556155"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snadata"

versions:
 - "1.40.0--r41hdfd78af_1"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snadata", "latest": {"1.48.0--r43hdfd78af_0": "sha256:0bd37da97bea2f7927fdcc4c9a6745083fa935318d205e73b45d60448d0b6c97"}, "tags": {"1.40.0--r41hdfd78af_1": "sha256:f240f78ad6def4226e57a2db88c968acc15c33b8f835f19e6399082a8db620b6", "1.44.0--r42hdfd78af_0": "sha256:cac8c6fea69ce105a5041f847ba505c03c7e1e6dfb221e2f077e9a4e6b3097cc", "1.46.0--r43hdfd78af_0": "sha256:423448f8d953ca116f6a25481a054b0df6e0ac19d05285c35bfae92a5ad74dd1", "1.48.0--r43hdfd78af_0": "sha256:0bd37da97bea2f7927fdcc4c9a6745083fa935318d205e73b45d60448d0b6c97"}, "docker": "quay.io/biocontainers/bioconductor-snadata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snadata.
shpc-registry automated BioContainers addition for bioconductor-snadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snadata:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snadata/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snadata/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snadata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snadata

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