---
layout: container
name:  "quay.io/biocontainers/bioconductor-organismdbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-organismdbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-organismdbi/container.yaml"
updated_at: "2024-04-25 02:45:11.321626"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-organismdbi"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-organismdbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-organismdbi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-organismdbi", "latest": {"1.44.0--r43hdfd78af_0": "sha256:1c587c0268a6dda986ac9c35e707e404435d6411cf90504a5038e75079612929"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:e34124f14d83ab2beaa52bca8ce80aa175a5e27a2818347805db5d860786e4d7", "1.40.0--r42hdfd78af_0": "sha256:a30539bed75ed1974c7a9c7f75add5f3c553d97109a60e359c01e4cf4c831747", "1.42.0--r43hdfd78af_0": "sha256:7aa05e9e3b3f76cd7812db240f8c4ef8f18ad929f32a3ffdb8bf252c08d91ecb", "1.44.0--r43hdfd78af_0": "sha256:1c587c0268a6dda986ac9c35e707e404435d6411cf90504a5038e75079612929"}, "docker": "quay.io/biocontainers/bioconductor-organismdbi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-organismdbi.
shpc-registry automated BioContainers addition for bioconductor-organismdbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-organismdbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-organismdbi:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-organismdbi/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-organismdbi/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-organismdbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-organismdbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-organismdbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-organismdbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-organismdbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-organismdbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-organismdbi

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