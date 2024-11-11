---
layout: container
name:  "quay.io/biocontainers/bioconductor-singlecellexperiment-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singlecellexperiment-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singlecellexperiment-scripts/container.yaml"
updated_at: "2024-11-11 03:27:58.454143"
latest: "0.0.3--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-singlecellexperiment-scripts"
aliases:
 - "bioconductor-singlecellexperiment-scripts-post-install-tests.sh"
 - "singlecellexperiment-create-single-cell-experiment.R"
 - "singlecellexperiment-get-random-cells.R"
 - "singlecellexperiment-get-random-genes.R"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.3--hdfd78af_1"
 - "0.0.3--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment-scripts"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singlecellexperiment-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment-scripts", "latest": {"0.0.3--hdfd78af_2": "sha256:54c87ddbfb7db87e443824823f9e09515c7657bf37a340d0e3b86f1e29f48975"}, "tags": {"0.0.3--hdfd78af_1": "sha256:cd0fbfa6937a7e6eae825c86ad560ffaf011ffef4546096016921326b7bbeecc", "0.0.3--hdfd78af_2": "sha256:54c87ddbfb7db87e443824823f9e09515c7657bf37a340d0e3b86f1e29f48975"}, "docker": "quay.io/biocontainers/bioconductor-singlecellexperiment-scripts", "aliases": {"bioconductor-singlecellexperiment-scripts-post-install-tests.sh": "/usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh", "singlecellexperiment-create-single-cell-experiment.R": "/usr/local/bin/singlecellexperiment-create-single-cell-experiment.R", "singlecellexperiment-get-random-cells.R": "/usr/local/bin/singlecellexperiment-get-random-cells.R", "singlecellexperiment-get-random-genes.R": "/usr/local/bin/singlecellexperiment-get-random-genes.R", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singlecellexperiment-scripts.
shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellexperiment-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellexperiment-scripts:0.0.3--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singlecellexperiment-scripts/0.0.3--hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-singlecellexperiment-scripts/0.0.3--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singlecellexperiment-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellexperiment-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellexperiment-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singlecellexperiment-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singlecellexperiment-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singlecellexperiment-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioconductor-singlecellexperiment-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconductor-singlecellexperiment-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-create-single-cell-experiment.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-create-single-cell-experiment.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-get-random-cells.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-get-random-cells.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlecellexperiment-get-random-genes.R

```bash
$ singularity exec <container> /usr/local/bin/singlecellexperiment-get-random-genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlecellexperiment-get-random-genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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