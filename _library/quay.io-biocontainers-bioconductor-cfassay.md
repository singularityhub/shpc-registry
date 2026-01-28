---
layout: container
name:  "quay.io/biocontainers/bioconductor-cfassay"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cfassay/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cfassay/container.yaml"
updated_at: "2026-01-28 03:58:28.514509"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cfassay"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cfassay"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cfassay", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cfassay", "latest": {"1.40.0--r44hdfd78af_0": "sha256:e8e3be6ec06e086d7e5954716fefb19befd0d88a79c90cb0f7bf2955e9a4dff4"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:c84ddc44aff2fb32ee4e512e5a20a246525f0c489bdf46a4143a975bd7b867fc", "1.32.0--r42hdfd78af_0": "sha256:fd66d3f8319935aeab98082dfb54ae8e1ee203c85e2afc4f454d4c8ff7eef142", "1.34.0--r43hdfd78af_0": "sha256:da23ba0dce35880643478bf97505eb823f4d3180848a13fb4f43ebc08cb5de4e", "1.36.0--r43hdfd78af_0": "sha256:62f8d745c9d5966543ed3f33a03db1666e73ff05b3d90444f865dda76bc878f4", "1.40.0--r44hdfd78af_0": "sha256:e8e3be6ec06e086d7e5954716fefb19befd0d88a79c90cb0f7bf2955e9a4dff4"}, "docker": "quay.io/biocontainers/bioconductor-cfassay"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cfassay.
shpc-registry automated BioContainers addition for bioconductor-cfassay
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cfassay
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cfassay:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cfassay/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cfassay/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cfassay-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cfassay-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cfassay-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cfassay-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cfassay-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cfassay-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cfassay

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