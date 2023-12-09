---
layout: container
name:  "quay.io/biocontainers/bioconductor-blacksheepr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-blacksheepr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-blacksheepr/container.yaml"
updated_at: "2023-12-09 02:59:35.019312"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-blacksheepr"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-blacksheepr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-blacksheepr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-blacksheepr", "latest": {"1.14.0--r43hdfd78af_0": "sha256:060b918cd7518905e6938c57cda88419f98de9b818f7b22c5d02b0bbee656d43"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:6dc20ff38ee83a99645bbc321f94a8fd5eab7cac65dc602896c7146f846ea2f0", "1.12.0--r42hdfd78af_0": "sha256:433eff93da9922b1c567b022bcf69ebf7934c7ac305ffd80dd5e676da210c91f", "1.14.0--r43hdfd78af_0": "sha256:060b918cd7518905e6938c57cda88419f98de9b818f7b22c5d02b0bbee656d43"}, "docker": "quay.io/biocontainers/bioconductor-blacksheepr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-blacksheepr.
shpc-registry automated BioContainers addition for bioconductor-blacksheepr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-blacksheepr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-blacksheepr:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-blacksheepr/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-blacksheepr/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-blacksheepr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blacksheepr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blacksheepr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-blacksheepr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-blacksheepr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-blacksheepr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-blacksheepr

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