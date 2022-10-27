---
layout: container
name:  "quay.io/biocontainers/dfast_qc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dfast_qc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dfast_qc/container.yaml"
updated_at: "2022-10-27 00:30:11.898886"
latest: "0.4.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/dfast_qc"
aliases:
 - ".checkm-genome-post-link.sh"
 - ".checkm-genome-pre-unlink.sh"
 - "dfast_qc"
 - "dqc_admin_tools.py"
 - "dqc_initial_setup.sh"
 - "pwiz.py"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
versions:
 - "0.4.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for dfast_qc"
config: {"url": "https://biocontainers.pro/tools/dfast_qc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dfast_qc", "latest": {"0.4.2--hdfd78af_0": "sha256:8d57ff93148df75e6eebf28ab35ce4e588127e7ec7921ed00b31d67cba9caf43"}, "tags": {"0.4.2--hdfd78af_0": "sha256:8d57ff93148df75e6eebf28ab35ce4e588127e7ec7921ed00b31d67cba9caf43"}, "docker": "quay.io/biocontainers/dfast_qc", "aliases": {".checkm-genome-post-link.sh": "/usr/local/bin/.checkm-genome-post-link.sh", ".checkm-genome-pre-unlink.sh": "/usr/local/bin/.checkm-genome-pre-unlink.sh", "dfast_qc": "/usr/local/bin/dfast_qc", "dqc_admin_tools.py": "/usr/local/bin/dqc_admin_tools.py", "dqc_initial_setup.sh": "/usr/local/bin/dqc_initial_setup.sh", "pwiz.py": "/usr/local/bin/pwiz.py", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dfast_qc.
shpc-registry automated BioContainers addition for dfast_qc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dfast_qc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dfast_qc:0.4.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dfast_qc/0.4.2--hdfd78af_0
$ module help quay.io/biocontainers/dfast_qc/0.4.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dfast_qc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dfast_qc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dfast_qc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dfast_qc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dfast_qc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dfast_qc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .checkm-genome-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.checkm-genome-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.checkm-genome-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.checkm-genome-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .checkm-genome-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.checkm-genome-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.checkm-genome-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.checkm-genome-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfast_qc

```bash
$ singularity exec <container> /usr/local/bin/dfast_qc
$ podman run --it --rm --entrypoint /usr/local/bin/dfast_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dqc_admin_tools.py

```bash
$ singularity exec <container> /usr/local/bin/dqc_admin_tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/dqc_admin_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dqc_admin_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dqc_initial_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/dqc_initial_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/dqc_initial_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dqc_initial_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pwiz.py

```bash
$ singularity exec <container> /usr/local/bin/pwiz.py
$ podman run --it --rm --entrypoint /usr/local/bin/pwiz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pwiz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-build

```bash
$ singularity exec <container> /usr/local/bin/sip-build
$ podman run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-distinfo

```bash
$ singularity exec <container> /usr/local/bin/sip-distinfo
$ podman run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-install

```bash
$ singularity exec <container> /usr/local/bin/sip-install
$ podman run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-module

```bash
$ singularity exec <container> /usr/local/bin/sip-module
$ podman run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-sdist

```bash
$ singularity exec <container> /usr/local/bin/sip-sdist
$ podman run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-wheel

```bash
$ singularity exec <container> /usr/local/bin/sip-wheel
$ podman run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
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