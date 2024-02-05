---
layout: container
name:  "quay.io/biocontainers/atlas-data-import"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/atlas-data-import/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/atlas-data-import/container.yaml"
updated_at: "2024-02-05 02:53:50.639137"
latest: "0.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/atlas-data-import"
aliases:
 - "data_import_post_install_tests.bats"
 - "data_import_post_install_tests.sh"
 - "get_experiment_data.R"
 - "import_classification_data.R"
 - "metadata_conda_debug.yaml"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for atlas-data-import"
config: {"url": "https://biocontainers.pro/tools/atlas-data-import", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for atlas-data-import", "latest": {"0.1.1--hdfd78af_0": "sha256:8874bfe643d54aee07dafa42351cd3258b136764da5110cbba1903b3957443f0"}, "tags": {"0.1.1--hdfd78af_0": "sha256:8874bfe643d54aee07dafa42351cd3258b136764da5110cbba1903b3957443f0"}, "docker": "quay.io/biocontainers/atlas-data-import", "aliases": {"data_import_post_install_tests.bats": "/usr/local/bin/data_import_post_install_tests.bats", "data_import_post_install_tests.sh": "/usr/local/bin/data_import_post_install_tests.sh", "get_experiment_data.R": "/usr/local/bin/get_experiment_data.R", "import_classification_data.R": "/usr/local/bin/import_classification_data.R", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/atlas-data-import.
shpc-registry automated BioContainers addition for atlas-data-import
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/atlas-data-import
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/atlas-data-import:0.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/atlas-data-import/0.1.1--hdfd78af_0
$ module help quay.io/biocontainers/atlas-data-import/0.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### atlas-data-import-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### atlas-data-import-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### atlas-data-import-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### atlas-data-import-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### atlas-data-import-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### atlas-data-import-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### data_import_post_install_tests.bats

```bash
$ singularity exec <container> /usr/local/bin/data_import_post_install_tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/data_import_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_import_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### data_import_post_install_tests.sh

```bash
$ singularity exec <container> /usr/local/bin/data_import_post_install_tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/data_import_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_import_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_experiment_data.R

```bash
$ singularity exec <container> /usr/local/bin/get_experiment_data.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_experiment_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_experiment_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_classification_data.R

```bash
$ singularity exec <container> /usr/local/bin/import_classification_data.R
$ podman run --it --rm --entrypoint /usr/local/bin/import_classification_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_classification_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
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