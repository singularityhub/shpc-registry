---
layout: container
name:  "quay.io/biocontainers/bioconductor-beadarraysnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beadarraysnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beadarraysnp/container.yaml"
updated_at: "2024-03-29 02:45:12.881537"
latest: "1.68.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beadarraysnp"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beadarraysnp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beadarraysnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beadarraysnp", "latest": {"1.68.0--r43hdfd78af_0": "sha256:5c1f410795eceefb939ccdcb35bd770f36d59bb612fc2e4126bd20794df6f6b4"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:d4308d93287b35f6f36bc7005f7e07e5741e29da9f31bfc8d1b447d34f91f37c", "1.64.0--r42hdfd78af_0": "sha256:63d0cd14fb48a6c39d36704d4e50d14e179468548c081e82a0a9a55bb824b069", "1.66.0--r43hdfd78af_0": "sha256:e0c64d75e4e9340041d4c70147d9a6587c801a4ca625a33490bd77892b9df415", "1.68.0--r43hdfd78af_0": "sha256:5c1f410795eceefb939ccdcb35bd770f36d59bb612fc2e4126bd20794df6f6b4"}, "docker": "quay.io/biocontainers/bioconductor-beadarraysnp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beadarraysnp.
shpc-registry automated BioContainers addition for bioconductor-beadarraysnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarraysnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarraysnp:1.68.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beadarraysnp/1.68.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-beadarraysnp/1.68.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beadarraysnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarraysnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarraysnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beadarraysnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beadarraysnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beadarraysnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beadarraysnp

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