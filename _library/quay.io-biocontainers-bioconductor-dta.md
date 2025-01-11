---
layout: container
name:  "quay.io/biocontainers/bioconductor-dta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dta/container.yaml"
updated_at: "2025-01-11 03:05:00.078144"
latest: "2.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dta"

versions:
 - "2.40.0--r41hdfd78af_0"
 - "2.44.0--r42hdfd78af_0"
 - "2.46.0--r43hdfd78af_0"
 - "2.48.0--r43hdfd78af_0"
 - "2.48.0--r43hdfd78af_1"
 - "2.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dta"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dta", "latest": {"2.52.0--r44hdfd78af_0": "sha256:9ee3acfe6aad84dda90ae1718aa962ce964028c8ae24ef36c474ea38dd7b1c4d"}, "tags": {"2.40.0--r41hdfd78af_0": "sha256:862f3b4c0b1f557b9d564b7eb81c10d4bf1d7f1c589fedadb6c79fd16b86f8a5", "2.44.0--r42hdfd78af_0": "sha256:76fbcf78249e545eb582beebda4b56ff5a967dde808c1060d66dd5ad887decc8", "2.46.0--r43hdfd78af_0": "sha256:b4a2ee4ad529a87d189e845eddedad4c0d27ff8a4980ba4bf973fff24f74bfe1", "2.48.0--r43hdfd78af_0": "sha256:5ef11c540a73e6a8bc1e6e11b3fb7dd4e825c2b5b89b0f395a8ba8413c41bf5b", "2.48.0--r43hdfd78af_1": "sha256:c9c46d35df6e83f3b7e8fc93fcee780254b97f540dfca3b614beacf054d41eed", "2.52.0--r44hdfd78af_0": "sha256:9ee3acfe6aad84dda90ae1718aa962ce964028c8ae24ef36c474ea38dd7b1c4d"}, "docker": "quay.io/biocontainers/bioconductor-dta"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dta.
shpc-registry automated BioContainers addition for bioconductor-dta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dta:2.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dta/2.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dta/2.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dta

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