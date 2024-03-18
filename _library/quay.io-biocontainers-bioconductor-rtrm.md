---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtrm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtrm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtrm/container.yaml"
updated_at: "2024-03-18 03:32:24.528589"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtrm"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtrm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtrm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtrm", "latest": {"1.40.0--r43hdfd78af_0": "sha256:a883c22de7f32e7ca2288b7093a180953bf725984259964c29be4ab35b55b6cd"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:c53846f25eae20bc9cc0fef9d7be389264cf0059b6192fc084a2917f0f09041b", "1.36.0--r42hdfd78af_0": "sha256:77a321e8a12c1f5f39bb8f1cdbe4ed93a66e3549fc98e96bde1bf5fe6efe2960", "1.38.0--r43hdfd78af_0": "sha256:2bc155ad83c5af396ea50306d00fe27bd0064df6eb2ea80254cf97784da82449", "1.40.0--r43hdfd78af_0": "sha256:a883c22de7f32e7ca2288b7093a180953bf725984259964c29be4ab35b55b6cd"}, "docker": "quay.io/biocontainers/bioconductor-rtrm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtrm.
shpc-registry automated BioContainers addition for bioconductor-rtrm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtrm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtrm:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtrm/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtrm/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtrm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtrm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtrm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtrm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtrm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtrm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtrm

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