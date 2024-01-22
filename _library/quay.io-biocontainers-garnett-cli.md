---
layout: container
name:  "quay.io/biocontainers/garnett-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/garnett-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/garnett-cli/container.yaml"
updated_at: "2024-01-22 03:30:49.129760"
latest: "0.0.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/garnett-cli"
aliases:
 - "garnett_check_markers.R"
 - "garnett_classify_cells.R"
 - "garnett_cli_post_install_tests.bats"
 - "garnett_cli_post_install_tests.sh"
 - "garnett_get_feature_genes.R"
 - "garnett_train_classifier.R"
 - "make_test_data.R"
 - "parse_expr_data.R"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "v0.0.1--r36_0"
 - "0.0.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for garnett-cli"
config: {"url": "https://biocontainers.pro/tools/garnett-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for garnett-cli", "latest": {"0.0.5--hdfd78af_1": "sha256:bfa33b0dedcaa5800c6cad483c99697b397eeb9e6fe8ec6a7a80c6f6ba0a001e"}, "tags": {"v0.0.1--r36_0": "sha256:38e89fa8f323b4abf55bf7304665172b007951f405494b62dad56e1fcccdde76", "0.0.5--hdfd78af_1": "sha256:bfa33b0dedcaa5800c6cad483c99697b397eeb9e6fe8ec6a7a80c6f6ba0a001e"}, "docker": "quay.io/biocontainers/garnett-cli", "aliases": {"garnett_check_markers.R": "/usr/local/bin/garnett_check_markers.R", "garnett_classify_cells.R": "/usr/local/bin/garnett_classify_cells.R", "garnett_cli_post_install_tests.bats": "/usr/local/bin/garnett_cli_post_install_tests.bats", "garnett_cli_post_install_tests.sh": "/usr/local/bin/garnett_cli_post_install_tests.sh", "garnett_get_feature_genes.R": "/usr/local/bin/garnett_get_feature_genes.R", "garnett_train_classifier.R": "/usr/local/bin/garnett_train_classifier.R", "make_test_data.R": "/usr/local/bin/make_test_data.R", "parse_expr_data.R": "/usr/local/bin/parse_expr_data.R", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/garnett-cli.
shpc-registry automated BioContainers addition for garnett-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/garnett-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/garnett-cli:0.0.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/garnett-cli/0.0.5--hdfd78af_1
$ module help quay.io/biocontainers/garnett-cli/0.0.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### garnett-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### garnett-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### garnett-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### garnett-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### garnett-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### garnett-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### garnett_check_markers.R

```bash
$ singularity exec <container> /usr/local/bin/garnett_check_markers.R
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_check_markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_check_markers.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### garnett_classify_cells.R

```bash
$ singularity exec <container> /usr/local/bin/garnett_classify_cells.R
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_classify_cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_classify_cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### garnett_cli_post_install_tests.bats

```bash
$ singularity exec <container> /usr/local/bin/garnett_cli_post_install_tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_cli_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_cli_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### garnett_cli_post_install_tests.sh

```bash
$ singularity exec <container> /usr/local/bin/garnett_cli_post_install_tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_cli_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_cli_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### garnett_get_feature_genes.R

```bash
$ singularity exec <container> /usr/local/bin/garnett_get_feature_genes.R
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_get_feature_genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_get_feature_genes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### garnett_train_classifier.R

```bash
$ singularity exec <container> /usr/local/bin/garnett_train_classifier.R
$ podman run --it --rm --entrypoint /usr/local/bin/garnett_train_classifier.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/garnett_train_classifier.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_test_data.R

```bash
$ singularity exec <container> /usr/local/bin/make_test_data.R
$ podman run --it --rm --entrypoint /usr/local/bin/make_test_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_test_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_expr_data.R

```bash
$ singularity exec <container> /usr/local/bin/parse_expr_data.R
$ podman run --it --rm --entrypoint /usr/local/bin/parse_expr_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_expr_data.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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