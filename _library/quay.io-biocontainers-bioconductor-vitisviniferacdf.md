---
layout: container
name:  "quay.io/biocontainers/bioconductor-vitisviniferacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vitisviniferacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vitisviniferacdf/container.yaml"
updated_at: "2025-09-21 03:49:46.535696"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-vitisviniferacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-vitisviniferacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vitisviniferacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vitisviniferacdf", "latest": {"2.18.0--r43hdfd78af_13": "sha256:f72ec129127a7852a5128ff87095e66f14de7f182ab45e8f38101078ff0d291e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:6c2e6d84b1efac41699e300669b3c49b578be12355ca7e7a16e70217cdeefb81", "2.18.0--r41hdfd78af_10": "sha256:0747b15cfd946eb3e44a9c1b626b92db831f0508139818ae106a09809c71a13b", "2.18.0--r42hdfd78af_11": "sha256:06f4ec115b6901b764aa63529abbb1667d5f1431b3ff67e31ec91be4f0dfa97a", "2.18.0--r43hdfd78af_12": "sha256:80b7feeb296c4ae5699f2948cf31a6d151e2429e97c5c0d40398652d4a23e3e5", "2.18.0--r43hdfd78af_13": "sha256:f72ec129127a7852a5128ff87095e66f14de7f182ab45e8f38101078ff0d291e"}, "docker": "quay.io/biocontainers/bioconductor-vitisviniferacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vitisviniferacdf.
shpc-registry automated BioContainers addition for bioconductor-vitisviniferacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vitisviniferacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vitisviniferacdf:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vitisviniferacdf/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-vitisviniferacdf/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vitisviniferacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vitisviniferacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vitisviniferacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vitisviniferacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vitisviniferacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vitisviniferacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vitisviniferacdf

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