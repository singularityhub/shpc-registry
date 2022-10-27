---
layout: container
name:  "quay.io/biocontainers/ruby-dna-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ruby-dna-tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ruby-dna-tools/container.yaml"
updated_at: "2022-10-27 00:42:03.603865"
latest: "1.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/ruby-dna-tools"

versions:
 - "1.0--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for ruby-dna-tools"
config: {"url": "https://biocontainers.pro/tools/ruby-dna-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ruby-dna-tools", "latest": {"1.0--hdfd78af_3": "sha256:ee7f4ce825a97980497193855ad35871b2cc24968540b276bc4126c9d6aa829d"}, "tags": {"1.0--hdfd78af_3": "sha256:ee7f4ce825a97980497193855ad35871b2cc24968540b276bc4126c9d6aa829d"}, "docker": "quay.io/biocontainers/ruby-dna-tools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ruby-dna-tools.
shpc-registry automated BioContainers addition for ruby-dna-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ruby-dna-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ruby-dna-tools:1.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ruby-dna-tools/1.0--hdfd78af_3
$ module help quay.io/biocontainers/ruby-dna-tools/1.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ruby-dna-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ruby-dna-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ruby-dna-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ruby-dna-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ruby-dna-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruby-dna-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ruby-dna-tools

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