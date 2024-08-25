---
layout: container
name:  "quay.io/biocontainers/dropletutils-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dropletutils-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dropletutils-scripts/container.yaml"
updated_at: "2024-08-25 03:10:38.459672"
latest: "0.0.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/dropletutils-scripts"
aliases:
 - "dropletutils-barcoderanks.R"
 - "dropletutils-downsample-matrix.R"
 - "dropletutils-empty-drops.R"
 - "dropletutils-make-test-sdrf.R"
 - "dropletutils-read-10x-counts.R"
 - "dropletutils-scripts-post-install-tests.bats"
 - "dropletutils-scripts-post-install-tests.sh"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for dropletutils-scripts"
config: {"url": "https://biocontainers.pro/tools/dropletutils-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dropletutils-scripts", "latest": {"0.0.5--hdfd78af_1": "sha256:97ed6b5d0d80e52634e9f38f921c79792516ecea41947c31cd5c270c9ef7c5dd"}, "tags": {"0.0.5--hdfd78af_1": "sha256:97ed6b5d0d80e52634e9f38f921c79792516ecea41947c31cd5c270c9ef7c5dd"}, "docker": "quay.io/biocontainers/dropletutils-scripts", "aliases": {"dropletutils-barcoderanks.R": "/usr/local/bin/dropletutils-barcoderanks.R", "dropletutils-downsample-matrix.R": "/usr/local/bin/dropletutils-downsample-matrix.R", "dropletutils-empty-drops.R": "/usr/local/bin/dropletutils-empty-drops.R", "dropletutils-make-test-sdrf.R": "/usr/local/bin/dropletutils-make-test-sdrf.R", "dropletutils-read-10x-counts.R": "/usr/local/bin/dropletutils-read-10x-counts.R", "dropletutils-scripts-post-install-tests.bats": "/usr/local/bin/dropletutils-scripts-post-install-tests.bats", "dropletutils-scripts-post-install-tests.sh": "/usr/local/bin/dropletutils-scripts-post-install-tests.sh", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dropletutils-scripts.
shpc-registry automated BioContainers addition for dropletutils-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dropletutils-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dropletutils-scripts:0.0.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dropletutils-scripts/0.0.5--hdfd78af_1
$ module help quay.io/biocontainers/dropletutils-scripts/0.0.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dropletutils-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dropletutils-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dropletutils-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dropletutils-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dropletutils-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dropletutils-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dropletutils-barcoderanks.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-barcoderanks.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-barcoderanks.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-barcoderanks.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-downsample-matrix.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-downsample-matrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-downsample-matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-downsample-matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-empty-drops.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-empty-drops.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-empty-drops.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-empty-drops.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-make-test-sdrf.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-make-test-sdrf.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-make-test-sdrf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-make-test-sdrf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-read-10x-counts.R

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-read-10x-counts.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-read-10x-counts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-read-10x-counts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-scripts-post-install-tests.bats

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-scripts-post-install-tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropletutils-scripts-post-install-tests.sh

```bash
$ singularity exec <container> /usr/local/bin/dropletutils-scripts-post-install-tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletutils-scripts-post-install-tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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