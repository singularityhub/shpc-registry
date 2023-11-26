---
layout: container
name:  "quay.io/biocontainers/bioconductor-canine2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-canine2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-canine2probe/container.yaml"
updated_at: "2023-11-26 02:55:51.276574"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-canine2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-canine2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-canine2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-canine2probe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:8068125529ccfe8a68ae9418e0cf404847ed5e569711ee1c67ba722054c2c22c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:55a66039c401b8402ec75b6033ed2f2a43789f1c8533e2dab78e2f67423c350f", "2.18.0--r42hdfd78af_10": "sha256:9cf7ccfe58ebaee402a9f213918f9af515f7e25bcfeba8ea69a31538d080c270", "2.18.0--r43hdfd78af_11": "sha256:8068125529ccfe8a68ae9418e0cf404847ed5e569711ee1c67ba722054c2c22c"}, "docker": "quay.io/biocontainers/bioconductor-canine2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-canine2probe.
shpc-registry automated BioContainers addition for bioconductor-canine2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-canine2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-canine2probe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-canine2probe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-canine2probe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-canine2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-canine2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-canine2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-canine2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-canine2probe

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