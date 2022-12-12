---
layout: container
name:  "quay.io/biocontainers/bioconductor-procoil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-procoil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-procoil/container.yaml"
updated_at: "2022-12-12 03:11:53.952260"
latest: "2.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-procoil"

versions:
 - "2.8.0--r351_0"
 - "2.26.0--r42hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r40hdfd78af_1"
 - "2.16.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-procoil"
config: {"url": "https://biocontainers.pro/tools/bioconductor-procoil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-procoil", "latest": {"2.26.0--r42hdfd78af_0": "sha256:974dffe99a43990cb7cf694463812ba6e8959ea4937808768c31840ba0fc22d7"}, "tags": {"2.8.0--r351_0": "sha256:c91e72c2c60c5dc76e41d7571da6fd0a5e7cc57dae3534f8ba5702bd23880379", "2.26.0--r42hdfd78af_0": "sha256:974dffe99a43990cb7cf694463812ba6e8959ea4937808768c31840ba0fc22d7", "2.22.0--r41hdfd78af_0": "sha256:79fe5751ca4971eb509d5bf86bd81e37e739e30c4f992e85a7d4cff632f66cbf", "2.20.0--r41hdfd78af_0": "sha256:b47113be5c688c0eae5bf68f4fc0daaf9f9f6afa8ff59751ddc3f6f94906e812", "2.18.0--r40hdfd78af_1": "sha256:e3c2c9fdc3791694a2f8e23a8fb4f4043afe7da372df2cfd1cede644e3e8abfc", "2.16.0--r40_0": "sha256:526b160e530a46a7806a75b021e69f853d31c27753fc36c8cd6239cb388b1162"}, "docker": "quay.io/biocontainers/bioconductor-procoil"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-procoil.
shpc-registry automated BioContainers addition for bioconductor-procoil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-procoil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-procoil:2.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-procoil/2.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-procoil/2.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-procoil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-procoil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-procoil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-procoil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-procoil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-procoil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-procoil

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