---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahpubmeddbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahpubmeddbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahpubmeddbs/container.yaml"
updated_at: "2025-10-09 03:17:45.927447"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ahpubmeddbs"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.5.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ahpubmeddbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahpubmeddbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahpubmeddbs", "latest": {"1.8.0--r44hdfd78af_0": "sha256:f73ffb24175dc69b0fc5bdf51a8e9d6a100b922c11ca2938d29af605203f03b3"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:5f951d14bf9971f96d6d827cc1be5e2eb107719b43fcada50c96805c81b86caa", "1.5.0--r42hdfd78af_0": "sha256:84145771150cc3a4602820f4c8c8854da651d2dad2cf5b7c2714a69b51fc1c8b", "1.6.0--r43hdfd78af_0": "sha256:cef7c44891d7e4ba8fec3d6a095910f50cb3791ec0f3c06ce1156bd04b8cd64d", "1.7.0--r43hdfd78af_0": "sha256:f2db9172a4c55ea6684896bf8cb70254e6604c12640dab655587f5dffbcabe6e", "1.8.0--r44hdfd78af_0": "sha256:f73ffb24175dc69b0fc5bdf51a8e9d6a100b922c11ca2938d29af605203f03b3"}, "docker": "quay.io/biocontainers/bioconductor-ahpubmeddbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahpubmeddbs.
shpc-registry automated BioContainers addition for bioconductor-ahpubmeddbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahpubmeddbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahpubmeddbs:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahpubmeddbs/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ahpubmeddbs/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahpubmeddbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahpubmeddbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahpubmeddbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahpubmeddbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahpubmeddbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahpubmeddbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahpubmeddbs

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