---
layout: container
name:  "quay.io/biocontainers/bioconductor-translatome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-translatome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-translatome/container.yaml"
updated_at: "2025-03-06 04:04:07.462933"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-translatome"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-translatome"
config: {"url": "https://biocontainers.pro/tools/bioconductor-translatome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-translatome", "latest": {"1.44.0--r44hdfd78af_0": "sha256:1f36562d0ca60f6b1df336a13c12e319b01d6a2e30e0c877852b40940aaa872a"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:dc36531fa59485be9f561f41cd4c19a92ded361c9e89ad8007f8a7751a8ecf25", "1.36.0--r42hdfd78af_0": "sha256:1fecde93724c64dc61655ce2f0155236b4cadd9c454e87e21ba687e5666f2ce4", "1.38.0--r43hdfd78af_0": "sha256:a48a72373fab6cd3ed0849b656bca2bf11ada604bebfb718479faf4aeb4e6ce5", "1.40.0--r43hdfd78af_0": "sha256:08423a15a399ae3467dd116899bb31252fd9f36680d9a23807d7b4d005d7f451", "1.44.0--r44hdfd78af_0": "sha256:1f36562d0ca60f6b1df336a13c12e319b01d6a2e30e0c877852b40940aaa872a"}, "docker": "quay.io/biocontainers/bioconductor-translatome"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-translatome.
shpc-registry automated BioContainers addition for bioconductor-translatome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-translatome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-translatome:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-translatome/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-translatome/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-translatome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-translatome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-translatome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-translatome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-translatome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-translatome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-translatome

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