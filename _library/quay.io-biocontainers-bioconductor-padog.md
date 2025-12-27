---
layout: container
name:  "quay.io/biocontainers/bioconductor-padog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-padog/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-padog/container.yaml"
updated_at: "2025-12-27 04:03:15.711664"
latest: "1.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-padog"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-padog"
config: {"url": "https://biocontainers.pro/tools/bioconductor-padog", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-padog", "latest": {"1.48.0--r44hdfd78af_0": "sha256:fdbc1f5f1a2f985856f1c0b9a27a5e90e7535f98a18b5ba536c0db38e44e960d"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:649c44d522b6614404306c6e551b63365b8a07bf9196f63fa66f1eb37e6b984c", "1.40.0--r42hdfd78af_0": "sha256:bc0dba38b294cd8f58057f027778e95668de353adca758974729c28cfb3df3a5", "1.42.0--r43hdfd78af_0": "sha256:5f0ee583210d864473c2abbcc683f7a9798393bc7d70dad238a26e92b4b2eb9f", "1.44.0--r43hdfd78af_0": "sha256:bdad9b857472d4575a583d8760595a8fcfadb525a53dd0c20b7ad91d873d129c", "1.48.0--r44hdfd78af_0": "sha256:fdbc1f5f1a2f985856f1c0b9a27a5e90e7535f98a18b5ba536c0db38e44e960d"}, "docker": "quay.io/biocontainers/bioconductor-padog"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-padog.
shpc-registry automated BioContainers addition for bioconductor-padog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-padog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-padog:1.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-padog/1.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-padog/1.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-padog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-padog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-padog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-padog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-padog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-padog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-padog

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