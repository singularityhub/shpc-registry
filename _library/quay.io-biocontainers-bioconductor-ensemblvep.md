---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensemblvep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensemblvep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensemblvep/container.yaml"
updated_at: "2025-01-20 04:15:07.573717"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ensemblvep"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ensemblvep"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensemblvep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensemblvep", "latest": {"1.44.0--r43hdfd78af_0": "sha256:50dd389dce8f8e35971669415cbd868da1b47b2e50ec647f4e530535445821e2"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:5d0921e90f42b7a3024c124738dab1ad6d8fcb199ade72db747c2a191599cc86", "1.40.0--r42hdfd78af_0": "sha256:65d9ded1611a533363ba97a93ea2f7762346857e57fbd61a89d1bbc06580c60a", "1.42.0--r43hdfd78af_0": "sha256:a2ecf773480511463a058a321c1e56d2e25b8d7aced83ed0cb97ec46fe14b71c", "1.44.0--r43hdfd78af_0": "sha256:50dd389dce8f8e35971669415cbd868da1b47b2e50ec647f4e530535445821e2"}, "docker": "quay.io/biocontainers/bioconductor-ensemblvep"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensemblvep.
shpc-registry automated BioContainers addition for bioconductor-ensemblvep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensemblvep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensemblvep:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensemblvep/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ensemblvep/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensemblvep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensemblvep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensemblvep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensemblvep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensemblvep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensemblvep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensemblvep

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