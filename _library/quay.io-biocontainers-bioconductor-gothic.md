---
layout: container
name:  "quay.io/biocontainers/bioconductor-gothic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gothic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gothic/container.yaml"
updated_at: "2025-09-18 03:43:00.308570"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gothic"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gothic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gothic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gothic", "latest": {"1.42.0--r44hdfd78af_0": "sha256:85eeea43343ce2436b108350d8eff570fc31f71fa95b940328bc608bf992a6b6"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:f78524a5146d258828cf227b59281f52ae691fc4b2ad34d2c617b86c0cdbff61", "1.34.0--r42hdfd78af_0": "sha256:42c1df3e61f9889cbd10f8feb3bc465c23325ef2f6f63d2707143c2120ecd6c2", "1.36.0--r43hdfd78af_0": "sha256:ed656b04188c86cd42854cc652409a948bc931fcd4bdf63434e6e798e0060255", "1.38.0--r43hdfd78af_0": "sha256:59dd3d8a38b8e7f21e27b02545c2319f417a3dc7fbd76f7927e5205d0637aec1", "1.42.0--r44hdfd78af_0": "sha256:85eeea43343ce2436b108350d8eff570fc31f71fa95b940328bc608bf992a6b6"}, "docker": "quay.io/biocontainers/bioconductor-gothic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gothic.
shpc-registry automated BioContainers addition for bioconductor-gothic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gothic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gothic:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gothic/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gothic/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gothic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gothic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gothic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gothic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gothic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gothic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gothic

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