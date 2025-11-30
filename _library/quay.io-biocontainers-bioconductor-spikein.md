---
layout: container
name:  "quay.io/biocontainers/bioconductor-spikein"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spikein/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spikein/container.yaml"
updated_at: "2025-11-30 04:06:12.139182"
latest: "1.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spikein"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spikein"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spikein", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spikein", "latest": {"1.48.0--r44hdfd78af_0": "sha256:85bd4ea60f137bec7b82785cfa429eaaa3e391523e156d9891f235bce0dbe38b"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:5ee88a68d7dee3ffaf53b6da2f63f9c545f13b9224a23d773baa3e6cff8bfe77", "1.40.0--r42hdfd78af_0": "sha256:e437d89116ada86d11876ff76730095f7a804f65aa165791c814ce5fda2fca6d", "1.42.0--r43hdfd78af_0": "sha256:e41583025739a8bc12fd2c895e40011eed6b010939e014eb18b4f5c71d40bcbd", "1.44.0--r43hdfd78af_0": "sha256:383762701561063e69769e40dabfed3c871343582dde8e19592d1f6faa839db9", "1.48.0--r44hdfd78af_0": "sha256:85bd4ea60f137bec7b82785cfa429eaaa3e391523e156d9891f235bce0dbe38b"}, "docker": "quay.io/biocontainers/bioconductor-spikein"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spikein.
shpc-registry automated BioContainers addition for bioconductor-spikein
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spikein
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spikein:1.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spikein/1.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spikein/1.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spikein-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikein-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikein-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spikein-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spikein-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spikein-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spikein

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