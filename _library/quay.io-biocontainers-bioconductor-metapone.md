---
layout: container
name:  "quay.io/biocontainers/bioconductor-metapone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metapone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metapone/container.yaml"
updated_at: "2023-11-05 02:58:38.506547"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metapone"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metapone"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metapone", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metapone", "latest": {"1.6.0--r43hdfd78af_0": "sha256:91736df5569066cd66334b04c25a930e1ebc4e3e70e314bc7c5f58aa940480d5"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:77bb95b319eb33b7f5d7ae9a767b352164b49921c40a198e4d2bb35739a8b677", "1.4.0--r42hdfd78af_0": "sha256:1a3f819f6b813946f797f704ebdc28753157b28f494ff607b942cf55e64068cc", "1.6.0--r43hdfd78af_0": "sha256:91736df5569066cd66334b04c25a930e1ebc4e3e70e314bc7c5f58aa940480d5"}, "docker": "quay.io/biocontainers/bioconductor-metapone"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metapone.
shpc-registry automated BioContainers addition for bioconductor-metapone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metapone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metapone:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metapone/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metapone/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metapone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metapone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metapone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metapone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metapone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metapone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metapone

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