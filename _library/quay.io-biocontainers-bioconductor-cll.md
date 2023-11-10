---
layout: container
name:  "quay.io/biocontainers/bioconductor-cll"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cll/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cll/container.yaml"
updated_at: "2023-11-10 02:50:37.331857"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cll"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cll"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cll", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cll", "latest": {"1.40.0--r43hdfd78af_0": "sha256:5880e2a853cb2dae49daa8f247c22b92260eb6f19f3575cd6a50fa74be704df6"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:017c03df4662b6a7eed60a4fc1e702538233ebff10a9d1c07d0f4d0c69201da3", "1.38.0--r42hdfd78af_0": "sha256:8c20d596ea64d86b2e36957f32914f2caae919addbf8291acd5bf30000488568", "1.40.0--r43hdfd78af_0": "sha256:5880e2a853cb2dae49daa8f247c22b92260eb6f19f3575cd6a50fa74be704df6"}, "docker": "quay.io/biocontainers/bioconductor-cll"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cll.
shpc-registry automated BioContainers addition for bioconductor-cll
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cll
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cll:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cll/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cll/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cll-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cll-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cll-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cll-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cll-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cll-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cll

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