---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatialdecon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatialdecon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatialdecon/container.yaml"
updated_at: "2024-12-26 03:16:34.720079"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatialdecon"

versions:
 - "1.3.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spatialdecon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatialdecon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spatialdecon", "latest": {"1.16.0--r44hdfd78af_0": "sha256:2670a4895764981db61040bc9a6d360d98d6acb44bc7e14917ad1672aac6843e"}, "tags": {"1.3.0--r41hdfd78af_0": "sha256:dd063ae6f426fa6e58d0ef84e823438c2513e792cb8908c23ecfdc5b42681a72", "1.8.0--r42hdfd78af_0": "sha256:6066d4c65561d7cf09f05614fde02487919647a581aa746e93ed3bafd45a770b", "1.10.0--r43hdfd78af_0": "sha256:97ddbdd29fea2dde6659463a34dd59719079ec921b65b574d29907e7ae415de6", "1.12.0--r43hdfd78af_0": "sha256:266cf0db832899c55640a15bdfb4e276eb6d58f44412c3781bd0f82674838611", "1.16.0--r44hdfd78af_0": "sha256:2670a4895764981db61040bc9a6d360d98d6acb44bc7e14917ad1672aac6843e"}, "docker": "quay.io/biocontainers/bioconductor-spatialdecon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatialdecon.
shpc-registry automated BioContainers addition for bioconductor-spatialdecon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialdecon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialdecon:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatialdecon/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatialdecon/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatialdecon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialdecon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialdecon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatialdecon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatialdecon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatialdecon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spatialdecon

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