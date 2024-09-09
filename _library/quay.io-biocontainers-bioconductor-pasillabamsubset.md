---
layout: container
name:  "quay.io/biocontainers/bioconductor-pasillabamsubset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pasillabamsubset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pasillabamsubset/container.yaml"
updated_at: "2024-09-09 06:11:45.896688"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pasillabamsubset"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pasillabamsubset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pasillabamsubset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pasillabamsubset", "latest": {"0.40.0--r43hdfd78af_0": "sha256:0618c3413bc3dba37ff937ece61a24a7f61cd869e16dae50091197fe201a03c0"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:984480b1161fa562fb6a6d9bc510e2559d1cb6b52e93b3207c9bce9188edc819", "0.35.0--r42hdfd78af_0": "sha256:5cbfc78debcc183e2446bfd4f33fadf2b49a8cf03663199fe365ddaa85a8d145", "0.38.0--r43hdfd78af_0": "sha256:2511045500a7e99bb4b0cd6ba614c36b25633cb99f36a876324acd6b7e2f3e41", "0.40.0--r43hdfd78af_0": "sha256:0618c3413bc3dba37ff937ece61a24a7f61cd869e16dae50091197fe201a03c0"}, "docker": "quay.io/biocontainers/bioconductor-pasillabamsubset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pasillabamsubset.
shpc-registry automated BioContainers addition for bioconductor-pasillabamsubset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pasillabamsubset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pasillabamsubset:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pasillabamsubset/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pasillabamsubset/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pasillabamsubset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pasillabamsubset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pasillabamsubset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pasillabamsubset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pasillabamsubset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pasillabamsubset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pasillabamsubset

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