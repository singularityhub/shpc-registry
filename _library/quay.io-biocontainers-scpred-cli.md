---
layout: container
name:  "quay.io/biocontainers/scpred-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scpred-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scpred-cli/container.yaml"
updated_at: "2024-12-09 03:37:30.395854"
latest: "0.1.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/scpred-cli"
aliases:
 - "get_test_data.R"
 - "scpred_get_feature_space.R"
 - "scpred_get_std_output.R"
 - "scpred_post_install_tests.bats"
 - "scpred_post_install_tests.sh"
 - "scpred_predict.R"
 - "scpred_train_model.R"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "pandoc"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for scpred-cli"
config: {"url": "https://biocontainers.pro/tools/scpred-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scpred-cli", "latest": {"0.1.0--hdfd78af_2": "sha256:d6f6e9e201377651996133a3e6f3e51e061e1e125f880cf0d58ffd0096534bb5"}, "tags": {"0.1.0--hdfd78af_2": "sha256:d6f6e9e201377651996133a3e6f3e51e061e1e125f880cf0d58ffd0096534bb5"}, "docker": "quay.io/biocontainers/scpred-cli", "aliases": {"get_test_data.R": "/usr/local/bin/get_test_data.R", "scpred_get_feature_space.R": "/usr/local/bin/scpred_get_feature_space.R", "scpred_get_std_output.R": "/usr/local/bin/scpred_get_std_output.R", "scpred_post_install_tests.bats": "/usr/local/bin/scpred_post_install_tests.bats", "scpred_post_install_tests.sh": "/usr/local/bin/scpred_post_install_tests.sh", "scpred_predict.R": "/usr/local/bin/scpred_predict.R", "scpred_train_model.R": "/usr/local/bin/scpred_train_model.R", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "pandoc": "/usr/local/bin/pandoc", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scpred-cli.
shpc-registry automated BioContainers addition for scpred-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scpred-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scpred-cli:0.1.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scpred-cli/0.1.0--hdfd78af_2
$ module help quay.io/biocontainers/scpred-cli/0.1.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scpred-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scpred-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scpred-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scpred-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scpred-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scpred-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_test_data.R

```bash
$ singularity exec <container> /usr/local/bin/get_test_data.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_test_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_test_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_get_feature_space.R

```bash
$ singularity exec <container> /usr/local/bin/scpred_get_feature_space.R
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_get_feature_space.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_get_feature_space.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_get_std_output.R

```bash
$ singularity exec <container> /usr/local/bin/scpred_get_std_output.R
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_get_std_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_get_std_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_post_install_tests.bats

```bash
$ singularity exec <container> /usr/local/bin/scpred_post_install_tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_post_install_tests.sh

```bash
$ singularity exec <container> /usr/local/bin/scpred_post_install_tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_predict.R

```bash
$ singularity exec <container> /usr/local/bin/scpred_predict.R
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_predict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_predict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scpred_train_model.R

```bash
$ singularity exec <container> /usr/local/bin/scpred_train_model.R
$ podman run --it --rm --entrypoint /usr/local/bin/scpred_train_model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scpred_train_model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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