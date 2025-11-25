---
layout: container
name:  "quay.io/biocontainers/bioconductor-squadd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-squadd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-squadd/container.yaml"
updated_at: "2025-11-25 04:01:00.205648"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-squadd"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-squadd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-squadd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-squadd", "latest": {"1.52.0--r43hdfd78af_0": "sha256:e3ebf5f2facbdb5435b9b5566fea8276762d66f8536c3f507381e783fa1e2c77"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:b8626207fcc5e1ef622c545d962d0c537f0fb8f57d3281bb17ec8ad7c24ca9ba", "1.48.0--r42hdfd78af_0": "sha256:cb35fa3ff8071e114774cb8d29f4b440516651caff54d1321c439df45b3f17c2", "1.50.0--r43hdfd78af_0": "sha256:e0da72c84a170db2735abfdb88b94469da94970a08cffa3e00b8b3f5a37975ba", "1.52.0--r43hdfd78af_0": "sha256:e3ebf5f2facbdb5435b9b5566fea8276762d66f8536c3f507381e783fa1e2c77"}, "docker": "quay.io/biocontainers/bioconductor-squadd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-squadd.
shpc-registry automated BioContainers addition for bioconductor-squadd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-squadd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-squadd:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-squadd/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-squadd/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-squadd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-squadd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-squadd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-squadd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-squadd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-squadd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-squadd

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