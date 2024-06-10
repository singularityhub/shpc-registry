---
layout: container
name:  "quay.io/biocontainers/bioconductor-bindingsitefinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bindingsitefinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bindingsitefinder/container.yaml"
updated_at: "2024-06-10 02:55:52.485265"
latest: "2.0.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bindingsitefinder"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "2.0.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bindingsitefinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bindingsitefinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bindingsitefinder", "latest": {"2.0.0--r43hdfd78af_0": "sha256:bae61db263f1741c146f0bc88e0ff4fbf221a28c75bea793e485ec4ad04cb802"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:c81e8226b0f11dfd43bb76cc4fd946312acdc0643a962c38db953ab10ef15f6f", "1.4.0--r42hdfd78af_0": "sha256:9e6704a47636d46a0a26e4ce8b7ce7039e4409be66cb8e5455d773d04e0b25f0", "1.6.0--r43hdfd78af_0": "sha256:45acba8b6f2f426ded196d531cf69b689105714916f48738e95e9bcf5c749a75", "2.0.0--r43hdfd78af_0": "sha256:bae61db263f1741c146f0bc88e0ff4fbf221a28c75bea793e485ec4ad04cb802"}, "docker": "quay.io/biocontainers/bioconductor-bindingsitefinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bindingsitefinder.
shpc-registry automated BioContainers addition for bioconductor-bindingsitefinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bindingsitefinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bindingsitefinder:2.0.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bindingsitefinder/2.0.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bindingsitefinder/2.0.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bindingsitefinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bindingsitefinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bindingsitefinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bindingsitefinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bindingsitefinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bindingsitefinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bindingsitefinder

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