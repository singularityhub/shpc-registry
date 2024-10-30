---
layout: container
name:  "quay.io/biocontainers/bioconductor-poplarcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-poplarcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-poplarcdf/container.yaml"
updated_at: "2024-10-30 15:34:29.669916"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-poplarcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-poplarcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-poplarcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-poplarcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:242d2b6b3c54213e0a65389a0b155c5dc199e13beb1356698d8e41a4295feb8e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:8cced2db2c3a1426938de65f5dd7733605b2afaeb953e07a6eff4858e1c2e930", "2.18.0--r42hdfd78af_10": "sha256:5d387905f4abbbda490ca4829178a57c6238844900185032a47c3dd04abff4f1", "2.18.0--r43hdfd78af_11": "sha256:c44b24f919dc71588ce9cec8046c4f3d69ba9ca91b3400695221272c8e5f7629", "2.18.0--r43hdfd78af_12": "sha256:242d2b6b3c54213e0a65389a0b155c5dc199e13beb1356698d8e41a4295feb8e"}, "docker": "quay.io/biocontainers/bioconductor-poplarcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-poplarcdf.
shpc-registry automated BioContainers addition for bioconductor-poplarcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-poplarcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-poplarcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-poplarcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-poplarcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-poplarcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-poplarcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-poplarcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-poplarcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-poplarcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-poplarcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-poplarcdf

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