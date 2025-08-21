---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahmeshdbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahmeshdbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahmeshdbs/container.yaml"
updated_at: "2025-08-21 03:22:49.222665"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ahmeshdbs"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.5.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ahmeshdbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahmeshdbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahmeshdbs", "latest": {"1.8.0--r44hdfd78af_0": "sha256:607dcfe1d0aaef51b8edbde8b48735152d3d31e80731ff907478ba1f7310c6b6"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:73a548296ef6d743f730fa2fcdb22165fb217aded3dc6b4a106a5ee5e82771ab", "1.5.0--r42hdfd78af_0": "sha256:3fe39e191658511e980d9b1a1c6c0bfa6811f50ac38f4569b41ef46330da3527", "1.6.0--r43hdfd78af_0": "sha256:1eaae3633406f6614c2d8241d80d4ab3adaf591943e15c1fb00dda37fbc21c38", "1.7.0--r43hdfd78af_0": "sha256:6abbba02e6d0247adf6316efdc0703e9b82e5614bcf5fd402475d03c99486c8d", "1.8.0--r44hdfd78af_0": "sha256:607dcfe1d0aaef51b8edbde8b48735152d3d31e80731ff907478ba1f7310c6b6"}, "docker": "quay.io/biocontainers/bioconductor-ahmeshdbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahmeshdbs.
shpc-registry automated BioContainers addition for bioconductor-ahmeshdbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahmeshdbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahmeshdbs:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahmeshdbs/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ahmeshdbs/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahmeshdbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahmeshdbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahmeshdbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahmeshdbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahmeshdbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahmeshdbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahmeshdbs

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