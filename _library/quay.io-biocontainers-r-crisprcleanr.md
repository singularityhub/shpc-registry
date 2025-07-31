---
layout: container
name:  "quay.io/biocontainers/r-crisprcleanr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-crisprcleanr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-crisprcleanr/container.yaml"
updated_at: "2025-07-31 11:20:55.133848"
latest: "3.0.0--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-crisprcleanr"

versions:
 - "2.3.1--r41hdfd78af_0"
 - "2.3.1--r42hdfd78af_1"
 - "3.0.0--r42hdfd78af_0"
 - "3.0.0--r42hdfd78af_1"
 - "3.0.0--r43hdfd78af_2"
 - "3.0.0--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-crisprcleanr"
config: {"url": "https://biocontainers.pro/tools/r-crisprcleanr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-crisprcleanr", "latest": {"3.0.0--r44hdfd78af_3": "sha256:b15593c0745cc7161288d8afe7c5171cbe6d818d503a642b17ffaf26a5b02f0f"}, "tags": {"2.3.1--r41hdfd78af_0": "sha256:6b6ac5be02b266bb7f645cea235f7a97abe00c8203424730de1dd04e54128eb1", "2.3.1--r42hdfd78af_1": "sha256:2bd10491471084d969f258316680bb9c93a3fcd16276e9b6ae4de8f5d590ad7e", "3.0.0--r42hdfd78af_0": "sha256:b9e21664b6e4cca1c13dda84622887e269cb5c39760bbcb84fa32bd49873d21b", "3.0.0--r42hdfd78af_1": "sha256:338862ffb97d96c21a241d802258f5f4a535c264bfbce6df6c8cc0380ad33df8", "3.0.0--r43hdfd78af_2": "sha256:b72ef583ecbc419f021f02dedc9adc835a29eab482bf4275a23c577b08f4be3f", "3.0.0--r44hdfd78af_3": "sha256:b15593c0745cc7161288d8afe7c5171cbe6d818d503a642b17ffaf26a5b02f0f"}, "docker": "quay.io/biocontainers/r-crisprcleanr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-crisprcleanr.
shpc-registry automated BioContainers addition for r-crisprcleanr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-crisprcleanr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-crisprcleanr:3.0.0--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-crisprcleanr/3.0.0--r44hdfd78af_3
$ module help quay.io/biocontainers/r-crisprcleanr/3.0.0--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-crisprcleanr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-crisprcleanr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-crisprcleanr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-crisprcleanr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-crisprcleanr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-crisprcleanr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-crisprcleanr

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