---
layout: container
name:  "quay.io/biocontainers/bioconductor-differentialregulation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-differentialregulation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-differentialregulation/container.yaml"
updated_at: "2024-04-04 04:31:05.221025"
latest: "2.0.2--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-differentialregulation"
aliases:
 - "installBiocDataPackage.sh"
 - "tomlq"
 - "xq"
 - "yq"
 - "jq"
 - "onig-config"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.2.0--r42hc247a5b_0"
 - "1.2.0--r42hf17093f_1"
 - "1.4.2--r43hf17093f_0"
 - "2.0.2--r43hf17093f_0"
description: "singularity registry hpc automated addition for bioconductor-differentialregulation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-differentialregulation", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-differentialregulation", "latest": {"2.0.2--r43hf17093f_0": "sha256:5d706722c5f3c79e8a115360a6340413f405bb04d436987b22fc30f7ed3e2e92"}, "tags": {"1.2.0--r42hc247a5b_0": "sha256:2bad62e65adc65d6cf5bb3cfd5ef0e3de222911991010551e229abc4f3190e47", "1.2.0--r42hf17093f_1": "sha256:49b52d5f4fb0c99e91750acb5a1d5e8e10d14cd6d23550b77c20352e0e24d9f3", "1.4.2--r43hf17093f_0": "sha256:580e9e3d8beed11ac2e97638fce305c1ed36f02a98e38f656c76d60b8d070937", "2.0.2--r43hf17093f_0": "sha256:5d706722c5f3c79e8a115360a6340413f405bb04d436987b22fc30f7ed3e2e92"}, "docker": "quay.io/biocontainers/bioconductor-differentialregulation", "aliases": {"installBiocDataPackage.sh": "/usr/local/bin/installBiocDataPackage.sh", "tomlq": "/usr/local/bin/tomlq", "xq": "/usr/local/bin/xq", "yq": "/usr/local/bin/yq", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-differentialregulation.
singularity registry hpc automated addition for bioconductor-differentialregulation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-differentialregulation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-differentialregulation:2.0.2--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-differentialregulation/2.0.2--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-differentialregulation/2.0.2--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-differentialregulation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-differentialregulation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-differentialregulation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-differentialregulation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-differentialregulation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-differentialregulation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### installBiocDataPackage.sh

```bash
$ singularity exec <container> /usr/local/bin/installBiocDataPackage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/installBiocDataPackage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installBiocDataPackage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tomlq

```bash
$ singularity exec <container> /usr/local/bin/tomlq
$ podman run --it --rm --entrypoint /usr/local/bin/tomlq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tomlq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xq

```bash
$ singularity exec <container> /usr/local/bin/xq
$ podman run --it --rm --entrypoint /usr/local/bin/xq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yq

```bash
$ singularity exec <container> /usr/local/bin/yq
$ podman run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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